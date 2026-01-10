from setuptools import setup, find_packages

setup(
    name="GitHubGuard",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["requests"],
    description="Automatically create GitHub issues from Python scripts.",
    author="Matteo",
    url="https://github.com/Xehia/GitHubGuard",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
