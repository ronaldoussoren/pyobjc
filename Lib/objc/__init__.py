"""
new-style pyobjc
"""
from _objc import *
from _objc import __version__



# Import values used to define signatures
import _objc
gl = globals()
for nm in [ x for x in dir(_objc) if x.startswith('_C_') ]:
	gl[nm] = getattr(_objc, nm)
del gl, nm, _objc




#
# Administration of methods that transfer ownership of objects to the
# caller. This list is used by the runtime to automaticly correct the
# refcount to the object.
#
# These must be set before any proxy classes are created.
#
# These 5 are documented in Apple's Objective-C book, in theory these
# are the only methods that transfer ownership.
ALLOCATOR_METHODS['alloc'] = 1
ALLOCATOR_METHODS['allocWithZone:'] = 1
ALLOCATOR_METHODS['copy'] = 1
ALLOCATOR_METHODS['copyWithZone:'] = 1
ALLOCATOR_METHODS['mutableCopyWithZone:'] = 1



# Add usefull utility functions below


class _runtime:
	"""
	Backward compatibility interface.
	"""
	def __getattr__(self, name):
		if name == '__objc_classes__':
			return class_list()
		elif name == '__kind__':
			return 'python'

		return lookup_class(name)

	def __eq__(self, other):
		if self is other:
			return 1
		return 0

	def __repr__(self):
		return "objc.runtime"
runtime = _runtime()

# Outlets in Interface Builder are instance variables
IBOutlet = ivar

# Signature for an action in Interface Builder
def IBAction(func):
	return selector(func, signature="v@:@")

# Aliases for Objective-C lovers...
YES=1
NO=0
nil=None

import _convenience

# Some special modules needed to correctly wrap all
# methods in the Foundation framework. Doing it here
# is ugly, but it is also something that would be very
# hard to avoid...
try:
	import _FoundationSignatures
	del _FoundationSignatures
except ImportError:
	pass

try:
	import _FoundationMapping
	del _FoundationMapping
except ImportError:
	pass

# This is a hack, should probably patch python:
# - We want the resources directory to be on the python search-path
# - It must be at the start of the path
# - The CWD must not be on the path
b = lookup_class('NSBundle').mainBundle()
if b:
	import sys
	sys.path.insert(0, '%s/Contents/Resources'%str(b.bundlePath()))
	try:
		del sys.path[sys.path.index('')]
	except ValueError:
		pass
	del sys
del b

