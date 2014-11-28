.. Parsimony documentation master file, created by
   sphinx-quickstart on Wed Nov 26 17:18:05 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Parsimony's documentation!
=====================================

Contents:

.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _module-docs:

:mod:`parsimony`: Base classes and utilities
=============================================
.. automodule:: parsimony

Classes
-------
.. currentmodule:: parsimony
.. autoclass:: ParsimonyException
   :no-inherited-members:


Functions
---------
.. currentmodule:: parsimony
.. autofunction:: generate


:mod:`parsimony.configuration`: Sets the implementations used by parsimony.
===========================================================================
.. automodule:: parsimony.configuration


Functions
---------
.. currentmodule:: parsimony.configuration
.. autofunction:: callable_wrapper
.. autofunction:: obfuscator
.. autofunction:: store



:mod:`parsimony.generators`: Definition of generator functionality and some basic generators.
=============================================================================================
.. automodule:: parsimony.generators

Classes
-------
.. currentmodule:: parsimony.generators
.. autoclass:: Generator
   :no-inherited-members:

.. autoclass:: PickledCallableWrapper
   :no-inherited-members:

.. autoclass:: TextFile
   :no-inherited-members:


:mod:`parsimony.persistence`: Storage and retrieval mechanisms
==============================================================
.. automodule:: parsimony.persistence

Classes
-------
.. currentmodule:: parsimony.persistence
.. autoclass:: DataObfuscator
   :no-inherited-members:

.. autoclass:: SHA512Obfuscator
   :no-inherited-members:

.. autoclass:: ParameterStore
   :no-inherited-members:

.. autoclass:: ObfuscatedParameterStore
   :no-inherited-members:

.. autoclass:: PickledParameterStore
   :no-inherited-members:


