Supported platforms
===================

PyObjC is a project that targets macOS and does not work on other platforms,
such as iOS, Linux or Windows. The project targets macOS 10.9 or later, and
is tested regularly on the current release of macOS using the Python installers
on `www.python.org <https://www.python.org/downloads/macos/>`_.

PyObjC supports the Python versions that are supported by the CPython core
developers when the major release of PyObjC was released (generally in October),
and will add new versions of Python when they come available.

Currently PyObjC supports Python 3.7 upto and including 3.13.

.. note::

   PyObjC does at this time *not* support free-threading
   (as introduced in Python 3.13) and subinterpreters.

.. warning::

   PyObjC 11 will drop support for Python 3.7, which goes out of support later
   this year.


.. admonition:: Old Python versions

   The list belows shows which versions of PyObjC are the latest that can be used with old
   (and no longer supported) Python versions. None of these PyObjC versions are supported.

   ====== ======
   Python PyObjC
   ====== ======
   3.7    9.2
   3.6    8.5
   2.7    5.3
   ====== ======
