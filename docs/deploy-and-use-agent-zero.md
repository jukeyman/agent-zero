# Deploy and Use Agent Zero (Upload + Run)

This guide is the fastest path to get your customized Agent Zero online so you can view and use it.

## 1) Local deployment (fastest way to use now)

### Option A — Docker image (recommended)
1. Pull image:
   - `docker pull agent0ai/agent-zero`
2. Run container:
   - `docker run -p 50001:80 --name agent-zero-rj agent0ai/agent-zero`
3. Open UI:
   - `http://localhost:50001`

### Option B — from this customized repo
1. Create env and install:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip3 install -r requirements.txt`
2. Run app:
   - `python3 run_ui.py`
3. Open UI URL shown in terminal (default usually `http://127.0.0.1:50001`).

---

## 2) Load your integration keys safely

1. Copy template:
   - `cp .env.integrations.example .env.integrations.local`
2. Fill values in `.env.integrations.local` locally.
3. Start Agent Zero (keys auto-load from `.env` and optional `.env.integrations.local`).

> Never commit real secrets.

---

## 3) Verify integration readiness

Call status endpoint:
- `GET /api/integrations_status`

Example:
- `curl http://127.0.0.1:50001/api/integrations_status`

You will get grouped configured/missing counts and `fully_connected`.

---

## 4) Upload your customized repo to GitHub

From your local clone:

1. Create repo on GitHub.
2. Push branch:
   - `git remote add origin <your_repo_url>`
   - `git push -u origin <your_branch>`
3. If needed, merge to `main` via PR.

---

## 5) Deploy publicly to view/use from anywhere

### A) Cloudflare Tunnel to your running local instance (quick public URL)
1. Run Agent Zero locally.
2. Open the built-in Tunnel settings in Agent Zero UI and start tunnel.
3. Use generated public URL.

### B) VPS / dedicated server with Docker
1. Install Docker on server.
2. Run:
   - `docker pull agent0ai/agent-zero`
   - `docker run -d -p 80:80 --restart unless-stopped --name agent-zero-rj agent0ai/agent-zero`
3. Put Nginx/Cloudflare in front for HTTPS + domain.

---

## 6) Apply your RJ model preset

In Agent Zero Settings:
- Enable **RJ custom mode**.

This auto-applies:
- Primary: `gemini-3.1-pro`
- Utility: `gemini-3.1-flash`
- Image routing: `nano-banana-pro-2`
- Video routing: `veo`

---

## 7) Production checklist

- [ ] UI login/password set
- [ ] `.env.integrations.local` present on host
- [ ] `GET /api/integrations_status` checked
- [ ] Backup created before upgrades
- [ ] HTTPS + domain configured (if public)
- [ ] Secrets rotated if ever exposed in chat/logs
