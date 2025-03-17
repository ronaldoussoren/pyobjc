Support for ``FSRef``
=====================

.. py:currentmodule:: objc

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

    .. method:: __fspath__

       Alias for :meth:`as_pathname`, which makes it possible
       to use :class:`FSRef` instances as arguments to APIs
       accepting an :class:`os.PathLike` object.


       .. versionadded: 11.1
