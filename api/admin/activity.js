const { noStore, sendError } = require("../_security");
const { firestore, requireAdminSession } = require("../_firebase");

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "GET") {
      res.setHeader("Allow", "GET");
      return res.status(405).json({ error: "METHOD_NOT_ALLOWED" });
    }
    await requireAdminSession(req);
    const snapshot = await firestore().collection("activityLogs").orderBy("createdAt", "desc").limit(50).get();
    noStore(res);
    return res.status(200).json(snapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() })));
  } catch (error) {
    return sendError(res, error);
  }
};
