py2app - Create standalone Mac OS X applications with Python
````````````````````````````````````````````````````````````

.. contents::


Abstract
--------

py2app is a Python `setuptools`_ command which will allow you
to make standalone application bundles and plugins from Python
scripts. py2app is similar in purpose and design to `py2exe`_ for
Windows.

This documentation corresponds to version 0.3.5 of py2app.


Installation
------------

Uninstalling py2app 0.2.x (or earlier)
======================================

If you have a pre-setuptools version of py2app installed, you must first
remove it before installing (you may have to run the interpreter with sudo,
depending on how and where py2app was originally installed). There are
three paths that need to be removed: ``py2app`` and ``py2app.pth`` in your
site-packages folder, and the ``py2applet`` script which may be in
``/usr/local/bin/`` or otherwise in the bin directory belonging to the Python
framework that was installed.

Here is a Python script that should find these three paths and remove them
if they exist (you may have to use sudo)::

    #!/usr/bin/env python
    import os, shutil
    from distutils.sysconfig import *
    py2app = os.path.join(get_python_lib(), 'py2app')
    import shutil           
    if os.path.isdir(py2app): 
        print "Removing " + py2app
        shutil.rmtree(py2app)
        
    if os.path.exists(py2app + '.pth'):
        print "Removing " + py2app + '.pth'
        os.unlink(py2app + '.pth')
    
    for path in os.environ['PATH'].split(':'):
        script = os.path.join(path, 'py2applet')
        if os.path.exists(script):
            print "Removing " + script
            os.unlink(script)


Installing with easy_install
============================

To install py2app using `easy_install`_ you must make sure you have a recent
version of `setuptools`_ installed (as of this writing, 0.6b4 or later)::

    $ curl -O http://peak.telecommunity.com/dist/ez_setup.py
    $ sudo python ez_setup.py -U setuptools

To install or upgrade to the latest released version of py2app::

    $ sudo easy_install -U py2app


Installing from source
======================

To install py2app from source, simply use the normal procedure for
installing any Python package. Since py2app uses `setuptools`_,
all dependencies (including `setuptools`_ itself) will be automatically
acquired and installed for you as appropriate::

    $ python setup.py install

If you're using a svn checkout, it's recommended to use the `setuptools`_
`develop command`_, which will simply activate py2app directly from your
source directory. This way you can do a ``svn up`` or make changes to the
source code without re-installing every time::

    $ python setup.py develop


Upgrade Notes
-------------

The ``setup.py`` template has changed slightly in py2app 0.3 in order
to accommodate the enhancements brought on by `setuptools`_. Old ``setup.py``
scripts look like this::

    from distutils.core import setup
    import py2app

    setup(
        app=["myscript.py"],
    )

New py2app scripts should look like this::

    from setuptools import setup
    setup(
        app=["myscript.py"],
	setup_requires=["py2app"],
    )


Tutorial
--------

Converting your scripts to Mac OS X applications is easy with py2app.

Create a setup.py file
======================

The first step is to create a ``setup.py`` file for your script. ``setup.py``
is the "project file" that tells `setuptools`_ everything it needs to know
to build your application. We'll use the `py2applet`_ script to do that::

    $ py2applet --make-setup MyApplication.py
    Wrote setup.py

If your application has an icon (in ``.icns`` format) or data files that it
requires, you should also specify them as arguments to `py2applet`_.


Clean up your build directories
===============================

Before starting development or switching development modes it's usually
a good idea to ensure that your ``build`` and ``dist`` directories are
cleaned out::

    $ rm -rf build dist


Development with alias mode
===========================

Alias mode (the ``-A`` or ``--alias`` option) instructs py2app to build
an application bundle that uses your source and data files in-place. It
does not create standalone applications, and the applications built in
alias mode are not portable to other machines. This mode is similar to the
`setuptools`_ ``develop`` command, or `Xcode`_'s zero-link feature.

To build the application in alias mode, execute ``setup.py`` with the
``py2app`` command and specify the ``-A`` option (or ``--alias``)::

    $ python setup.py py2app -A

After this, py2app will spit out a bunch of messages to your terminal
and you'll end up with new ``build`` and ``dist`` folders. The ``build``
folder contains build sludge that you'll never need to touch,
and the ``dist`` folder contains your application bundle.
The application bundle will be named after your script; if your script was
named ``MyApplication.py``, then your application bundle will be named
``MyApplication.app``. Note that Finder displays application bundles without
the ``.app`` extension.

You only need to run this command again when you add data files or change
options. Changes to your source code won't require rebuilding!


Running your application
========================

During development, it's often useful to have your application
attached to the Terminal. This allows you to better debug it, e.g. by
inserting ``import pdb; pdb.set_trace()`` into your code to inspect it
interactively at runtime.

To run your application directly from the Terminal::

    $ ./dist/MyApplication.app/Contents/MacOS/MyApplication

To start your application normally with LaunchServices, you can use the
``open`` tool::

    $ open -a dist/MyApplication.app

If you want to specify "open document" events, to simulate dropping files on
your application, just specify them as additional arguments to ``open``.

You may of course also double-click your application from Finder.

When run normally, your application's stdout and stderr output will go to the
Console logs. To see them, open the Console application::

    $ open -a Console


Building for deployment
=======================

After you've got your application working smoothly in alias mode, it's time
to start building a redistributable version. Since we're switching from
alias mode to normal mode, you should remove your ``build`` and ``dist``
folders as above.

Building a redistributable application consists of simply running the
``py2app`` command::

    $ python setup.py py2app

This will assemble your application as ``dist/MyApplication.app``. Since
this application is self-contained, you will have to run the ``py2app``
command again any time you change any source code, data files, options, etc.

The easiest way to wrap your application up for distribution at this point
is simply to right-click the application from Finder and choose
"Create Archive".


Online Resources
----------------

There are several online resources to help you get along with py2app.

Mailing list:
    http://www.python.org/community/sigs/current/pythonmac-sig/

Trac (issue tracker/wiki/source browser):
    http://trac.pythonmac.org/py2app/

Subversion Trunk (latest sources):
    http://svn.pythonmac.org/py2app/py2app/trunk/

CheeseShop Entry:
    http://cheeseshop.python.org/pypi/py2app/

If you're looking for help, pay special attention to the ``examples``
folder in the source, which demonstrates many common use cases.


Tweaking your Info.plist
------------------------

It's often useful to make some tweaks to your Info.plist file to change how
your application behaves and interacts with Mac OS X. The most complete
reference for the keys available to you is in Apple's
`Runtime Configuration Guidelines`_.


Commonly customized keys
========================

Here are some commonly customized property list keys relevant to py2app
applications:

``CFBundleDocumentTypes``:
    An array of dictionaries describing document types supported by the bundle.
    Use this to associate your application with opening or editing document
    types, and/or to assign icons to document types.

``CFBundleGetInfoString``:
    The text shown by Finder's Get Info panel.

``CFBundleIdentifier``:
    The identifier string for your application (in reverse-domain syntax),
    e.g. ``"org.pythonmac.py2app"``.

``CFBundleURLTypes``:
    An array of dictionaries describing URL schemes supported by the bundle.

``LSBackgroundOnly``:
    If ``True``, the bundle will be a faceless background application. 

``LSUIElement``:
    If ``True``, the bundle will be an agent application. It will not appear
    in the Dock or Force Quit window, but still can come to the foreground
    and present a UI.

``NSServices``:
    An array of dictionaries specifying the services provided by the
    application.


Specifying customizations
=========================

There are three ways to specify ``Info.plist`` customizations to py2app.

You can specify an Info.plist XML file on the command-line with the
``--plist`` option, or as a string in your ``setup.py``::

    setup(
        app=['MyApplication.py'],
	options=dict(py2app=dict(
	    plist='Info.plist',
	)),
    )

You may also specify the plist as a Python dict in the ``setup.py``::

    setup(
        app=['MyApplication.py'],
	options=dict(py2app=dict(
	    plist=dict(
	        LSPrefersPPC=True,
	    ),
	)),
    )

Or you may use a hybrid approach using the standard library plistlib module::

    from plistlib import Plist
    plist = Plist.fromFile('Info.plist')
    plist.update(dict(
        LSPrefersPPC=True,
    ))
    setup(
        app=['MyApplication.py'],
	options=dict(py2app=dict(
	    plist=plist,
	)),
    )


Universal Binaries
==================

py2app is currently fully compatible with Universal Binaries, however
it does not try and detect which architectures your application will
correctly run on.

If you are building your application with a version of Python that is not
universal, or have extensions that are not universal, then you must set
the ``LSPrefersPPC`` Info.plist key to ``True``. This will force the
application to run translated with Rosetta by default. This is necessary
because the py2app bootstrap application is universal, so Finder
will try and launch natively by default.

Alternatively, the ``--prefer-ppc`` option can be used as a shortcut to
ensure that this Info.plist key is set.


Example setup.py templates
--------------------------

Basic
=====

The simplest possible ``setup.py`` script to build a py2app application
looks like the following::

    """
    py2app build script for MyApplication

    Usage:
        python setup.py py2app
    """
    from setuptools import setup
    setup(
        app=["MyApplication.py"],
	setup_requires=["py2app"],
    )

The `py2applet`_ script can create ``setup.py`` files of this variety
for you automatically::

    $ py2applet --make-setup MyApplication.py


Self-bootstrapping
==================

For ease of distribution, you may wish to have your ``setup.py`` script
automatically ensure that `setuptools`_ is installed. This requires having a
copy of ``ez_setup`` in your project, which can be obtained from here::

    http://peak.telecommunity.com/dist/ez_setup.py

Or it may be referenced from `svn:externals`_ as such::

    ez_setup svn://svn.eby-sarna.com/svnroot/ez_setup

If choosing the `svn:externals`_ approach you should consider that your
project's source code will depend on a third party, which has reliability
and security implications. Also note that the ``ez_setup`` external uses
the ``svn://`` protocol (TCP port 3690) rather than ``http://`` so it is
somewhat less likely to work behind some firewalls or proxies.

Once this is done, you simply add the two line ``ez_setup`` preamble to the
very beginning of your ``setup.py``::

    """
    py2app build script for MyApplication.

    Will automatically ensure that all build prerequisites are available
    via ez_setup.

    Usage:
        python setup.py py2app
    """
    import ez_setup
    ez_setup.use_setuptools()

    from setuptools import setup
    setup(
        app=["MyApplication.py"],
	setup_requires=["py2app"],
    )


Cross-platform
==============

Cross-platform applications can share a ``setup.py`` script for both
`py2exe`_ and py2app. Here is an example `Self-bootstrapping`_
``setup.py`` that will build an application on Windows or Mac OS X::

    """
    py2app/py2exe build script for MyApplication.

    Will automatically ensure that all build prerequisites are available
    via ez_setup

    Usage (Mac OS X):
        python setup.py py2app

    Usage (Windows):
        python setup.py py2exe
    """
    import ez_setup
    ez_setup.use_setuptools()

    import sys
    from setuptools import setup
    
    mainscript = 'MyApplication.py'

    if sys.platform == 'darwin':
        extra_options = dict(
	    setup_requires=['py2app'],
	    app=[mainscript],
	    # Cross-platform applications generally expect sys.argv to
	    # be used for opening files.
	    options=dict(py2app=dict(argv_emulation=True)),
	)
    elif sys.platform == 'win32':
        extra_options = dict(
	    setup_requires=['py2exe'],
	    app=[mainscript],
	)
   else:
        extra_options = dict(
	    # Normally unix-like platforms will use "setup.py install"
	    # and install the main script as such
	    scripts=[mainscript],
	)

   setup(
       name="MyApplication",
       **extra_options
   )


py2app Options
--------------

Options can be specified to py2app to influence the build procedure in three
different ways:

At the command line::

    $ python setup.py py2app --argv-emulation

In your ``setup.py``::

    setup(
        app=['MyApplication.py'],
        options=dict(py2app=dict(
            argv_emulation=1,
        )),
    )

In a ``setup.cfg`` file::

   [py2app]
   argv-emulation=1

Note that when translating command-line options for use in ``setup.py``, you
must replace hyphens (``-``) with underscores (``_``). ``setup.cfg`` files
may use either hyphens or underscores, but command-line options must always
use the hyphens.


Option Reference
================

To enumerate the options that py2app supports, use the following command::

    $ python setup.py py2app --help

Options for 'py2app' command::

  --optimize (-O)         optimization level: -O1 for "python -O", -O2 for
                          "python -OO", and -O0 to disable [default: -O0]
  --includes (-i)         comma-separated list of modules to include
  --packages (-p)         comma-separated list of packages to include
  --iconfile              Icon file to use
  --excludes (-e)         comma-separated list of modules to exclude
  --dylib-excludes (-E)   comma-separated list of frameworks or dylibs to
                          exclude
  --datamodels            xcdatamodels to be compiled and copied into
                          Resources
  --resources (-r)        comma-separated list of additional data files and
                          folders to include (not for code!)
  --frameworks (-f)       comma-separated list of additional frameworks and
                          dylibs to include
  --plist (-P)            Info.plist template file, dict, or plistlib.Plist
  --extension             Bundle extension [default:.app for app, .plugin for
                          plugin]
  --graph (-g)            output module dependency graph
  --xref (-x)             output module cross-reference as html
  --no-strip              do not strip debug and local symbols from output
  --no-chdir (-C)         do not change to the data directory
                          (Contents/Resources) [forced for plugins]
  --semi-standalone (-s)  depend on an existing installation of Python 2.4
  --alias (-A)            Use an alias to current source file (for development
                          only!)
  --argv-emulation (-a)   Use argv emulation [disabled for plugins]
  --argv-inject           Inject some commands into the argv
  --use-pythonpath        Allow PYTHONPATH to effect the interpreter's
                          environment
  --bdist-base (-b)       base directory for build library (default is build)
  --dist-dir (-d)         directory to put final built distributions in
                          (default is dist)
  --site-packages         include the system and user site-packages into
                          sys.path
  --strip (-S)            strip debug and local symbols from output (on by
                          default, for compatibility)
  --prefer-ppc		  Force application to run translated on i386
                          (LSPrefersPPC=True)
  --debug-modulegraph     Drop to pdb console after the module finding phase
                          is complete
  --debug-skip-macholib   skip macholib phase (app will not be standalone!)


Recipes
-------

py2app includes a mechanism for working around package incompatibilities,
and stripping unwanted dependencies automatically. These are called recipes.

A future version of py2app will support packaging of `Python Eggs`_. Once
this is established, recipes will be obsolete since eggs contain all of the
metadata needed to build a working standalone application.


Common causes for incompatibility
=================================

Some Python packages are written in such a way that they aren't compatible
with being packaged. There are two main causes of this:

- Using ``__import__`` or otherwise importing code without usage of the
  ``import`` statement.
- Requiring in-package data files


Built-in recipes
================

``cjkcodecs``:
    All codecs in the package are imported.

``docutils``:
    Several of its internal components are automatically imported
    (``languages``, ``parsers``, ``readers``, ``writers``,
    ``parsers.rst.directives``, ``parsers.rst.langauges``).

``matplotlib``:
    A dependency on ``pytz.zoneinfo.UTC`` is implied, and the ``matplotlib``
    package is included in its entirety out of the zip file.

``numpy``:
    The ``numpy`` package is included in its entirety out of the zip file.

``PIL``:
    Locates and includes all image plugins (Python modules that end with
    ``ImagePlugin.py``), removes unwanted dependencies on ``Tkinter``.
    
``pydoc``:
    The implicit references on the several modules are removed (``Tkinter``,
    ``tty``, ``BaseHTTPServer``, ``mimetools``, ``select``, ``threading``,
    ``ic``, ``getopt``, ``nturl2path``).

``pygame``:
    Several data files that are included in the zip file where ``pygame`` can
    find them (``freesansbold.ttf``, ``pygame_icon.tiff``,
    ``pygame_icon.icns``).

``PyOpenGL``:
    If the installed version of PyOpenGL reads a ``version`` file to determine
    its version, then the ``OpenGL`` package is included in its entirety out of
    the zip file.

``scipy``:
    The ``scipy`` and ``numpy`` packages are included in their entirety
    out of the zip file.

``sip``:
    If ``sip`` is detected, then all sip-using packages are included
    (e.g. PyQt).


Developing Recipes
==================

py2app currently searches for recipes only in the ``py2app.recipes`` module.
A recipe is an object that implements a ``check(py2app_cmd, modulegraph)``
method.

``py2app_cmd``:
   The py2app command instance (a subclass of ``setuptools.Command``).
   See the source for ``py2app.build_app`` for reference.

``modulegraph``:
   The ``modulegraph.modulegraph.ModuleGraph`` instance.

A recipe should return either ``None`` or a ``dict`` instance.

If a recipe returns ``None`` it should not have performed any actions with
side-effects, and it may be called again zero or more times.

If a recipe returns a ``dict`` instance, it will not be called again. The
returned ``dict`` may have any of these optional string keys:

``filters``:
    A list of filter functions to be called with every module in the 
    modulegraph during flattening. If the filter returns False, the module
    and any of its dependencies will not be included in the output. This is
    similar in purpose to the ``excludes`` option, but can be any predicate
    (e.g. to exclude all modules in a given path).

``loader_files``:
    Used to include data files inside the ``site-packages.zip``. This is a
    list of 2-tuples: ``[(subdir, files), ...]``. ``subdir`` is the path
    within ``site-packages.zip`` and ``files`` is the list of files to include
    in that directory.

``packages``:
    A list of package names to be included in their entirety outside of the
    ``site-packages.zip``.

``prescripts``:
    A list of additional Python scripts to run before initializing the main
    script. This is often used to monkey-patch included modules so that they
    work in a frozen environment. The prescripts may be module names,
    file names, or file-like objects containing Python code (e.g. StringIO).
    Note that if a file-like object is used, it will not currently be scanned
    for additional dependencies.


Implementation Details
----------------------

For those interested in the implementation of py2app, here's a quick
rundown of what happens.


Argument Parsing
================

When ``setup.py`` is run, the normal `setuptools`_ / `distutils`_
``sys.argv`` parsing takes place.


Run build command
=================

The ``build`` command is run to ensure that any extensions specified in the
``setup.py`` will be built prior to the ``py2app`` command. The build
directory will be added to ``sys.path`` so that ``modulegraph`` will find
the extensions built during this command.


Depdency resolution via modulegraph
===================================

The main script is compiled to Python bytecode and analyzed by modulegraph
for ``import`` bytecode. It uses this to build a dependency graph of all
involved Python modules.

The dependency graph is primed with any ``--includes``, ``--excludes``, or
``--packages`` options.


Apply recipes
=============

All of the `Recipes`_ will be run in order to find library-specific tweaks
necessary to build the application properly.


Apply filters
=============

All filters specified in recipes or otherwise added to the py2app Command
object will be run to filter out the dependency graph.

The built-in filter ``not_system_filter`` will
always be run for every application built. This ensures that the contents
of your Mac OS X installation (``/usr/``, ``/System/``, excluding
``/usr/local/``) will be excluded.

If the ``--semi-standalone`` option is used (forced if a vendor Python is
being used), then the ``not_stdlib_filter`` will be automatically added to
ensure that the Python standard library is not included.


Produce graphs
==============

If the ``--xref`` or ``--graph`` option is used, then the ``modulegraph`` is
output to HTML or `GraphViz`_ respectively. The ``.html`` or ``.dot`` file
will be in the ``dist`` folder, and will share the application's name.


Create the .app bundle
======================

An application bundle will be created with the name of your application.

The ``Contents/Info.plist`` will be created from the ``dict`` or filename
given in the ``plist`` option. py2app will fill in any missing keys as
necessary.

A ``__boot__.py`` script will be created in the ``Contents/Resources/`` folder
of the application bundle. This script runs any prescripts used by the
application and then your main script.

If the ``--alias`` option is being used, the build procedure is finished.

The main script of your application will be copied *as-is* to the 
``Contents/Resources/`` folder of the application bundle. If you want to
obfuscate anything (by having it as a ``.pyc`` in the zip), then you
*must not* place it in the main script!

Packages that were explicitly included with the ``packages`` option, or by
a recipe, will be placed in ``Contents/Resources/lib/python2.X/``.

A zip file containing all Python dependencies is created at
``Contents/Resources/Python/site-packages.zip``.

Extensions (which can't be included in the zip) are copied to the
``Contents/Resources/lib/python2.X/lib-dynload/`` folder.


Include Mach-O dependencies
===========================

`macholib`_ is used to ensure the application will run on other computers
without the need to install additional components. All Mach-O
files (executables, frameworks, bundles, extensions) used by the application
are located and copied into the application bundle.

The Mach-O load commands for these Mach-O files are then rewritten to be
``@executable_path/../Frameworks/`` relative, so that dyld knows to find
them inside the application bundle.

``Python.framework`` is special-cased here so as to only include the bare
minimum, otherwise the documentation, entire standard library, etc. would've
been included. If the ``--semi-standalone`` option or a vendor Python is used,
then the ``Python.framework`` is ignored. All other vendor files (those in
``/usr/`` or ``/System/`` excluding ``/usr/local/``) are also excluded.


Strip the result
================

Unless the ``--no-strip`` option is specified, all Mach-O files in the 
application bundle are stripped using the `strip`_ tool. This removes
debugging symbols to make your application smaller.


Copy Python configuration
=========================

This only occurs when not using a vendor Python or using the
``--semi-standalone`` option.

The Python configuration, which is used by ``distutils`` and ``pkg_resources``
is copied to ``Contents/Resources/lib/python2.X/config/``. This is needed
to acquire settings relevant to the way Python was built.


Scripts installed by py2app
---------------------------

py2applet
=========

The ``py2applet`` script can be used either to create an application
quickly in-place, or to generate a ``setup.py`` file that does the same.

In normal usage, simply run ``py2applet`` with the options you would
normally pass to the ``py2app`` command, plus the names of any scripts,
packages, icons, plist files, or data files that you want to generate
the application from.

The ``--argv-emulation`` option is assumed to be desired by default for
``py2applet`` scripts.

The first ``.py`` file is the main script. The application's name will
be derived from this main script.

The first ``.icns`` file, if any, will be used as the application's icon
(equivalent to using the ``--iconfile`` option).

Any folder given that contains an ``__init__.py`` will be wholly included as
out of the zip file (equivalent to using the ``--packages`` option).

Any other file or folder will be included in the ``Contents/Resources/``
directory of the application bundle (equivalent to the ``--resources``
option).

If ``--make-setup`` is passed as the first option to ``py2applet``, it will
generate a ``setup.py`` file that would do the above if run. This can
be used to quickly generate a ``setup.py`` for a new project, or if you
need to tweak a few complex options. The `Tutorial`_ demonstrates this
functionality.


Dependencies
------------

Note that these dependencies should automatically be satisfied by the
installation procedure and do not need to be acquired separately.

setuptools:
   `setuptools`_ provides enhancements to `distutils`_, as well as the
   mechanisms for creating and working with `Python Eggs`_. py2app
   is distributed only as a `Python Egg`_.

bdist_mpkg:
   `bdist_mpkg`_ is another `setuptools`_ command that allows users to
   build Installer packages from Python packages. py2app does not 
   actually depend on `bdist_mpkg`_, however previous versions of
   py2app were distributed with `bdist_mpkg`_ so it is a dependency
   for convenience and familiarity.

macholib:
    `macholib`_ reads and writes the Mach-O object file format. 
    Used by py2app to build a dependency graph of dyld and framework
    dependencies for your application, and then to copy them into your
    application and rewrite their load commands to be ``@executable_path``
    relative. The end result is that your application is going to be
    completely standalone beyond a default install of Mac OS X. You no
    longer have to worry about linking all of your dependencies statically,
    using `install_name_tool`_, etc. It's all taken care of!

modulegraph:
    `modulegraph`_ is a replacement for the Python standard library
    `modulefinder`_. Stores the module dependency tree in a graph data
    structure and allows for advanced filtering and analysis capabilities,
    such as `GraphViz`_ dot output.

altgraph:
    `altgraph`_ is a fork of `Istvan Albert`_'s graphlib, and it used
    internally by both `macholib`_ and `modulegraph`_. It contains
    several small feature and performance enhancements over the original
    graphlib.

    
License
-------

py2app may be distributed under the `MIT`_ or `PSF`_ open source
licenses.

Copyright (c) 2004-2006 Bob Ippolito <bob at redivi.com>.

.. _`macholib`: http://cheeseshop.python.org/pypi/macholib/
.. _`altgraph`: http://cheeseshop.python.org/pypi/altgraph/
.. _`bdist_mpkg`: http://cheeseshop.python.org/pypi/bdist_mpkg/
.. _`modulegraph`: http://cheeseshop.python.org/pypi/modulegraph/
.. _`Python Eggs`: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _`Python Egg`: http://peak.telecommunity.com/DevCenter/PythonEggs
.. _`svn:externals`: http://svnbook.red-bean.com/en/1.1/ch07s04.html
.. _`setuptools`: http://cheeseshop.python.org/pypi/setuptools/
.. _`easy_install`: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _`develop command`: http://peak.telecommunity.com/DevCenter/setuptools#development-mode
.. _`Runtime Configuration Guidelines`: http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/index.html
.. _`PSF`: http://www.python.org/psf/license.html
.. _`MIT`: http://www.opensource.org/licenses/mit-license.php
.. _`Xcode`: http://developer.apple.com/tools/xcode/
.. _`distutils`: http://docs.python.org/lib/module-distutils.html
.. _`py2exe`: http://cheeseshop.python.org/pypi/py2exe/
.. _`Istvan Albert`: http://www.personal.psu.edu/staff/i/u/iua1/
.. _`strip`: x-man-page://1/strip
.. _`install_name_tool`: x-man-page://1/install_name_tool
.. _`modulefinder`: http://docs.python.org/lib/module-modulefinder.html
.. _`GraphViz`: http://www.research.att.com/sw/tools/graphviz/
