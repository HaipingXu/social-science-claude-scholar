---
description: Update README documentation and push changes to GitHub.
---

# Update README

Update README.md file with latest project information and push to GitHub.

## Instructions

1. **Analyze Current State**
   - Read existing README.md
   - Check recent code changes (git log)
   - Identify documentation gaps

2. **Determine Updates Needed**
   Check for:
   - New features added
   - Configuration changes
   - Dependencies updated
   - Installation instructions
   - Usage examples
   - API changes

3. **Propose README Updates**
   Show sections that need updating:
   ```markdown
   Proposed changes:
   - [ ] Update Installation section (new dependencies)
   - [ ] Add usage example for feature X
   - [ ] Update API documentation
   - [ ] Fix broken links
   ```

4. **Update README**
   - Apply proposed changes
   - Maintain markdown formatting
   - Keep language consistent (中文/English)
   - Preserve structure

5. **Commit and Push**
   - Run `/update-github` with `docs(readme):` type
   - Example commit: `docs(readme): 更新 README 文档`

## Example Usage

```
User: /update-readme

1. Analyzing repository state...

Recent changes:
- feat(data): 添加新的数据加载器
- fix(model): 修复训练时的内存泄漏
- chore: 更新依赖到 v2.0.0

2. Checking README.md...

Current README sections:
- Installation
- Usage
- API Reference
- Contributing

3. Proposed updates:
   [ ] Installation - 添加新的依赖说明
   [ ] Usage - 添加数据加载器示例
   [ ] API Reference - 更新模型接口文档

4. Applying updates...

   Updating Installation:
   + pip install torch>=2.0.0
   + pip install transformers>=4.30.0

   Adding usage example:
   ## 数据加载示例
   ```python
   from data import DataLoader
   loader = DataLoader(batch_size=32)
   ```

5. Review changes before committing...
   [Show diff]

6. Proceed with commit?
   > yes

7. Committing with: docs(readme): 更新 README 文档
   Co-Authored-By: Claude <noreply@anthropic.com>

✅ README updated and pushed to GitHub!
```

## README Structure Template

When updating README, follow this structure:

```markdown
# 项目名称

简短描述项目用途。

## 安装

### 依赖要求
- Python >= 3.8
- uv 或 pip

### 安装步骤
```bash
uv sync
```

## 使用

### 基本用法
```python
# 示例代码
```

### 配置
说明配置文件位置和格式。

## API 文档

主要接口说明。

## 开发

### 运行测试
```bash
pytest
```

### 代码规范
- 遵循 PEP 8
- 使用 mypy 进行类型检查
- 使用 ruff 进行 linting

## 贡献

欢迎提交 Pull Request。

## 许可证

MIT License
```

## Arguments

$ARGUMENTS can be:
- `--full` - Complete README rewrite
- `--quick` - Only update critical sections (installation, usage)
- `<section>` - Update specific section only

## Integration

After updating README, this command automatically invokes `/update-github` with `docs(readme):` commit type.
