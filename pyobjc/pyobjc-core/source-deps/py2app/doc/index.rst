py2app - convert python scripts into standalone Mac OS X applications
=====================================================================

.. contents::

Abstract
--------

**py2app** is a Python `distutils`_ suite which provides several
useful features for distributing Python applications and libraries
on the Mac OS X platform.  The **py2app** suite contains the following
packages:

**py2app**:

    A `distutils`_ command that converts Python scripts into
    executable Mac OS X applications, able to run without requiring
    a Python installation.  It has been used to create standalone
    application bundles and plug-ins for open source, commercial,
    and in-house projects.  It is known compatible with GUI
    frameworks such as `wxPython`_, `Tkinter`_, `pygame`_, `PyQt`_, and
    `PyObjC`_, but it should work in the context of any framework with
    little or no effort.  It may also be used in conjunction with
    `PyObjC`_ to write plug-ins for Cocoa applications, screen
    savers, preference panes, etc.  This is a complete replacement
    for the `bundlebuilder`_ tool included in the Python standard library.

**bdist_mpkg**:

    Creates Mac OS X installer ``.mpkg`` files from Python libraries.
    Installer packages are familiar to Mac OS X users, provide a
    safe and easy way to authenticate as root to install privileged
    files such as headers and scripts.  Once a **bdist_mpkg**
    distribution has been created, it may be installed to other
    machines with a similar Python environment without requiring a
    compiler.  Installer packages can be used to do distributed
    installations with tools such as `Apple Remote Desktop`_ or they
    could be integrated into a custom Mac OS X installation DVD
    with a tool such as `Slipy`_.

**macholib**:

    Reads and writes the Mach-O object file format.  Used by **py2app**
    to build a dependency graph of dyld and framework dependencies for your
    application, and then to copy them into your application and rewrite
    their load commands to be ``@executable_path`` relative.  The end
    result is that your application is going to be completely standalone
    beyond a default install of Mac OS X.   You no longer have to worry
    about linking all of your dependencies statically, using
    `install_name_tool`_, etc.  It's all taken care of!

**modulegraph**:

    A replacement for the Python standard library `modulefinder`_.  Stores
    the module dependency tree in a graph data structure and allows for
    advanced filtering and analysis capabilities, such as `GraphViz`_ dot
    output.  This is used internally by **py2app**, but the code should
    be completely cross-platform.  It is hoped that this package will be
    adopted by application packaging software for other platforms in the
    future, such as `py2exe`_ and `cx_Freeze`_.

**altgraph**:

    This is a fork of `Istvan Albert`_'s `graphlib`_, and it used internally
    by both **macholib** and **modulegraph**.  It contains several small
    feature and performance enhancements over the original `graphlib`_.
    
License
-------

Any components of the **py2app** suite may be distributed under the MIT
or PSF open source licenses.

Downloads
---------

Note that the installer for `PyObjC`_ 1.2 ships with **py2app** 0.1.7. 

An installer for **py2app** 0.1.8 may be downloaded from:

- http://undefined.org/python/packages.html

The source to **py2app** 0.1.8 may be downloaded here:

- http://undefined.org/python/py2app-0.1.8.tgz

**py2app** maintains a public subversion source code repository currently
located at:

- http://svn.red-bean.com/bob/py2app/trunk/


As of version 0.1.6, **py2app** uses the ``extra_path`` feature of 
`distutils`_, which changes the installation layout.  
If you have **py2app** 0.1.5 or earlier installed, you must manually
remove the following directories from your site-packages directory
(probably ``/Library/Python/2.3``) if they exist before upgrading:

- ``py2app``
- ``macholib``
- ``bdist_mpkg``
- ``modulegraph``
- ``altgraph``

py2app Documentation
--------------------

- How do I use **py2app**?

  **py2app** is a `distutils`_ command that is used in a similar manner to
  **py2exe**.  For your application, you must create a Python script
  (conventionally named ``setup.py``) that looks like the following::

    #!/usr/bin/env python
    """
    setup.py - script for building MyApplication

    Usage:
        % python setup.py py2app
    """
    from distutils.core import setup
    import py2app

    setup(
        app=['MyApplication.py'],
    )

  When running this script as directed, **py2app** will do the following:

  - Process the command line for arguments.  The arguments accepted by the **py2app**
    command can be enumerated using the following command line::

      % python setup.py py2app --help
      Global options:
        ... (these are available from any distutils command)
      Options for 'py2app' command:
        ... (these are specific to py2app)
      usage: 
        ... (this is a generic distutils usage message)

    Note that any of the options accepted on the command line may also be used
    in your ``setup.py`` script!  For example::

      #!/usr/bin/env python
      """
      setup.py - script for building MyApplication
      """
      from distutils.core import setup
      import py2app

      # Note that you must replace hypens '-' with underscores '_'
      # when converting option names from the command line to a script.
      # For example, the --argv-emulation option is passed as 
      # argv_emulation in an options dict.
      py2app_options = dict(
          # Map "open document" events to sys.argv.
          # Scripts that expect files as command line arguments
          # can be trivially used as "droplets" using this option.
          # Without this option, sys.argv should not be used at all
          # as it will contain only Mac OS X specific stuff.
          argv_emulation=True,

          # This is a shortcut that will place MyApplication.icns
          # in the Contents/Resources folder of the application bundle,
          # and make sure the CFBundleIcon plist key is set appropriately.
          iconfile='MyApplication.icns',
      )

      setup(
          app=['MyApplication.py'],
          options=dict(
              # Each command is allowed to have its own
              # options, so we must specify that these
              # options are py2app specific.
              py2app=py2app_options,
          )
      )

  - Issue the `distutils`_ ``build`` command

    - If your application needs any Extensions, then these will be
      built at this time, and the build directory will be added to ``sys.path``.

  - Analyze the application for Python dependencies
    
    - Compile ``MyApplication.py`` to Python bytecode and analyze it for 
      `import`_ statements.
    - Build a dependency graph of everything it finds (with **modulegraph**).
    - It will look for modules and packages in the same manner as Python would
      if you ran ``python MyApplication.py``.  Namely, it will look first in the
      same directory as ``MyApplication.py``, and then it will search ``sys.path``.
      If for some reason you need it to look somewhere else, simply modify your
      ``setup.py`` script such that it modifies ``sys.path`` before calling the
      `distutils`_ ``setup(...)`` function.

  - Make sense of the dependencies

    - Using special library-specific tweaks called recipes, it will modify
      this dependency graph as needed.  For example, it will perform such tasks
      as eliminating unwanted dependencies (`pydoc`_'s import of `Tkinter`_) and
      including "plugins" for certain libraries that do not use the normal import
      statements (`PIL`_, `docutils`_).  See the section below on recipes for
      more information about this process.

  - Create the application bundle

    - An application bundle will be created in the dist directory with the name
      of your application.
    - Based upon information in **py2app** and information you passed to
      ``setup(...)``, an ``Info.plist`` will be created in the application bundle
      with metadata appropriate to your application.
    - A ``__boot__.py`` script will be created in the ``Contents/Resources`` folder
      of the application bundle containing **py2app** specific bootstrapping code
      to get your application running.
    - The main script of your application will be copied as-is to the
      ``Contents/Resources/Python`` folder.  This may change in the future,
      but it is currently in source form and is not obfuscated in any way
      other than its location.
    - Packages that were explicitly included with the ``--packages`` option are
      placed in ``Contents/Resources/Python/site-packages``.
    - A zip file containing all other dependencies is created at
      ``Contents/Resources/Python/site-packages.zip``.
    - Extensions that could not be included in the zip file are copied to
      appropriate locations in ``Contents/Resources/Python/lib-dynload``.

  - Make the application bundle standalone

    - Since a typical Python application may have C library dependencies, such as
      the Python interpreter itself, wxWidgets, etc. a second dependency resolution
      pass occurs on the application bundle.
    - Scan the application bundle for all Mach-O files (executables, shared libraries,
      plugins, extensions, etc.).
    - Read the load commands from every Mach-O file (using **macholib**) and build
      a dependency graph.
    - Copy in every dependent dylib (shared library) and framework that is not already
      in the application bundle.  Note that dylibs and frameworks in vendor locations
      (``/System`` and ``/usr`` - except for ``/usr/local``) are NOT included in your
      application bundle.  This can include the Python interpreter, if you are using
      a Python interpreter shipped with Mac OS X.  Thus your application may be
      "tightly bound" to a particular major version of Mac OS X if you are using
      the vendor Python.
    - Rewrite the Mach-O load commands such that the libraries know that
      they have moved inside of an application bundle (i.e. using
      ``@executable_path`` relative ids).
    - Strip every Mach-O file of extraneous information (debugging symbols, etc.) 
      to save space.  This may be disabled with ``--no-strip``.


- What recipes does **py2app** come with?

  `docutils`_:

    Locates and includes all plugins that ship with docutils (languages,
    parsers, readers, writers)

  `pydoc`_:

    Removes several dependencies that are only used when running the `pydoc`_
    web server or `Tkinter`_ GUI (Tkinter, tty, BaseHTTPServer, mimetools, select,
    threading, ic, getopt).

  `pygame`_:

    Includes the whole `pygame`_ package as-is, so that it will locate its data
    files correctly.  This recipe may be improved in the future if `pygame`_
    undergoes appropriate modifications.

  `PIL`_:

    Locates and includes all image plugins (Python modules that end with
    ``ImagePlugin.py``), removes unwanted dependencies on `Tkinter`_.

  `pyOpenGL`_:

    Includes the whole `pyOpenGL`_ package as-is, so that it can read its version
    file during __init__.py.  This recipe may be improved in the future if
    `PyOpenGL`_ undergoes appropriate modifications.

  **py2app**:

    Includes the whole **py2app** package as-is, so that it has copies of the
    executable and plugin templates.  This recipe may be improved in the future
    if **py2app** undergoes appropriate modifications.

  `sip`_:

    If ANY extension that uses `sip`_ is detected, include all extensions that use
    `sip`_.  This is necessary because `sip`_ generates C code to do its imports,
    and is thus not trackable by bytecode analysis.  The only package known to use
    `sip`_ is `PyQt`_, so what this means is that if you use any of `PyQt`_, then
    all of it will be included.

  Note that recipes are developed on an
  as-needed basis, and coverage of every single Python library is not possible.
  If you have trouble with a particular library, please let us know.

  The following packages are known to need recipes, but none currently exist:

  `PEAK`_:

    The workaround is to include `PEAK`_ using the ``packages`` option.
 
  Anything that uses `Pango`_ or `GTK+`_:

    These C libraries require data files and environment variables set up.
    A workaround exists, but one has not yet been written and tested.

  `wxPython`_ 2.4.x:

    A ``data_files`` option to include a resource file must be added to
    ``setup.py``::

        #!/usr/bin/env python
        """
        setup.py - workaround for wxPython 2.4.x

        Usage:
            % python setup.py py2app
        """
        from distutils.core import setup
        import py2app
        setup(
            app=['test.py'],
            data_files=[('../Frameworks', [
                '/usr/local/lib/libwx_mac-2.4.0.rsrc',
                ]
            )],
        )
   

- The **py2app** development model

  Currently, the best description for the preferred development model when
  doing **py2app** based development lives in the `PyObjC tutorial`_.

- What is an alias bundle (the ``--alias`` option)?

  An alias bundle is intended to be used only during development.  Alias bundles
  Are *not* portable to other machines and are not standalone in any way.
  Alias bundles have the following features:

  - Creating them is extremely fast, as no dependency resolution, copying, etc. happens.
  - They use an alias to your main script, and symlinks to your data files. So, unless you need to change the ``setup.py``, you do not need to rebuild the alias bundle.
  - This means that you can simply edit the source, and restart the application!

  An alias bundle is similar to `BundleBuilder`_'s ``--link`` option, and is
  roughly equivalent to the idea of `Xcode`_'s `ZeroLink`_ feature.

- What does **py2app** install?

  ``/Library/Python/2.3`` (or your ``site-packages`` directory):

    A **py2app** folder containing the **py2app**, **macholib**,
    **altgraph**, and **bdist_mpkg** packages.  A **py2app.pth** file
    is also created, so that this **py2app** folder is automatically
    added to your ``sys.path``.  This corresponds to the ``src`` folder
    in the **py2app** sources.

  ``/usr/local/bin``:

    Several command line tools that make the **py2app** suite easier to use,
    see the `Tools`_ section.  This corresponds to the ``scripts`` folder
    in the **py2app** sources.

  ``/Developer/Python/py2app/Examples``:

    Several examples of **py2app** ``setup.py`` scripts of varying complexity.
    This corresponds to the ``examples`` folder in the **py2app** sources.

  ``/Developer/Applications/Python Tools/py2app``:

    Several GUI tools and droplets that make the **py2app** suite easier to
    use, see the `GUI Tools`_ section.  This corresponds to the ``tools``
    folder in the **py2app** sources.

- How does **py2app** differ from `py2exe`_ or `cx_Freeze`_?

  - **py2app** has a richer system for managing Python module dependencies,
    **modulegraph**, where `py2exe`_ and `cx_Freeze`_ use some cruft on top
    of the standard library `modulefinder`_.
  
  - **py2app** works on Mac OS X, the others don't (and vice versa for their
    respective operating systems).

  - (XXX: describe syntax differences here)

- What are the similarities between **py2app**, `py2exe`_, and `cx_Freeze`_?
  
  XXX

- What is the canonical way for my application to detect if it is being
  run in a bundled application environment?

  Currently this information is in the `pythonmac.org FAQ`_.

- When should I subclass the **py2app** command?

  There are no known cases where this has been necessary, so you probably
  don't!

- Known issues with **py2app**

  Current issues with **py2app** are reflected in the `TODO`_ document
  in the source tree.  The linked document reflects the current development
  version.  Also see the errata in the section about recipes above.

bdist_mpkg Documentation
------------------------

- How do I use **bdist_mpkg**?

  **bdist_mpkg** is intended to package existing Python software that
  already has a `distutils`_ ``setup.py`` script.

  The easiest way to use the features of **bdist_mpkg** is simply to
  use the **bdist_mpkg** tool, as documented in the `Tools`_ section below.

  Otherwise, in order to enable the **bdist_mpkg** command in a 
  given ``setup.py`` script, simply add an ``import bdist_mpkg`` statement 
  near the top of the ``setup.py`` script.

- What options does **bdist_mpkg** accept?

  To see the list of options that **bdist_mpkg** accepts, simply run it with
  the ``--help`` option (this must be done in a directory containing a
  `distutils`_ ``setup.py`` script)::

    % bdist_mpkg --help
    Global options:
      ... (these are available from any distutils command)
    Options for 'bdist_mpkg' command:
      ... (these are specific to bdist_mpkg)
    usage: 
      ... (this is a generic distutils usage message)

- When should I subclass the **bdist_mpkg** command?

  Subclassing **bdist_mpkg** is currently necessary in order to add
  additional features to the installation package, such as
  documentation, examples, tools, etc.

  Currently, the documentation
  for doing this is the source, and the examples are the source to
  the **py2app** and `PyObjC`_ ``setup.py`` scripts.

  The API for
  **bdist_mpkg** is not guaranteed to be stable, so avoid subclassing
  at this time unless you plan to communicate with the author
  about your requirements and are willing to make changes to accommodate
  changes in the API as **bdist_mpkg** improves.

Tools
-----

By default, the following tools are installed to ``/usr/local/bin``:

**bdist_mpkg**:

    A convenient way to run the **bdist_mpkg** `distutils`_ command.
    Equivalent to editing the ``setup.py`` in the current
    directory to import **bdist_mpkg** and running the following
    command::

        % python setup.py bdist_mpkg --open

    If any options are given, then they are given in place of ``--open``.
    
**macho_find**:

    A tool for finding Mach-O object files using **macholib**.
    The arguments may be files or directories.  The output of this tool is
    identical to that of the BSD `find`_ command.

**macho_standalone**:

    A tool that makes a valiant attempt to make the given application
    bundle standalone using **macholib** using machinery similar, but not
    identical to, what happens when using **py2app**.  This tool modifies
    the given application bundle in-place, so you may want to make a backup
    before performing this operation.  This tool works for ANY Mach-O
    executable bundle, and contains no Python-specific functionality.

**py2applet**:

    A convenient way to run the **py2app** `distutils`_ command without
    creating a ``setup.py``.  The first python script passed as an
    argument will be the main script, any additional files or directories
    will be considered as data files.  If a file with the ``.icns``
    extension is passed, it will be used as the application's icon.  If
    a file named ``Info.plist`` is given, it will be used as the template
    for the application's ``Info.plist``.  The application will be built
    with the ``--argv-emulation`` on.  It is not possible to pass options
    to py2applet.  If you need anything more, you should create a
    ``setup.py`` and use the **py2app** command in the normal fashion.

GUI Tools
---------

By default, the following GUI tools are installed to
``/Developer/Applications/Python Tools/py2app``:

**PackageInstaller**:

    A droplet version of the **bdist_mpkg** tool, it does
    not have any interactivity, so it is not possible to use this tool
    to pass options other than the default.  Errors and informational
    messages will go to the Console.

**py2applet**:

    A droplet version of the **py2applet** tool.  It works in
    exactly the same way and provides no interactivity.  Note that
    since you have no guarantee of the order of files in the pasteboard,
    you should drag only one at a time to this script.  Errors and
    informational messages will go to the console.

----------

Copyright (c) 2004, 2005 Bob Ippolito <bob at redivi.com>.

.. _`pythonmac.org FAQ`: http://pythonmac.org/wiki/FAQ
.. _`TODO`: http://svn.red-bean.com/bob/py2app/trunk/TODO.txt
.. _`ZeroLink`: http://developer.apple.com/documentation/DeveloperTools/Conceptual/Build_System/Using_ZeroLink/Using_ZeroLink.html
.. _`Xcode`: http://developer.apple.com/tools/xcode/
.. _`PyObjC tutorial`: http://pyobjc.sourceforge.net/doc/tutorial.php
.. _`GTK+`: http://www.gtk.org/
.. _`Pango`: http://www.pango.org/
.. _`PEAK`: http://peak.telecommunity.com/
.. _`docutils`: http://docutils.sourceforge.net/
.. _`PIL`: http://www.pythonware.com/products/pil/
.. _`pydoc`: http://docs.python.org/lib/module-pydoc.html
.. _`sip`: http://www.riverbankcomputing.co.uk/sip/index.php
.. _`pyOpenGL`: http://pyopengl.sourceforge.net/
.. _`import`: http://docs.python.org/ref/import.html
.. _`distutils`: http://docs.python.org/lib/module-distutils.html
.. _`wxPython`: http://www.wxpython.org/
.. _`Tkinter`: http://www.python.org/moin/TkInter
.. _`pygame`: http://www.pygame.org/
.. _`PyQt`: http://www.riverbankcomputing.co.uk/pyqt/index.php
.. _`PyObjC`: http://pyobjc.sourceforge.net/
.. _`bundlebuilder`: http://www.python.org/moin/BundleBuilder
.. _`Apple Remote Desktop`: http://www.apple.com/remotedesktop/
.. _`Slipy`: http://www.versiontracker.com/dyn/moreinfo/macosx/24178
.. _`py2exe`: http://starship.python.net/crew/theller/py2exe/
.. _`cx_Freeze`: http://starship.python.net/crew/atuining/cx_Freeze/
.. _`graphlib`: http://www.personal.psu.edu/staff/i/u/iua1/python/graphlib/html/public/graphlib-module.html
.. _`Istvan Albert`: http://www.personal.psu.edu/staff/i/u/iua1/
.. _`find`: x-man-page://1/find
.. _`install_name_tool`: x-man-page://1/install_name_tool
.. _`modulefinder`: http://pydoc.org/2.3/modulefinder.html
.. _`GraphViz`: http://www.research.att.com/sw/tools/graphviz/
