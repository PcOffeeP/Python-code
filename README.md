<!-- DOCUMENT-CONTRACT
Purpose: 说明本仓库如何保存编程训练、长期学习状态与复习产物。
Scope: 仓库职责、目录边界、题目生命周期、状态文件、复习流程与扩展步骤。
Must Preserve:
- 每道正式训练题都必须在 problems/ 下拥有独立目录。
- 学习笔记与 Online Judge 提交代码必须保持分离。
- 指定为追加写入的状态日志必须保持机器可读与 append-only。
- GPT 集成内容必须位于 instructions/ 与 knowledge/ 下。
- 面向阅读者的说明以中文为主，程序依赖的字段名、枚举值与代码标识符保持稳定。
Non-goals:
- 完整的 GPT Instructions 或详细教学 Knowledge。
- 完整聊天记录或临时草稿。
-->

<!-- DECISION-LOG
D001 — 面向阅读者的项目文档统一使用中文，机器可读标识符与必要技术术语保留原文。
Why: 用户明确要求项目整体文档以中文介绍；保留稳定标识符可避免破坏 State 数据结构、代码与自动处理流程。
-->

# AI / 算法机考训练 Workspace

本仓库是用于 AI Coding 与算法机考训练的长期 Workspace。它以稳定、可预测的目录保存每道题的学习产物、可提交代码、后续重写版本与长期学习状态。

仓库中面向阅读者的说明以中文为主。文件路径、代码标识符、状态枚举以及需要准确对应实现的英文技术术语按需保留原文。

## 目录结构

```text
state/          当前快照、能力等级、复习队列与追加式日志
problems/       每道正式训练题的独立目录
sessions/       具有长期价值的精简训练总结
templates/      新题目与 Session 更新的起始模板
```

每道题的目录包含：

```text
README.md       稳定的题目信息、算法、复杂度、关键模式与当前状态
notes.ipynb     理解、推导、实验、错误与复习笔记
solution.py     仅使用标准输入输出的干净提交代码
tests.py        常规、边界、并列与最小用例
reviews/        空白重写、限时重写及复习日志
```

## 题目生命周期

1. 从 `templates/problem-template/` 复制并创建新的题目目录。
2. 在该题的 `README.md` 中记录题目约定与当前状态。
3. 在 `notes.ipynb` 中完成理解、推导、实验与学习记录。
4. 仅将最终可提交版本放入 `solution.py`，并在 `tests.py` 中加入针对性测试。
5. 将正式 Attempt 与可复用错误模式追加到 `state/`。
6. 在 `state/review_queue.yaml` 中安排空白重写、限时重写、概念复习或 Python 模式复习。
7. 将后续实现保存在 `reviews/` 中；只有新证据足以支持变化时，才更新题目状态与能力矩阵。

## State 状态系统

- `current_state.yaml`：简短的当前状态快照。训练重点改变时可以整体更新。
- `skill_matrix.yaml`：保存基于证据的能力等级，从 `0`（unknown）到 `5`（retained）。
- `review_queue.yaml`：保存可执行的复习计划。
- `problem_history.jsonl`：append-only；每次正式 Attempt 对应一行 JSON Object。
- `mistake_log.jsonl`：append-only；每个可复用错误模式对应一行 JSON Object。

State 文件不保存叙事式聊天记录。只有具备长期价值的 Session Summary 才应保存到 `sessions/`。

## Notebook 与 solution.py 的职责边界

`notes.ipynb` 是学习界面：解释、中间推导、实验、局部实现和错误分析都放在这里。`solution.py` 是提交界面：不得包含交互提示、教学提示、Notebook 专用辅助代码或对话式文字。

## 复习机制

Review 是有意进行的重新实现，而不是直接修改原答案。使用 `2026-09-19-blank-rewrite.py`、`2026-09-22-timed-rewrite.py` 等带日期的文件名，并将结果记录到 `reviews/review-log.md` 与 append-only 状态日志中。

## 如何新增一道题

1. 将 `templates/problem-template/` 复制到 `problems/<problem-slug>/`。
2. 替换 README 与 Notebook 中的全部占位内容。
3. 保持 `solution.py` 可直接提交，并添加具有代表性的测试。
4. 将第一次 Attempt 追加到 `state/problem_history.jsonl`。
5. 仅在新证据确实带来变化时，更新 `current_state.yaml`、`skill_matrix.yaml` 与 `review_queue.yaml`。
