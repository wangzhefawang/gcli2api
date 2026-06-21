# GCLI2API 使用指南

## 环境准备

本项目使用 Pixi 管理 Python 运行环境，不再需要手动创建 `.venv` 或执行 `pip install -r requirements.txt`。

安装 Pixi 后，在项目根目录执行：

```powershell
pixi install
```

Pixi 会根据 `pyproject.toml` 创建隔离环境，并安装 Python 与项目依赖。

## 启动服务

Windows、Linux 和 macOS 都可以在项目根目录执行：

```powershell
pixi run start
```

也可以使用项目脚本：

```powershell
.\start.bat
```

Linux 或 macOS 使用：

```bash
bash start.sh
```

默认服务地址是：

- 控制面板：`http://127.0.0.1:7861`
- 探活接口：`http://127.0.0.1:7861/keepalive`
- OpenAI 兼容模型接口：`http://127.0.0.1:7861/v1/models`

## 配置密码

默认通用密码是 `pwd`。

推荐复制 `.env.example` 为 `.env` 后修改：

```env
PASSWORD=your_password
PORT=7861
HOST=0.0.0.0
```

如果需要区分 API 和控制面板密码，可以设置：

```env
API_PASSWORD=your_api_password
PANEL_PASSWORD=your_panel_password
```

`PASSWORD` 优先级最高；如果设置了 `PASSWORD`，会覆盖 `API_PASSWORD` 和 `PANEL_PASSWORD`。

## 添加凭证

启动后打开控制面板：

```text
http://127.0.0.1:7861
```

使用控制面板密码登录，然后在凭证管理页面添加或上传 Google OAuth 凭证。

默认 SQLite 数据库和凭证数据存放在项目根目录的 `creds/`，该目录已被 `.gitignore` 忽略，不能提交真实凭证。

## 调用 OpenAI 兼容接口

模型列表：

```powershell
Invoke-WebRequest `
  -Uri "http://127.0.0.1:7861/v1/models" `
  -Headers @{ Authorization = "Bearer pwd" }
```

聊天接口：

```powershell
$body = @{
  model = "gemini-2.5-pro"
  messages = @(
    @{ role = "user"; content = "你好" }
  )
} | ConvertTo-Json -Depth 10

Invoke-WebRequest `
  -Uri "http://127.0.0.1:7861/v1/chat/completions" `
  -Method Post `
  -Headers @{
    Authorization = "Bearer pwd"
    "Content-Type" = "application/json"
  } `
  -Body $body
```

把示例中的 `pwd` 替换成你的 `API_PASSWORD` 或 `PASSWORD`。

## 常用 Pixi 命令

```powershell
pixi run start
pixi run test
pixi run format
pixi run lint
pixi run typecheck
```

## 停止服务

在前台运行时按 `Ctrl+C` 停止。

如果以后台进程方式启动，可以在 PowerShell 中查找并停止：

```powershell
Get-Process python,pythonw -ErrorAction SilentlyContinue
Stop-Process -Id <PID>
```
