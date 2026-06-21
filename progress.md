# 部署进度

## 2026-06-19

- 已读取 planning-with-files 技能说明。
- 已确认仓库根目录文件列表和当前 git 状态。
- 已创建任务计划、发现记录和进度记录。
- 已读取 `pyproject.toml`、`requirements.txt`、启动脚本、`docker-compose.yml`、`.env.example`、`web.py` 和部分 README。
- 已确认部署方式采用虚拟环境加 `python web.py`。
- 已创建 `.venv`。
- 已通过 `.venv\Scripts\python.exe -m pip install -r requirements.txt` 安装运行依赖。
- pip 安装完成，但提示检查 pip 最新版本失败；这不影响依赖安装结果。
- 已尝试后台启动 `web.py`，进程 PID 为 `34364`。
- 启动后 `7861` 未监听，`/keepalive` 和 `/v1/models` 均连接被拒绝。
- 用户要求改用 Pixi 管理 Python 环境。
- 已在 `pyproject.toml` 添加 Pixi workspace、Python 依赖和常用任务。
- 已把 `start.bat` 和 `start.sh` 改为 `pixi install` 加 `pixi run start`。
- 已新增 `docs/USAGE_zh.md` 使用指南。
- `pixi install` 首次因用户缓存目录权限失败，已在用户批准后用非沙箱权限执行成功。
- Pixi 环境使用 Python `3.13.14`。
- 已通过 Pixi 环境运行 `py_compile` 检查关键 Python 文件。
- 已在沙箱外通过 Pixi 启动常驻服务，进程 PID 为 `31612`。
- 已验证 `HEAD /keepalive` 返回 200。
- 已验证 `GET /v1/models` 携带 `Authorization: Bearer pwd` 返回 200。
- 已新增 `tests/test_smoke.py`。
- 已运行 `pixi run test`，结果为 `1 passed, 6 warnings`。
