from setuptools import setup, find_packages

setup(
    name="pdf_to_text",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyPDF2"
    ],
    entry_points={
        "console_scripts": [
            "extract-pdf=pdf_to_text.cli:main"
        ]
    },
    author="Leo Matei",
    description="A simple PDF text extraction tool",
    url="https://github.com/leomatei/pdf_to_text",
)
