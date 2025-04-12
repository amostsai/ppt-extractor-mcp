# PPT Extractor MCP

PowerPoint 文字提取器 MCP 服務，可從 PowerPoint 檔案中提取文字內容並以結構化格式呈現。

## 功能特點

- 支援從 .pptx 檔案提取文字內容
- 可選擇包含講者備註
- 可選擇包含空白投影片
- 支援 Markdown 或純文字輸出格式
- 基於 FastMCP 實現，提供簡單易用的 API

## 系統需求

- Python 3.10-3.12
- 相依套件：
  - fastmcp
  - pydantic
  - python-pptx

## 安裝

```bash
git clone git@github.com:amostsai/ppt-extractor-mcp.git
cd ppt_extractor_mcp
pip install -e .
```

## 使用方式

### 啟動服務

```bash
python -m ppt_extractor_mcp
```

### 參數說明

- `format`: 輸出格式，可選 "markdown"（預設）或 "plain"
- `include_notes`: 是否包含講者備註，預設為 False
- `include_empty_slides`: 是否包含沒有文字的幻燈片，預設為 False


## 專案結構
ppt-extractor-mcp/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── extractors.py
│   └── server.py
├── .gitignore
├── example_mcp_config.json
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
└── uv.lock

## 授權條款

MIT License
