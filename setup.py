from setuptools import setup, find_packages

setup(
    name="ppt_extractor_mcp",
    version="1.0.0",
    description="從 PowerPoint 檔案中提取並結構化文字內容的 MCP 服務",
    author="Amos Tsai",
    author_email="amos.tsai@gmail.com",
    url="https://github.com/amostsai/ppt-extractor-mcp",
    packages=find_packages(),
    install_requires=[
        "fastmcp>=0.1.0",
        "pydantic>=1.10.0",
        "python-pptx>=0.6.21",
    ],
    entry_points={
        "console_scripts": [
            "ppt_extractor_mcp=ppt_extractor_mcp.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
)
