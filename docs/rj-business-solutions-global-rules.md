# RJ Business Solutions — Supreme Global Agent Rules

> Source: User-provided governance policy, version 3.0 FINAL (March 5, 2026).
> Scope in this repository: documentation-standard reference for build and delivery processes.

---

# ═══════════════════════════════════════════════════════════════════
# 🏗️  RJ BUSINESS SOLUTIONS — SUPREME GLOBAL AGENT RULES
#     Developer : Rick Jefferson | rickjeffersonsolutions.com
#     Version   : 3.0 FINAL | March 5, 2026
#     Verified  : All rules checked against official docs Mar 2026
# ═══════════════════════════════════════════════════════════════════

---

## 🖥️  SECTION 1 — MAC / ZSH ENVIRONMENT (READ FIRST — MANDATORY)

- OS: macOS (Apple Silicon / Intel)
- Shell: zsh ONLY — every command runs in zsh
- Node manager: fnm — NEVER nvm
- Package manager: pnpm — NEVER npm or yarn for project deps
- Python binary: python3 — NEVER bare 'python'
- Pip: pip3 inside active venv ONLY — NEVER global pip3
- NEVER use 'cmd /c' — Windows-only, BREAKS on Mac
- NEVER use 'powershell' — does not exist on Mac
- Command not found: run 'source ~/.zshrc' once, then retry
- setopt NO_BANG_HIST before any command containing '!'
- Escape zsh special chars (!, #, $) inside strings

### MANDATORY file-write method — NEVER heredoc in zsh:

For single files:
  python3 -c "open('file.ext','w').write('content here')"

For multiple or large files — write a .py script first, then run:
  cat > write_files.py << 'PYEOF'
  open('target.ts','w').write('full content')
  PYEOF
  python3 write_files.py

NEVER use:  cat << 'EOF' ... EOF  (breaks on zsh special chars)
NEVER pipe curl output directly to zsh

---

## ⚡  SECTION 2 — TERMINAL ANTI-FREEZE PROTOCOL

- Every command MUST be self-terminating
- Long-running servers MUST be backgrounded with '&'
  - CORRECT: uvicorn main:app --reload &
  - CORRECT: pnpm dev &
  - WRONG:   uvicorn main:app --reload      ← hangs forever
  - WRONG:   pnpm dev                       ← hangs forever
- ONE command per execution block — confirm result before next
- NEVER chain more than 2 commands with &&
- Hangs > 30 seconds: kill it, report it, retry once
- After EVERY command: explicitly confirm success or failure
- NEVER silently retry — always show exact error text first
- Check background processes:  jobs  OR  ps aux | grep [name]
- Kill by port:  kill $(lsof -ti:[port]) 2>/dev/null
- Kill by name:  pkill -9 -f "process-name" 2>/dev/null

---

## 🔁  SECTION 3 — ANTI-LOOP PROTOCOL (ZERO TOLERANCE)

- Same command run more than TWICE → STOP immediately
- Same fix attempted more than TWICE → STOP, show verbatim error
- NEVER enter fix → break → fix → break silently
- Stuck → output EXACT error text → WAIT for instruction
- NEVER assume a fix worked — run a verification command
- Max retries per error: 2
- On 3rd failure → STOP → summarize all attempts → ask me
- Repeating same file write → STOP → show current file state

---

## 📦  SECTION 4 — ATOMIC BUILD PROTOCOL

- Break ALL tasks into single atomic steps
- Max chunk per message: 1 file OR 1 function OR 1 route
- NEVER skip or combine steps
- Confirm each step completed before proceeding

### Universal build order (follow every time):
1.  Scaffold folder structure
2.  .env.example + install dependencies
3.  Database schema (schema.sql)
4.  Backend models (one file at a time)
5.  Backend routes / API endpoints (one router at a time)
6.  Authentication system
7.  Frontend pages (one page at a time)
8.  Frontend components (one component at a time)
9.  Payment integration
10. Testing
11. Deployment config
12. GitHub push

---

## 🏗️  SECTION 5 — 10-PHASE ENTERPRISE BUILD PIPELINE

Use for all SaaS, enterprise, or complex multi-feature builds.
Each phase → fresh context → structured JSON output → feeds Phase N+1.
Validate between every phase before proceeding.

Phase 1  STRATEGY     → vision, business_case, competitive_analysis, monetization_plan
Phase 2  PRD          → personas, feature_list (P0/P1/P2), acceptance_criteria, NFR, release_phases
Phase 3  ARCHITECTURE → C4 diagrams (Mermaid), ERD (SQL), OpenAPI 3.1 spec, 10+ ADRs, infra_plan
Phase 4  DESIGN       → design_tokens (CSS vars), component_library, screen_inventory, responsive_strategy
Phase 5  SCAFFOLD     → complete file tree, all config files, docker-compose, .env.example
Phase 6  BACKEND      → all .py / .ts files: models, schemas, routers, services, tests, migrations
Phase 7  FRONTEND     → all .tsx/.ts files: pages, components, hooks, stores, tests
Phase 8  INFRA        → GitHub Actions YAML, Dockerfiles, K8s manifests, Terraform, monitoring
Phase 9  SECURITY     → OWASP Top 10 audit, fix patches, dependency scan, secrets audit
Phase 10 DEPLOY+DOCS  → README, CHANGELOG, SECURITY.md, DEPLOYMENT.md, RUNBOOK.md, git push

### Validation gates (must PASS before next phase starts):
Gate 1  → ≥3 real competitors, TAM/SAM/SOM are numbers, pricing has dollar amounts
Gate 2  → ≥3 personas, all P0 features have Given/When/Then, NFR has specific numbers
Gate 3  → ERD SQL parseable, ≥10 ADRs, all API paths trace to a user story
Gate 4  → every PRD screen in screen_inventory, WCAG AA contrast verified
Gate 5  → docker compose config passes, all version numbers resolve to real packages
Gate 6  → ruff check + mypy + pytest all pass
Gate 7  → tsc --noEmit + eslint + next build all pass
Gate 8  → terraform validate + kubeval + actionlint all pass
Gate 9  → 0 critical findings, 0 high findings, 0 hardcoded secrets anywhere

---

## 🛠️  SECTION 6 — VERIFIED TECH STACK (March 5, 2026)

### Frontend
- Next.js:        16.1.6  — App Router ONLY, NEVER Pages Router
- React:          19.2.4
- TypeScript:     5.7+    — strict mode ON, NEVER 'any', NEVER plain JS
- Tailwind CSS:   v4      — NO tailwind.config.js, use @import + @theme in globals.css
- shadcn/ui:      3.5.0
- Framer Motion:  latest  — all transitions and interactions
- Zustand:        5.x     — client state only
- TanStack Query: 5.x     — all server state / data fetching
- React Hook Form + Zod   — ALL forms, client AND server validation
- Lucide React            — icons
- next/font               — self-host ALL fonts, zero external font requests
- next/image              — ALL images, auto-optimize, WebP, prevent CLS
- next/script             — ALL third-party scripts, deferred, non-blocking

### Next.js 16 BREAKING CHANGES (non-negotiable):
- proxy.ts NOT middleware.ts (file rename + function rename)
- Named export must be 'proxy' not 'middleware'
- skipProxyUrlNormalize NOT skipMiddlewareUrlNormalize
- ALL async APIs (cookies, headers, params, searchParams) are
  async ONLY — synchronous access fully removed in v16
  ALWAYS: const { id } = await params
- Node.js 20.9+ required minimum
- Turbopack is default for dev AND build
- ESLint flat config (eslint.config.mjs) — legacy .eslintrc removed
- 'next lint' command removed — use ESLint CLI directly
- 'next build' no longer runs linting
- cacheComponents replaces experimental.dynamicIO
- serverRuntimeConfig + publicRuntimeConfig removed — use env vars
- NEXT_PUBLIC_ prefix required for ALL client-accessible env vars
- All parallel route slots require explicit default.js files
- images.domains deprecated — use images.remotePatterns
- images.minimumCacheTTL default changed to 4 hours (14400s)
- next/legacy/image deprecated — use next/image
- AMP support fully removed
- pnpm create next-app — always run with --yes flag
- NEVER put eslint config inside next.config.ts
- Add app/global-error.tsx — uncaught error fallback for entire app
- Add app/global-not-found.tsx — 404 fallback for all unmatched routes
- Use taint API to prevent sensitive server data reaching client
- Server Actions MUST verify authorization — NEVER trust client auth
- NEVER call Route Handlers from Server Components (extra server round trip)
- Use <Suspense> around ALL Dynamic API usage (cookies, searchParams)
- Dynamic APIs opt ENTIRE route into dynamic rendering — be intentional
- Use Promise.all() for parallel data fetches — NEVER waterfall
- Use connection() before reading process.env at runtime in Server Components
- Use useReportWebVitals hook — send Core Web Vitals to analytics
- Run @next/bundle-analyzer before every production deploy
- Add sitemap.ts + robots.ts to every public-facing project
- Add opengraph-image.tsx (1200×630px) to every public-facing page
- Add unique <title> + meta description (150-160 chars) on every page

### Backend — Cloudflare Workers (PRIMARY for ALL new builds)
- Runtime:     Cloudflare Workers + Hono framework
- Language:    TypeScript strict
- wrangler.toml → PROJECT ROOT always (never inside apps/)
- Hono install → PROJECT ROOT: pnpm add hono from monorepo root
- wrangler deploy → runs from PROJECT ROOT always
- compatibility_date → set to TODAY's date on every new project
- compatibility_flags: ["nodejs_compat"] — ALWAYS include
- Run wrangler types after EVERY binding or package change
- Structured JSON logging: console.log(JSON.stringify({...}))
- console.error for errors, console.warn for warnings
- Enable observability in ALL wrangler.toml configs
- NEVER use global mutable state — leaks between requests
- Pass state via function args or env bindings only
- NEVER use Math.random() for security — use crypto.randomUUID()
- Timing-safe secret comparison: crypto.subtle.timingSafeEqual()
- Use ctx.waitUntil() for background work after response sent
- NEVER destructure ctx: const { waitUntil } = ctx ← BREAKS
- Always: ctx.waitUntil(promise) ← CORRECT
- Use bindings (D1, KV, R2, Queue) — NEVER REST API from Worker
- Stream large responses — NEVER buffer with await response.text()
- NEVER use passThroughOnException() — use explicit try/catch
- Use service bindings for Worker-to-Worker calls (zero network hop)
- Use Hyperdrive for remote PostgreSQL connections from Workers
- Use Workers Static Assets for static sites — prefer over Pages

### Cloudflare Workers — wrangler.toml template (every project):

name = "project-worker"
main = "src/index.ts"
compatibility_date = "2026-03-05"
compatibility_flags = ["nodejs_compat"]

[observability]
enabled = true
[observability.logs]
head_sampling_rate = 1
[observability.traces]
enabled = true
head_sampling_rate = 0.01

[[d1_databases]]
binding = "DB"
database_name = "rj-credit-pro-db"
database_id = "636221a1-c728-4726-86be-ab40b4071297"

[[kv_namespaces]]
binding = "SESSIONS"
id = "d6aa41f7a0294edb9594c56d0a74f77b"

[[kv_namespaces]]
binding = "CACHE"
id = "9e1cb9202d884c32a9fa653cbd45e63c"

[[kv_namespaces]]
binding = "RATE_LIMITS"
id = "62fb4d47abb645788db1aa889338a34d"

[[r2_buckets]]
binding = "ASSETS"
bucket_name = "rj-credit-pro-assets"

[[queues.producers]]
binding = "JOBS"
queue = "rj-credit-pro-jobs"

[env.production]
name = "project-worker-production"

[env.staging]
name = "project-worker-staging"

### Backend — FastAPI (AI/ML heavy builds ONLY)
- Python 3.13+ ONLY
- FastAPI 0.135.1, Pydantic v2.7+, SQLAlchemy 2.0 async
- Pydantic v1 support dropped — NEVER use v1 syntax
- asyncpg driver, Alembic async migrations, Uvicorn 0.34+
- SQLAlchemy syntax: Mapped[], mapped_column() — no legacy Column()
- ALWAYS: python3 -m venv venv && source venv/bin/activate
- ALWAYS pip3 install inside active venv — NEVER globally
- pyproject.toml NOT requirements.txt

### Database — Cloudflare First
- Edge:    Cloudflare D1 (SQLite) — PRIMARY for Workers builds
- Hosted:  Supabase PostgreSQL 17 — for FastAPI builds
- Cache:   Cloudflare KV — replaces Redis for Workers
- Storage: Cloudflare R2 — replaces S3/Supabase Storage
- Queue:   Cloudflare Queues — replaces Bull/Celery
- Stateful: Cloudflare Durable Objects — real-time, coordination, WebSocket
- Vector:  Cloudflare Vectorize — replaces Pinecone
- ALWAYS enable RLS on ALL Supabase tables
- ALWAYS parameterized queries — NEVER string concatenation

### RJ Business Solutions Cloudflare Resource IDs:
D1 Database:   rj-credit-pro-db → 636221a1-c728-4726-86be-ab40b4071297
KV SESSIONS:   d6aa41f7a0294edb9594c56d0a74f77b
KV CACHE:      9e1cb9202d884c32a9fa653cbd45e63c
KV RATE_LIMITS:62fb4d47abb645788db1aa889338a34d
R2 Bucket:     rj-credit-pro-assets
Queue:         rj-credit-pro-jobs
Pages Project: rj-credit-pro → https://rj-credit-pro.pages.dev

### Auth
- Primary:  Supabase Auth + NextAuth v5
- JWT:      RS256 ONLY — NEVER HS256 in production
- Access:   15 min max, Refresh: 7 day rotation
- Passwords: argon2id ONLY — NEVER bcrypt, MD5, SHA1, plain text
- CAPTCHA:  Cloudflare Turnstile — NEVER reCAPTCHA
- Sessions: Cloudflare KV with 24hr TTL
- Rate limit ALL auth endpoints via Cloudflare KV
- CSRF protection on all state-changing endpoints

### Payments — MANDATORY
- Stripe ONLY — no PayPal, Square, Braintree, or any other provider
- Always build: subscriptions + one-time + customer portal
- Verify Stripe webhook signatures on EVERY event
- Handle ALL 6 Stripe webhooks:
  checkout.session.completed
  customer.subscription.created
  customer.subscription.updated
  customer.subscription.deleted
  invoice.payment_succeeded
  invoice.payment_failed

### Credit Monitoring — MyFreeScoreNow ONLY
- MANDATORY: MyFreeScoreNow ONLY — NEVER Experian/TransUnion/Equifax/Credit Karma directly
- AID: RickJeffersonSolutions
- Base URL: https://api.myfreescorenow.com/api
- Auth: rickjefferson@rickjeffersonsolutions.com
- Default PID: 49914
- PID + commission table:
  49914 → $29.90/mo, 7-day $1 trial, $11.00/mo commission
  75497 → $29.90/mo, no trial,       $12.25/mo commission
  51271 → $29.90/mo, 7-day $1 trial, $11.00/mo commission
  26081 → $24.97/mo, 7-day $1 trial, $7.00/mo  commission
  51314 → $29.90/mo, 7-day $1 trial, $11.00/mo commission
  30639 → $39.90/mo, no trial,       $16.00/mo commission
- Enrollment URL: https://myfreescorenow.com/enroll/?AID=RickJeffersonSolutions&PID={pid}
- MFSN API endpoints:
  POST /auth/login                          → JWT token
  POST /auth/3B/report.json                 → 3-bureau report
  POST /auth/v2/3B/epic/report.json         → Epic Pro report
  POST /auth/enroll/start                   → enrollment step 1
  POST /auth/enroll/idverification          → enrollment step 2
  POST /auth/enroll/updatecard             → enrollment step 3
  POST /auth/enroll/securityquestions      → enrollment step 4
  POST /auth/snapshot/credit/enroll        → credit snapshot enroll
  POST /auth/snapshot/funding/enroll       → funding snapshot enroll
  POST /auth/snapshot/{credit|funding}/verify → verify snapshot
  POST /auth/snapshot/{credit|funding}/score  → get snapshot score
  POST /auth/logout                         → logout

### Infrastructure — Cloudflare Maximalist
- CDN + DNS + WAF + DDoS: Cloudflare (already configured)
- Frontend: Cloudflare Pages PRIMARY → Vercel fallback only
- Backend:  Cloudflare Workers PRIMARY → Railway/Fly.io fallback
- CI/CD:    GitHub Actions — auto-deploy on push to main
- Containers: Docker + docker-compose for LOCAL DEV ONLY
- IaC:      Terraform 1.14.6 + Wrangler CLI
- Monitoring: Sentry + Cloudflare Analytics + Workers Observability
- NEVER use: AWS, GCP, Azure, Netlify, Heroku, DigitalOcean

### AI Stack
- Gateway:       Cloudflare AI Gateway — ALL LLM calls route through it
- Edge AI:       Workers AI (@cf/meta/llama-3.1-8b-instruct)
- Agents SDK:    @cloudflare/agents — for stateful AI agents on DO
- AIChatAgent:   built-in persistent chat, resumable streams, tools
- Orchestration: CrewAI Flows with typed Pydantic state
- LLM Routing:   OpenRouter through CF AI Gateway
- Embeddings:    Cloudflare Vectorize + HuggingFace
- NEVER call OpenAI/Anthropic directly — always through CF AI Gateway

---

## ⚙️  SECTION 7 — CLOUDFLARE WORKFLOWS: RULES OF WORKFLOWS

Apply these to every multi-step build pipeline and background job.

- Steps MUST be idempotent — check if op already happened before doing it
- One step = one atomic operation — NEVER put 2 unrelated calls in one step
- NEVER store state outside step.do() returns — engine hibernates and loses it
- All state must come exclusively from step.do() return values
- NEVER mutate the event object — changes NOT persisted across steps
- Step names MUST be deterministic — NEVER use Date.now() or Math.random() in names
- Step names are the cache key — same name = cached result on retry
- ALWAYS await step.do() and await step.sleep() — unawaited steps swallow errors
- Wrap Promise.race()/Promise.any() inside a step.do() for deterministic caching
- Use createBatch() when creating multiple Workflow instances — NEVER loop create()
- Step state limit: 1 MiB max — store large data in R2, return reference key only
- Step timeout: 30 minutes max — use step.waitForEvent() for longer operations
- Non-deterministic values (Math.random, Date.now) MUST be inside step.do()
- Control flow conditions MUST be based on event.payload or step returns only
- DB connections (non-serializable) are OK outside steps — re-created automatically
- Composite instance IDs: instanceId = userId + '-' + crypto.randomUUID().slice(0,6)
- NEVER use raw userId as Workflow instance ID — must be unique across all runs
- Logic outside steps may execute more than once on engine restart — no side effects
- console.log() outside steps may log twice — put logs inside steps
- Use step.waitForEvent() for human-in-the-loop approval flows
- Import: from 'cloudflare:workers' → WorkflowEntrypoint

### CrewAI Flows pattern (all multi-agent pipelines):
from crewai.flow.flow import Flow, listen, start, router
from pydantic import BaseModel, Field

class PhaseState(BaseModel):
    data: dict = Field(default_factory=dict)
    validated: bool = False
    errors: list = Field(default_factory=list)

class ProjectFlow(Flow[PhaseState]):
    @start()
    def phase_one(self): ...

    @router(phase_one)
    def validate_one(self):
        return "proceed" if self.state.validated else "retry"

    @listen("proceed")
    def phase_two(self): ...

---

## 🏛️  SECTION 8 — DURABLE OBJECTS: RULES OF DURABLE OBJECTS

Use Durable Objects when you need:
- Coordination (chat, multiplayer, collaborative docs)
- Strong consistency (inventory, booking, turn-based logic)
- Per-entity storage (multi-tenant SaaS, per-user data)
- Persistent WebSocket connections (real-time, notifications)
- Scheduled work per entity (subscription renewals, game timers)

Use plain Workers (stateless) when you need:
- API endpoints, proxies, transformations with no shared state
- Maximum global distribution (nearest edge)
- High fan-out (each request fully independent)

### Core rules:
- One Durable Object per logical unit — chat room, game session, user, tenant
- NEVER create one global Durable Object for all requests — becomes a bottleneck
- Throughput: ~500-1000 req/sec simple, ~200-500 req/sec complex — shard beyond this
  Required DOs = (Total req/sec) / (req/sec per DO capacity)
- Use getByName() with deterministic strings — same input always same DO
- Use newUniqueId() only when creating new instances and storing the mapping in D1
- Use SQLite storage (new_sqlite_classes) — NOT legacy KV storage for new DOs
- Use blockConcurrencyWhile() in constructor for schema migrations ONLY
- NEVER use blockConcurrencyWhile() on every request — kills throughput (200 req/sec max)
- For regular ops: rely on input/output gates and write coalescing instead
- Use transaction() for atomic read-modify-write — NOT blockConcurrencyWhile()
- Multiple writes without await = automatically coalesced into one atomic transaction
- In-memory state is lost on eviction/crash — always persist critical state to SQLite
- Use in-memory cache for performance, invalidate on writes, rebuild from SQLite on miss
- Add SQL indexes on all frequently-filtered columns — idx_table_column naming
- Use RPC methods (compatibility_date 2024-04-03+) — NOT legacy fetch() handler
- ALWAYS await DO stub method calls — unawaited calls swallow errors and lose returns
- Wrap risky operations in try/catch — uncaught exceptions can terminate DO instance
- Check error.retryable and error.overloaded on DO call failures
- Use Hibernation API (ctx.acceptWebSocket) for WebSocket — NOT ws.accept()
- setWebSocketAutoResponse for ping/pong — does NOT wake hibernating DO
- Store per-connection metadata with ws.serializeAttachment() — survives hibernation
- ALWAYS call ws.close(code, reason) in webSocketClose — prevents 1006 errors
- Use Alarms API (ctx.storage.setAlarm) for per-entity scheduled work
- Alarms do NOT repeat — call setAlarm() again in alarm() handler for repeat
- DO does NOT know its own name/ID — pass via init() method and store in SQLite
- Location hint: env.MY_DO.get(id, { locationHint: 'wnam' }) for US-West
- Use parent/child DO pattern for hierarchical data (server → matches, workspace → projects)
- Non-storage I/O like fetch() allows request interleaving — use optimistic locking
- DO class storage: declare in wrangler.toml migrations:
  [[durable_objects.bindings]]
  name = "MY_DO"
  class_name = "MyDurableObject"
  [[migrations]]
  tag = "v1"
  new_sqlite_classes = ["MyDurableObject"]

### Cloudflare Agents SDK (for AI agents):
- Install: pnpm add @cloudflare/agents
- Each agent runs on a Durable Object — stateful, persistent, global
- Extend Agent for general agents, AIChatAgent for chat agents
- @callable() decorator exposes typed RPC methods to clients
- Built-in SQL database + KV state syncs to clients in real-time
- State survives restarts, deploys, hibernation
- useAgent() React hook for client-side connection
- useAgentChat() React hook for AI chat UI
- Schedule tasks: this.schedule(delay, 'methodName', params)
- Browse web: built-in headless browser API
- Human-in-the-loop: step.waitForEvent() approval flows
- Expose tools via MCP for other agents and LLMs
- Stream responses over WebSocket or Server-Sent Events

---

## 🔐  SECTION 9 — SECURITY (NON-NEGOTIABLE)

- NEVER hardcode API keys, secrets, tokens, or passwords anywhere
- Workers secrets: wrangler secret put KEY_NAME (interactive prompt only)
  Generate secrets with: openssl rand -base64 32
- Next.js secrets: .env.local ONLY — never committed
- NEVER commit any .env file — always in .gitignore
- JWT: RS256 ONLY — NEVER HS256 in production
- Access tokens: 15 min max | Refresh tokens: 7 day rotation
- Passwords: argon2id ONLY — NEVER bcrypt, MD5, SHA1, plain text
- CORS: explicit origins ONLY — NEVER wildcard '*' in production
- Input validation: Zod (frontend) + Pydantic v2 (Python) on ALL inputs
- SQL: parameterized queries ONLY — NEVER string concatenation
- Timing-safe comparison: crypto.subtle.timingSafeEqual() for secrets
- Security headers (ALL required in production):
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: (configured per-project)
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: (configured per-project)
- HTTPS enforced in all production configs
- No global mutable state in Workers — leaks between requests
- GitHub: NEVER put tokens in code, prompts, or committed files
- Git auth: SSH keys or gh auth login ONLY — zero hardcoded PATs
- Run wrangler types after every binding change
- Server Actions: ALWAYS verify authorization — never trust client
- Use taint API to prevent sensitive data reaching client components
- Add Content Security Policy via Next.js proxy.ts headers
- OWASP Top 10: check ALL items before every production deploy
- Run pnpm audit before every deploy — zero high/critical CVEs
- Run pip-audit before every FastAPI deploy

---

## 📊  SECTION 10 — OBSERVABILITY & PERFORMANCE BUDGETS

### Sentry (errors — required in all production builds)
- Initialize in instrumentation.ts (Next.js 16 standard location)
- Capture server AND client errors separately in instrumentation
- Add Sentry.captureException(error) in every catch block
- Upload source maps on every deploy via CI
- tracesSampleRate: 0.1 in production (10%) — NEVER 1.0 in prod
- Set environment: 'production' | 'staging' | 'development'

### Cloudflare Workers Observability (built-in — always enable)
- observability.enabled: true in ALL wrangler.toml files
- logs.head_sampling_rate: 1 for low-traffic, 0.1 for high-traffic
- traces.enabled: true, head_sampling_rate: 0.01 for production
- Structured JSON ONLY: console.log(JSON.stringify({ message, ...context }))
- console.error for errors (shows as ERROR in dashboard)
- console.warn for warnings (shows as WARN in dashboard)

### Performance budgets (enforce in CI — fail build if exceeded)
- LCP  (Largest Contentful Paint):    < 2.5 seconds
- INP  (Interaction to Next Paint):   < 200ms
- CLS  (Cumulative Layout Shift):     < 0.1
- p95 API response time:              < 500ms
- p99 API response time:              < 1000ms
- Error rate alert threshold:         > 1%
- Bundle size: run @next/bundle-analyzer before every deploy
- Lighthouse score target: > 90 on all 4 categories

---

## 📌  SECTION 11 — DEPENDENCY MANAGEMENT

- Pin ALL versions exactly in package.json — NEVER ^ or ~ in production
- pnpm-lock.yaml MUST be committed — NEVER in .gitignore
- pnpm audit before every deploy — zero high/critical vulnerabilities
- pnpm dedupe after adding packages — prevents version conflicts
- pip-audit before every FastAPI deploy — zero high/critical CVEs
- wrangler types after EVERY binding or package change
- Python: pin all versions in pyproject.toml — NEVER floating
- Configure Dependabot or Renovate for weekly dependency PRs
- Review and merge dependency PRs weekly — never let them pile up

---

## ♿  SECTION 12 — ACCESSIBILITY + SEO (EVERY PUBLIC BUILD)

### Accessibility (WCAG 2.1 AA — mandatory on all UI)
- Text contrast: minimum 4.5:1 (AA) — verify with Colour Contrast Analyser
- Interactive elements: minimum 44×44px touch target
- Images: meaningful alt text — NEVER empty alt on content images
- Forms: <label htmlFor> linked to every input
- Modals: focus trap + Escape key dismissal
- Keyboard navigation: ALL elements reachable via Tab
- Skip-to-content link at top of every page layout
- Use eslint-plugin-jsx-a11y — all warnings are errors
- Test with VoiceOver (Mac built-in) before every launch

### SEO (every public-facing page — non-negotiable)
- Unique <title> on every page via Next.js Metadata API
- Meta description on every page (150-160 chars)
- OG image (1200×630px) via opengraph-image.tsx
- Canonical URL on all pages
- sitemap.ts — auto-generated, submit to Google Search Console
- robots.ts — allow public, block /api/ and /admin/
- JSON-LD structured data on landing + product pages
- Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1
- useReportWebVitals hook — send vitals to analytics on all pages

---

## 💻  SECTION 13 — LOCAL DEVELOPMENT SETUP

### Required global installs (run ONCE on fresh Mac):
brew install fnm pnpm gh wrangler
fnm install 20 && fnm use 20 && fnm default 20
gh auth login

### For EVERY new project (in order):
1.  Clone or init repo
2.  pnpm install
3.  cp .env.example .env.local — fill in all values
4.  docker compose up -d — starts postgres + redis locally
5.  pnpm db:migrate — runs migrations
6.  pnpm dev — starts Next.js on :3000

### .vscode/extensions.json (auto-install for all team members):
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "usernamehans9.vscode-cloudflare-workers",
    "sentry.vscode-sentry",
    "eamodio.gitlens",
    "streetsidesoftware.code-spell-checker",
    "biomejs.biome"
  ]
}

### .vscode/settings.json (always include):
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  },
  "typescript.tsdk": "node_modules/typescript/lib",
  "tailwindCSS.experimental.classRegex": [
    ["cn\(([^)]*)\)", "["'`]([^"'`]*).*?["'`]"]
  ],
  "eslint.rules.customizations": [
    { "rule": "@typescript-eslint/no-floating-promises", "severity": "error" },
    { "rule": "jsx-a11y/*", "severity": "error" }
  ]
}

---

## 🐙  SECTION 14 — GITHUB AUTO-DEPLOY (MANDATORY AFTER EVERY BUILD)

Execute these steps after ANY completed build:
1.  git init (if needed)
2.  git branch -M main
3.  Create .gitignore with all required entries below
4.  Create README.md with RJ Business Solutions branding
5.  git add .
6.  git commit -m "feat: [name] — RJ Business Solutions March 2026"
7.  gh repo create rjbizsolution23-wq/[project-name] --public --source=. --push
8.  NEVER use hardcoded PAT tokens — use gh auth login or SSH only

### Required .gitignore entries (ALL must be present):
node_modules/
.env
.env.local
.env.production
.env.staging
__pycache__/
*.pyc
.next/
.next/dev/
dist/
build/
.DS_Store
*.log
.turbo/
coverage/
.pytest_cache/
.mypy_cache/
.ruff_cache/
.wrangler/
venv/
*.egg-info/
.terraform/
*.tfstate
*.tfstate.backup
pnpm-debug.log*

---

## 📁  SECTION 15 — REQUIRED PROJECT STRUCTURE (EVERY BUILD)

project-name/
├── .github/
│   └── workflows/
│       ├── ci.yml              ← lint + typecheck + test on PR
│       └── deploy.yml          ← deploy on push to main
├── .vscode/
│   ├── settings.json
│   ├── extensions.json
│   ├── launch.json
│   └── tasks.json
├── apps/
│   ├── web/                    ← Next.js 16 (App Router)
│   │   ├── app/
│   │   │   ├── layout.tsx
│   │   │   ├── page.tsx
│   │   │   ├── proxy.ts        ← NOT middleware.ts
│   │   │   ├── loading.tsx
│   │   │   ├── error.tsx
│   │   │   ├── not-found.tsx
│   │   │   ├── global-error.tsx    ← catches all uncaught errors
│   │   │   ├── global-not-found.tsx ← 404 for all unmatched routes
│   │   │   ├── sitemap.ts          ← auto-generated sitemap
│   │   │   ├── robots.ts           ← crawler rules
│   │   │   ├── (auth)/
│   │   │   │   ├── login/page.tsx
│   │   │   │   ├── register/page.tsx
│   │   │   │   ├── forgot-password/page.tsx
│   │   │   │   └── layout.tsx
│   │   │   ├── (dashboard)/
│   │   │   │   ├── layout.tsx
│   │   │   │   ├── page.tsx
│   │   │   │   └── [domain]/
│   │   │   │       ├── page.tsx
│   │   │   │       ├── [id]/page.tsx
│   │   │   │       ├── new/page.tsx
│   │   │   │       └── default.js  ← REQUIRED in Next.js 16
│   │   │   └── opengraph-image.tsx ← 1200×630 OG image
│   │   ├── components/
│   │   │   ├── ui/             ← shadcn/ui components
│   │   │   ├── layouts/
│   │   │   └── forms/
│   │   ├── lib/
│   │   │   ├── api-client.ts
│   │   │   ├── auth.ts
│   │   │   └── utils.ts
│   │   ├── hooks/
│   │   ├── stores/
│   │   ├── styles/
│   │   │   └── globals.css     ← @import "tailwindcss" + @theme
│   │   └── instrumentation.ts  ← Sentry init (server + client)
│   └── api/                    ← Cloudflare Worker (Hono) OR FastAPI
├── database/
│   ├── schema.sql
│   └── migrations/
├── docs/
│   ├── ARCHITECTURE.md         ← C4 diagrams, tech decisions, ADRs
│   ├── API.md                  ← from OpenAPI 3.1 spec
│   ├── DEPLOYMENT.md           ← dev/staging/prod + rollback procedure
│   ├── RUNBOOK.md              ← ops, incident response, escalation
│   ├── SECURITY.md             ← vulnerability reporting process
│   ├── CONTRIBUTING.md         ← branch, commit format, PR process
│   ├── CHANGELOG.md            ← conventional commits (v0.1.0 entry)
│   └── TROUBLESHOOTING.md      ← common issues per environment
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── monitoring/
│   ├── prometheus/prometheus.yml
│   └── grafana/dashboards/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── .env.example                ← every env var with description
├── .gitignore
├── docker-compose.yml          ← local dev: postgres + redis + services
├── package.json                ← exact pinned versions, NO ^ or ~
├── pnpm-workspace.yaml
├── turbo.json
├── wrangler.toml               ← at PROJECT ROOT always
└── README.md                   ← with RJ Business Solutions branding

---

## 🎨  SECTION 16 — CODE QUALITY STANDARDS

- TypeScript: strict mode ON — zero 'any' types — zero implicit any
- Python: PEP8 + full type hints on all functions + mypy strict
- Functions: max 50 lines — split if longer
- Comments: explain WHY not WHAT
- Zero TODO comments in production code — finish it or delete it
- Zero placeholder code — 100% complete working implementations only
- Every API endpoint: error handling + correct HTTP status codes
- Every form: Zod client + Pydantic/Zod server validation
- Every DB query: error handling, never swallow exceptions
- Workers: NEVER floating promises — always await, return, or waitUntil
- Workers: NEVER global mutable state — pass via function args or env
- ESLint rules (enforced as errors, never warnings):
  @typescript-eslint/no-floating-promises: error
  @typescript-eslint/no-explicit-any: error
  jsx-a11y/* all rules: error

---

## 🧪  SECTION 17 — TESTING STANDARDS

- Workers: @cloudflare/vitest-pool-workers — runs in real Workers runtime
  Confirm wrangler.toml has nodejs_compat — vitest injects it but prod needs it
- Python: pytest inside venv, pytest-asyncio for async tests
- TypeScript: Jest + React Testing Library
- E2E: Playwright
- Unit tests: every utility function and service method
- Integration tests: every API endpoint (happy + error paths)
- Component tests: every form, every critical UI interaction
- All tests in /tests directory — mirror src structure
- Test before every commit: pnpm test && python3 -m pytest (in venv)
- CI blocks merge if any test fails

---

## 🚨  SECTION 18 — INCIDENT RESPONSE & ROLLBACK

### Rollback procedures:
Cloudflare Workers:
  wrangler rollback --env production

Cloudflare Pages:
  wrangler pages deployment list --project-name [name]
  wrangler pages deployment rollback [deployment-id] --project-name [name]

Git (any platform):
  git revert HEAD --no-edit && git push origin main

### Incident severity levels:
P0 — Production down, all users affected    → fix within 1 hour
P1 — Major feature broken, most affected    → fix within 4 hours
P2 — Minor feature broken, some affected    → fix within 24 hours
P3 — Cosmetic or edge case                  → fix next sprint

### On every P0/P1 incident (in order):
1.  Rollback immediately — fix-forward is second choice
2.  Check Cloudflare Workers Observability dashboard
3.  Check Sentry error spike + stack trace
4.  Post user status update within 15 minutes
5.  Write 5-whys incident report after resolution

### Feature flags (prevent incidents proactively):
- Store flags in Cloudflare KV: key = 'ff:feature-name', value = 'true'/'false'
- ALL new features behind a flag on first deploy — NEVER dark-launch naked
- Rollout stages: 1% → 10% → 50% → 100% with monitoring at each stage
- Kill switch: flip KV flag to 'false' to disable any feature in <1 minute

---

## 📋  SECTION 19 — RESPONSE FORMAT (MANDATORY)

- Tell me WHAT before doing it
- Confirm COMPLETION after every step with verification result
- On ANY failure: show exact error → explain why → propose fix → WAIT for approval
- NEVER say "this should work" — verify it actually works
- NEVER auto-proceed on failure — always surface and wait

Progress format (use this exactly):
  ✅ DONE: [what completed + verification command result]
  🔄 NEXT: [exactly what comes next]
  ⚠️ BLOCKED: [needs input — describe precisely what is needed]

---

## 🚧  SECTION 20 — ALWAYS STOP AND ASK BEFORE:

- Deleting any files or directories
- Dropping database tables or running destructive migrations
- Changing authentication configuration
- Modifying production environment variables
- Running sudo commands
- Installing global packages (npm -g, pip3 globally outside venv)
- Pushing directly to main branch (use feature branches)
- Running wrangler deploy to production without explicit confirmation

---

## 📚  SECTION 21 — THE 12 ESSENTIAL DOCUMENTS (ENTERPRISE BUILDS)

1.  Vision Document   — problem, solution, ICP, KPIs            (Phase 1)
2.  Business Case     — TAM/SAM/SOM, ROI, pricing, risks        (Phase 1)
3.  PRD               — personas, user stories, criteria, NFRs  (Phase 2)
4.  SAD               — C4 diagrams, tech stack + ADRs          (Phase 3)
5.  ERD + Schema      — tables, columns, constraints, indexes   (Phase 3)
6.  API Specification — OpenAPI 3.1, auto-gen type-safe client  (Phase 3)
7.  ADRs (≥10)        — why each tech decision was made         (Phase 3)
8.  Design System     — tokens, components, screen inventory    (Phase 4)
9.  Test Plan         — pyramid, tools, coverage, entry/exit    (Phase 6-7)
10. DEPLOYMENT.md     — step-by-step + rollback procedure       (Phase 8)
11. RUNBOOK.md        — ops, incident response, SLO/SLA, DR     (Phase 8)
12. README + CHANGELOG + SECURITY.md — standard repo docs       (Phase 10)

### Automated instead of documented:
Coding standards    → ESLint + Prettier + Ruff configs
Git workflow        → CONTRIBUTING.md
Test cases          → /tests files (code IS the test cases)
Test data           → conftest.py fixtures
Bug log             → GitHub Issues
Perf report         → k6/Locust in CI output
Security scan       → Trivy + Semgrep in CI (auto-generated)
Changelog           → auto-generated from Conventional Commits

---

## 🔄  SECTION 22 — SLASH COMMAND WORKFLOWS

Invoke with /workflow-name in Antigravity agent chat:

/build-saas         → Next.js 16 + CF Workers + D1 + Stripe + MFSN full SaaS
/build-landing      → Conversion funnel: Framer Motion + Tailwind v4 + Stripe
/build-api          → CF Worker API: Hono + D1 + KV + auth + rate limiting
/build-dashboard    → Admin dashboard: CRUD + CF Analytics + RLS + charts
/build-agent        → CF Agents SDK: AIChatAgent + tools + human-in-the-loop
/build-workflow     → CF Workflow: multi-step durable pipeline with retries
/build-do           → Durable Object: SQLite + WebSocket + Hibernation API
/build-crewai       → 10-phase CrewAI Flow pipeline with Pydantic state
/deploy-cf          → Build → push GitHub → deploy CF Pages + Worker
/new-feature        → Add one feature atomically to existing project
/fix-bug            → Surface error → propose fix → confirm → apply
/security-audit     → Full OWASP Top 10 checklist on codebase
/audit-codebase     → Full folder-by-folder code audit and fix loop
/build-docs         → Generate all 12 essential docs for current project
/perf-audit         → Bundle analysis + Core Web Vitals + Lighthouse run
/accessibility-audit → WCAG 2.1 AA full check on all UI components

---

## 🏢  SECTION 23 — COMPANY BRANDING (APPLY TO EVERYTHING)

Company:   RJ Business Solutions
Developer: Rick Jefferson
Address:   1342 NM 333, Tijeras, New Mexico 87059
Website:   https://rickjeffersonsolutions.com
Email:     rjbizsolution23@gmail.com
GitHub:    rjbizsolution23-wq
Logo:      https://storage.googleapis.com/msgsndr/qQnxRHDtyx0uydPd5sRl/media/67eb83c5e519ed689430646b.jpeg
LinkedIn:  in/rick-jefferson-314998235
TikTok:    @rick_jeff_solution
Twitter:   @ricksolutions1

Apply branding to: README headers, email templates, landing pages,
admin dashboards, error pages, PDF exports, all client-facing UI.

### README.md header template (every single project):
# [Project Name]
![RJ Business Solutions](https://storage.googleapis.com/msgsndr/qQnxRHDtyx0uydPd5sRl/media/67eb83c5e519ed689430646b.jpeg)
**Built by RJ Business Solutions** | Rick Jefferson
📍 1342 NM 333, Tijeras, NM 87059 | 🌐 rickjeffersonsolutions.com
📅 Built: March 2026 | ⚡ Stack: Next.js 16 + Cloudflare Workers

---

# ═══════════════════════════════════════════════════════════════════
# END OF GLOBAL RULES — RJ BUSINESS SOLUTIONS v3.0 FINAL
# 23 sections | verified March 5, 2026
# Apply to every project, every build, every agent session.
# No MVPs. No iterations. Production-grade or nothing.
# ═══════════════════════════════════════════════════════════════════
