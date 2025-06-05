Supported platforms
===================

PyObjC is a project that targets macOS and does not work on other platforms,
such as iOS, Linux or Windows. The project targets macOS 10.9 or later, and
is tested regularly on the current release of macOS using the Python installers
on `www.python.org <https://www.python.org/downloads/macos/>`_.

PyObjC supports the Python versions that are supported by the CPython core
developers when the major release of PyObjC was released (generally in October),
and will add new versions of Python when they come available.

Currently PyObjC supports Python 3.9 upto and including 3.13.

Free-threading as introduced in Python 3.13 is supported experimentally, mostly
because of limited testing. Free-threading support for PyObjC works better in
Python 3.14 due to some new CPython APIs that enable fixing a race condition.


.. admonition:: Old Python versions

   The list below shows which versions of PyObjC are the latest that can be used with old
   (and no longer supported) Python versions. None of these PyObjC versions are supported.

   ====== ======
   Python PyObjC
   ====== ======
   3.8    10.3
   3.7    9.2
   3.6    8.5
   2.7    5.3
   ====== ======

Objective-C Garbage Collection
------------------------------

In macOS 10.5 up to 10.12 Objective-C optional Garbage Collection (GC) instead of
retains counts for code that was explicitly compiled to support (or require) garbage
collection. PyObjC does not support this feature.

Note that this is different from Automatic Reference Counts (ARC), which is supported
by PyObjC although PyObjC itself must be compiled with this feature disabled.
