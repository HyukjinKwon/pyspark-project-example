#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(name='pyexample',
      version='0.0.1',
      description='PySpark Project Example',
      author='Hyukjin Kwon',
      author_email='gurwls223@gmail.com',
      url='https://github.com/HyukjinKwon/pyspark-project-example',
      packages=find_packages(exclude=['*.tests']),
      install_requires=['py4j==0.9.0'])
