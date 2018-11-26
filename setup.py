#!/usr/bin/env python
# coding=utf-8

from setuptools import setup,find_packages

setup(name="pirate",
      version="0.1",
      author='nunum',
      author_email='ntmg.22@gmail.com',
      description='Search for oyur favourite movies',
      packages=find_packages(),
      package_data={
        'pirate': ['*.cfg'],
      },
      entry_points={
        'console_scripts': [
            'pirate = pirate.pirate:main'
        ]
    })
