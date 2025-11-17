"""
Setup configuration for Social Content Creator
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="social-content-creator",
    version="0.1.0",
    author="Social Content Creator AI",
    description="AI-powered social media content creation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aifreak32/Social-Content-Creator",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
        "requests>=2.31.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "openai>=1.0.0",
        "anthropic>=0.18.0",
        "Pillow>=10.0.0",
        "beautifulsoup4>=4.12.0",
        "python-dateutil>=2.8.2",
        "pytz>=2023.3",
    ],
    entry_points={
        "console_scripts": [
            "social-content-creator=social_content_creator.cli:main",
        ],
    },
)
