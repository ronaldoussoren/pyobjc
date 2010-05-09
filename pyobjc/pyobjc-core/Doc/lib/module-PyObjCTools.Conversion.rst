=========================================================
:mod:`PyObjCTools.Conversion` -- Convert data structures
=========================================================

.. module:: PyObjCTools.Conversion
   :synopsis: Convert data structures
   
Functions for converting between Cocoa and pure Python data structures.

.. function:: propertyListFromPythonCollection(pyCol, conversionHelper=None)

    Convert a Python collection (dictionary, array, tuple, string) into an 
    Objective-C collection.
    
    If conversionHelper is defined, it must be a callable.  It will be called 
    for any object encountered for which ``propertyListFromPythonCollection()``
    cannot automatically convert the object.   The supplied helper function 
    should convert the object and return the converted form.  If the conversion 
    helper cannot convert the type, it should raise an exception or return None.

.. function:: pythonCollectionFromPropertyList(ocCol, conversionHelper=None)

    Converts a Foundation based collection-- a property list-- into a Python 
    collection.  Like ``propertyListFromPythonCollection()``, ``conversionHelper``
    is an optional callable that will be invoked any time an encountered object 
    cannot be converted.
