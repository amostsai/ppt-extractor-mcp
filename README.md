# PowerPoint 文字提取器 MCP

一個基於 FastMCP 框架的 Model Context Protocol (MCP) 服務，用於從 PowerPoint 簡報中提取文字內容並以結構化格式呈現。

## 功能特點

- 🔍 從 PowerPoint (.pptx) 檔案中提取所有文字內容
- 📊 保留幻燈片的結構和順序
- 📝 支援 Markdown 和純文字輸出格式
- 📢 可選擇包含講者備註
- 🔄 可與任何支援 MCP 協議的客戶端整合

## 安裝

### 使用 pip 安裝

```bash
pip install ppt_extractor_mcp
```

### 從源碼安裝

```bash
git clone https://github.com/yourusername/ppt_extractor_mcp.git
cd ppt_extractor_mcp
pip install -e .
```

### 使用 Docker

```bash
# 使用 Docker Compose
docker-compose up -d

# 或直接使用 Docker
docker build -t ppt_extractor_mcp .
docker run -p 8000:8000 ppt_extractor_mcp
```

## 使用方法

### 作為獨立服務運行

```bash
python -m ppt_extractor_mcp
```

服務將在 http://localhost:8000 上啟動。


### API 參數

- `format`: 輸出格式，可選 `markdown`（默認）或 `plain`
- `include_notes`: 是否包含講者備註，`true` 或 `false`（默認）
- `include_empty_slides`: 是否包含沒有文字的幻燈片，`true` 或 `false`（默認）

## 程式碼示例

### Python 客戶端

```python
from fastmcp.client import MCPClient

# 創建客戶端
client = MCPClient(base_url="http://localhost:8000")

# 讀取 PowerPoint 文件
with open("my_presentation.pptx", "rb") as f:
    file_content = f.read()

# 發送請求
response = client.complete(
    provider="ppt-extractor",
    files=[("my_presentation.pptx", file_content)],
    parameters={
        "format": "markdown",
        "include_notes": True
    }
)

# 處理響應
print(response.completion)
```

### 使用 curl

```bash
curl -X POST http://localhost:8000/v1/complete \
  -H "Content-Type: multipart/form-data" \
  -F "provider=ppt-extractor" \
  -F "parameters={\"format\": \"markdown\", \"include_notes\": true}" \
  -F "files=@/path/to/your/presentation.pptx"
```

## 專案結構
ppt-extractor-mcp/
├── examples/
│   └── extract_ppt_example.py
├── ppt_extractor_mcp/
│   ├── __init__.py
│   ├── __main__.py
│   ├── api.py
│   └── extractors.py
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── example_mcp_config.json
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── setup.py


## 集成到其他項目

您可以將 `ppt_extractor_mcp` 作為庫導入到您自己的 Python 專案中：

```python
from ppt_extractor_mcp.extractors import extract_text_from_ppt, format_as_markdown

# 讀取檔案
with open("presentation.pptx", "rb") as f:
    content = f.read()

# 提取內容
slides_content = extract_text_from_ppt(content, include_notes=True)

# 格式化為 Markdown
markdown_text = format_as_markdown(slides_content, "presentation.pptx")
```

## 貢獻

歡迎提交問題報告、功能請求和改進建議！請參閱 [CONTRIBUTING.md](CONTRIBUTING.md) 了解詳情。

## 授權

MIT 授權 - 詳見 [LICENSE](LICENSE) 文件