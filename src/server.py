"""
PowerPoint 提取器的 MCP API 實現
"""
import os
import logging
from typing import Optional

from fastmcp import FastMCP
from pydantic import BaseModel, Field

from extractors import extract_text_from_ppt, format_as_markdown, format_as_plain_text


# 設置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ppt_extractor_mcp")

# 定義參數模型
class PPTExtractorParams(BaseModel):
    format: Optional[str] = Field(
        default="markdown", 
        description="輸出格式: markdown 或 plain"
    )
    include_notes: Optional[bool] = Field(
        default=False, 
        description="是否包含講者備註"
    )
    include_empty_slides: Optional[bool] = Field(
        default=False, 
        description="是否包含沒有文字的幻燈片"
    )

# 創建 MCP 實例
mcp = FastMCP("ppt-extractor")

@mcp.tool()
def extract_ppt_text(file_path: str, params: PPTExtractorParams) -> str:
    """從 PowerPoint 檔案中提取文字並返回結構化內容"""
    logger.info(f"接收到提取請求: 檔案={file_path}, 參數={params}")

    if not file_path.lower().endswith(".pptx"):
        logger.warning(f"不支援的檔案類型: {file_path}")
        return f"錯誤: 檔案 '{file_path}' 不是 PowerPoint (.pptx) 格式。"

    try:
        with open(file_path, "rb") as f:
            ppt_content = f.read()

        text_content = extract_text_from_ppt(
            ppt_content, 
            include_notes=params.include_notes,
            include_empty_slides=params.include_empty_slides
        )

        if params.format == "plain":
            result = format_as_plain_text(text_content, os.path.basename(file_path))
        else:
            result = format_as_markdown(text_content, os.path.basename(file_path))

        logger.info(f"成功處理檔案: {file_path}")
        return result

    except Exception as e:
        logger.error(f"處理檔案時發生錯誤: {str(e)}", exc_info=True)
        return f"處理 PowerPoint 時發生錯誤: {str(e)}"
