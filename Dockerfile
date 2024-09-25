# 使用官方 Python 运行时作为父镜像
FROM python:3.11-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到容器的 /app 中
COPY . /app

# 安装需要的包
RUN pip3 install --no-cache-dir -r requirements.txt

# 安装 gunicorn
RUN pip3 install gunicorn

# 让端口 8000 可以从容器外部访问
EXPOSE 8000

# 定义环境变量
ENV PYTHONUNBUFFERED=1 PYTHONIOENCODING=utf-8

# 运行 app.py
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers", "10", "--timeout", "600","--worker-class", "gevent"]