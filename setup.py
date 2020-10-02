# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup
from codecs import open

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

setup(
    name='IwannaPE',
    version='1.0.0',
    description='Fast! Easy! Interesting!!! Easy create Iwanna Game',
    long_description=readme,
    author='Tosirukun',
    author_email='tosirusan@gmail.com',
    url='https://github.com/Tosirukun/IwannaPE',
    license=license,
    install_requires=['pygame', 'asyncio'],
    keywords='IwannaPE iwannape Tosirukun tosirukun IwannabethePythonEngine',
    packages=['IwannaPE']
)
