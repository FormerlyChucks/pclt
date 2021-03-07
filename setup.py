from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name="pclt",
    py_modules=["download",
		"pprint",
		"pyecho",
		"removefile",
		"makefolder"],
    entry_points={"console_scripts": ["download=download:download",
				                      "pprint=pprint:pprint",
				                      "removefile=removefile:removefile"]},
    version="0.0.7",
    description="Python Command Line Tools",
    long_description=readme(),
    author="diogenesjunior",
    author_email="diogenesjunior@protonmail.com",
    url="https://github.com/ilikepyt/pclt/",
    install_requires=['requests','downsyndrome']
)
