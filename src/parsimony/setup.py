from setuptools import setup, find_packages
import parsimony
setup(
    name="parsimony",
    version=parsimony.__version__,
    packages=find_packages(),
    install_requires=['dill>=0.2.1'],
    description="A library for simple caching and lazy initialization."
)