const { bearerToken, noStore, requireSameOrigin, sendError } = require("../_security");
const { clearSessionCookie, createAdminSession, requireAdminSession, setSessionCookie } = require("../_firebase");

module.exports = async function handler(req, res) {
  try {
    if (req.method === "GET") {
      const user = await requireAdminSession(req);
      noStore(res);
      return res.status(200).json({ email: user.email, authenticated: true });
    }
    if (req.method === "POST") {
      requireSameOrigin(req);
      const { sessionCookie } = await createAdminSession(bearerToken(req));
      setSessionCookie(res, sessionCookie);
      noStore(res);
      return res.status(204).end();
    }
    if (req.method === "DELETE") {
      requireSameOrigin(req);
      clearSessionCookie(res);
      noStore(res);
      return res.status(204).end();
    }
    res.setHeader("Allow", "GET, POST, DELETE");
    return res.status(405).json({ error: "METHOD_NOT_ALLOWED" });
  } catch (error) {
    return sendError(res, error);
  }
};
