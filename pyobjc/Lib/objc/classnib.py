"""
This module contains functions and classes for dealing with the classes.nib
file in a NIB 'file'.

def parse_classes_nib(nibfile):
	Parse the classes.nib file inside the given NIB file.

def generate_wrapper_module(outfp, classinfolist):
	Generate the wrapper module given the class data in one or more
	NIB files.


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


def parse_classes_nib(nibfile):
	"""
	Parse a classes.nib file inside a NIB file.
	"""
	import os
	return ClassNibParser(
		open(os.path.join(nibfile, 'classes.nib'))).parse()

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

class Tokenizer:
	"""
	A simple lexer for classes.nib files. This more or less assumes valid 
	input, which should be pretty safe as the classes.nib is machine
	generated.

	There are two types of tokens: Some special characters and strings of
	alphanumeric characters. There is optional whitespace between tokens.
	"""

	def __init__(self, fp):
		self.buf = fp.read()

	def nextToken(self):
		while self.buf and self.buf[0].isspace():
			self.buf = self.buf[1:]

		if not self.buf:
			return None

		if self.buf[0] in '(){};=,':
			res = self.buf[0]
			self.buf = self.buf[1:]
		else:
			if not self.buf[0].isalnum():
				raise ValueError, "Token error: "+self.buf[0]
			res = ''
			while self.buf[0] and self.buf[0].isalnum():
				res += self.buf[0]
				self.buf = self.buf[1:]
		return res


class ClassNibParser:
	"""
	This class is used to parse a 'classes.nib' file. It returns a python
	datastructure that corresponds with the contents of the file.

	The only public entry points in this class are the contructor and
	the parse method.
	"""

	def __init__(self, fp):
		self._tokenizer = Tokenizer(fp)
		self._value = None

	def _parse_dict(self):
		# '{' (KEY = VALUE ';')* '}'
		# The leading '{' is already consumed.

		result = {}

		token = self._tokenizer.nextToken()
		if token == '}':
			return res

		while 1:
			if not token[0].isalnum():
				raise ValueError, "Bad dictionary: " + token
			key = token

			token = self._tokenizer.nextToken()
			if token != '=':
				raise ValueError, "Bad dictionary"

			token = self._tokenizer.nextToken()
			if token == '{':
				value = self._parse_dict()
			elif token == '(':
				value = self._parse_tuple()
			elif token[0].isalnum():
				value = token
			else:
				raise ValueError, "Bad dictionary"

			token = self._tokenizer.nextToken()
			if token != ';':
				raise ValueError, "Missing ';'"

			result[key] = value

			token = self._tokenizer.nextToken()
			if token == '}':
				break

		return result

	def _parse_tuple(self):
		# '(' (VALUE ',')* ')'
		# The leading '(' is already consumed.

		result = []

		token = self._tokenizer.nextToken()
		if token == ')':
			return tuple(result)

		while 1:
			if token == '{':
				value = self._parse_dict()
			elif token == '(':
				value = self._parse_tuple()
			else:
				value = token

			result.append(value)

			token = self._tokenizer.nextToken()
			if token == ',':
				pass
			elif token == ')':
				break
			else:
				raise ValueError, "Missing ','"

			token = self._tokenizer.nextToken()

		return tuple(result)


	def parse(self):
		"""
		Parse the file. Can safely be called multiple times.
		"""
		if not self._value:
			token = self._tokenizer.nextToken()
			if token != '{':
				raise ValueError, "Not a classes.nib?"
			self._value = self._parse_dict()
		return self._value

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
		self._didGenerate = False
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
		fw = self._frameworkForClass(supername)
		if fw:
			supername = '%s.%s'%(fw, supername)
	
		self._fp.write('class %sBase (%s):\n'%(clsname, supername))
		self._fp.write('\t"Base class for class \'%s\'"\n'%clsname)
		if not actions and not outlets:
			self._fp.write('\tpass\n')
	
		for o in outlets:
			self._fp.write('\t%s = IBOutlet("%s")\n'%(o, o))
		if outlets:
			self._fp.write('\n')

		for a in actions:
			self._fp.write('\tdef %s_(self, sender): pass\n\n'%a)

		self._fp.write('\n')



if __name__ == '__main__':
	import sys
	classinfo = parse_classes_nib('English.lproj/MainMenu.nib')
	generate_wrapper_module(sys.stdout, [classinfo])
