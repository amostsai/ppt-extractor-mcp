"""
PowerPoint 提取器 MCP 客戶端使用示例
"""
import argparse
import sys
import os

from fastmcp.client import MCPClient

def main():
    parser = argparse.ArgumentParser(description="從 PowerPoint 提取文字內容")
    parser.add_argument("file", help="PowerPoint 檔案路徑")
    parser.add_argument("--format", choices=["markdown", "plain"], default="markdown",
                        help="輸出格式 (default: markdown)")
    parser.add_argument("--include-notes", action="store_true",
                        help="包含講者備註")
    parser.add_argument("--output", "-o", help="輸出檔案路徑 (默認: 標準輸出)")
    parser.add_argument("--mcp-url", default="http://localhost:8000",
                        help="MCP 服務 URL (默認: http://localhost:8000)")
    args = parser.parse_args()

    # 檢查檔案是否存在
    if not os.path.exists(args.file):
        print(f"錯誤: 檔案 '{args.file}' 不存在", file=sys.stderr)
        sys.exit(1)

    # 檢查檔案是否為 PowerPoint
    if not args.file.lower().endswith(".pptx"):
        print(f"警告: 檔案 '{args.file}' 可能不是 PowerPoint 檔案", file=sys.stderr)

    # 創建 MCP 客戶端
    client = MCPClient(base_url=args.mcp_url)

    try:
        # 讀取檔案內容
        with open(args.file, "rb") as f:
            file_content = f.read()

        # 發送請求
        print(f"正在處理 PowerPoint 檔案: {args.file}", file=sys.stderr)
        response = client.complete(
            provider="ppt-extractor",
            files=[(os.path.basename(args.file), file_content)],
            parameters={
                "format": args.format,
                "include_notes": args.include_notes
            }
        )

        # 輸出結果
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(response.completion)
            print(f"結果已保存至: {args.output}", file=sys.stderr)
        else:
            print(response.completion)

    except Exception as e:
        print(f"錯誤: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()