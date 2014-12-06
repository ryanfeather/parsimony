from setuptools import setup, find_packages

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.4'
]

exec(open('parsimony/release.py').read())

setup(

    name="parsimony",
    version=__version__,
    packages=find_packages(),
    install_requires=['dill>=0.2.1'],
    description="A library for simple caching and lazy initialization.",
    classifiers=classifiers
)