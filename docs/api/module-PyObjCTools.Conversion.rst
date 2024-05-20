=========================================================
:mod:`PyObjCTools.Conversion` -- Convert data structures
=========================================================

.. module:: PyObjCTools.Conversion
   :synopsis: Convert data structures

Functions for converting between Cocoa and pure Python data structures. These
functions are only needed when a use case requires instances of "native" classes,
in most use cases instances of "foreign" classes can be used without problems.

.. function:: propertyListFromPythonCollection(pyCol, conversionHelper=None)

    Convert a Python collection (dictionary, array, tuple, string) into an
    Objective-C collection.

    :param pyCol: The python value to convert
    :param conversionHelper: Callable with a single argument that accepts a value
                             and returns the Cocoa equivalent. This function is
                             called for values which *propertyListFromPythonCollection*
                             cannot convert automatically.
    :returns: The Cocoa representation of *pyCol*

.. function:: pythonCollectionFromPropertyList(ocCol, conversionHelper=None)

    Converts a Foundation based collection-- a property list-- into a Python
    collection.

    :param ocCol: The Cocoa value to convert
    :param conversionHelper: Callable with a single argument that accepts a value
                             and returns the Python equivalent. This function is
                             called for values which *pythonCollectionFromPropertyList*
                             cannot convert automatically.
    :returns: The Python representation of *ocCol*

.. function:: serializePropertyList(aPropertyList, format="xml") -> bytes

   Serialize a property list into a byte string.

   .. note:: For cross platform code the standard library module :mod:`plistlib` should be used.

   :param aPropertyList: A property list value (list, dict, ...)
   :param format: The format to use, ``"xml"`` for an XML property list, or
                  ``"binary"`` for a binary property list.
   :returns: A serialized property list with the contents of *aPropertyList*

.. function:: deserializePropertyList(propertyListData)

   Deserialize a property list from a byte string.

   .. note:: For cross platform code the standard library module :mod:`plistlib` should be used.

   :param propertyListData: A byte string with the serialized property list
   :returns: The deserialized value (dict, tuple, ...)

.. function:: toPythonDecimal(aNSDecimalNumber) -> decimal.Decimal

   Convert an instance of ``NSDecimalNumber`` to ``decimal.Decimal``

   :param aNSDecimalNumber: The value to convert
   :returns: *aNSDecimalNumber* converted to :class:`decimal.Decimal`


.. function:: fromPythonDecimal(aPythonDecimal) -> NSDecimalNumber

   Convert an instance of ``decimal.Decimal`` to ``NSDecimalNumber``

   :param aPythonDecimal: The value to convert
   :returns: *aPythonDecimal* converted to :class:`NSDecimalNumber`.
