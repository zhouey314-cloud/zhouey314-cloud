# Portfolio Index

[Visual project hub](https://zhouey314-cloud.github.io/projects.html) · [90-second flagship tour](#90-second-tour) · [Resume Project Bank](RESUME_PROJECT_BANK.md)

Status vocabulary: `LIVE_DEMO` is a public interactive preview, `LOCAL_RUNNABLE` a reproducible local path, `OFFLINE_TOOL` an offline executable, `PROTOTYPE` an unproven product path, `OPEN_SOURCE` a reusable public template and `EXPERIMENT` a bounded lab project. None means customer production.

## Flagship six

| Project | Problem | Stack | Demo / Evidence | Tests / Evidence | Status |
|---|---|---|---|---|---|
| [Multi-Tenant Workflow](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas) | Tenant isolation and review gates | Node.js, JavaScript | [Pages](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/) | 10 tests; role/state browser flow | LIVE_DEMO |
| [Enterprise RAG Starter](https://github.com/zhouey314-cloud/enterprise-rag-starter) | ACL, citations and no-answer retrieval | Python, embeddings, JS | [Pages lexical](https://zhouey314-cloud.github.io/enterprise-rag-starter/) | 19 tests; 4 synthetic lexical cases | LIVE_DEMO |
| [AI Eval Engineering](https://github.com/zhouey314-cloud/ai-eval-engineering) | Distinguish fixture checks from model quality | Python, JSONL | [Example report](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/example-report.md) | 5 synthetic fixtures; MODEL_QUALITY=NOT_RUN | LOCAL_RUNNABLE |
| [AI Video Workflow Engine](https://github.com/zhouey314-cloud/ai-video-workflow-engine) | Asset-gap, render and QA state | Python, FFmpeg | [Synthetic MP4](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/demo-output.mp4) | 25 tests; 6-second video; HUMAN_REVIEW | OFFLINE_TOOL |
| [AI CRM Sales Copilot](https://github.com/zhouey314-cloud/ai-crm-sales-copilot) | Shared opportunity/pipeline/forecast state | JavaScript, localStorage | [Pages](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/) | automated and browser/reload checks | LIVE_DEMO |
| [Portable Agent Skills](https://github.com/zhouey314-cloud/ai-agent-skills) | Reusable, explicit agent workflow contracts | Markdown, Python | [Skill catalog](https://github.com/zhouey314-cloud/ai-agent-skills/tree/main/skills) | 10 structural checks; 3 synthetic cases; model quality NOT_RUN | LOCAL_RUNNABLE |

## 90-second tour

Start at the [visual hub](https://zhouey314-cloud.github.io/projects.html). Follow a public browser flow in Multi-Tenant Workflow; inspect RAG access-filtered retrieval; see Eval's explicit quality gate; watch Video's synthetic FFmpeg output; try CRM's rule-based sales flow; then clone Portable Agent Skills and run its offline contract tests. Each repo explains its own limitations. The visuals and tests are engineering evidence, not user adoption, client acceptance or model success rates.

## Supporting

| Project | Problem / role | Status | Demo / evidence | Boundary |
|---|---|---|---|---|
| [Recruitment Review](https://github.com/zhouey314-cloud/ai-recruitment-workflow-demo) | Evidence and risk review with a human decision gate | LIVE_DEMO | [Synthetic browser demo](https://zhouey314-cloud.github.io/ai-recruitment-workflow-demo/); 13 tests and 36 parity cases | No real candidate decisions |
| [Thought to X](https://github.com/zhouey314-cloud/thought-to-x) | Idea → structure → draft → review writing workflow | LOCAL_RUNNABLE | [Example output](https://github.com/zhouey314-cloud/thought-to-x/blob/main/examples/destiny-example.md); 10 tests | No automatic platform publishing |
| [Obsidian AI Inbox](https://github.com/zhouey314-cloud/obsidian-ai-inbox) | Capture and search inside a selected local vault | LOCAL_RUNNABLE | [Interface screenshot](https://github.com/zhouey314-cloud/obsidian-ai-inbox/blob/main/docs/inbox-demo.png); 64 tests | Private vault data stays local |
| [NovaMach](https://github.com/zhouey314-cloud/novamach-b2b-multilingual-demo) | Multilingual B2B catalog and RFQ flow | LIVE_DEMO | [Fictional site preview](https://0-1-b2b-demo-demo-novamach.vercel.app/); build/smoke checks | Fictional brand and sample RFQs |
| [AI Director](https://github.com/zhouey314-cloud/ai_director) | Silence-to-timeline interchange prototype | PROTOTYPE | [Synthetic EDL](https://github.com/zhouey314-cloud/ai_director/blob/main/examples/sample-davinci.edl); SRT/EDL/FCPXML checks | Editing quality and optional provider path unverified |

## Open source templates

| Project | Use | Status | Evidence | Boundary |
|---|---|---|---|---|
| [Agentic Coding Starter](https://github.com/zhouey314-cloud/agentic-coding-starter) | Copyable task rules and handoff scaffold | OPEN_SOURCE | [Sample handoff](https://github.com/zhouey314-cloud/agentic-coding-starter/blob/main/examples/sample-handoff.md) | Structural checks do not prove agent performance |
| [AI Delivery Starter Kit](https://github.com/zhouey314-cloud/ai-delivery-starter-kit) | Scope, acceptance, eval and handoff templates | OPEN_SOURCE | [Example set](https://github.com/zhouey314-cloud/ai-delivery-starter-kit/tree/main/examples) | Templates are not accepted customer deliveries |

## Lab

| Project | Experiment | Status | Evidence | Boundary |
|---|---|---|---|---|
| [AI Content Workflow](https://github.com/zhouey314-cloud/ai-content-workflow) | Evidence-to-draft workflow with a review gate | EXPERIMENT | [Synthetic draft](https://github.com/zhouey314-cloud/ai-content-workflow/blob/main/examples/draft.json); 8 deterministic tests | No company prompt, customer content, model provider or platform publishing |

Portfolio infrastructure: [GitHub profile](https://github.com/zhouey314-cloud/zhouey314-cloud) and [website](https://github.com/zhouey314-cloud/zhouey314-cloud.github.io). Upstream-derived `dbskill`, sensitive local work and thin legacy repositories are excluded from original Selected Work. This index makes no customer production or adoption claim.
