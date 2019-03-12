from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy


ext_modules = [
    Extension("primes",["primes.pyx"]),
    Extension(
        "alter_array",
        ["alter_array.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    ),
    Extension("Haversine",["Haversine.pyx"],
        include_dirs=[numpy.get_include()])
]


setup(
    ext_modules=cythonize(ext_modules),
    )
