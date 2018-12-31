from distutils.core import setup
from setuptools import find_packages

setup(name='chickenstrumentation',
      version='0.1',
      py_modules=['chickenstrumentation'],
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      )
