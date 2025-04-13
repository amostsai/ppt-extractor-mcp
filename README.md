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

## 手動安裝

```bash
cd ~/Documents/Cline/MCP/
git clone https://github.com/amostsai/ppt-extractor-mcp.git
cd ppt-extractor-mcp
pip install -e .
```

## vscode mcp設定
編輯 ~/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
將以下內容貼到mcpServers大括號內
根據電腦實際情形修改args路徑設定
存檔後若設定正確可以發現左側ppt-extractor會出現綠燈（底下紅字是INFO log訊息不用管他）
```
"ppt-extractor": {
      "command": "python",
      "args": ["/home/你的電腦帳號/Documents/Cline/MCP/ppt-extractor-mcp/src/__main__.py"],
      "env": {
        "LOG_LEVEL": "INFO"
      },
      "disabled": false,
      "autoApprove": []
    }
```

## 使用方式
1. 將要讀取的pptx檔（不支援ppt舊格式）放到專案資料夾中
2. 打開vscode的cline擴充功能
3. 輸入"讀取目前專案底下的abc.pptx檔整理成大綱並儲存為md檔"
4. 若AI回應找不到檔案請他用list方式讀取專案目錄或直接在步驟3直接給他完整檔案路徑
5. 正常就會發現已經幫你整理好一個md檔 ：）


### 參數說明（給AI使用）

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
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.py
└── uv.lock

## 授權條款

MIT License
