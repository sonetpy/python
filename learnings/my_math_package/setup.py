# In this setup, the mymath module contains a single function square that takes a number and returns its square. 
# The setup.py file is used to build and distribute the package.
from setuptools import setup, find_packages

setup(
    name='my_math_package',
    version='0.1',
    packages=find_packages(),
)
