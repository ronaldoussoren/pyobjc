Support for ``FSRef`` and ``FSSpec``
====================================

PyObjC has its own wrappers for the types ``FSRef`` and ``FSSpec``, and also
supports the wrappers for these types in ``Carbon.File``.

.. class:: objc.FSRef

    This type represents an opaque ``FSRef`` structure.

    New instances are created using the ``from_pathname`` method:
    .. sourcecode:: pycon
    
        >>> ref = objc.FSRef.from_pathname("/Libray")
        >>> isinstance(ref, objc.FSRef)
        True
    
    Instances of ``objc.FSRef`` are opaque and don't provide access to 
    specific fields in the structure. The following methods and properties
    are available to access an instance:

    .. attribute:: data

        A bytestring containing the value of the ``FSRef`` object.

    .. method:: as_pathname

        Returns the POSIX path for the ``FSRef`` object.

    .. method:: as_carbon

        Returns a ``Carbon.File.FSRef`` instance for the ``FSRef`` object.

        NOTE: This method is only available when ``Carbon`` support is
        enabled in the Python build.

    NOTE: ``Carbon.File.FSRef`` instances can be used as the argument
    of functions that have an ``FSRef`` structure as one of their
    arguments.

.. class:: objc.FSSpec

    This type represents an opaque ``FSSpec`` structure. It is not possible
    to create ``FSSpec`` instances in Python code.

    Instances of ``objc.FSSpec`` are opaque and don't provide access to 
    specific fields in the structure. The following methods and properties
    are available to access an instance:

    .. attribute:: aref.data

        A bytestring containing the value of the ``FSRef`` object.

    .. method:: aref.as_carbon

        Returns a ``Carbon.File.FSRef`` instance for the ``FSRef`` object.

        NOTE: This method is only available when ``Carbon`` support is
        enabled in the Python build.
    
    NOTE: ``Carbon.File.FSSpec`` instances can be used as the argument
    of functions that have an ``FSSpec`` structure as one of their
    arguments.
