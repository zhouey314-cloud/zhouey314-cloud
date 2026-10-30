# 恩宇 / Ethan Zhou

**AI 应用与工作流开发。把一个具体问题，推进到能运行、能验证、能交接。**

中原工学院广播电视编导专业本科在读，现居郑州。自 2026 年 6 月参与企业 GEO 与 AI 应用实践。编导训练让我先理解人和场景；工程工作里，我关注数据从哪里来、请求如何流转、失败如何处理、结果如何验收。

[作品网站](https://zhouey314-cloud.github.io/) · [操作三个重点作品](https://zhouey314-cloud.github.io/workbench.html) · [简历](https://zhouey314-cloud.github.io/resume.html) · [联系合作](#website--contact)

## 可以一起解决什么问题

| 你的问题 | 我能承担的实现 | 可检查的交付 |
|---|---|---|
| 资料分散，回答难以追溯 | 整理文档结构，接入本地检索，处理版本、权限与引用 | CLI/HTTP、资料与权限说明、固定回归、备份恢复步骤 |
| AI 接口偶发失败，缺少排查线索 | 集成 HTTP/SSE，区分超时、取消、协议与容量问题 | 本地网关、元数据报告、复现脚本、故障恢复说明 |
| 内容制作依赖手动串流程 | 串接素材清单、时间轴、字幕、FFmpeg 和媒体检查 | 可重跑任务、校验清单、交付包、人工审片入口 |
| 改过 AI 工作流，却说不清有没有改善 | 建立用例/响应记录、执行机械约束、对比失败与回归 | 版本报告、可复跑命令、待人工确认的问题 |

适合从范围明确的原型、内部工具或现有流程改造开始。先对齐问题、可用资料和验收目标，再交付最小可运行版本与交接记录。涉及真实模型、生产身份或客户数据时，需要在具体项目中完成相应验证。

## 三个代表工程

| 工程 | 我实现的部分 | 直接查看 |
|---|---|---|
| **Enterprise RAG Starter** | 三格式文档入库、版本/生效期、身份过滤、引用与拒答、SQLite 备份恢复 | [源码](https://github.com/zhouey314-cloud/enterprise-rag-starter) · [运维流程](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/OPERATIONS.md) · [在线操作](https://zhouey314-cloud.github.io/workbench.html#rag) |
| **RelayAudit / AgentGuard** | 固定上游代理、HTTP/SSE 保真、独立观察队列、容量控制、异常报告 | [源码](https://github.com/zhouey314-cloud/relay-audit) · [容量与故障](https://github.com/zhouey314-cloud/relay-audit/blob/main/docs/CAPACITY.md) · [报告检查器](https://zhouey314-cloud.github.io/workbench.html#relay) |
| **AI Video Workflow Engine** | 素材/时间轴/字幕、真实渲染与 QA、可校验交付包、人工审片门禁 | [源码](https://github.com/zhouey314-cloud/ai-video-workflow-engine) · [交付包](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/DELIVERY_BUNDLES.md) · [54 秒原创动画](https://zhouey314-cloud.github.io/workbench.html#video) |

公开网页 RAG 为合成资料上的词法检索；网关报告不确认真实模型身份；动画样片的人工批准只适用于其确切文件。工程证据与适用范围在各仓库相邻说明。

[本轮工程审查](ENGINEERING_STATUS.md) · [全部项目与阶段](PORTFOLIO.md) · [项目贡献记录](RESUME_PROJECT_BANK.md) · [多租户 HTTP 工程](https://github.com/zhouey314-cloud/multi-tenant-ai-workflow-saas/blob/main/docs/HTTP_API.md) · [响应评测器](https://github.com/zhouey314-cloud/ai-eval-engineering/blob/main/docs/RECORDED_EVAL.md)

## Reproduce and inspect

<details>
<summary>复现命令、评测边界与文件证据</summary>


- **RAG:** [local architecture / trust boundary](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/adr-local-rag.md), [existing lexical UI screenshot](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/images/demo-query.png), and [local CLI / HTTP QuickStart](https://github.com/zhouey314-cloud/enterprise-rag-starter/blob/main/docs/local-quickstart.md). `python local_service.py init` starts a new local index; follow the QuickStart for fictional sources and private token files. The browser preview is lexical and does not demonstrate authenticated local-service access. The pre-repair `45e2daa8` baseline passed 48 Python + 10 Node tests and 4 lexical / 9 answerability cases; current excerpt-fix results are recorded in the [repository verification section](https://github.com/zhouey314-cloud/enterprise-rag-starter#eval-and-verification). The recorded synthetic_unverified local candidate run is 60/62 over 56 distinct questions (required lexical-contract cases 60/60), with two semantic-paraphrase misses preserved and zero real-model calls. The user confirmed completing review of all 62 cases; no per-case adjudication or expected-answer edits are inferred. Provenance remains synthetic_unverified, not an independently verified Golden Set; enterprise and semantic quality are unverified.
- **RelayAudit:** `Agent → fixed-route proxy → configured upstream`, with independent bounded parser/detector queues and separate notifications. [Protocol / source](https://github.com/zhouey314-cloud/relay-audit/blob/main/relay_audit/guard/proxy.py) · [five-minute synthetic QuickStart](https://github.com/zhouey314-cloud/relay-audit/blob/main/examples/guard-synthetic/README.md). Run `python -m relay_audit guard demo --out agentguard-demo/profile-001` in a fresh output directory. [Original Actions evidence](https://github.com/zhouey314-cloud/relay-audit/actions/runs/39608139134) is retained; its downloadable artifact has finite retention and is not the stable demo entry. C1/N100 and C8/N200 measurements retain p50/p95, throughput and Python peak allocations; zero extra model requests does not mean zero latency or 100% performance.
- **Video:** [architecture](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/docs/architecture.md) · [nine-shot contact sheet](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/contact-sheet.jpg) · [sample commands and rights manifest](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/README.md). Generate via `python examples/original_54s/generate.py --output output/original54 --font /path/to/licensed-font.ttc`, then use the linked FFmpeg workflow command. 47 tests pass. The exact 54-second, nine-shot original animation is user-viewed APPROVED; [artifact-specific review](https://github.com/zhouey314-cloud/ai-video-workflow-engine/blob/main/examples/original_54s/human-review.json) pins SHA256 `0a7f73e9a5a014a352aa5f27a2852b39e558546ccc38f93016785cf2fba0e1a9`. It is animation, not real-person talking-head footage or customer/model/commercial acceptance.

</details>

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

可以直接带着一个具体问题来聊：现在哪一步最费时间、有哪些资料和系统、怎样算做成。我会据此拆解可交付范围与验收方式。
