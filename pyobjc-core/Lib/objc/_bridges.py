from objc._objc import *
from objc import _objc
import struct
import sys
import collections

__all__ = [ 'registerListType', 'registerMappingType' ]

def registerListType(type):
    """
    Register 'type' as a list-like type that will be proxied
    as an NSMutableArray subclass.
    """
    OC_PythonArray = lookUpClass('OC_PythonArray')
    OC_PythonArray.depythonifyTable().append(type)

def registerMappingType(type):
    """
    Register 'type' as a list-like type that will be proxied
    as an NSMutableArray subclass.
    """
    OC_PythonDictionary = lookUpClass('OC_PythonDictionary')
    OC_PythonDictionary.depythonifyTable().append(type)


registerListType(xrange if sys.version_info[0] == 2 else range)

registerListType(collections.Sequence)
registerMappingType(collections.Mapping)
