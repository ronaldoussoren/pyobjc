PyObjC metadata system
======================

The Objective-C runtime does not expose 
enough information to provide completely 
automatic bindings of all APIs.  Because of 
this PyObjC needs a way to load additional
information about APIs.

The additianal information is loaded through
a metadata system, the documents below describe
the methods by which the metadata can be loaded.
  
.. toctree::
   :maxdepth: 1

   bridgesupport
   compiled
   manual
