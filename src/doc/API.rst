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
.. autofunction:: mark_dirty
.. autofunction:: set_defaults


:mod:`parsimony.configuration`: Sets the implementations used by parsimony.
===========================================================================
.. automodule:: parsimony.configuration


Functions
---------
.. currentmodule:: parsimony.configuration
.. autofunction:: callable_wrapper
.. autofunction:: obfuscator
.. autofunction:: store
.. autofunction:: cache
.. autofunction:: parsimony_directory
.. autofunction:: context_name
.. autofunction:: set_context
.. autofunction:: set_configuration_file
.. autofunction:: update_configuration


:mod:`parsimony.generators`: Definition of generator functionality and some basic generators.
=============================================================================================
.. automodule:: parsimony.generators

Classes
-------
.. currentmodule:: parsimony.generators
.. autoclass:: Generator
   :no-inherited-members:

.. autoclass:: StoredCallableWrapper
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

.. autoclass:: Store
   :no-inherited-members:

.. autoclass:: PickleStore
   :no-inherited-members:

.. autoclass:: Cache
   :no-inherited-members:

.. autoclass:: MemCache
   :no-inherited-members:
