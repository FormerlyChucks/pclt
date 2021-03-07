from setuptools import setup

setup(author="diogenesjunior",
      author_email="diogenesjunior@protonmail.com",
      description="Python Command Line Tools",
      entry_points={"console_scripts": ["dl=pclt:dl", "pp=pclt:pp", "rf=pclt:rf"]},
      install_requires=['requests','downsyndrome'],
      long_description=open('README.rst').read(),
      name="pclt",
      packages=['pclt'],
      py_modules=["dl", "pp", "rf"],
      url="https://github.com/ilikepyt/pclt/",
      version="0.0.8")
