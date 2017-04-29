#!/usr/bin/env python

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np

extra_compile_args = ['-fopenmp']
extra_link_args = ['-fopenmp']

ext_modules = cythonize('**/*.pyx')
for e in ext_modules:
    e.extra_compile_args.extend(extra_compile_args)
    e.extra_link_args.extend(extra_link_args)

setup(name='sum_anti_diag',
      version='0.1',
      author='Scott Linderman',
      ext_modules=ext_modules,
      install_requires=['numpy'],
      include_dirs=[np.get_include()]
     )