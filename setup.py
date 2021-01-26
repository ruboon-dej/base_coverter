from setuptools import find_packages, setup

setup(
    name="baseconverter",
    packages=find_packages(include=["lib"]),
    version="0.1.0",
    author="Ruboon Dej-Udom",
    license="MIT",
    test_suite="tests",
)