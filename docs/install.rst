Installing PyObjC
=================

Preferred way to install PyObjC
-------------------------------

PyObjC is distributed as a collection of Python packages and can be installed
using `pip`_.  Manual installation is also supported, but is a lot more work and is
therefore more of a power-user feature.

Installing or upgrading PyObjC using `pip`_ is easy:

.. sourcecode:: console

   $ python3 -mpip install -U pyobjc

For most users this will install PyObjC using `wheel <https://pypi.org/project/wheel>`_ binary
archives, which means you don't have to have a compiler on your machine.

Some use cases require installation of all framework bindings, not just those that are
relevant for the current system. To do this use the *allbindings* extra:

.. sourcecode:: console

   $ python3 -mpip install -U 'pyobjc[allbindings]'

This requires using binary wheels, otherwise this can attempt to install bindings that
require a newer SDK than available on the current machine.

Source based installation through pip
-------------------------------------

The installation method in the previous section will use binary wheels for most
users. Some users prefer installing from source even when binary wheels are available.

.. sourcecode:: console

   $ python3 -mpip install -U --no-binary :all: pyobjc

This does require having a system compiler installed, either Xcode or
the Command Line Tools, for both with either the latest SDK for the current
version of macOS, or an SDK for a later version of macOS. Using an older
SDK can lead to build errors.

Building from source using a checkout
-------------------------------------

It is possible to install PyObjC from source using the GitHub repository,
but that is more involved than pointing pip at the repository.  This does require
having a system compiler installed, either Xcode or the Command Line Tools, for
both with either the latest SDK for the current version of macOS, or an SDK
for a later version of macOS. Using an older SDK can lead to build errors.

.. sourcecode:: console

   $ git clone https://github.com/ronaldoussoren/pyobjc
   $ cd pyobjc
   $ python3 install.py

Use ``develop.py`` instead of ``install.py`` to end up with an editable installation.

Distributing to older versions of macOS
---------------------------------------

PyObjC's code is written in such a way that binaries created on later versions
of macOS can be distributed as far back as macOS 10.9, assuming the Python interpreter
used was build with a suitable deployment target (and CPU architecture).

The binary wheels for PyObjC combined with the
`Python installer on python.org <https://www.python.org/downloads/macos/>`_ can
be used to build application distributions that target any version of macOS between
10.9 and the current release of macOS.

Note that other extension modules, both on PyPI and those for your own code might
cause problems when running on older versions of macOS due to hard linking to
symbols that aren't available on those versions of macOS.

.. _pip: https://pypi.org/project/pip/
