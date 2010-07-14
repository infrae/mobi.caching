#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION="1.0b1"

setup(name='mobi.caching',
      version=VERSION,
      description='Cache utils',
      author='Infrae',
      author_email='info@infrae.com',
      url='infrae.com',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['mobi'],
      install_requires=[
        'repoze.lru',
      ],
     )
