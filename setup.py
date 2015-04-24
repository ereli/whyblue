from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'color_extractor',
  ext_modules = cythonize("color_extractor.pyx"),
)
