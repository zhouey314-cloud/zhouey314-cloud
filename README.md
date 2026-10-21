# Ethan Zhou

### 编导背景 · AI Builder

把内容制作和业务问题做成能运行、能复现、边界清楚的工具。I build practical AI workflows and show the code, evidence and limits.

**Contact / 联系我:** [Telegram @ethanyu520](https://t.me/ethanyu520) · [Email](mailto:zhouey314@gmail.com) · [WeChat QR / 微信二维码](#website--contact)

## Selected Work · Three projects

| Project / Problem | Demo | Code | Evidence | Current limit |
|---|---|---|---|---|
| **Enterprise RAG** — 让检索回答遵守身份、来源与拒答边界 | [Lexical preview](https://zhouey314-cloud.github.io/enterprise-rag-starter/) | [Repository](https://github.com/zhouey314-cloud/enterprise-rag-starter) | [Local service / ACL](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/3) · [Candidate evals](https://github.com/zhouey314-cloud/enterprise-rag-starter/pull/4) | 确定性摘录；两条语义改写漏检，不代表企业质量 |
| **RelayAudit / AgentGuard** — 被动观察代理协议，同时保留业务响应与已知故障原因 | [Synthetic demo / download](https://github.com/zhouey314-cloud/relay-audit/actions/runs/39608139134) | [Repository](https://github.com/zhouey314-cloud/relay-audit) | [125 tests / stream fix](https://github.com/zhouey314-cloud/relay-audit/pull/2) | 有实测开销；不能验证上游模型身份 |
| **Video Workflow Engine** — 让素材缺口、渲染、QA、失败退出与人工审片可复现 | [54s original animation](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/c9e698de3880609014b0b83bf349a01dcad3af4d/examples/original_54s/sample.mp4) | [Repository](https://github.com/zhouey314-cloud/ai-video-workflow-engine) | [Sample / review / CI](https://github.com/zhouey314-cloud/ai-video-workflow-engine/pull/4) | APPROVED 只限此动画样片，不扩展到真人或客户交付 |

[Visual portfolio](https://zhouey314-cloud.github.io/projects.html) · [Full project index](PORTFOLIO.md) · [Resume Project Bank](RESUME_PROJECT_BANK.md)

## Reproduce and inspect

- **RAG:** [local architecture / trust boundary](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/adr-local-rag.md), [existing lexical UI screenshot](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/images/demo-query.png), and [local CLI / HTTP QuickStart](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/local-quickstart.md). `python local_service.py init` starts a new local index; follow the QuickStart for fictional sources and private token files. The browser preview is lexical and does not demonstrate authenticated local-service access. 48 Python + 10 Node tests pass; the existing 4 lexical / 9 answerability cases are retained. The synthetic_unverified local candidate run is 60/62 over 56 distinct questions (required lexical-contract cases 60/60), with two semantic-paraphrase misses preserved and zero real-model calls. The user confirmed completing review of all 62 cases; no per-case adjudication or expected-answer edits are inferred. Provenance remains synthetic_unverified, not an independently verified Golden Set; enterprise and semantic quality are unverified.
- **RelayAudit:** `Agent → fixed-route proxy → configured upstream`, with independent bounded parser/detector queues and separate notifications. [Protocol / source](https://github.com/zhouey314-cloud/relay-audit/blob/main/relay_audit/guard/proxy.py) · [five-minute synthetic QuickStart](https://github.com/zhouey314-cloud/relay-audit/blob/main/examples/guard-synthetic/README.md). Run `python -m relay_audit guard demo --out agentguard-demo/profile-001` in a fresh output directory. C1/N100 and C8/N200 measurements retain p50/p95, throughput and Python peak allocations; zero extra model requests does not mean zero latency or 100% performance.
- **Video:** [architecture](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/architecture.md) · [nine-shot contact sheet](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/contact-sheet.jpg) · [sample commands and rights manifest](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/README.md). Generate via `python examples/original_54s/generate.py --output output/original54 --font /path/to/licensed-font.ttc`, then use the linked FFmpeg workflow command. 47 tests pass. The exact 54-second, nine-shot original animation is user-viewed APPROVED; [artifact-specific review](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/human-review.json) pins SHA256 `0a7f73e9a5a014a352aa5f27a2852b39e558546ccc38f93016785cf2fba0e1a9`. It is animation, not real-person talking-head footage or customer/model/commercial acceptance.

Each repository records mechanical tests separately from AI evaluation and human acceptance. These are personal tools, prototypes and demos; no customer production, commercial success or model-identity accuracy is implied.

## Other work and boundaries

The [portfolio index](PORTFOLIO.md) retains the original sixteen public project sources, grouped as other flagships, supporting work, templates and experiments. It also labels legacy prototypes and upstream-derived work. Private source archives and their component directories are not counted as production products.

`dbskill` is third-party work from [dontbesilent](https://github.com/dontbesilent2025/dbskill), under [CC BY-NC 4.0 / non-commercial terms](https://github.com/zhouey314-cloud/dbskill/blob/main/LICENSE). I do not present it as an original project or change its license. Company/client material, GEO work under IP review and private voices/data stay outside original Selected Work.

I am interested in AI application engineering, retrieval, evaluation, automation and content workflows. The practical standard is a runnable path, evidence matched to risk, explicit failure states and a handoff another person can reproduce.

## Website / Contact

[Personal website](https://zhouey314-cloud.github.io/) · [X](https://x.com/UPing123zzz) · [GitHub](https://github.com/zhouey314-cloud)

[Telegram @ethanyu520](https://t.me/ethanyu520) · [Email: zhouey314@gmail.com](mailto:zhouey314@gmail.com) · [WeChat / 微信：Ethan 恩宇](https://u.wechat.com/MJNJhDRZFiAFKD09uKIRGvM?s=3)

<a href="https://u.wechat.com/MJNJhDRZFiAFKD09uKIRGvM?s=3">
  <img src="assets/wechat-qr.svg" alt="Ethan 恩宇微信二维码" width="220">
</a>

微信扫码添加 Ethan 恩宇。

Open to discussing AI product engineering, FDE-style implementation and evidence-first delivery. Public demos are not claims of customer production use.
