Manual metadata loading
=======================

.. py:currentmodule:: objc

Introduction
------------

When the other two metadata systems aren't suitable it
is also possible to load metadata through code. The other
two systems use the functionality described in this section
to actually load the metadata.

.. seealso::

   :doc:`bridgesupport`
     Loading metadata from XML files

   :doc:`compiled`
     Loading metadata using compiled files


API description
---------------

For now see :doc:`the main API description <lib/module-objc` for the
functions that are used to load metadata.

The contains of the metadata dictionary argument for 
:func:`registerMetaDataForSelector` is not documented at the moment.


Deprecated APIs
---------------

.. function:: setSignatureForSelector(class_name, selector, signature)

   .. deprecated:: 2.3

   Use the metadata system instead

   Register a replacement signature for a specific selector. This can
   be used to provide a more exact signature for a method.
