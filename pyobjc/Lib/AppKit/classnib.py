"""
This module contains functions and classes for dealing with the classes.nib
file in a NIB 'file'.

Usage for this module:
	NIBFILE1 = "MainMenu.nib"
	NIBFILE2 = "DocumentWindow.nib"

	info1 = parse_classes_nib(NIBFILE1)
	info2 = parse_classes_nib(NIBFILE2)
	fp = open('nibclasses.py', 'w')
	generate_wrapper_module(fp, [info1, info2])

Using the generated module:
	import nibclasses

	class MyNibDefinedClass (nibclasses.MyNibDefinedClassBase):
		def someAction_(self, sender):
			pass


The generated module contains base-classes for all classes defined in the
NIB file. The base class serves as documentation for the list of methods
that need to be implemented in subclasses, as wel as a way to avoid working
with explicit method signatures.
"""
#
#An example classes.nib:
#{
#    IBClasses = (
#        {CLASS = FirstResponder; LANGUAGE = ObjC; SUPERCLASS = NSObject; },
#        {
#            ACTIONS = {nextImage = id; };
#            CLASS = PyModel;
#            LANGUAGE = ObjC;
#            OUTLETS = {Image = id; nextButton = id; };
#            SUPERCLASS = NSObject;
#        }
#    );
#    IBVersion = 1;
#}
#
import sys


def parse_classes_nib(nibfile):
	"""
	Parse a classes.nib file inside a NIB file. Returns a list of
	class information.
	"""
	import os
	d = NSDictionary.dictionaryWithContentsOfFile_(
		os.path.join(nibfile, 'classes.nib'))

	if not d:
		raise ValueError, "Invalid or non-existing NIB: %s"%nibfile
	return d

def generate_wrapper_module(outfp, classinfolist):
	"""
	Generate the wrapper module given the class data in one or more
	NIB files.
	"""
	generator = ClassNibGenerator(outfp)
	for n in classinfolist:
		generator.add_classnib(n)
	generator.generate()


#
#
# Beyond this are classes and functions used to implement the public functions,
# all of which are defined above here.
#
#

import objc

NSBundle = objc.lookup_class('NSBundle')
NSDictionary = objc.lookup_class('NSDictionary')

def _mergelists(l1, l2):
	r = {}
	for i in l1:
		r[i] = 1
	for i in l2:
		r[i] = 1
	return r.keys()

class ClassNibGenerator:
	"""
	Class for generating a python module containing the utility classes 
	needed to use the NIB file. For every class X in the classes.nib we
	generate class 'XBase'. The user is supposed to subclass 'X' from this
	class.
	"""
	def __init__(self, fp):
		self._fp = fp
		self._didGenerate = 0
		self._classes = []
	
	def add_classnib(self, nibinfo):
		if not nibinfo.has_key('IBVersion'):
			raise ValueError, "Invalid NIB info"
		if nibinfo['IBVersion'] != '1':
			raise ValueError, "Unsupported NIB version"

		self._classes.extend(nibinfo['IBClasses'])

	def generate(self):
		assert not self._didGenerate

		self._unique_classes()
		self._generate_header()

		for cls in self._classes:
			if cls['CLASS'] == 'FirstResponder':
				# This is special, ignore
				continue

			self._generate_class(cls)

	def _frameworkForClass(self, clsname):
		"""
		Return framework containing the class, as a python package.
		"""
		cls = objc.lookup_class(clsname)

		path = NSBundle.bundleForClass_(cls).bundlePath()
		if path == '/System/Library/Frameworks/Foundation.framework':
			return 'Foundation'
		elif path == '/System/Library/Frameworks/AppKit.framework':
			return 'AppKit'
		else:
			return ''

		
	def _generate_header(self):
		"""
		Generate header of the sub-module. 
		TODO: Import the right modules, even if some of the superclasses
		are in 'foreign' frameworks
		"""
		frameworks = {}

		for cls in self._classes:
			try:
				frameworks[self._frameworkForClass(cls['SUPERCLASS'])].append(cls['SUPERCLASS'])
			except KeyError:
				frameworks[self._frameworkForClass(cls['SUPERCLASS'])] = [cls['SUPERCLASS']]
			except objc.error:
				continue

		self._fp.write("# THIS FILE IS GENERATED. DO NOT EDIT!!!\n")
		self._fp.write("# Interface classes for using NIB files\n")
		self._fp.write("\n")
		self._fp.write("from objc import IBOutlet\n")
		for pkg in frameworks.keys():
			self._fp.write('from %s import %s\n'%(
				pkg, ', '.join(_mergelists(frameworks[pkg],()))))
		self._fp.write('\n')			



	def _unique_classes(self):
		"""
		Merge the class-lists from the various classnibs. It should
		be possible to define the same class in multiple nibs, as long
		as they are consistent enough.
		"""
		clsdict = {}
		for cls in self._classes:
			nm = cls['CLASS']
			if not clsdict.has_key(nm):
				clsdict[nm] = cls
			else:
				curcls = clsdict[nm]
				curcls['OUTLETS'] = _mergelists(
					curcls.get('OUTLETS', ()),
					cls.get('OUTLETS', ()))
				curcls['ACTIONS'] = _mergelists(
					curcls.get('ACTIONS', ()),
					cls.get('ACTIONS', ()))
				if curcls['SUPERCLASS'] != cls['SUPERCLASS']:
					raise ValueError, \
						"Incompatible superclass for %s"%nm
		self._classes = clsdict.values()	

	def _generate_class(self, classinfo):
		"""
		Generate a python class for a class description in the NIBInfo

		Fields in the classinfo:
		{
			'OUTLETS': {'Image': 'id', 'nextButton': 'id'}, 
			'SUPERCLASS': 'NSObject', 
			'CLASS': 'PyModel', 
			'ACTIONS': {'nextImage': 'id'}, 
			'LANGUAGE': 'ObjC'
		}
		"""
		if classinfo['LANGUAGE'] != 'ObjC':
			raise ValueError, 'Classes.nib not for Objective-C'

		clsname = classinfo['CLASS']
		supername = classinfo['SUPERCLASS']
		actions = classinfo.get('ACTIONS', ())
		outlets = classinfo.get('OUTLETS', ())
		try:
			fw = self._frameworkForClass(supername)
		except objc.error:
			sys.stderr.write(
				'WARN: Skipping %s: no superclass %s\n'%(
					clsname, supername))
			return

		#if fw:
		#	supername = '%s.%s'%(fw, supername)
	
		self._fp.write('class %sBase (%s):\n'%(clsname, supername))
		self._fp.write('\t"Base class for class \'%s\'"\n'%clsname)
		if not actions and not outlets:
			self._fp.write('\tpass\n')
	
		if outlets:
			for o in outlets.keys():
				# Might want to check type (outlets[o])
				self._fp.write('\t%s = IBOutlet("%s")\n'%(o, o))

		if outlets:
			self._fp.write('\n')

		if actions:
			for a in actions.keys():
				self._fp.write('\tdef %s_(self, sender): pass\n\n'%a)

		self._fp.write('\n')



if __name__ == '__main__':
	import sys
	classinfo = parse_classes_nib('English.lproj/MainMenu.nib')
	generate_wrapper_module(sys.stdout, [classinfo])
