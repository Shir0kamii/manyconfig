"""
Manyconfig
"""

import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="manyconfig",
    version="0.0.0",
    author="Shir0kamii",
    author_email="shir0kamii@gmail.com",
    description="An easy-to-use declarative loader of configuration",
    long_description=read("README.rst"),
    url="https://github.com/Shir0kamii/manyconfig",
    download_url="https://github.com/Shir0kamii/manyconfig/tags",
    platforms="any",
    packages=find_packages(),
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
