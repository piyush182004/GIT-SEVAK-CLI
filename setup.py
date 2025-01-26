from setuptools import setup, find_packages

setup(
    name="git-sevak",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "psutil"
    ],
    entry_points={
        "console_scripts": [
            "git-sevak=git_sevak.cli:main",
        ],
    },
    author="Piyush Mondal",
    author_email="your_email@example.com",
    description="A CLI tool for GitHub repository management and system information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/git-sevak",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
