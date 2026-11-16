# Sources and Assumptions

## Search scope

- 日期：2026-11-15
- 语言：英文为主，中文检索补充
- 查询：18 组，覆盖 AI 依赖/批判性思维、桌面机器人、注意力支持、物理阻断、脑训练争议、竞品价格
- 来源：6–10 个核心来源；初筛 2 个独立来源，关键主张 3 个独立来源（至少 1 个非自述）
- 限制：没有本地访谈；没有样机；没有付费测试；部分竞品价格为第三方评测/页面，非官方实时价

## Source table

| # | Claim | Source | Date | Type | Confidence | Counterexample |
|---|---|---|---|---|---|---|
| 1 | 319 名知识工作者：对 GenAI 信心越高，自报批判性思考越少 | Microsoft Research, CHI 2025, https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/ | 2025-03-24 | survey, self-report | medium | 自报，不是客观测试；不能证明因果 |
| 2 | 54 人 EEG：LLM 组脑连接最弱，自报 ownership 最低 | MIT Media Lab, https://www.media.mit.edu/publications/your-brain-on-chatgpt/ | 2025-06-10 | EEG experiment, preprint | medium-low | 样本小；预印本；任务为 essay writing |
| 3 | 1,623 名大学生：AI 依赖中介学业压力→倦怠/焦虑，降低 self-efficacy | BMC Psychology, https://link.springer.com/article/10.1186/s40359-026-04911-w | 2026-05-30 | survey, mediation | medium | 横断面；不能证明长期因果 |
| 4 | 18–25 岁用户自述依赖三因素：chronic use、efficiency、delegation；伴随能力萎缩感 | arXiv 2608.07592, https://arxiv.org/html/2608.07592 | 2026-09-21 | qualitative testimonials | medium | 自述；样本为问卷 testimonial |
| 5 | 26 项研究/47 效应量：GenAI 支持的学习平均 CT 更高，g=0.544；异质性大 | Educational Psychology Review, https://link.springer.com/article/10.1007/s10648-026-10180-1 | 2026-06-06 | meta-analysis | medium | 不能直接推“AI 导致依赖”；子组证据有限 |
| 6 | 5 场参与式设计：记录参与者对桌面机器人的期待与设计方向；屏幕内注意力工具易被忽略 | HKUST, HRI Companion 2026, https://researchportal.hkust.edu.hk/en/publications/envisioning-an-attention-supportive-desktop-robot-a-participatory/ | 2026-03-16 | qualitative design study | medium | 是设计研究/期待，不是效果验证；关注“注意力”，不是“认知独立” |
| 7 | N=36：桌面机器人行为影响工作体验/生产力/机器人感知 | ACM CHI EA 2024, DOI 10.1145/3613905.3651027 | 2024-05 | lab experiment | medium | 任务为 digitization；不是认知训练 |
| 8 | Brick：$59 物理 puck 阻断 app，无订阅；5 次紧急解锁 | NBC News Select, https://www.nbcnews.com/select/shopping/brick-phone-app-blocker-review-rcna259740 | 2026-02; accessed 2026-11-15 | product review | medium | 价格支持“替代品存在”，不证明愿意为“训练”付费；阻断不等于训练 |
| 9 | LOOI：约 $179；手机当脸/大脑；ChatGPT/GPT-4o；novelty is the product | Pocket Animus, https://pocketanimus.com/guides/looi-robot/ | 2026-07-15 | product review | medium | 第三方评测；价格区间 $159–189 |
| 10 | Eilik：$139.99；230g；无 Wi-Fi/账号/app；动画重复 | Offbrand Human, https://www.offbrandhuman.com/blog/eilik-robot-review | 2026-11-09 | product review | medium | 评测基于 295 条评论；非亲自使用 |
| 11 | 脑训练产品益处证据薄弱，迁移到现实能力有限 | PMC 4445580, https://www.ncbi.nlm.nih.gov/pmc/articles/4445580 | 2015; accessed 2026-11-15 | review | medium | 针对 brain games，不是 AI 产品 |
| 12 | 认知卸载是常见的、能提高表现的行为；问题在元认知错误导致的次优卸载 | Risko & Gilbert, Trends Cogn Sci 2016, https://samgilbert.net/pubs/Risko2016TiCS.pdf | 2016 | review | high | 不能把“卸载”本身病理化 |

## Assumptions

| # | Assumption | Why not evidence | How to test |
|---|---|---|---|
| 1 | 目标用户愿意为“先想”付 99–199 美元 | 没有价格测试 | 三档真实预售/定金 |
| 2 | 桌面物件比便利贴更能坚持 | 只有注意力机器人和 Brick 的间接证据 | A/B 2 周日记 |
| 3 | 用户不会把机器人当 oracle | 没有样机 | 记录“你直接告诉我答案”的请求 |
| 4 | 22–35 研究生/初级知识工作者是 beachhead | 样本框，不是观察 | 8–10 人招募，按行为筛选 |
| 5 | 隐私可接受（本地处理、麦克风物理断开） | 未做隐私测试 | 访谈 + 场景测试 |

## Counterexamples

| # | What contradicts the thesis | Source | Implication |
|---|---|---|---|
| 1 | GenAI 平均能提高批判性思维 | Meta-analysis 2026 | 不能把“用 AI”本身当问题；只打“无反思 delegation” |
| 2 | 认知卸载常常有益 | Risko & Gilbert 2016 | 产品不能承诺“少用 AI”；应承诺“先有自己的答案” |
| 3 | 脑训练迁移证据弱 | PMC 4445580 | 不要承诺 IQ/记忆力提升 |
| 4 | 桌面机器人 novelty 退潮/重复 | Eilik review; LOOI review | 身体必须证明 adherence，不是可爱 |

## Not found

| # | What was searched | Result | Next check |
|---|---|---|---|
| 1 | 直接竞品“认知独立桌面机器人” | 未找到成熟产品 | 继续检索；可能是空白，也可能是无需求 |
| 2 | 中国本地价格/付费意愿 | 未获取 | 本地预售/访谈 |
| 3 | 长期（>3 个月）行为改变证据 | 未获取 | 2 周日记只能看方向 |
