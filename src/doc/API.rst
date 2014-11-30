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

.. autoclass:: PathMonitor
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

.. autoclass:: PickledParameterStore
   :no-inherited-members:
