from setuptools import setup, find_packages

setup(
    name="ai-token-monitor",
    version="0.1.0",
    author="Tharanika",
    author_email="kavintharanika@gmail.com",
    description="AI Token & Cost Monitoring SDK for OpenAI, OpenRouter, and Groq",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100.0",
        "openai>=1.0.0",
        "starlette>=0.27.0",   # ← was missing in original
        "python-dotenv>=1.0.0", # ← was missing in original
        "uvicorn>=0.22.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
