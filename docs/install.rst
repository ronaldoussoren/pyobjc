Installing PyObjC
=================

Supported versions
------------------

PyObjC is regularly tested with Python 2.7, 3.4, 3.5 and the CPython trunk.
PyObjC does not support other python implementation such as PyPy and Jython.

PyObjC is regularly tested on Mac OS X 10.11 and should work on Mac OS X
10.5 or later for the i386, x86_64 and ppc architectures. PPC64 (64-bit
on PowerMac G5 or iMac G5 systems) is not supported.

Requirements
------------

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

.. todo::

   describe which python versions need the command-line tools, and why
   you should or shouldn't install them.


Installation
------------

PyObjC is distributed as a collection of Python packages that use distribute
and can be installed using both `pip`_ and `easy_install`_. Manual installation
is also supported, but is a lot more work and is therefore more of a power-user
feature.

Installation using pip
.......................

Installing or upgrading PyObjC using `pip`_ is easy:

.. sourcecode:: sh

   $ pip install -U pyobjc

For most users this will install PyObjC using `wheel <https://pypi.python.org/pypi/wheel>`_ binary
archives, which means you don't have to have a compiler on your machine.

Installation using easy_install
...............................

Installing or upgrading PyObjC using `easy_install`_ is easy:

.. sourcecode:: sh

   $ easy_install -U pyobjc


.. note::

   With PyObjC 3.1 or earlier installing PyObjC takes quite some
   time due to :issue:`21`. To avoid this problem install ``pyobjc-core``
   before install the rest of PyObjC:

   .. sourcecode:: sh

      $ easy_install -U pyobjc-core
      $ easy_install -U pyobjc


.. warning::

   Building on OSX 10.7 or 10.8 might give a compiler error when using
   Xcode 4 and a binary installer for Python. When installing fails because
   a compiler named 'gcc-4.2' cannot find the header 'stdarg.h' you have
   to install using a slightly different procedure::

     $ env CC=clang easy_install -U pyobjc-core
     $ env CC=clang easy_install -U pyobjc


Upgrades with pip or easy_install
.................................

Running ``easy_install -U`` or ``pip install -U`` to update an existing installation
of PyObjC can fail with an error message about conflicting versions. This is due
to :issue:`21` and is not something that can easily be fixed in PyObjC itself.

The easiest workaround is to first update "pyobjc-core" and only then perform the
full update.



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

.. _easy_install: https://setuptools.readthedocs.io/en/latest/easy_install.html

.. _pip: https://pypi.python.org/pypi/pip/
