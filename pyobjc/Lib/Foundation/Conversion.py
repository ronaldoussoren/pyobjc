#!/usr/bin/env python

"""Conversion.py -- Tools for converting between Python and Objective-C objects.

Conversion offers API to convert between Python and Objective-C instances of various classes.   Currently, the focus is on Python and Objective-C collections.
"""

from Foundation import *
from types import *

def propertyListFromPythonCollection(aPyCollection, conversionHelper=None):
    """Convert a Python collection (dictionary, array, tuple, string) into an Objective-C collection.

    If conversionHelper is defined, it must be a callable.  It will be called for any object encountered for which propertyListFromPythonCollection() cannot automatically convert the object.   The supplied helper function should convert the object and return the converted form.  If the conversion helper cannot convert the type, it should raise an exception or return None.
    """
    containerType = type(aPyCollection)
    if containerType == DictType:
        collection = NSMutableDictionary.dictionary()
        for aKey in aPyCollection:
            convertedValue = propertyListFromPythonCollection( aPyCollection[aKey], conversionHelper=conversionHelper )
            if convertedValue is not None:
                collection.setObject_forKey_( convertedValue , aKey )
        return collection
    elif containerType in [TupleType, ListType]:
        collection = NSMutableArray.array()
        for aValue in aPyCollection:
            convertedValue = propertyListFromPythonCollection( aValue, conversionHelper=conversionHelper )
            if convertedValue is not None:
                collection.addObject_( convertedValue  )
        return collection
    elif containerType in StringTypes:
        return aPyCollection # bridge will convert to NSString
    elif containerType == IntType:
        return NSNumber.numberWithInt_( aPyCollection )
    elif containerType == LongType:
        return NSNumber.numberWithLong_( aPyCollection )
    elif containerType == FloatType:
        return NSNumber.numberWithFloat_( aPyCollection )
    elif containerType == NoneType:
        return NSNull.null()
    else:
        if conversionHelper:
            return conversionHelper(aPyCollection)
    raise TypeError, "Type '%s' encountered in python collection;  don't know how to convert." % containerType

def pythonCollectionFromPropertyList(aCollection, conversionHelper=None):
    """Converts a Foundation based collection-- a property list-- into a Python collection.

    Like propertyListFromPythonCollection(), conversionHelper is an optional callable that will be invoked any time an encountered object cannot be converted.
    """
    if isinstance(aCollection, NSDictionary):
        pyCollection = {}
        for k in aCollection:
            convertedValue = pythonCollectionFromPropertyList(aCollection[k], conversionHelper)
            pyCollection[k] = convertedValue
        return pyCollection
    elif isinstance(aCollection, NSArray):
        pyCollection = [] * len(aCollection)
        for i in range(len(aCollection)):
            convertedValue = pythonCollectionFromPropertyList(aCollection[i], conversionHelper)
            pyCollection.append(convertedValue)
        return pyCollection
    elif isinstance(aCollection, NSNumber):
        objCType = aCollection.objCType()
        if objCType is 'c': return aCollection.charValue()
        elif objCType is 'C': return aCollection.charValue()
        elif objCType is 's': return aCollection.shortValue()
        elif objCType is 'S': return aCollection.unsignedShortValue()
        elif objCType is 'i': return aCollection.intValue()
        elif objCType is 'I': return aCollection.unsignedIntValue()
        elif objCType is 'l': return aCollection.longValue()
        elif objCType is 'L': return aCollection.unsignedLongValue()
        elif objCType is 'f': return aCollection.floatValue()
        elif objCType is 'd': return aCollection.doubleValue()
        elif objCType is 'b': return aCollection.boolValue()
        elif objCType is 'q': return aCollection.longLongValue()
        raise TypeError, "Type '%s' encountered within an instance of the NSValue class." % type(objCType)
    elif type(aCollection) in StringTypes:
        return aCollection
    elif type(aCollection) in (IntType, LongType, FloatType):
        return aCollection
    else:
        if conversionHelper:
            return conversionHelper(aCollection)
    raise TypeError, "Type '%s' encountered in ObjC collection;  don't know how to convert." % type(aCollection)
