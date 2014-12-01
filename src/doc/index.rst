.. Parsimony documentation master file, created by
   sphinx-quickstart on Wed Nov 26 17:18:05 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Parsimony Documentation
=====================================
Parsimony is a simple and efficient way to perform persistent caching of Python function results.

Many basic applications can get by with a combination of the default generator and file monitors.

Example
-------
As a toy example, let's do some task that takes a few seconds twice in one session.

::

   import pandas as pd
   import time
   import parsimony

   summer  = lambda dframe: dframe['SalePrice'].sum() #helper function

   path = parsimony.generators.PathMonitor('myfile','Train.csv')#>100MB

   #nothing cached
   t0 = time.time()
   x = parsimony.generators.StoredCallableWrapper('x',pd.read_csv,filepath_or_buffer=path
   t1 = time.time()
   print('Time taken {0:1.5f}s'.format(t1-t0))#nothing happened, default lazy init

   t0 = time.time()
   y = parsimony.generate('y',summer,dframe=x) #everything happens
   t1 = time.time()
   print('Time taken {0:1.5f}s'.format(t1-t0))
   print("y={0:}".format(y))

   t0 = time.time()
   x = parsimony.generators.StoredCallableWrapper('x',pd.read_csv,filepath_or_buffer=path)
   t1 = time.time()
   print('Time taken {0:1.5f}s'.format(t1-t0))#nothing happened, default lazy init
   t0 = time.time()
   y = parsimony.generate('y',summer,dframe=x) #retrieve from memory cache
   t1 = time.time()
   print('Time taken {0:1.5f}s'.format(t1-t0))#nothing happened, cached
   print("y={0:}".format(y))

Prints
::

   Time taken 0.00023s
   Time taken 8.76389s
   y=12474872316
   Time taken 0.05012s
   Time taken 0.02810s
   y=12474872316



However, this is not that useful of an example.  Let's run this script again immediately.
::

   Time taken 0.00011s
   Time taken 0.00061s
   y=12474872316
   Time taken 0.00016s
   Time taken 0.00060s
   y=12474872316

Because intermediate results were cached, the large CSV file does not need to be read. In fact, the only computation to
get y is a check that parameters are up to date. The parameter store is read and the value of y is retrieved directly.

API
===

.. toctree::
   :titlesonly:

   API Docs <API>

Get Parsimony
=============

.. toctree::
   :titlesonly:

   Installation <install>