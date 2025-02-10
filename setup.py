from setuptools import setup, find_packages

setup(
    name="hangman",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Medha Agarwal",
    author_email="medsss19@gmail.com",
    description="A command-line Hangman game with multiple word categories",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/medss19/hangman",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "hangman=src.hangman:main",
        ],
    },
)