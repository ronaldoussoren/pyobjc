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
module, it does not implement the ideas described on the `NewPackageManager`__
page on the `MacPython wiki`_.

Features w.r.t. the official Package Manager:

- You can have a list of favorite databases

- The scroll-list doesn't scroll back automatically ;-)

Building
--------

This version requires the latest version of PyObjC (1.1b1) and Mac OS X 10.3.
Please let me know if it also works on OSX 10.2.

Run ``python setup.py py2app`` to create the application.

TODO
----

- Auto-update the status, this mostly works at the moment.
- Testing!
- Implement help menu
- A --semi-standalone version cannot detect if the system contains PyObjC,
  should run detection code in a seperate process. 

In the further future the pimp should be replaced by something better, see
the `MacPython wiki`_ for more information.

.. _`MacPython wiki`: http://pythonmac.org/wiki
