#!/usr/bin/env python

"""

loadClassesForNib(nibPath):


loadClassesForNibFromBundle(nibName[, sourceBundle=<mainbundle>]):


NibClassBuilder -- metaclass

  class PyModel(NSTbleSource):
      __metaclass__ = NibClassBuilder
      ...


NibInfo

"""
import sys
import os
import objc


__all__ = ["AutoBaseClass", "NibClassBuilder", "loadClassesForNib",
           "loadClassesForNibFromBundle", "NibInfo"]


NSDictionary = objc.lookup_class("NSDictionary")
NSObject = objc.lookup_class("NSObject")
NSBundle = objc.lookup_class("NSBundle")


class NibLoaderError(Exception): pass


class ClassInfo:

	__slots__ = ("nibs", "name", "super", "actions", "outlets")

	def merge(self, other):
		assert self.name == other.name
		if self.super != other.super:
			raise NibLoaderError, \
					"Incompatible superclass for %s" % self.name
		self.nibs = mergeLists(self.nibs, other.nibs)
		self.outlets = mergeLists(self.outlets, other.outlets)
		self.actions = mergeLists(self.actions, other.actions)

	def __cmp__(self, other):
		s = [getattr(self, x) for x in self.__slots__]
		o = [getattr(other, x) for x in self.__slots__]
		return cmp(s, o)


class NibInfo(object):

	def __init__(self):
		self.classes = {}

	def keys(self):
		return self.classes.keys()

	def len(self):
		return len(self.classes)

	def __iter__(self):
		return iter(self.classes)

	def __getitem__(self, name):
		return self.classes[name]

	def get(self, name, default=None):
		return self.classes.get(name, default)

	def loadClassesForNib(self, nibPath):
		nibName = os.path.basename(nibPath)
		nibInfo = NSDictionary.dictionaryWithContentsOfFile_(
				os.path.join(nibPath, 'classes.nib'))
		if nibInfo is None:
			raise NibLoaderError, "Invalid NIB file [%s]" % nibPath
		if not nibInfo.has_key('IBVersion'):
			raise NibLoaderError, "Invalid NIB info"
		if nibInfo['IBVersion'] != '1':
			raise NibLoaderError, "Unsupported NIB version"
		for rawClsInfo in nibInfo['IBClasses']:
			self._addClass(nibName, rawClsInfo)

	def loadClassesForNibFromBundle(self, nibName, sourceBundle=None):
		if not sourceBundle:
			sourceBundle = NSBundle.mainBundle()

		if nibName[-4:] == '.nib':
			nibPath = sourceBundle.pathForResource_ofType_(nibName, None)
		else:
			nibPath = sourceBundle.pathForResource_ofType_(nibName, 'nib')

		if not nibPath:
			raise NibLoaderError, ("Could not find nib named '%s' "
					"in bundle '%s'" % (nibName, sourceBundle))
		self.loadClassesForNib(nibPath)

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
		clsInfo = self.classes.get(name)
		if clsInfo is None:
			raise NibLoaderError, ("No class named '%s' found in "
					"nibs" % name)

		try:
			superClass = objc.lookup_class(clsInfo.super)
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
				methods[a] = _actionStub

		return metaClass(name, bases, methods)

	def printTemplate(self, file=None):
		if file is None:
			file = sys.stdout
		writer = IndentWriter(file)
		self._printTemplateHeader(writer)
		
		classes = self.classes.values()
		classes.sort()  # see ClassInfo.__cmp__
		for clsInfo in classes:
			classExists = 1
			if _classExists(clsInfo.super):
				self._printClass(writer, clsInfo)
			else:
				writer.writeln("if 0:")
				writer.indent()
				writer.writeln("# *** base class not found: %s" % clsInfo.super)
				self._printClass(writer, clsInfo)
				writer.dedent()

	def _printTemplateHeader(self, writer):
		frameworks = {}
		for clsInfo in self.classes.values():
			super = clsInfo.super
			framework = self._frameworkForClass(super)
			if not framework:
				continue  # don't know what to do
			try:
				frameworks[framework].append(super)
			except KeyError:
				frameworks[framework] = [super]
		
		items = frameworks.items()
		if items:
			items.sort()
			for framework, classes in items:
				classes.sort()
				writer.writeln("from %s import %s" % (framework, ", ".join(classes)))
		writer.writeln("from AppKit.NibLoader import AutoBaseClass")
		writer.writeln()
		writer.writeln()

	def _printClass(self, writer, clsInfo):
			nibs = clsInfo.nibs
			if len(nibs) > 1:
				nibs[-2] = nibs[-2] + " and " + nibs[-1]
				del nibs[-1]
			nibs = ", ".join(nibs)
			writer.writeln("# class defined in %s" % nibs)
			writer.writeln("class %s(AutoBaseClass):" % clsInfo.name)
			writer.indent()
			writer.writeln("# the actual base class is %s" % clsInfo.super)
			outlets = clsInfo.outlets
			actions = clsInfo.actions
			if not actions:
				writer.writeln("pass")
				writer.writeln()
			else:
				writer.writeln()
				if outlets:
					writer.writeln("# The following outlets are added to the class:")
					outlets.sort()
					for o in outlets:
						#writer.writeln("# %s" % o)
						writer.writeln("%s = ivar('%s')" % (o, o))
					writer.writeln()
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

	def _frameworkForClass(self, className):
		"""Return the name of the framework containing the class."""
		try:
			cls = objc.lookup_class(className)
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
	try:
		objc.lookup_class(className)
	except objc.error:
		return 0
	else:
		return 1

def _actionStub(self, sender): pass


class IndentWriter:

	def __init__(self, file=None, indentString="\t"):
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


class NibClassBuilder(type):
	
	def _newSubclass(cls, name, bases, methods):
		# Constructor for AutoBaseClass: create an actual
		# instance that can be subclassed to invoke the
		# magic behavior.
		return type.__new__(cls, name, bases, methods)
	_newSubclass = classmethod(_newSubclass)
	
	def __new__(cls, name, bases, methods):
		# __new__ would normally create a subclass of cls, but
		# instead we create a completely different class.
		if bases and bases[0].__class__ is cls:
			bases = bases[1:]
		return _nibInfo.makeClass(name, bases, methods)


# AutoBaseClass is a class that has NibClassBuilder is its' metaclass.
# This means that if you subclass from AutoBaseClass, NibClassBuilder
# will be used to create the new "subclass". This will however _not_
# be a real subclass of AutoBaseClass, but rather a subclass of the
# Cocoa class specified in the nib.
AutoBaseClass = NibClassBuilder._newSubclass("AutoBaseClass", (), {})


_nibInfo = NibInfo()

loadClassesForNib =  _nibInfo.loadClassesForNib
loadClassesForNibFromBundle =  _nibInfo.loadClassesForNibFromBundle


#
# The rest of this file is a simple command line tool.
#

commandline_doc = """\
NibLoader.py [-th] nib1 [...nibN]
  Print an overview of the classes found in the nib file(s) specified,
  listing their superclass, actions and outlets as Python source. This
  output can be used as a template or a stub.
  -t Instead of printing the overview, perform a simple test.
  -h Print this text."""

def usage(msg, code):
	if msg:
		print msg
	print commandline_doc
	sys.exit(code)

def test(nibFiles):
	for nibPath in nibFiles:
		print "Loading", nibPath
		loadClassesForNib(nibPath)
	print
	classNames = _nibInfo.keys()
	classNames.sort()
	for className in classNames:
		try:
			# instantiate class, equivalent to
			# class %(className):
			#     __metaclass__ = NibClassBuilder
#			cls = NibClassBuilder(className, (), {})
			cls = type(className, (AutoBaseClass,), {})
		except NibLoaderError, why:
			print "*** Failed class: %s; NibLoaderError: %s" % (
					className, why[0])
		else:
			print "Created class: %s, superclass: %s" % (cls.__name__,
					cls.__bases__[0].__name__)

def printTemplate(nibFiles):
	info = NibInfo()
	for nibPath in nibFiles:
		info.loadClassesForNib(nibPath)
	info.printTemplate()

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
		test(nibFiles)
	else:
		printTemplate(nibFiles)


if __name__ == "__main__":
	commandline()
