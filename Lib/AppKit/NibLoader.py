#!/usr/bin/env python


import os
import objc


NSDictionary = objc.lookup_class("NSDictionary")
NSObject = objc.lookup_class("NSObject")
NSBundle = objc.lookup_class("NSBundle")

class NibLoaderError(Exception): pass


class _NibClassBuilder(object):

	def __init__(self):
		self._classes = {}
	
	def addNib(self, nibPath):
		nibInfo = NSDictionary.dictionaryWithContentsOfFile_(
				os.path.join(nibPath, 'classes.nib'))
		if nibInfo is None:
			raise NibLoaderError, "Invalid NIB file [%s]" % nibPath
		if not nibInfo.has_key('IBVersion'):
			raise NibLoaderError, "Invalid NIB info"
		if nibInfo['IBVersion'] != '1':
			raise NibLoaderError, "Unsupported NIB version"
		classes = self._classes
		for classInfo in nibInfo['IBClasses']:
			self._addClass(classInfo)
	
	def _addClass(self, classInfo):
		classes = self._classes
		name = classInfo['CLASS']
		if name == "FirstResponder": return
		if not classes.has_key(name):
			classes[name] = classInfo
		else:
			curcls = classes[name]
			curcls['OUTLETS'] = _mergelists(
				curcls.get('OUTLETS', ()),
				classInfo.get('OUTLETS', ()))
			curcls['ACTIONS'] = _mergelists(
				curcls.get('ACTIONS', ()),
				classInfo.get('ACTIONS', ()))
			if curcls['SUPERCLASS'] != classInfo['SUPERCLASS']:
				raise NibLoaderError, \
					"Incompatible superclass for %s" % name
	
	def makeClass(self, name, bases, methods):
		classInfo = self._classes.get(name)
		if classInfo is None:
			raise NibLoaderError, ("No class named '%s' found in "
					"nibs" % name)
		superName = classInfo['SUPERCLASS']
		actions = classInfo.get('ACTIONS', {})
		outlets = classInfo.get('OUTLETS', {})
		
		try:
			superClass = objc.lookup_class(superName)
		except objc.nosuchclass_error:
			raise NibLoaderError, ("Superclass '%s' for '%s' not "
					"found." % (superName, name))
		bases = (superClass,) + bases
		metaClass = superClass.__class__
		
		if hasattr(outlets, "keys"):
			outlets = outlets.keys()
		for o in outlets:
			if not methods.has_key(o):
				methods[o] = objc.IBOutlet(o)

		if hasattr(actions, "keys"):
			actions = actions.keys()
		for a in actions:
			a = a + "_"
			if not methods.has_key(a):
				methods[a] = _dummyAction
		
		return metaClass(name, bases, methods)


def _mergelists(l1, l2):
	r = {}
	for i in l1:
		r[i] = 1
	for i in l2:
		r[i] = 1
	return r.keys()

def _dummyAction(self, sender): pass


_nibClassBuilder = _NibClassBuilder()

addNib = _nibClassBuilder.addNib

def addNibFromBundle( nibName, sourceBundle = None ):
	if not sourceBundle:
		sourceBundle = NSBundle.mainBundle()

	if nibName[-4:] == '.nib':
		nibPath = sourceBundle.pathForResource_ofType_( nibName, None )
	else:
		nibPath = sourceBundle.pathForResource_ofType_( nibName, '.nib' )

	if not nibPath:
		raise NibLoaderError, "Could not find nib named '%s' in bundle '%s'" % ( nibName, sourceBundle )

	addNib( nibPath )


class _NibLoader(type):
	
	def __new__(meta, name, bases, methods):
		print "n: %s" % name
		if not bases:
			return type.__new__(meta, name, bases, methods)
		else:
			assert bases[0].__class__ is meta
			return _nibClassBuilder.makeClass(name, bases[1:], methods)


class NibLoader:
	__metaclass__ = _NibLoader


if __name__ == "__main__":
	import sys
	for nibPath in sys.argv[1:]:
		print "loading", nibPath
		addNib(nibPath)
	
	classNames = _nibClassBuilder._classes.keys()
	classNames.sort()
	for name in classNames:
		print "making test class for", name
		try:
			cls = type(name, (NibLoader,), {})
		except NibLoaderError, why:
			print "****** NibLoaderError", why[0]
		else:
			print "Class: %s, superclass: %s" % (cls, cls.__bases__[0])
		print
