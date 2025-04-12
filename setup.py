from setuptools import setup, find_packages

setup(
    name="ppt_extractor_mcp",
    version="1.0.0",
    description="從 PowerPoint 檔案中提取並結構化文字內容的 MCP 服務",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/ppt_extractor_mcp",
    packages=find_packages(),
    install_requires=[
        "fastmcp>=0.1.0",
        "python-pptx>=0.6.21",
        "pydantic>=1.10.0",
        "uvicorn>=0.15.0",
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
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
