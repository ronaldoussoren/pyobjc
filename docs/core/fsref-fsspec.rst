Support for ``FSRef`` and ``FSSpec``
====================================

.. py:currentmodule:: objc

PyObjC has its own wrappers for the types ``FSRef`` and ``FSSpec``, and also
supports the wrappers for these types in ``Carbon.File``. The wrappers in

.. note::

   The wrappers for these types in ``Carbon.File`` should not be used,
   that module is not available in Python 3 and has been unmaintained
   in Python 2.x with the introduction of macOS.

   The types in this document are fully supported, and will be supported
   as long as macOS supports these types.

.. class:: FSRef

    This type represents an opaque ``FSRef`` structure.

    .. note::

       All API's using the FSRef type are deprecated by Apple as of macOS 10.8,
       for most of those APIs there are alternate APIs that use URL objects
       (:c:type:`NSURL` or :c:type:`CFURL`).

    New instances are created using the ``from_pathname`` method:

    .. sourcecode:: python

        >>> ref = objc.FSRef.from_pathname("/Library")
        >>> isinstance(ref, objc.FSRef)
        True

    Instances of ``objc.FSRef`` are opaque and don't provide access to
    specific fields in the structure. The following methods and properties
    are available to access an instance:

    .. attribute:: data

        A bytestring containing the value of the ``FSRef`` object.

    .. method:: as_pathname

        Returns the POSIX path for the ``FSRef`` object.


.. class:: FSSpec

    This type represents an opaque ``FSSpec`` structure. It is not possible
    to create ``FSSpec`` instances in Python code.

    .. note::

       "FSSpec" is a deprecated type in Apple's APIs. The type is not
       available for 64-bit code, and shouldn't be used for new development.

    Instances of ``objc.FSSpec`` are opaque and don't provide access to
    specific fields in the structure. The following methods and properties
    are available to access an instance:

    .. attribute:: aref.data

        A bytestring containing the value of the ``FSSpec`` object.
