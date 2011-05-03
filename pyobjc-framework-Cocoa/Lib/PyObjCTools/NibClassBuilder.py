#!/usr/bin/env python

"""NibClassBuilder.py -- Tools for working with class definitions in
"Next Interface Builder" files ("nibs").

NOTE: This module is deprecated and is not supported with modern versions
of Interface Builder because those uses a NIB format that is not compatibility
with NibClassBuilder. We have no intention whatsoever to fix the compatibility
issues, use explicit definitions instead. On a more possitive note: IB 3.0
fully supports reading class definitions from Python files, which removes
the reason why we wrote this module in the first place.




Extracting class definitions from nibs.

The module maintains a global set of class definitions, extracted from
nibs. To add the classes from a nib to this set, use the extractClasses()
function. It can be called in two ways:

    extractClasses(nibName, bundle=<main-bundle>)
        This finds the nib by name from a bundle. If no bundle
        if given, the main bundle is searched.

    extractClasses(path=pathToNib)
        This uses an explicit path to a nib.

extractClasses() can be called multiple times for the same bundle: the
results are cached so no almost extra overhead is caused.


Using the class definitions.

The module contains a "magic" base (super) class called AutoBaseClass.
Subclassing AutoBaseClass will invoke some magic that will look up the
proper base class in the class definitions extracted from the nib(s).
If you use multiple inheritance to use Cocoa's "informal protocols",
you _must_ list AutoBaseClass as the first base class. For example:

    class PyModel(AutoBaseClass, NSTableSource):
        ...


The NibInfo class.

The parsing of nibs and collecting the class definition is done by the
NibInfo class. You normally don't use it directly, but it's here if you
have special needs.


The command line tool.

When run from the command line, this module invokes a simple command
line program, which you feed paths to nibs. This will print a Python
template for all classes defined in the nib(s). For more documentation, see
the commandline_doc variable, or simply run the program without
arguments. It also contains a simple test program.
"""

#
# Written by Just van Rossum <just@letterror.com>, borrowing heavily
# from Ronald Oussoren's classnib.py module, which this module
# supercedes. Lots of additional input from Bill Bumgarner and Jack
# Jansen.
#

import sys
import os
import objc

import warnings
warnings.warn("PyObjCTools.NibClassBuilder is deprecated, use explicit definitions instead", DeprecationWarning)


__all__ = ["AutoBaseClass", "NibInfo", "extractClasses"]


from Foundation import NSDictionary, NSObject, NSBundle
import AppKit  # not used directly, but we look up classes from AppKit
               # dynamically, so it has to be loaded.


class NibLoaderError(Exception): pass


class ClassInfo:

    attrNames = ("nibs", "name", "super", "actions", "outlets")

    def __repr__(self):
        items = self.__dict__.items()
        items.sort()
        return self.__class__.__name__ + "(" + \
            ", ".join([ "%s=%s"%i for i in items ]) + ")"

    def merge(self, other):
        assert self.name == other.name
        if self.super != other.super:
            raise NibLoaderError, \
                    "Incompatible superclass for %s" % self.name
        self.nibs = mergeLists(self.nibs, other.nibs)
        self.outlets = mergeLists(self.outlets, other.outlets)
        self.actions = mergeLists(self.actions, other.actions)

    def __cmp__(self, other):
        s = [getattr(self, x) for x in self.attrNames]
        o = [getattr(other, x) for x in self.attrNames]
        return cmp(s, o)


class NibInfo(object):

    def __init__(self):
        self.classes = {}
        self.parsedNibs = {}

    # we implement a subset of the dictionary protocol, for convenience.

    def keys(self):
        return self.classes.keys()

    def has_key(self, name):
        return self.classes.has_key(name)

    def len(self):
        return len(self.classes)

    def __iter__(self):
        return iter(self.classes)

    def __getitem__(self, name):
        return self.classes[name]

    def get(self, name, default=None):
        return self.classes.get(name, default)

    def extractClasses(self, nibName=None, bundle=None, path=None):
        """Extract the class definitions from a nib.

        The nib can be specified by name, in which case it will be
        searched in the main bundle (or in the bundle specified), or
        by path.
        """
        if path is None:
            self._extractClassesFromNibFromBundle(nibName, bundle)
        else:
            if nibName is not None or bundle is not None:
                raise ValueError, ("Can't specify 'nibName' or "
                    "'bundle' when specifying 'path'")
            self._extractClassesFromNibFromPath(path)

    def _extractClassesFromNibFromBundle(self, nibName, bundle=None):
        if not bundle:
            bundle = objc.currentBundle()
        if nibName[-4:] == '.nib':
            resType = None
        else:
            resType = "nib"
        path = bundle.pathForResource_ofType_(nibName, resType)
        if not path:
            raise NibLoaderError, ("Could not find nib named '%s' "
                    "in bundle '%s'" % (nibName, bundle))
        self._extractClassesFromNibFromPath(path)

    def _extractClassesFromNibFromPath(self, path):
        path = os.path.normpath(path)
        if self.parsedNibs.has_key(path):
            return  # we've already parsed this nib
        nibName = os.path.basename(path)
        nibInfo = NSDictionary.dictionaryWithContentsOfFile_(
                os.path.join(path, 'classes.nib'))
        if nibInfo is None:
            raise NibLoaderError, "Invalid NIB file [%s]" % path
        if not nibInfo.has_key('IBVersion'):
            raise NibLoaderError, "Invalid NIB info"
        if nibInfo['IBVersion'] != '1':
            raise NibLoaderError, "Unsupported NIB version"
        for rawClsInfo in nibInfo['IBClasses']:
            self._addClass(nibName, rawClsInfo)
        self.parsedNibs[path] = 1

    def _addClass(self, nibName, rawClsInfo):
        classes = self.classes
        name = rawClsInfo['CLASS']
        if name == "FirstResponder":
            # a FirstResponder never needs to be made
            return

        clsInfo = ClassInfo()
        clsInfo.nibs = [nibName]  # a class can occur in multiple nibs
        clsInfo.name = name
        clsInfo.super = rawClsInfo.get('SUPERCLASS', 'NSObject')
        clsInfo.actions = [a + "_" for a in rawClsInfo.get('ACTIONS', ())]
        clsInfo.outlets = list(rawClsInfo.get('OUTLETS', ()))

        if not classes.has_key(name):
            classes[name] = clsInfo
        else:
            classes[name].merge(clsInfo)

    def makeClass(self, name, bases, methods):
        """Construct a new class using the proper base class, as specified
        in the nib.
        """
        clsInfo = self.classes.get(name)
        if clsInfo is None:
            raise NibLoaderError, ("No class named '%s' found in "
                    "nibs" % name)

        try:
            superClass = objc.lookUpClass(clsInfo.super)
        except objc.nosuchclass_error:
            raise NibLoaderError, ("Superclass '%s' for '%s' not "
                    "found." % (clsInfo.super, name))
        bases = (superClass,) + bases
        metaClass = superClass.__class__

        for o in clsInfo.outlets:
            if not methods.has_key(o):
                methods[o] = objc.IBOutlet(o)

        for a in clsInfo.actions:
            if not methods.has_key(a):
                # XXX we could issue warning here!
                pass
                # don't insert a stub as it effectively disables
                # AppKit's own method validation
                #methods[a] = _actionStub

        return metaClass(name, bases, methods)

    def printTemplate(self, file=None):
        """Print a Python template of classes, matching their specification
        in the nib(s).
        """
        if file is None:
            file = sys.stdout
        writer = IndentWriter(file)
        self._printTemplateHeader(writer)

        classes = self.classes.values()
        classes.sort()  # see ClassInfo.__cmp__
        for clsInfo in classes:
            if _classExists(clsInfo.super):
                self._printClass(writer, clsInfo)
            else:
                writer.writeln("if 0:")
                writer.indent()
                writer.writeln("# *** base class not found: %s" % clsInfo.super)
                self._printClass(writer, clsInfo)
                writer.dedent()

        self._printTemplateFooter(writer)

    def _printTemplateHeader(self, writer):
        nibs = {}
        for clsInfo in self.classes.values():
            for nib in clsInfo.nibs:
                nibs[nib] = 1

        writer.writeln("import objc")
        writer.writeln("from Foundation import *")
        writer.writeln("from AppKit import *")
        writer.writeln("from PyObjCTools import NibClassBuilder, AppHelper")
        writer.writeln()
        writer.writeln()
        nibs = nibs.keys()
        nibs.sort()
        for nib in nibs:
            assert nib[-4:] == ".nib"
            nib = nib[:-4]
            writer.writeln("NibClassBuilder.extractClasses(\"%s\")" % nib)
        writer.writeln()
        writer.writeln()

    def _printTemplateFooter(self, writer):
        writer.writeln()
        writer.writeln('if __name__ == "__main__":')
        writer.indent()
        writer.writeln('AppHelper.runEventLoop()')
        writer.dedent()

    def _printClass(self, writer, clsInfo):
        nibs = clsInfo.nibs
        if len(nibs) > 1:
            nibs[-2] = nibs[-2] + " and " + nibs[-1]
            del nibs[-1]
        nibs = ", ".join(nibs)
        writer.writeln("# class defined in %s" % nibs)
        writer.writeln("class %s(NibClassBuilder.AutoBaseClass):" % clsInfo.name)
        writer.indent()
        writer.writeln("# the actual base class is %s" % clsInfo.super)
        outlets = clsInfo.outlets
        actions = clsInfo.actions
        if outlets:
            writer.writeln("# The following outlets are added to the class:")
            outlets.sort()
            for o in outlets:
                writer.writeln("# %s" % o)
            writer.writeln()
        if not actions:
            writer.writeln("pass")
            writer.writeln()
        else:
            if actions:
                actions.sort()
                for a in actions:
                    writer.writeln("def %s(self, sender):" % a)
                    writer.indent()
                    writer.writeln("pass")
                    writer.dedent()
                writer.writeln()
        writer.writeln()
        writer.dedent()


def _frameworkForClass(className):
    """Return the name of the framework containing the class."""
    try:
        cls = objc.lookUpClass(className)
    except objc.error:
        return ""
    path = NSBundle.bundleForClass_(cls).bundlePath()
    if path == "/System/Library/Frameworks/Foundation.framework":
        return "Foundation"
    elif path == "/System/Library/Frameworks/AppKit.framework":
        return "AppKit"
    else:
        return ""


def _classExists(className):
    """Return True if a class exists in the Obj-C runtime."""
    try:
        objc.lookUpClass(className)
    except objc.error:
        return 0
    else:
        return 1


class IndentWriter:

    """Simple helper class for generating (Python) code."""

    def __init__(self, file=None, indentString="    "):
        if file is None:
            file = sys.stdout
        self.file = file
        self.indentString = indentString
        self.indentLevel = 0

    def writeln(self, line=""):
        if line:
            self.file.write(self.indentLevel * self.indentString +
                    line + "\n")
        else:
            self.file.write("\n")

    def indent(self):
        self.indentLevel += 1

    def dedent(self):
        assert self.indentLevel > 0, "negative dedent"
        self.indentLevel -= 1


def mergeLists(l1, l2):
    r = {}
    for i in l1:
        r[i] = 1
    for i in l2:
        r[i] = 1
    return r.keys()


class _NibClassBuilder(type):

    def _newSubclass(cls, name, bases, methods):
        # Constructor for AutoBaseClass: create an actual
        # instance of _NibClassBuilder that can be subclassed
        # to invoke the magic behavior.
        return type.__new__(cls, name, bases, methods)
    _newSubclass = classmethod(_newSubclass)

    def __new__(cls, name, bases, methods):
        # __new__ would normally create a subclass of cls, but
        # instead we create a completely different class.
        if bases and bases[0].__class__ is cls:
            # get rid of the AutoBaseClass base class
            bases = bases[1:]
        return _nibInfo.makeClass(name, bases, methods)


# AutoBaseClass is a class that has _NibClassBuilder is its' metaclass.
# This means that if you subclass from AutoBaseClass, _NibClassBuilder
# will be used to create the new "subclass". This will however _not_
# be a real subclass of AutoBaseClass, but rather a subclass of the
# Cocoa class specified in the nib.
AutoBaseClass = _NibClassBuilder._newSubclass("AutoBaseClass", (), {})


_nibInfo = NibInfo()

extractClasses = _nibInfo.extractClasses


#
# The rest of this file is a simple command line tool.
#

commandline_doc = """\
NibLoader.py [-th] nib1 [...nibN]
  Print an overview of the classes found in the nib file(s) specified,
  listing their superclass, actions and outlets as Python source. This
  output can be used as a template or a stub.
  -t Instead of printing the overview, perform a simple test on the
     arguments.
  -h Print this text."""

def usage(msg, code):
    if msg:
        print msg
    print commandline_doc
    sys.exit(code)

def test(*nibFiles):
    for path in nibFiles:
        print "Loading", path
        extractClasses(path=path)
    print
    classNames = _nibInfo.keys()
    classNames.sort()
    for className in classNames:
        try:
            # instantiate class, equivalent to
            # class <className>(AutoBaseClass):
            #     pass
            cls = type(className.encode('ascii'), (AutoBaseClass,), {})
        except NibLoaderError, why:
            print "*** Failed class: %s; NibLoaderError: %s" % (
                    className, why[0])
        else:
            print "Created class: %s, superclass: %s" % (cls.__name__,
                    cls.__bases__[0].__name__)

def printTemplate(*nibFiles):
    for path in nibFiles:
        extractClasses(path=path)
    _nibInfo.printTemplate()

def commandline():
    import getopt

    try:
        opts, nibFiles = getopt.getopt(sys.argv[1:], "th")
    except getopt.error, msg:
        usage(msg, 1)

    doTest = 0
    for opt, val in opts:
        if opt == "-t":
            doTest = 1
        elif opt == "-h":
            usage("", 0)

    if not nibFiles:
        usage("No nib file specified.", 1)

    if doTest:
        test(*nibFiles)
    else:
        printTemplate(*nibFiles)


if __name__ == "__main__":
    commandline()
