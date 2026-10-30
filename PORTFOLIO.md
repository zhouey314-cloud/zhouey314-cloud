# Portfolio Index

[Visual portfolio](https://zhouey314-cloud.github.io/projects.html) · [Profile](README.md) · [Resume Project Bank](RESUME_PROJECT_BANK.md)

This index distinguishes personal engineering evidence, demos, templates, legacy code and upstream sources. `LOCAL_RUNNABLE`, `OFFLINE_TOOL`, `LIVE_DEMO` and `EXPERIMENT` describe a bounded path, never customer production or accepted AI quality. Historical evidence snapshot: 2026-10-21. Current engineering increment: 2026-10-30, below.

## Selected three

### Enterprise RAG Starter

- **Problem / code:** [versioned local retrieval with trusted identity, tenant/role ACL, citations and refusal](https://github.com/zhouey314-cloud/enterprise-rag-starter).
- **Architecture / demo:** [local SQLite / FTS5 + overlap RRF / trust-boundary ADR](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/adr-local-rag.md); [lexical browser preview](https://zhouey314-cloud.github.io/enterprise-rag-starter/) and [its real screenshot](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/images/demo-query.png). The browser preview is separate from the authenticated local CLI/HTTP reference.
- **Reproduce:** follow the [licensed synthetic corpus / local QuickStart](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/local-quickstart.md); trusted CLI provisions opaque tokens, then HTTP accepts only question/top_k. [Service and PDF-page repair](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/3).
- **Evidence / limits:** The pre-repair `45e2daa8` baseline passed 48 Python + 10 Node tests and 4 lexical / 9 answerability cases; [current excerpt-fix results](https://github.com/zhouey314-cloud/enterprise-rag-starter#eval-and-verification) are recorded separately. The recorded synthetic_unverified local candidate run is 60/62 over 56 distinct questions (required lexical-contract cases 60/60), with two semantic-paraphrase misses preserved and zero real-model calls. The user confirmed completing review of all 62 cases; no per-case adjudication or expected-answer edits are inferred. Provenance remains synthetic_unverified, not an independently verified Golden Set; enterprise and semantic quality are unverified. [Candidate suite and human-review queue](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/4). Exact excerpts and lexical gates are not semantic entailment; no customer corpus or paid provider acceptance is claimed.

### RelayAudit / AgentGuard

- **Problem / code:** [fixed-route passive proxy](https://github.com/zhouey314-cloud/relay-audit) with response preservation, explicit monitoring degradation and separate notifications.
- **Architecture / demo:** Agent → fixed upstream gateway → upstream; observation copies enter bounded parser/detector queues. [Proxy implementation](https://github.com/zhouey314-cloud/relay-audit/blob/main/relay_audit/guard/proxy.py), [synthetic request fixture / QuickStart](https://github.com/zhouey314-cloud/relay-audit/blob/main/examples/guard-synthetic/README.md), [stable v0.2.1 demo download](https://github.com/zhouey314-cloud/relay-audit/releases/tag/v0.2.1), [original Actions evidence](https://github.com/zhouey314-cloud/relay-audit/actions/runs/39608139134).
- **Reproduce:** `python evals/run_acceptance.py --out acceptance-new --requests 100 --concurrency 1`; use a second new directory for `--requests 200 --concurrency 8`. Installation is in the linked QuickStart; all workload requests are fake-key loopback calls.
- **Evidence / limits:** [PR2 and three-version CI](https://github.com/zhouey314-cloud/relay-audit/pull/2), 125 tests; bidirectional repeated Connection filtering retained. Direct/disabled/full-passive JSON/SSE measurements: zero extra model requests, HTTP/entity errors and queue drops in the measured runs. Full passive has measurable latency/throughput overhead; memory is whole-process Python allocations, not proxy-only RSS. No real API, identity calibration or production-capacity claim.

### AI Video Workflow Engine

- **Problem / code:** [offline FFmpeg workflow](https://github.com/zhouey314-cloud/ai-video-workflow-engine) for missing assets, rendering, QA, deliverables and reliable failure exits.
- **Architecture / demo:** [architecture](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/architecture.md), [54-second original nine-shot animation](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/c9e698de3880609014b0b83bf349a01dcad3af4d/examples/original_54s/sample.mp4), [contact sheet](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/contact-sheet.jpg).
- **Reproduce / rights:** [sample commands, generated assets and font-license provenance](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/README.md). No company/customer footage or private voice is used.
- **Evidence / limits:** 47 tests pass. The exact 54-second, nine-shot original animation is user-viewed APPROVED; [artifact-specific review](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/human-review.json) pins SHA256 `0a7f73e9a5a014a352aa5f27a2852b39e558546ccc38f93016785cf2fba0e1a9`. It is animation, not real-person talking-head footage or customer/model/commercial acceptance. [Focused sample PR](https://github.com/zhouey314-cloud/ai-video-workflow-engine/pull/4). Approval applies only to the exact reviewed animation; real-person editing, customer delivery, paid generation, social publishing and commercial acceptance are NOT_TESTED.

## Other flagships

| Project / source | Role | Demo / engineering evidence | Limit |
|---|---|---|---|
| [Multi-Tenant Workflow](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas) | Tenant isolation and review gates | [Browser demo](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/); [11 policy tests](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas/pull/2) | Role selectors are demo controls, not production authentication |
| [AI Eval Engineering](https://github.com/zhouey314-cloud/ai-eval-engineering) | Separate fixture validation from model quality | [Example report](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/example-report.md); [4 validator regressions + 5 synthetic fixtures](https://github.com/zhouey314-cloud/ai-eval-engineering/pull/2) | MODEL_QUALITY=NOT_RUN |
| [AI CRM Sales Copilot](https://github.com/zhouey314-cloud/ai-crm-sales-copilot) | One local opportunity / forecast / rule-guidance state | [Browser demo](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/); [7 persistence-recovery scenarios](https://github.com/zhouey314-cloud/ai-crm-sales-copilot/pull/1) | Synthetic data, localStorage, no production auth/provider |
| [Portable Agent Skills](https://github.com/zhouey314-cloud/ai-agent-skills) | Ten reusable workflow contracts | [Skill catalog](https://github.com/zhouey314-cloud/ai-agent-skills/tree/main/skills); [normal/optimized validator regressions](https://github.com/zhouey314-cloud/ai-agent-skills/pull/2) | Offline contracts and synthetic fixtures; model quality NOT_RUN |

## Supporting

| Project / source | Role / evidence | Limit |
|---|---|---|
| [Recruitment Review](https://github.com/zhouey314-cloud/ai-recruitment-workflow-demo) | [Synthetic browser flow](https://zhouey314-cloud.github.io/ai-recruitment-workflow-demo/); 13 tests / 36 parity cases | No real candidate decisions or validated model quality |
| [Thought to X](https://github.com/zhouey314-cloud/thought-to-x) | [Example](https://github.com/zhouey314-cloud/thought-to-x/blob/main/examples/destiny-example.md); [13 tests / installed-wheel prompt-only path](https://github.com/zhouey314-cloud/thought-to-x/pull/1) | Factual and voice approval remain human; no platform posting |
| [Obsidian AI Inbox](https://github.com/zhouey314-cloud/obsidian-ai-inbox) | [Screenshot](https://github.com/zhouey314-cloud/obsidian-ai-inbox/blob/main/docs/inbox-demo.png); [70 executions / 39 unique cases](https://github.com/zhouey314-cloud/obsidian-ai-inbox/pull/1) | Selected-vault scope; hidden dotfiles excluded; private notes stay local |
| [NovaMach](https://github.com/zhouey314-cloud/novamach-b2b-multilingual-demo) | [Fictional multilingual catalog / RFQ preview](https://0-1-b2b-demo-demo-novamach.vercel.app/); build/smoke checks | Fictional brand and sample RFQs; no customer acceptance |
| [AI Director](https://github.com/zhouey314-cloud/ai_director) | [Synthetic timeline / EDL](https://github.com/zhouey314-cloud/ai_director/blob/main/examples/sample-davinci.edl); [6 tests / FCPXML repair](https://github.com/zhouey314-cloud/ai_director/pull/1) | Actual editor import and editing quality unverified |
| [Voice Clone Video](https://github.com/zhouey314-cloud/voice-clone-video) | [Synthetic subtitle fixture](https://github.com/zhouey314-cloud/voice-clone-video/blob/main/examples/synthetic-subtitles.srt); offline Mock path | Real voice cloning requires consent; voice quality/human acceptance NOT_TESTED |

## Templates

| Source | Reusable asset | Limit |
|---|---|---|
| [Agentic Coding Starter](https://github.com/zhouey314-cloud/agentic-coding-starter) | [Task rules and sample handoff](https://github.com/zhouey314-cloud/agentic-coding-starter/blob/main/examples/sample-handoff.md) | Structure does not prove Agent performance |
| [AI Delivery Starter Kit](https://github.com/zhouey314-cloud/ai-delivery-starter-kit) | [Scope / acceptance / eval / handoff examples](https://github.com/zhouey314-cloud/ai-delivery-starter-kit/tree/main/examples) | Templates are not accepted customer deliveries |

## Experiments

[AI Content Workflow](https://github.com/zhouey314-cloud/ai-content-workflow): [synthetic evidence-to-draft fixture](https://github.com/zhouey314-cloud/ai-content-workflow/blob/main/examples/draft.json), 8 deterministic tests; no company prompt, customer content, provider or platform publishing.

## Legacy prototypes

- [My Money App](https://github.com/zhouey314-cloud/my-money-app): [16 offline mechanical tests / safe ledger repair](https://github.com/zhouey314-cloud/my-money-app/pull/1). Schema/amount/date validation, duplicate guard, byte backups, locks and atomic saves protect local files. No real ledger/API or extraction-accuracy acceptance; not production accounting or financial advice. Never publish a ledger or backup.
- [Amazon FBM Agent](https://github.com/zhouey314-cloud/amazon-fbm-agent): [5 offline MOCK checks](https://github.com/zhouey314-cloud/amazon-fbm-agent/pull/1). Fixed VOC/strategy/cost examples, no real model or market analysis; not purchasing or investment advice.

## Upstream and excluded boundaries

- [dbskill](https://github.com/zhouey314-cloud/dbskill) comes from [dontbesilent](https://github.com/dontbesilent2025/dbskill); [CC BY-NC 4.0](https://github.com/zhouey314-cloud/dbskill/blob/main/LICENSE), non-commercial. It is third-party/upstream-derived, not an original Selected Work project; its license is unchanged.
- [GEO legacy repository](https://github.com/zhouey314-cloud/geo-saas-mvp): [public historical-source startup repair](https://github.com/zhouey314-cloud/geo-saas-mvp/pull/1) is merged; company/current GEO IP remains **FROZEN** and excluded from personal original work. BossProVideo, customer assets, private voices, unauthorized source and collaboration-only repositories are also outside this portfolio's authorship/production claims.
- Private personal source archives and component directories retain their own provenance, license and test boundaries. They are not public product launches or production deliveries; this index does not expose their runtime data.

The original sixteen public project sources remain represented above: 3 selected + 4 other flagships + 6 supporting + 2 templates + 1 experiment. Infrastructure: [Profile repository](https://github.com/zhouey314-cloud/zhouey314-cloud) and [website repository](https://github.com/zhouey314-cloud/zhouey314-cloud.github.io).

## 2026-10-30 工程增量

| 项目 | 已实现与复现入口 | 本轮本地验证 |
|---|---|---|
| RAG | [备份、恢复、doctor 与 phone/email 值检查](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/OPERATIONS.md) | 55 Python + 36 Node；原 62 候选期望不变，必需 60/60，完整 60/62 |
| AgentGuard | [并发容量、503 与重复凭据拒绝](https://github.com/zhouey314-cloud/relay-audit/blob/main/docs/CAPACITY.md) | 128 回归；并发 4 / 每档 30 的 loopback 合成验收 |
| Video | [每任务交付包与校验](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/DELIVERY_BUNDLES.md) | 56 测试，含真实 FFmpeg 编码/完整解码 |
| Multi-tenant workflow | [事务持久化与 HTTP 错误契约](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas/blob/main/docs/HTTP_API.md) | 14 测试，含磁盘故障回滚与重启 |
| Eval engineering | [响应与轨迹规则、baseline 比较](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/RECORDED_EVAL.md) | 12 测试、5 条手写记录的机械示例；模型质量未评测 |

这些增量改善可运行性、故障处理和交付证据。其余项目按原有阶段展示，历史测试数字保留其日期；没有新增客户、职位、收入、生产 SLA 或模型质量结论。
