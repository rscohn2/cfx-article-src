from setuptools import setup
from spex import CppExtension, BuildExtension

def setup_relative(dir):
    return os.path.join(os.path.dirname(__file__), dir)

setup(
    name='colfax-cutlass-article',
    ext_modules=[
        CppExtension(
                name="copy_cute",  
                sources=["copy_cute.cpp"],
                include_dirs=[setup_relative('..')],
        )],
    cmdclass={
      'build_ext': BuildExtension
    })
