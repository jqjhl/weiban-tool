# WeiBan Tool

WeiBan Tool 是一个自动化工具，用于辅助完成课程学习和考试。本项目是 [https://github.com/Coaixy/weiban-tool](https://github.com/Coaixy/weiban-tool) 的二次开发版本。

## 功能特点

- 自动登录
- 自动选择
- 支持自动考试功能
- 提供 Web 界面，方便操作

## 安装说明

### 前提条件

- Python 3.9+
- Docker (仅用于 Docker 安装方式)

### 方式一：不使用 Docker

1. 克隆仓库：
   ```
   git clone https://github.com/yourusername/weiban-tool.git
   cd weiban-tool
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```
   python app.py
   ```

4. 打开浏览器，访问 `http://localhost:8000`。

### 方式二：使用 Docker

1. 克隆仓库：
   ```
   git clone https://github.com/yourusername/weiban-tool.git
   cd weiban-tool
   ```

2. 构建 Docker 镜像：
   ```
   docker build -t weibantool:latest .
   ```

3. 运行 Docker 容器：
   ```
   docker run -d --name weiban-tool -p 8000:8000 --restart always weibantool:latest
   ```

4. 打开浏览器，访问 `http://localhost:8000`。

## 使用方法

1. 在 Web 界面中输入以下信息：
   - 账号
   - 密码
   - 学校名称
   - 是否自动验证
   - 项目编号
   - 是否自动考试
   - 允许错题数

2. 点击"开始"按钮，程序将自动执行相应操作。

3. 查看输出日志，了解执行进度和结果。

## 注意事项

- 本工具仅用于学习和研究目的，请勿用于其他用途。
- 使用本工具可能违反使用条款，请自行承担使用风险。
- 请确保你有权限使用输入的账号信息。

## 贡献指南

欢迎贡献代码或提出建议。请遵循以下步骤：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 联系方式

如有任何问题或建议，请通过以下方式联系我们：

- 项目地址：[https://github.com/jqjhl/weiban-tool](https://github.com/jqjhl/weiban-tool)
- 电子邮件：hdcsrcy@gmail.com

## 致谢

本项目基于 [Coaixy/weiban-tool](https://github.com/Coaixy/weiban-tool) 进行二次开发。感谢原作者的贡献。
