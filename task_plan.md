# 部署项目并创建使用指南

## 目标

在本机部署并验证 gcli2api 项目，整理一份可执行的中文使用指南。

## 阶段

| 阶段 | 状态 | 内容 |
|---|---|---|
| 1 | complete | 梳理项目依赖、配置和启动入口 |
| 2 | complete | 切换为 Pixi 环境管理并安装依赖 |
| 3 | complete | 启动服务并验证健康状态 |
| 4 | complete | 创建使用指南文档 |
| 5 | complete | 汇总部署结果和后续操作 |

## 决策记录

| 时间 | 决策 |
|---|---|
| 2026-06-19 | 优先采用项目已有 Python/FastAPI 本地启动方式；如依赖缺失再安装。 |
| 2026-06-19 | 不使用 `start.bat` 或 `start.sh` 部署，因为它们会执行 `git reset --hard` 覆盖本地改动。 |
| 2026-06-19 | 用户要求改为 Pixi 管理 Python 环境，改用 `pyproject.toml` 的 `[tool.pixi]` 配置。 |

## 错误记录

| 错误 | 尝试 | 处理 |
|---|---|---|
| PowerShell workdir 未生效，命令落到 C:\ | 读取项目文件 | 改用完整路径访问项目文件。 |
| 项目本地 planning-with-files 技能不存在 | 读取 .agents/skills | 使用全局技能说明继续。 |
| 后台启动后 7861 端口未监听 | Start-Process 启动 `web.py` | 直接捕获前台启动输出定位错误。 |
| 后台启动从错误目录解析 `./creds` | `pythonw.exe web.py` | 将默认路径改为基于项目根目录解析。 |
| 沙箱内 pytest 读取父目录失败 | `pixi run test` | 固定测试根目录并在非沙箱验证；随后新增 smoke test。 |
