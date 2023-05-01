Installing PyObjC
=================

Supported versions
------------------

PyObjC supports Python 3.6 or later and does not support Python 2.

PyObjC does not support other python implementation such as PyPy and Jython.

PyObjC is regularly tested on macOS 10.14 and should work on macOS
10.9 or later for the i386 and x86_64 architectures.

PyObjC only supports macOS and does not support other platform (iOS, Linux, ...)

Installation
------------

PyObjC is distributed as a collection of Python packages and can be installed
using `pip`_.  Manual installation is also supported, but is a lot more work and is
therefore more of a power-user feature.

Installation using pip
.......................

Installing or upgrading PyObjC using `pip`_ is easy:

.. sourcecode:: sh

   $ pip3 install -U pyobjc

For most users this will install PyObjC using `wheel <https://pypi.org/project/wheel>`_ binary
archives, which means you don't have to have a compiler on your machine.

Some use cases require installation of all framework bindings, not just those that are
relevant for the current system. In PyObjC 8 or later you can install framework bindings
using the *allbindings** extra:

.. sourcecode:: sh

   $ pip3 install -U 'pyobjc[allbindings]'

This requires using binary wheels, otherwise this can attempt to install bindings that
require a newer SDK than available on the current machine.

.. note::

   Pip will install PyObjC 5 for users of Python 2.7, but only when using
   pip 9 or later.


Manual installation
...................

Manual installation is slightly involved, but still pretty easy.

* First download the source code packages from the cheeseshop, you
  need at least `pyobjc-core <https://pypi.org/project/pyobjc-core>`_ and
  `pyobjc-framework-Cocoa <https://pypi.org/project/pyobjc-framework-Cocoa>`_.
  You do not need `pyobjc <https://pypi.org/project/pyobjc>`_, that's a helper package that is only
  used to pull in the other packages when installing using `pip`_.

* Extract the archives

* Install every packages using the standard recipe for Python package
  installation:

  .. sourcecode:: sh

     $ python setup.py install

  Due to package dependencies you need to install the packages in a
  particular order:

  - `pyobjc-core <https://pypi.org/project/pyobjc-core>`_

  - `pyobjc-framework-Cocoa <https://pypi.org/project/pyobjc-framework-Cocoa>`_

  - `pyobjc-framework-Quartz <https://pypi.org/project/pyobjc-framework-Quartz>`_

  - all other packages (in arbitrary order)


Requirements for building from source
-------------------------------------

PyObjC contains extensions and is distributed as source code. You therefore
need a compiler to install PyObjC. The easiest way to get a compiler is do
download `Xcode from the Mac App Store <https://apps.apple.com/us/app/xcode/id497799835?mt=12>`_.

Depending on the Python release you may need to install the Command Line
Tools for Xcode. To install the Command Line Tools first install Xcode from
the Mac App Store. The next action depends on the OSX release you are using.

If you use OSX 10.8 or earlier, open Xcode and then open
the Xcode preferences.  The downloads tab contains an option "components" and
that list contains an option to install the "Command Line Tools".

If you use OSX 10.9 or later, open a Terminal window and run ``xcode-select --install``.


Advanced installation options
-----------------------------

Distributing binaries to other macOS releases
.............................................

It is possible to create self-contained application bundles for PyObjC based
application using `py2app <https://pypi.org/project/py2app>`_. You do need to take some care when
you want to ship these applications to machines running a different
version of macOS than the one you used for the build

* Later versions of macOS should work fine

* Earlier version of macOS work fine, but you do need to ensure that
  Python itself is build with ``MACOSX_DEPLOYMENT_TARGET`` set to the earliest
  version of macOS you want to support. PyObC, and other extension packages,
  should automatically pick up the deployment target from the Python build.

* Using the latest version of macOS to build binaries gives the most featureful
  binaries, building on older macOS versions can drop specific support for
  some newer APIs.

  .. note::

     PyObjC contains code that explicitly weak-links to a number of APIs that
     are not available on all macOS releases.

     You might still end up with an application that won't run on earlier
     releases when you use another extension module that (accidentally) hard links
     to an API that is not available in the earlier release.

.. _pip: https://pypi.org/project/pip/
