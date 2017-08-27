Installing PyObjC
=================

Supported versions
------------------

PyObjC is regularly tested with Python 2.7, 3.4, 3.5 and 3.6.
PyObjC does not support other python implementation such as PyPy and Jython.

PyObjC is regularly tested on Mac OS X 10.12 and should work on Mac OS X
10.5 or later for the i386, x86_64 and ppc architectures. PPC64 (64-bit
on PowerMac G5 or iMac G5 systems) is not supported.


Installation
------------

PyObjC is distributed as a collection of Python packages and can be installed
using `pip`_.  Manual installation is also supported, but is a lot more work and is
therefore more of a power-user feature.

Installation using pip
.......................

Installing or upgrading PyObjC using `pip`_ is easy:

.. sourcecode:: sh

   $ pip install -U pyobjc

For most users this will install PyObjC using `wheel <https://pypi.python.org/pypi/wheel>`_ binary
archives, which means you don't have to have a compiler on your machine.

Manual installation
...................

Manual installation is slightly involved, but still pretty easy.

* First download the source code packages from the cheeseshop, you
  need at least :pypi:`pyobjc-core` and :pypi:`pyobjc-framework-Cocoa`.
  You do not need :pypi:`pyobjc`, that's a helper package that is only
  used to pull in the other packages when installing using `easy_install`_
  or `pip`_.

* Extract the archives

* Install every packages using the standard recipe for Python package
  installation:

  .. sourcecode:: sh

     $ python setup.py install

  Due to package dependencies you need to install the packages in a
  particular order:

  - :pypi:`pyobjc-core`

  - :pypi:`pyobjc-framework-Cocoa`

  - :pypi:`pyobjc-framework-Quartz`

  - all other packages (in arbitrary order)


Requirements for building from source
-------------------------------------

PyObjC contains extensions and is distributed as source code. You therefore
need a compiler to install PyObjC. The easiest way to get a compiler is do
download `Xcode from the Mac App Store <https://itunes.apple.com/us/app/xcode/id497799835?mt=12>`_.

Depending on the Python release you may need to install the Command Line
Tools for Xcode. To install the Command Line Tools first install Xcode from
the Mac App Store. The next action depends on the OSX release you are using.

If you use OSX 10.8 or earlier, open Xcode and then open
the Xcode preferences.  The downloads tab contains an option "components" and
that list contains an option to install the "Command Line Tools".

If you use OSX 10.9 or later, open a Terminal window and run ``xcode-select --install``.

.. note::

   The Command Line Tools package may not be automaticly updated when you install
   a new version of Xcode. Every time Xcode is updated through the Mac App Store
   you need to start Xcode to check if there is a new version of the Command Line Tools.


Advanced installation options
-----------------------------

PyObjC for PowerPC systems
..........................

To build a version of PyObjC that runs on PowerPC systems you need a system
running Mac OS X 10.6 (or earlier) running Xcode 3. The version of Xcode that
is available in the Mac App Store can not create PowerPC binaries.


Distributing binaries to other Mac OS X releases
.................................................

It is possible to create self-contained application bundles for PyObjC based
application using :pypi:`py2app`. You do need to take some care when
you want to ship these applications to machines running a different
version of Mac OS X than the one you used for the build

* Later versions of Mac OS X should work fine

* Earlier version of Mac OS X work fine, but you do need to ensure that
  Python itself is build with ``MACOSX_DEPLOYMENT_TARGET`` set to the earliest
  version of Mac OS X you want to support. PyObC, and other extension packages,
  should automaticly pick up the deployment target from the Python build.

  .. note::

     PyObjC contains code that explictly weak-links to a number of APIs that
     are not available on all Mac OS X releases.

     You might still end up with an application that won't run on earlier
     releases when you use another extension module that (accidently) hard links
     to an API that is not available in the earlier release.

.. _pip: https://pypi.python.org/pypi/pip/
