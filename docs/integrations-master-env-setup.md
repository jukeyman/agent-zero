# Master Integration Environment Setup (Secure)

This repository now includes `.env.integrations.example` as a **safe template** for all requested integrations.

## Important security note
- Never commit real keys/tokens/secrets.
- The credentials shared in chat should be considered compromised and rotated immediately.
- Keep secrets only in local `.env` files, Docker secrets, or provider secret managers.

## How to enable all integrations safely
1. Copy template:
   - `cp .env.integrations.example .env.integrations.local`
2. Fill in real values locally.
3. Load variables at runtime (example):
   - `set -a && source .env.integrations.local && set +a`
4. Start Agent Zero in the same shell/session.

## Recommended secret storage
- Local dev: `.env.integrations.local` (gitignored by default patterns for `.env`).
- Docker: use compose `env_file` or secret mounts.
- Cloud: use provider-managed secret stores.

## Validation checklist
- Confirm required env vars are present for each enabled integration.
- Verify no secrets appear in git diff:
  - `git status --short`
  - `git diff -- .env*`
- Run a smoke test for each integration from settings/API workflow.


## Default model routing profile
- Primary reasoning/chat model: `gemini-3.1-pro`
- Preferred image generation model: `nano-banana-pro-2`
- Preferred video generation model: `veo`
- Fallback behavior: route to best available model for the requested task when preferred models are unavailable.

> Note: Image/video model execution depends on installed integrations/tools (for example MCP servers or custom extensions).


## Connectivity status check
After setting your local integration env file, you can check current connectivity coverage via API:

- `GET /api/integrations_status`

The response returns grouped counts of configured vs missing integration keys and a `fully_connected` boolean.


## RJ custom mode preset
- Agent Zero now includes a `RJ custom mode` settings toggle.
- When enabled, it auto-applies:
  - chat/browser: `gemini-3.1-pro`
  - utility: `gemini-3.1-flash`
  - image routing: `nano-banana-pro-2`
  - video routing: `veo`
- This lets you apply your full preferred routing profile in one action.
