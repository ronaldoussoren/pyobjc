=====================
Cocoa Package Manager
=====================

NOTE:

    The Package Manager infrastructure is currently unmaintained.  This
    example is not intended for actual use, but remains to show how such an
    application could be built.

This application is a Cocoa version of the Package Manager application that
is included with MacPython.

This is a first version of the application, using an unmodified ``pimp`` 
module, it does not implement the ideas described on the NewPackageManager
page on the `MacPython wiki`_.

Features w.r.t. the official Package Manager:

- You can have a list of favorite databases

- The scroll-list doesn't scroll back automatically ;-)

Building
--------

Run ``python setup.py py2app`` to create the application.

.. _`MacPython wiki`: http://pythonmac.org/wiki
