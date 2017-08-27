Key-Value Observing and Python
==============================

Key-Value Coding and Key-Value Observing are supported by PyObjC. Key-Value
Observing is only supported for Cocoa objects though, because it is technically 
impossible to generate the right events for pure python objects (such as 
``dict`` or ``list`` instances)[1].

* _[1]: at least not without patching the Python interpreter itself.

PyObjC will automaticly call ``willChangeValueForKey:`` and 
``didChangeValueForKey:`` when changing the attribute of an object that is
a subclass of ``NSObject``. It is therefore not necessary to call those 
methods in most use-cases for Key-Value Observing.

.. warning::

   The 'change' dictionary for ``observeValueForKeyPath:ofObject:change:context:``
   can be changed after the method call, don't store a reference to this dictionary
   but make a copy when you want to use its contents later on.
