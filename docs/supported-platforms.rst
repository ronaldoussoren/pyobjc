Supported platforms
===================

PyObjC is a project that targets macOS and does not work on other platforms,
such as iOS, Linux or Windows. The project targets macOS 10.9 or later, and
is tested regularly on the current release of macOS using the Python installers
on `www.python.org <https://www.python.org/downloads/macos/>`_.

PyObjC supports the Python versions that will be supported by the CPython core
developers uhtil the next the major release of PyObjC will be released
(generally in October), and will add new versions of Python when they come available.

Currently PyObjC supports Python 3.10 upto and including 3.14. Python 3.15 (alpha)
is supported experimentally.

Free-threading as introduced in Python 3.13 is supported, see :doc:`notes/free-threading`
for more information.

.. admonition:: Old Python versions

   The list below shows which versions of PyObjC are the latest that can be used with old
   (and no longer supported) Python versions. None of these PyObjC versions are supported.

   ====== ======
   Python PyObjC
   ====== ======
   3.9    11.1
   3.8    10.3
   3.7    9.2
   3.6    8.5
   2.7    5.3
   ====== ======

MacOS platform support
----------------------

PyObjC currently supports macOS 10.9 or later for the x86_64 and arm64 (aka Apple Silicon)
CPU types when build from source.

The binary wheels on PyPI have the same macOS version support as the CPython installers. This
means that wheels for Python 3.10 and 3.11 support macOS 10.9, while wheels for newer Python
versions support macOS 10.13 (or later).

Binary wheels will include support for x86_64 as long as it is possible to do so using the
latest Apple SDK, or as long as I have access to hardware where I can test such support.  I've
not yet determined if there will be a separate set of x86_64 wheels
once Xcode drops support for building for x86_64.

Objective-C Garbage Collection
------------------------------

In macOS 10.5 up to 10.12 Objective-C optionally used  Garbage Collection (GC)
instead of retains counts for code that was explicitly compiled to support
(or require) garbage collection. PyObjC does not support this feature.

Note that this is different from Automatic Reference Counts (ARC), which is supported
by PyObjC although PyObjC itself must be compiled with this feature disabled.
