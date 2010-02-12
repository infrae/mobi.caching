#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='playmobile.caching',
      version='0.1dev',
      description='Cache utils',
      author='Infrae',
      author_email='info@infrae.com',
      url='infrae.com',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['playmobile'],
      install_requires=[],
     )
