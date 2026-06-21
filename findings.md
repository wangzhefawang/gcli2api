# 部署发现

## 项目结构

- 项目根目录包含 `web.py`、`config.py`、`requirements.txt`、`pyproject.toml`、`docker-compose.yml`、`Dockerfile`、`start.sh` 和 `start.bat`。
- `git status --short` 显示 `AGENTS.md` 是未跟踪文件，后续不会修改或回退它。

## 环境发现

- 直接设置工作目录的工具调用未落到仓库目录，后续命令使用完整路径。
- 仓库中未发现 `.agents/skills/planning-with-files/SKILL.md`，已读取全局技能说明。
- `pyproject.toml` 要求 Python `>=3.12`，当前系统 `python --version` 为 `Python 3.14.4`。
- 项目根目录当前没有 `.venv`，需要创建本地虚拟环境。
- 项目根目录当前没有 `.env`，可用环境变量或默认值启动；默认端口是 `7861`，默认密码是 `pwd`。
- `web.py` 会通过 Hypercorn 启动 FastAPI 应用，控制面板地址记录为 `http://127.0.0.1:{PORT}`。
- `start.bat` 和 `start.sh` 都包含 `git reset --hard`，不适合在已有本地改动的工作区中直接运行。
- 本机已安装 `pixi 0.63.2`。
- 切换前项目没有 Pixi 配置，实际使用的是 `.venv + pip`。
- `.gitignore` 会忽略 `*.toml`，所以 Pixi 配置放入现有 `pyproject.toml`，避免新增 `pixi.toml` 被忽略。
