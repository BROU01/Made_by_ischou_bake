const { noStore, requireSameOrigin, sendError } = require("../../_security");
const { catalogue } = require("../../_catalogue");
const { firestore, requireAdminSession } = require("../../_firebase");

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "POST") {
      res.setHeader("Allow", "POST");
      return res.status(405).json({ error: "METHOD_NOT_ALLOWED" });
    }
    requireSameOrigin(req);
    const admin = await requireAdminSession(req);
    const db = firestore();
    const refs = catalogue.map((product) => db.collection("products").doc(product.id));
    const current = await Promise.all(refs.map((ref) => ref.get()));
    const missing = catalogue.filter((product, index) => !current[index].exists);
    if (!missing.length) {
      noStore(res);
      return res.status(200).json({ inserted: 0, message: "Le catalogue était déjà initialisé." });
    }
    const now = new Date();
    const batch = db.batch();
    missing.forEach((product) => batch.set(db.collection("products").doc(product.id), { ...product, createdAt: now, updatedAt: now, updatedBy: admin.email }));
    batch.set(db.collection("activityLogs").doc(), { action: "catalogue_initialise", targetType: "catalogue", targetId: null, actorEmail: admin.email, createdAt: now, count: missing.length });
    await batch.commit();
    noStore(res);
    return res.status(201).json({ inserted: missing.length, message: "Le catalogue validé a été initialisé." });
  } catch (error) {
    return sendError(res, error);
  }
};
