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


__all__ = ["NibClassBuilder", "loadClassesForNib", "loadClassesForNibFromBundle", "NibInfo"]


NSDictionary = objc.lookup_class("NSDictionary")
NSObject = objc.lookup_class("NSObject")
NSBundle = objc.lookup_class("NSBundle")


class NibLoaderError(Exception): pass


class ClassInfo:

	__slots__ = ("nib", "name", "super", "actions", "outlets")

	def merge(self, other):
		assert self.name == other.name
		if self.super != other.super:
			raise NibLoaderError, \
					"Incompatible superclass for %s" % self.name
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
		clsInfo.nib = nibName
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

	def printOverview(self, file=None):
		classes = self.classes.values()
		classes.sort()  # see ClassInfo.__cmp__
		nib = None
		INDENT = "   "
		for clsInfo in classes:
			if nib != clsInfo.nib:
				if nib:
					print >>file
				nib = clsInfo.nib
				print >>file, "%s:" % nib
			print >>file, INDENT + "%s(%s):" % (clsInfo.name, clsInfo.super)
			for attrName in ["actions", "outlets"]:
				attrs = getattr(clsInfo, attrName)
				label = attrName.capitalize()
				attrs.sort()
				print >>file, 2 * INDENT + "%s:" % label
				if not attrs:
					print >>file, 3 * INDENT + "<none>"
				else:
					for name in attrs:
						print >>file, 3 * INDENT + name


def _actionStub(self, sender): pass


def mergeLists(l1, l2):
	r = {}
	for i in l1:
		r[i] = 1
	for i in l2:
		r[i] = 1
	return r.keys()


class NibClassBuilder(type):
	def __new__(cls, name, bases, methods):
		return _nibInfo.makeClass(name, bases, methods)

_nibInfo = NibInfo()

loadClassesForNib =  _nibInfo.loadClassesForNib
loadClassesForNibFromBundle =  _nibInfo.loadClassesForNibFromBundle


#
# The rest of this file is a simple command line tool.
#

commandline_doc = """\
NibLoader.py [-th] nib1 [...nibN]
  Print an overview of the classes found in the nib file(s) specified,
  listing their superclass, actions and outlets.
  -t Instead of printing the overvies, perform a simple test.
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
			cls = NibClassBuilder(className, (), {})
		except NibLoaderError, why:
			print "*** Failed class: %s; NibLoaderError: %s" % (
					className, why[0])
		else:
			print "Created class: %s, superclass: %s" % (cls.__name__,
					cls.__bases__[0].__name__)

def printOverview(nibFiles):
	for nibPath in nibFiles:
		info = NibInfo()
		info.loadClassesForNib(nibPath)
		info.printOverview()
		print

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
		printOverview(nibFiles)


if __name__ == "__main__":
	commandline()
