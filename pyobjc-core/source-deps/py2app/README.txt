py2app is a suite of distutils extensions for Python
development on the Mac.  The additional distutils
commands (when imported) are as follows:

py2app:

    Converts python scripts into executable Mac OS X
    applications, able to run without requiring an
    existing python installation. This is a
    replacement for bundlebuilder.

bdist_mpkg:
    
    Extensible Mac OS X installer package creation
    command.  By default it creates a self-contained
    metapackage that separates your package's
    components by install scheme (platlib, scripts,
    headers, etc.).  It can be subclassed to provide
    additional subpackages such as dependencies,
    example code, documentation, applications, Xcode
    templates, etc.

The following pieces of the py2app suite may also be
of general interest:
    
py2app.modulegraph:
    
    Cross-platform extremely flexible replacement for
    modulefinder that uses a graph data structure to
    track dependencies.
    
altgraph:

    General purpose graph library, forked from graphlib.

macholib:
    
    Mach-O header tool suite.  Can be used to analyze and
    rewrite dependencies or symbols in Mach-O headers.
    Primarily used as a replacement for otool
    and install_name_tool.
