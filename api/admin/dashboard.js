const { noStore, sendError } = require("../_security");
const { firestore, requireAdminSession } = require("../_firebase");

module.exports = async function handler(req, res) {
  try {
    if (req.method !== "GET") {
      res.setHeader("Allow", "GET");
      return res.status(405).json({ error: "METHOD_NOT_ALLOWED" });
    }
    await requireAdminSession(req);
    const db = firestore();
    const [products, orders, media, settings, activity] = await Promise.all([
      db.collection("products").count().get(),
      db.collection("orders").count().get(),
      db.collection("mediaAssets").count().get(),
      db.collection("storeSettings").count().get(),
      db.collection("activityLogs").orderBy("createdAt", "desc").limit(8).get(),
    ]);
    noStore(res);
    return res.status(200).json({
      products: products.data().count,
      orders: orders.data().count,
      media: media.data().count,
      settings: settings.data().count,
      recentActivity: activity.docs.map((doc) => ({ id: doc.id, ...doc.data() })),
    });
  } catch (error) {
    return sendError(res, error);
  }
};
