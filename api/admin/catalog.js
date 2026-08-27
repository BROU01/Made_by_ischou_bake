const { AdminAccessError, noStore, parseJsonBody, requireSameOrigin, sendError } = require("../_security");
const { firestore, requireAdminSession } = require("../_firebase");

function publicProduct(id, value) {
  return {
    id,
    family: value.family,
    name: value.name,
    description: value.description,
    price: value.price,
    unitLabel: value.unitLabel,
    announcedQuantity: value.announcedQuantity ?? null,
    isEstimatedPrice: Boolean(value.isEstimatedPrice),
    isActive: value.isActive !== false,
    position: value.position,
  };
}

function validateUpdate(input) {
  const result = {};
  if (typeof input.name === "string") result.name = input.name.trim().slice(0, 80);
  if (typeof input.description === "string") result.description = input.description.trim().slice(0, 500);
  if (typeof input.price !== "undefined") result.price = Number(input.price);
  if (typeof input.unitLabel === "string") result.unitLabel = input.unitLabel.trim().slice(0, 24);
  if (typeof input.announcedQuantity !== "undefined") result.announcedQuantity = input.announcedQuantity === null ? null : Number(input.announcedQuantity);
  if (typeof input.isEstimatedPrice === "boolean") result.isEstimatedPrice = input.isEstimatedPrice;
  if (typeof input.isActive === "boolean") result.isActive = input.isActive;
  if (!result.name || !result.description || !Number.isFinite(result.price) || result.price < 0 || !result.unitLabel || (result.announcedQuantity !== undefined && result.announcedQuantity !== null && (!Number.isInteger(result.announcedQuantity) || result.announcedQuantity < 1))) {
    throw new AdminAccessError(400, "INVALID_PRODUCT", "Les informations du produit sont incomplètes ou invalides.");
  }
  return result;
}

module.exports = async function handler(req, res) {
  try {
    const admin = await requireAdminSession(req);
    const db = firestore();
    if (req.method === "GET") {
      const snapshot = await db.collection("products").orderBy("position", "asc").get();
      noStore(res);
      return res.status(200).json(snapshot.docs.map((doc) => publicProduct(doc.id, doc.data())));
    }
    if (req.method === "PATCH") {
      requireSameOrigin(req);
      const input = parseJsonBody(req);
      if (typeof input.id !== "string" || !/^[a-z0-9-]{3,80}$/.test(input.id)) throw new AdminAccessError(400, "INVALID_PRODUCT", "Le produit demandé est invalide.");
      const ref = db.collection("products").doc(input.id);
      const current = await ref.get();
      if (!current.exists) throw new AdminAccessError(404, "PRODUCT_NOT_FOUND", "Ce produit n’existe pas dans le catalogue.");
      const update = validateUpdate(input);
      const now = new Date();
      await Promise.all([
        ref.update({ ...update, updatedAt: now, updatedBy: admin.email }),
        db.collection("activityLogs").add({ action: "catalogue_modifie", targetType: "product", targetId: input.id, actorEmail: admin.email, createdAt: now }),
      ]);
      noStore(res);
      return res.status(200).json(publicProduct(input.id, { ...current.data(), ...update }));
    }
    res.setHeader("Allow", "GET, PATCH");
    return res.status(405).json({ error: "METHOD_NOT_ALLOWED" });
  } catch (error) {
    return sendError(res, error);
  }
};
