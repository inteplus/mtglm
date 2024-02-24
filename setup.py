#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages
from mt.glm.version import version

setup(
    name="mtglm",
    version=version,
    description="Minh-Tri Pham's extra modules for dealing with GLM in Python",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    # scripts=[
    #     "scripts/immview",
    # ],
    install_requires=[
        "pyglm",
        # "mtbase>=4.25",  # we don't need mtbase yet
    ],
)
