# Portfolio Index

[Project / Lab hub](https://zhouey314-cloud.github.io/projects.html) · [90-second tour](#90-second-tour) · [Resume Project Bank](RESUME_PROJECT_BANK.md)

Status vocabulary: `LIVE_DEMO` means a public interactive preview, `LOCAL_RUNNABLE` a reproducible local tool, `OFFLINE_ENGINEERING_DEMO` an offline artifact, and `MOCK_INTEGRATION` a connected-looking but explicitly disconnected interface. None means customer production.

| Project | Problem | Stack | Demo | Tests / Evidence | Status |
|---|---|---|---|---|---|
| [NovaMach](https://github.com/zhouey314-cloud/novamach-b2b-multilingual-demo) | Multilingual B2B product-to-RFQ journey | React, TS, Vite | [Vercel](https://0-1-b2b-demo-demo-novamach.vercel.app/) | lint/typecheck/build/smoke; synthetic RFQ check | LIVE_DEMO |
| [Multi-Tenant Workflow](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas) | Tenant isolation and review gates | Node.js, JavaScript | [Pages](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/) | 10 tests, role/state browser flow | LIVE_DEMO |
| [Enterprise RAG Starter](https://github.com/zhouey314-cloud/enterprise-rag-starter) | ACL, citations and no-answer retrieval | Python, sentence-transformers, JS | [Pages lexical](https://zhouey314-cloud.github.io/enterprise-rag-starter/) | 19 tests; local synthetic modes 5/5, 8/8, 8/8 | LIVE_DEMO |
| [Recruitment Review](https://github.com/zhouey314-cloud/ai-recruitment-workflow-demo) | Human-gated, evidence-traced review | Python, JS | [Pages](https://zhouey314-cloud.github.io/ai-recruitment-workflow-demo/) | 13 tests, 5 fixtures, 36 parity cases | LIVE_DEMO |
| [AI CRM Sales Copilot](https://github.com/zhouey314-cloud/ai-crm-sales-copilot) | Shared opportunity/pipeline/forecast state | JavaScript, localStorage | [Pages](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/) | automated and browser/reload checks | LIVE_DEMO |
| [AI Video Workflow Engine](https://github.com/zhouey314-cloud/ai-video-workflow-engine) | Asset-gap, render and QA state | Python, FFmpeg | [MP4 sample](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/demo-output.mp4) | 25 tests, 6s synthetic video, HUMAN_REVIEW | OFFLINE_ENGINEERING_DEMO |
| [AI Eval Engineering](https://github.com/zhouey314-cloud/ai-eval-engineering) | Distinguish fixture checks from model quality | Python, JSONL | [Example report](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/example-report.md) | 5 synthetic cases, MODEL_QUALITY=NOT_RUN | LOCAL_RUNNABLE |
| [Thought to X](https://github.com/zhouey314-cloud/thought-to-x) | Preserve author intent in X drafts | Python, modular prompts | [Illustrative example](https://github.com/zhouey314-cloud/thought-to-x/blob/main/examples/destiny-example.md) | Offline CLI tests; human style review needed | LOCAL_RUNNABLE |

## 90-second tour

Start with [the six-project visual hub](https://zhouey314-cloud.github.io/projects.html). Open NovaMach to see a fictional multilingual B2B journey; open Multi-Tenant Workflow for isolation and human review; inspect Enterprise RAG for access-filtered citations and no-answer; open Recruitment Review for the mandatory reviewer decision; use CRM to see a rule-based assistant tied to local opportunity state; finish with the Video Engine's real FFmpeg sample and HUMAN_REVIEW gate. Each repository's `docs/case-study.md`, `docs/resume-bullets.md` and `docs/interview-notes.md` explain implementation, evidence and limits.

Other public tools include [Obsidian AI Inbox](https://github.com/zhouey314-cloud/obsidian-ai-inbox), [AI Agent Skills](https://github.com/zhouey314-cloud/ai-agent-skills), [AI Content Workflow](https://github.com/zhouey314-cloud/ai-content-workflow) and [Agentic Coding Starter](https://github.com/zhouey314-cloud/agentic-coding-starter). They are not prioritized above the six-project tour. Upstream-derived `dbskill` is excluded from original Selected Work.
