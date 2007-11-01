import sys
import objc
import pprint

from Foundation import *
from PyObjCTools.Conversion import propertyListFromPythonCollection

input = { 'a' : [1, 2, 3, 4], 'b' : 'c', 'd' : 3, 'e' : None, 'f' : [1, {'2' : 3, 'a' : 'b'}, [3, 4]], 'g' : {'h' : 'i'}, 'j' : (1, 2, 3, 'k', 'l')}

print "Converting (Python Collection):"
pprint.pprint(input)

convertedCollection = propertyListFromPythonCollection(input)

print
print
print "Converted (ObjC collection):"
print "%s" % convertedCollection.description()
