FROM python:3.12-slim

WORKDIR /app

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 複製必要文件
COPY requirements.txt .
COPY pyproject.toml .
COPY setup.py .
COPY src ./ppt_extractor_mcp

# 安裝 Python 依賴
RUN pip install --no-cache-dir -e . fastmcp

# 暴露 MCP 服務端口
EXPOSE 8000

# 執行應用
CMD ["python", "-m", "ppt_extractor_mcp"]
