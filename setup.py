from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="markdown-link-checker",
    script_name="link_checker",
    version="0.1.0",
    author="Jose Salvatierra",
    description="A command-line interface that, given a markdown file, verifies all the links work.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tecladocode/markdown-link-checker",
    py_modules=["link_checker"],
    install_requires=["Click", "markdown", "beautifulsoup4", "requests", "rich"],
    entry_points={
        "console_scripts": [
            "link_checker = link_checker:check_file_links",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
