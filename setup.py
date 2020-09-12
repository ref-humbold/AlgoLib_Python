# -*- coding: utf-8 -*-
import setuptools

PYTHON_MIN_VERSION = 3.6

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(name="AlgoLib",
                 version="0.0.0",
                 author="Rafal Kaleta",
                 description="Library of various algorithms and data structures.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(),
                 python_requires=f">={PYTHON_MIN_VERSION}",
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: Apache Software License",
                              "Operating System :: OS Independent",
                              "Development Status :: 1 - Planning",
                              "Intended Audience :: Developers"])
