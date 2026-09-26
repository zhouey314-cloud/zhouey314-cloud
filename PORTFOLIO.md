# Portfolio Index

[Six-project visual hub](https://zhouey314-cloud.github.io/projects.html) · [90-second tour](#90-second-tour) · [Resume Project Bank](RESUME_PROJECT_BANK.md)

Status vocabulary: `LIVE_DEMO` is a public interactive preview, `LOCAL_RUNNABLE` a reproducible local tool, and `OFFLINE_ENGINEERING_DEMO` an offline artifact. None means customer production.

## Flagship six

| Project | Problem | Stack | Demo / Evidence | Tests / Evidence | Status |
|---|---|---|---|---|---|
| [Multi-Tenant Workflow](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas) | Tenant isolation and review gates | Node.js, JavaScript | [Pages](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/) | 10 tests; role/state browser flow | LIVE_DEMO |
| [Enterprise RAG Starter](https://github.com/zhouey314-cloud/enterprise-rag-starter) | ACL, citations and no-answer retrieval | Python, embeddings, JS | [Pages lexical](https://zhouey314-cloud.github.io/enterprise-rag-starter/) | 19 tests; 4 synthetic lexical cases | LIVE_DEMO |
| [AI Eval Engineering](https://github.com/zhouey314-cloud/ai-eval-engineering) | Distinguish fixture checks from model quality | Python, JSONL | [Example report](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/example-report.md) | 5 synthetic fixtures; MODEL_QUALITY=NOT_RUN | LOCAL_RUNNABLE |
| [AI Video Workflow Engine](https://github.com/zhouey314-cloud/ai-video-workflow-engine) | Asset-gap, render and QA state | Python, FFmpeg | [Synthetic MP4](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/demo-output.mp4) | 25 tests; 6-second video; HUMAN_REVIEW | OFFLINE_ENGINEERING_DEMO |
| [AI CRM Sales Copilot](https://github.com/zhouey314-cloud/ai-crm-sales-copilot) | Shared opportunity/pipeline/forecast state | JavaScript, localStorage | [Pages](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/) | automated and browser/reload checks | LIVE_DEMO |
| [Portable Agent Skills](https://github.com/zhouey314-cloud/ai-agent-skills) | Reusable, explicit agent workflow contracts | Markdown, Python | [Skill catalog](https://github.com/zhouey314-cloud/ai-agent-skills/tree/main/skills) | 10 structural checks; 3 synthetic cases; model quality NOT_RUN | LOCAL_RUNNABLE |

## 90-second tour

Start at the [visual hub](https://zhouey314-cloud.github.io/projects.html). Follow a public browser flow in Multi-Tenant Workflow; inspect RAG access-filtered retrieval; see Eval's explicit quality gate; watch Video's synthetic FFmpeg output; try CRM's rule-based sales flow; then clone Portable Agent Skills and run its offline contract tests. Each repo explains its own limitations. The visuals and tests are engineering evidence, not user adoption, client acceptance or model success rates.

## Supporting projects

[Recruitment Review](https://github.com/zhouey314-cloud/ai-recruitment-workflow-demo) (synthetic, human-gated demo) · [NovaMach](https://github.com/zhouey314-cloud/novamach-b2b-multilingual-demo) (fictional multilingual B2B demo) · [Thought to X](https://github.com/zhouey314-cloud/thought-to-x) · [Obsidian AI Inbox](https://github.com/zhouey314-cloud/obsidian-ai-inbox) · [AI Content Workflow](https://github.com/zhouey314-cloud/ai-content-workflow) · [Agentic Coding Starter](https://github.com/zhouey314-cloud/agentic-coding-starter).

Upstream-derived `dbskill` is excluded from original Selected Work. Do not upload private local projects or materials without separate provenance and security review.
