#!/usr/bin/env python

from distutils.core import setup

setup(name='Utils',
      version='0.1',
      description='Utils',
      author='Alberic Walsh',
      url='https://github.com/albericwalsh/Utils.git',
      packages=['Utils'],
      package_dir={'Utils': 'Utils'},
      package_data={'Utils': ['*.py']},
      )
