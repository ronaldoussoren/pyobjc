import sys
import objc
import pprint

from Foundation import *

input = { 'a' : [1, 2, 3, 4], 'b' : 'c', 'd' : 3, 'e' : None, 'f' : [1, {2 : 3, 'a' : 'b'}, [3, 4]], 'g' : {'h' : 'i'}, 'j' : (1, 2, 3, 'k', 'l')}

print "Converting (Python Collection):"
pprint.pprint(input)

from types import *
def convertPyContainerToObjCContainer(aPyContainer):
    containerType = type(aPyContainer)
    if containerType == DictType:
        collection = NSMutableDictionary.dictionary()
        for aKey in aPyContainer:
            convertedValue = convertPyContainerToObjCContainer( aPyContainer[aKey] )
            collection.setObject_forKey_( convertedValue , aKey )
        return collection
    elif containerType in [TupleType, ListType]:
        collection = NSMutableArray.array()
        for aValue in aPyContainer:
            convertedValue = convertPyContainerToObjCContainer( aValue )
            collection.addObject_( convertedValue  )
        return collection
    elif containerType in StringTypes:
        return aPyContainer # bridge will convert to NSString
    elif containerType == IntType:
        return NSNumber.numberWithInt_( aPyContainer )
    elif containerType == LongType:
        return NSNumber.numberWithLong_( aPyContainer )
    elif containerType == FloatType:
        return NSNumber.numberWithFloat_( aPyContainer )
    elif containerType == NoneType:
        return NSNull.null()
    else:
        raise "UnrecognizedTypeException", "Type %s encountered in python collection;  don't know how to convert." % containerType

convertedCollection = convertPyContainerToObjCContainer(input)

print
print
print "Converted (ObjC collection):"
print "%s" % convertedCollection.description()


