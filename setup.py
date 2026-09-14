from setuptools import find_packages, setup

setup(
    name="gaussian-docs-scraper",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "pypdf",
        "python-docx",
        "python-pptx",
    ],
    extras_require={
        "test": ["pytest"],
    },
)
