const { noStore, sendError } = require("../_security");

module.exports = async function handler(_req, res) {
  try {
    const config = {
      apiKey: process.env.FIREBASE_WEB_API_KEY,
      authDomain: process.env.FIREBASE_WEB_AUTH_DOMAIN,
      projectId: process.env.FIREBASE_PROJECT_ID,
      appId: process.env.FIREBASE_WEB_APP_ID,
      messagingSenderId: process.env.FIREBASE_WEB_MESSAGING_SENDER_ID,
    };
    if (Object.values(config).some((value) => !value)) throw new Error("Configuration Firebase web manquante");
    noStore(res);
    return res.status(200).json(config);
  } catch (error) {
    return sendError(res, error);
  }
};
