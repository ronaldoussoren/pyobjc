#!/usr/bin/env python

# This scripts extracts the method signatures that seem to contain 
# pass-by-reference arguments. The test for this is fairly crude and there are
# some false positives (mostly return values, but also some pointers in 
# structures)
#
# The output contains two signature fields: One containing the actual signature,
# and one is reserved for user-defined overrides. The script 
# create_byref_module.py uses this second field to define signature overrides.
# 
import sys
import objc

if len(sys.argv) != 3:
	print "Usage: extract_byref_signatures.py framework storage"
	sys.exit(1)

try:
	existing = {}
	for cls, sel, real_sign, repl_sign in [
			ln.strip().split(ln[0])[1:] 
				for ln in file(sys.argv[2]).readlines()
		]:

		if not existing.has_key(cls):
			existing[cls] = {}
		existing[cls][sel] = (real_sign, repl_sign)

	def find_existing(cls, selector):
		try:
			v = existing[cls.__name__][selector]
			return (cls.__name__, selector, v[0], v[1])
		except KeyError:
			return None
except:
	def find_existing(cls, selector) :
		return None



NSBundle = objc.lookup_class('NSBundle')

def load_bundle(path):
        NSBundle.bundleWithPath_(path).load()
	classes = [ cls 
		for  cls in objc.class_list()
		if path == NSBundle.bundleForClass_(cls).bundlePath() ]
	return classes
classes = load_bundle(sys.argv[1])

result = []
for cls in classes:
	for key in dir(cls):
		# Getattr for a objective-C instance variable will raise an
		# exception when the first argument is an objective-C class.
		try:
			value = getattr(cls, key)
		except:
			continue



		if isinstance(value, objc.selector):
			prev_item = find_existing(cls, value.selector)

			# Check if the super-class already defines this method,
			# no need to redefine the signature twice.
			try:
				getattr(super(cls, cls), key)
				if prev_item:
					sys.stderr.write("DROPPING %s - %s\n"%(cls.__name__, value.selector))
				continue
			except:
				pass

			if '^' in value.signature:
				if prev_item:
					if prev_item[2] != value.signature:
						sys.stderr.write("WARNING: Signature for %s - %s changed\n"%(cls.__name__, value.selector))
					translated = prev_item[-1]
				else:
					sys.stderr.write('NEW: %s - %s\n'%(cls.__name__, value.selector))
					translated = ''

				result.append(",%s,%s,%s,%s"%(cls.__name__, 
					value.selector, 
					value.signature, 
					translated))
			else:
				if prev_item:
					sys.stderr.write("DROPPING %s - %s\n"%(cls.__name__, value.selector))
fp = open(sys.argv[2], 'w')
fp.write('\n'.join(result))
if result:
	fp.write('\n')

sys.stderr.write('DONE %d signatures\n'% len(result))
