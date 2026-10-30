# Resume Project Bank

Pick two or three projects appropriate to a role. These are evidence-backed engineering notes for a 编导 / AI Builder; demo evidence does not imply customer adoption or accepted commercial delivery. [Full index and sources](PORTFOLIO.md).

## Selected three

### Enterprise RAG Starter

- **Problem / action:** Build a bounded local retrieval reference where the caller cannot choose tenant/role, stale or unauthorized evidence cannot be cited, and unsupported questions can be refused.
- **Engineering:** Trusted token provisioning, server-owned identity, ACL-before-ranking, SQLite revisions, MD/PDF/DOCX provenance, authorized FTS5/overlap RRF and exact evidence excerpts. [Code / architecture](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/adr-local-rag.md).
- **Demo / evidence:** [Lexical preview](https://zhouey314-cloud.github.io/enterprise-rag-starter/), separate [local service / PDF-page regression](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/3), [candidate evaluation](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/4). The pre-repair `45e2daa8` baseline passed 48 Python + 10 Node tests and 4 lexical / 9 answerability cases; [current excerpt-fix results](https://github.com/zhouey314-cloud/enterprise-rag-starter#eval-and-verification) are recorded separately. The recorded synthetic_unverified local candidate run is 60/62 over 56 distinct questions (required lexical-contract cases 60/60), with two semantic-paraphrase misses preserved and zero real-model calls. The user confirmed completing review of all 62 cases; no per-case adjudication or expected-answer edits are inferred. Provenance remains synthetic_unverified, not an independently verified Golden Set; enterprise and semantic quality are unverified.
- **Boundary:** The browser demo is lexical; local exact extraction and synthetic gates are not semantic entailment or verified customer knowledge-base quality.
- **Draft bullet:** Implemented a local authenticated retrieval reference with pre-ranking tenant/role filtering, versioned citations and refusal paths; kept mechanical tests, candidate evaluation, user-reported review completion and unresolved semantic misses distinct.

### RelayAudit / AgentGuard

- **Problem / action:** Observe a configured proxy route without adding hidden model requests, corrupting streamed entities or hiding transport failures behind observer failures.
- **Engineering:** Fixed upstream routes, bounded independent queues, bidirectional hop-header filtering, fail-open observation, timeout/cancellation metadata and independent alerts. [Code](https://github.com/zhouey314-cloud/relay-audit).
- **Demo / evidence:** [Pure synthetic QuickStart](https://github.com/zhouey314-cloud/relay-audit/blob/main/examples/guard-synthetic/README.md), [PR2 / 125 tests](https://github.com/zhouey314-cloud/relay-audit/pull/2), [stable v0.2.1 demo download](https://github.com/zhouey314-cloud/relay-audit/releases/tag/v0.2.1), [original three-version CI](https://github.com/zhouey314-cloud/relay-audit/actions/runs/39608139134). Same-request C1/C8 direct/passive measurements show zero extra model requests and measurable overhead.
- **Boundary:** Fake-key loopback mechanics, whole-process Python allocation measurements and protocol observations do not prove upstream identity, calibration accuracy or production capacity.
- **Draft bullet:** Implemented and regression-tested passive proxy observation with entity preservation and explicit degradation; published reproducible latency/throughput/memory measurements alongside the zero-extra-request boundary.

### AI Video Workflow Engine

- **Problem / action:** Turn asset gaps, rendering failures, QA and packaging into reproducible CLI outcomes while retaining a human viewing gate.
- **Engineering:** Python / FFmpeg, asset validation, output consistency and pack-safe delivery; [architecture](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/architecture.md).
- **Demo / evidence:** [54-second original animation](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/c9e698de3880609014b0b83bf349a01dcad3af4d/examples/original_54s/sample.mp4), [source / assets / rights](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/README.md), [sample PR](https://github.com/zhouey314-cloud/ai-video-workflow-engine/pull/4). 47 tests pass. The exact 54-second, nine-shot original animation is user-viewed APPROVED; [artifact-specific review](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/human-review.json) pins SHA256 `0a7f73e9a5a014a352aa5f27a2852b39e558546ccc38f93016785cf2fba0e1a9`. It is animation, not real-person talking-head footage or customer/model/commercial acceptance.
- **Boundary:** The approved artifact is one specific animation, not real-person/client editing, publishing or commercial acceptance.
- **Draft bullet:** Built and tested an offline video workflow with reliable process failures, reproducible FFmpeg output and a rights-documented animation sample; retained artifact-specific human approval.

## Other flagships

| Project / source | Engineering note / evidence | Resume boundary |
|---|---|---|
| [Multi-Tenant Workflow](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas) | Shared tenant/role/state policy and review gate; [11 policy tests](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas/pull/2) / [demo](https://zhouey314-cloud.github.io/multi-tenant-ai-workflow-saas/) | Demo selectors are not production auth |
| [AI Eval Engineering](https://github.com/zhouey314-cloud/ai-eval-engineering) | Offline case/rubric kit; [4 validator regressions + 5 fixtures](https://github.com/zhouey314-cloud/ai-eval-engineering/pull/2) | MODEL_QUALITY=NOT_RUN |
| [AI CRM Sales Copilot](https://github.com/zhouey314-cloud/ai-crm-sales-copilot) | One local opportunity/pipeline/forecast state; [7 recovery scenarios](https://github.com/zhouey314-cloud/ai-crm-sales-copilot/pull/1) / [demo](https://zhouey314-cloud.github.io/ai-crm-sales-copilot/) | Synthetic browser state and rule guidance |
| [Portable Agent Skills](https://github.com/zhouey314-cloud/ai-agent-skills) | Ten explicit workflow contracts; [validator checks under normal/optimized Python](https://github.com/zhouey314-cloud/ai-agent-skills/pull/2) | No provider-backed quality/adoption claim |

## Supporting

| Source | Evidence-backed engineering note | Boundary |
|---|---|---|
| [Recruitment Review](https://github.com/zhouey314-cloud/ai-recruitment-workflow-demo) | Synthetic evidence/risk/human-decision flow; [demo](https://zhouey314-cloud.github.io/ai-recruitment-workflow-demo/), 13 tests / 36 parity cases | No real candidate decisions |
| [Thought to X](https://github.com/zhouey314-cloud/thought-to-x) | Portable prompt-only CLI; [13 tests / installed wheel](https://github.com/zhouey314-cloud/thought-to-x/pull/1), unchanged assembled prompts | Human fact/voice approval; no automatic posting |
| [Obsidian AI Inbox](https://github.com/zhouey314-cloud/obsidian-ai-inbox) | Selected-vault capture/search; [70 executions / 39 unique cases](https://github.com/zhouey314-cloud/obsidian-ai-inbox/pull/1) | Hidden dotfiles excluded; private notes remain local |
| [NovaMach](https://github.com/zhouey314-cloud/novamach-b2b-multilingual-demo) | Fictional multilingual catalog/RFQ; [preview](https://0-1-b2b-demo-demo-novamach.vercel.app/), build/smoke path | Fictional brand/sample inquiries |
| [AI Director](https://github.com/zhouey314-cloud/ai_director) | Silence-to-keep-list/EDL/FCPXML prototype; [6 tests / XML-URI repair](https://github.com/zhouey314-cloud/ai_director/pull/1) | Actual editor-import and editing quality unverified |
| [Voice Clone Video](https://github.com/zhouey314-cloud/voice-clone-video) | Consent-gated dubbing workflow; [synthetic SRT](https://github.com/zhouey314-cloud/voice-clone-video/blob/main/examples/synthetic-subtitles.srt) / offline Mock | Real voices need authorization; quality NOT_TESTED |

## Templates

[Agentic Coding Starter](https://github.com/zhouey314-cloud/agentic-coding-starter) and [AI Delivery Starter Kit](https://github.com/zhouey314-cloud/ai-delivery-starter-kit) provide task, scope, eval and handoff structures. Describe them as reusable templates, never as proof of Agent performance or accepted client delivery.

## Experiments

[AI Content Workflow](https://github.com/zhouey314-cloud/ai-content-workflow): an evidence-to-draft lab with 8 deterministic tests and synthetic fixtures; no company prompt, customer content, real provider or platform posting.

## Legacy / upstream / excluded

- [My Money App](https://github.com/zhouey314-cloud/my-money-app): [16 offline tests](https://github.com/zhouey314-cloud/my-money-app/pull/1) support schema, file-preservation and concurrency mechanics. Real expense extraction, personal ledgers and financial/business acceptance were not tested.
- [Amazon FBM Agent](https://github.com/zhouey314-cloud/amazon-fbm-agent): [5 MOCK checks](https://github.com/zhouey314-cloud/amazon-fbm-agent/pull/1), fixed outputs and assumptions; no real model, VOC analysis or validated market/profitability conclusion.
- [dbskill](https://github.com/zhouey314-cloud/dbskill): [dontbesilent upstream](https://github.com/dontbesilent2025/dbskill), [CC BY-NC 4.0 / non-commercial](https://github.com/zhouey314-cloud/dbskill/blob/main/LICENSE). Do not claim authorship of the upstream library or change its license.
- [GEO legacy](https://github.com/zhouey314-cloud/geo-saas-mvp) has a merged [public historical-source startup repair](https://github.com/zhouey314-cloud/geo-saas-mvp/pull/1); company/current GEO IP remains **FROZEN** and excluded from personal original-project claims. BossProVideo, customer/private material and private source-archive counts are not resume product achievements.

## Claim guardrails

Use runnable local reference, synthetic case, deterministic test, measured loopback overhead and artifact-specific human approval where accurate. Do not turn tests into model-quality scores, private archive/component counts into production products, assistance into independent leadership, or personal experiments into customers, revenue, staff titles or accepted commercial deliveries.

## 2026-10-30 可引用的工程贡献

- 将本地 RAG 的 phone/email 缺值误答修复接入原有回归，新增 SQLite 在线备份、独立恢复和健康检查。
- 为 AgentGuard 增加业务请求容量和显式 503，验证挂起 SSE、恢复和上游请求数量。
- 为 FFmpeg 工作流增加每任务交付包、输入/输出哈希、失败回收与本地校验器。
- 修复多租户演示服务写盘失败后内存仍保留修改的问题；用候选状态提交和真实 HTTP 重启回归验证。
- 将 eval 仓库从数据格式校验扩展为已记录响应与工具轨迹的机械规则执行和版本差异报告。

以上为个人开源实现和离线/loopback 验证，不推导客户投产或真实模型效果。
