---
description: Check and update CLAUDE.md memory based on changes to skills, commands, agents, and hooks.
---

# Update Memory

检查并更新 CLAUDE.md 全局记忆文件，确保其内容与 skills、commands、agents、hooks 的源文件保持同步。

## 功能概述

CLAUDE.md 是一个汇总记忆文件，包含：
- 技能目录结构（来自 `skills/`）
- 命令列表（来自 `commands/`）
- 代理配置（来自 `agents/`）
- 钩子定义（来自 `hooks/`）

当这些源文件发生变化时，CLAUDE.md 需要同步更新。

## 检测逻辑

1. **扫描源文件修改时间**
   - `~/.claude/skills/**/skill.md`
   - `~/.claude/commands/**/*.md`
   - `~/.claude/agents/**/*.md`
   - `~/.claude/hooks/**/*.{js,json}`

2. **对比 CLAUDE.md 最后修改时间**
   - 如果任意源文件比 CLAUDE.md 新 → 需要更新
   - 记录上次同步时间戳（`~/.claude/.last-memory-sync`）

3. **生成报告**
   - 列出所有变更的源文件
   - 显示需要更新的 CLAUDE.md 章节

## 更新流程

### 1. 扫描阶段

```
扫描 Skills: X 个
扫描 Commands: Y 个
扫描 Agents: Z 个
扫描 Hooks: W 个
```

### 2. 对比阶段

```
需要更新的章节:
- [ ] 技能目录结构 (3 个技能变更)
- [ ] 命令列表 (1 个命令新增)
- [ ] 代理配置 (无变更)
- [ ] 钩子定义 (2 个钩子修改)
```

### 3. 确认更新

询问用户是否执行更新：
```
是否更新 CLAUDE.md? (yes/no/diff)
- yes: 执行更新
- no: 取消
- diff: 显示详细差异
```

### 4. 执行更新

- 保留用户手动编辑的内容（如"用户背景"、"技术栈偏好"）
- 仅更新 AUTO-GENERATED 标记的章节
- 更新时间戳

## 使用方式

```
/update-memory          # 检查并提示更新
/update-memory --check  # 仅检查，不更新
/update-memory --force  # 强制更新，不询问
/update-memory --diff   # 显示差异对比
```

## 输出示例

### 检查结果

```
📋 CLAUDE.md 记忆状态检查

源文件状态:
✅ Skills: 24 个 (最近修改: ml-paper-writing)
✅ Commands: 14 个 (最近修改: update-readme)
✅ Agents: 7 个 (无变更)
✅ Hooks: 5 个 (最近修改: session-summary)

时间对比:
- CLAUDE.md 最后更新: 2024-01-15 10:30
- 源文件最后修改: 2024-01-16 14:22

⚠️ 检测到变更，建议更新 CLAUDE.md

变更详情:
1. skills/ml-paper-writing/skill.md (修改于 14:22)
2. commands/update-readme.md (修改于 13:15)
3. hooks/session-summary.js (修改于 11:45)

是否执行更新? (yes/no/diff)
```

### 更新完成

```
✅ CLAUDE.md 已更新

更新内容:
- 技能目录: 同步 24 个技能
- 命令列表: 同步 14 个命令
- 代理配置: 无变更
- 钩子定义: 同步 5 个钩子

下次同步时间戳已更新。
```

## 集成建议

- 在 `session-summary.js` 中集成检查提醒
- 在 PostToolUse 钩子中实时检测
- 建议定期执行（如每次会话结束时）
