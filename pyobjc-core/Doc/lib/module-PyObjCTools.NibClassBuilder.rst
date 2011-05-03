===================================================================
:mod:`PyObjCTools.NibClassBuilder` -- Extract definitions from NIBs
===================================================================

.. module:: PyObjCTools.NibClassBuilder
   :synopsis: Extract definitions from NIBs

Extracting class definitions from nibs
--------------------------------------

The module maintains a global set of class definitions, extracted from
nibs. To add the classes from a nib to this set, use the ``extractClasses()``
function. It can be called in two ways:

.. function:: extractClasses(nibName, bundle=<current-bundle>)

    This finds the nib by name from a bundle. If no bundle
    if given, the ``objc.currentBundle()`` is searched.

.. function:: extractClasses(path=pathToNib)

    This uses an explicit path to a nib.

``extractClasses()`` can be called multiple times for the same bundle: the
results are cached so no almost extra overhead is caused.

Using the class definitions
---------------------------

The module contains a "magic" base (super) class called ``AutoBaseClass``.
Subclassing ``AutoBaseClass`` will invoke some magic that will look up the
proper base class in the class definitions extracted from the nib(s).
If you use multiple inheritance to use Cocoa's "informal protocols",
you *must* list ``AutoBaseClass`` as the first base class. For example::

    class PyModel(AutoBaseClass, NSTableSource):
        ...


The ``NibInfo`` class
---------------------

The parsing of nibs and collecting the class definition is done by the
``NibInfo`` class. You normally don't use it directly, but it's here if you
have special needs.

The command line tool
---------------------

When run from the command line, this module invokes a simple command
line program, which you feed paths to nibs. This will print a Python
template for all classes defined in the nib(s). For more documentation,
see the commandline_doc variable, or simply run the program without
arguments. It also contains a simple test program.