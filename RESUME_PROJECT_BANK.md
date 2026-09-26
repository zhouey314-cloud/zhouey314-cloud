# Resume Project Bank

Pick two or three projects for a specific role. These are evidence notes and draft bullets, not claims of customer adoption. See the [full portfolio index](PORTFOLIO.md) for public links and status.

## Flagship projects

### Multi-Tenant Workflow

- **Problem:** Shared knowledge and approval can cross tenant or role boundaries.
- **Action:** Built a demo with role policy and a review-to-publish path.
- **Engineering:** Node.js and browser flows use the same tenant, role and state rules.
- **Evidence:** [Public demo](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/) and 10 tests.
- **Boundary:** Demo role selectors are not production authentication.
- **Resume bullet:** Built and tested a multi-tenant knowledge workflow with role checks and human review gates; documented the demo authentication boundary.

### Enterprise RAG Starter

- **Problem:** Retrieval answers need access filtering, citations and a no-answer path.
- **Action:** Built lexical, local semantic and hybrid retrieval over fictional documents.
- **Engineering:** Access control precedes retrieval output; citations and refusal behavior are explicit.
- **Evidence:** [Repository and lexical demo](https://github.com/zhouey314-cloud/enterprise-rag-starter), 19 tests and four synthetic lexical cases.
- **Boundary:** The browser demo is lexical; local embedding mode is separate. No customer knowledge base or model-quality score.
- **Resume bullet:** Implemented an access-filtered RAG starter with citations and no-answer behavior, verified with local tests and synthetic retrieval cases.

### AI Eval Engineering

- **Problem:** A passing fixture check can be mistaken for a passing model evaluation.
- **Action:** Created an offline JSONL case, rubric and release-gate kit.
- **Engineering:** Schema/provenance validation is separated from a provider-backed quality gate.
- **Evidence:** [Example report](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/example-report.md) and five synthetic fixtures.
- **Boundary:** Model quality is NOT_RUN without independent ground truth and a model run.
- **Resume bullet:** Built an offline AI evaluation kit that separates deterministic fixture validation from unrun model-quality claims.

### AI Video Workflow Engine

- **Problem:** Missing assets, render failures and human QA need a recoverable path.
- **Action:** Built an asset-gap, FFmpeg render and QA workflow.
- **Engineering:** Python state transitions and output checks produce a reproducible synthetic render.
- **Evidence:** [Six-second sample MP4](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/demo-output.mp4) and 25 tests.
- **Boundary:** The sample is synthetic; human acceptance and generated-video quality are not claimed.
- **Resume bullet:** Designed and tested a Python video workflow that tracks missing assets, renders a synthetic FFmpeg sample and retains a human QA gate.

### AI CRM Sales Copilot

- **Problem:** Pipeline, forecast and guidance diverge when they use separate opportunity records.
- **Action:** Built a browser demo around one local opportunity state.
- **Engineering:** Six-stage transitions, local audit, manager forecast and deterministic rule guidance.
- **Evidence:** [Live demo](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/), automated tests and browser reload checks.
- **Boundary:** Synthetic records, localStorage, no production authentication or real model provider.
- **Resume bullet:** Built a synthetic CRM workflow demo connecting pipeline transitions, forecast, audit and rule-based guidance on one browser-local state model.

### Portable Agent Skills

- **Problem:** Agent workflows are hard to reuse when inputs, outputs and failure paths are implicit.
- **Action:** Wrote ten single-purpose, clean-room skill contracts.
- **Engineering:** Markdown workflows plus offline Python structure and synthetic-fixture checks.
- **Evidence:** [Skill catalog](https://github.com/zhouey314-cloud/ai-agent-skills/tree/main/skills) and [examples](https://github.com/zhouey314-cloud/ai-agent-skills/tree/main/examples).
- **Boundary:** Provider-backed model quality and real user adoption are NOT_RUN.
- **Resume bullet:** Authored ten reusable agent workflow contracts with explicit inputs, outputs and failure paths, backed by offline validation and synthetic examples.

## Supporting projects

### Recruitment Review

- **Problem:** Hiring reviewers need traceable evidence and a mandatory human decision.
- **Action:** Built a synthetic evidence/risk review flow with reason and audit fields.
- **Engineering:** Browser rules and Python checks have parity cases.
- **Evidence:** [Live synthetic demo](https://zhouey314-cloud.github.io/ai-recruitment-workflow-demo/), 13 unit tests, five fixtures and 36 parity cases.
- **Boundary:** No real resumes, candidate decisions or validated model performance.
- **Resume bullet:** Built a synthetic recruitment review demo that traces evidence and risk while keeping the final decision with a human reviewer.

### Thought to X

- **Problem:** A raw idea needs structure and editorial review before publication.
- **Action:** Built a local idea-to-draft workflow and portable prompt set.
- **Engineering:** Python CLI supports a no-key prompt-only path.
- **Evidence:** [Example output](https://github.com/zhouey314-cloud/thought-to-x/blob/main/examples/destiny-example.md) and 10 unit tests.
- **Boundary:** No automated platform posting; factual and voice approval remain human.
- **Resume bullet:** Built a local idea-to-draft writing workflow with a portable CLI, tested prompt-only path and explicit human publishing gate.

### Obsidian AI Inbox

- **Problem:** Personal notes need a fast local capture and search path without broad vault access.
- **Action:** Built capture and keyword-search flows for a selected vault.
- **Engineering:** Local filesystem handling and a demo vault keep the interface inspectable.
- **Evidence:** [Interface screenshot](https://github.com/zhouey314-cloud/obsidian-ai-inbox/blob/main/docs/inbox-demo.png) and 64 local tests.
- **Boundary:** Private vault data stays on device; no claim of reading an entire Obsidian installation.
- **Resume bullet:** Built a local Obsidian inbox for selected-vault capture and keyword search, with a demo vault and local tests.

### NovaMach

- **Problem:** A B2B buyer needs to move from product discovery to a request for quotation across languages.
- **Action:** Built a fictional three-language industrial catalog and RFQ flow.
- **Engineering:** React, TypeScript and Vite with browser-local sample inquiry state.
- **Evidence:** [Live fictional preview](https://0-1-b2b-demo-demo-novamach.vercel.app/) and lint, typecheck, build and smoke checks.
- **Boundary:** Fictional brand, sample RFQs and no customer acceptance claim.
- **Resume bullet:** Built a fictional multilingual B2B product demo with a local RFQ workflow and verified build path.

### AI Director

- **Problem:** Silence-based cuts need a timeline that can be inspected and exchanged with editing tools.
- **Action:** Built an offline media/timeline prototype around a synthetic sample.
- **Engineering:** FFmpeg detection feeds a keep-list, EDL and FCPXML; SRT requires transcription input.
- **Evidence:** [Synthetic example and EDL](https://github.com/zhouey314-cloud/ai_director/tree/main/examples), timeline regression tests and local CLI smoke.
- **Boundary:** Prototype only; edit quality and optional provider integration are unverified.
- **Resume bullet:** Built a media timeline prototype that converts detected silence into inspectable keep-lists and editing interchange files, with timestamp regression checks.

## Claim guardrails

Use “self-built public demo,” “synthetic cases,” “locally verified,” or “manual deployment” where accurate. Do not claim paying customers, production integration, accepted deliveries, model-quality scores, company ownership or revenue from these repositories.
