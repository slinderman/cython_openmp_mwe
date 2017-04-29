#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

ext_modules = cythonize('**/*.pyx')
setup(name='cython_openmp_mwe',
      version='0.1',
      author='Scott Linderman',
      ext_modules=ext_modules,
      include_dirs=[np.get_include()]
     )