from _objc import *
import _objc
import struct

__all__ = [ 'registerListType', 'registerMappingType' ]

BRIDGED_STRUCTURES = {}
BRIDGED_STRUCTURES2 = {}
BRIDGED_TYPES = []

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


def _bridgePythonTypes():
    # Python to Obj-C
    OC_PythonObject = lookUpClass('OC_PythonObject')
    try:
        if BRIDGED_TYPES:
            OC_PythonObject.depythonifyTable().extend(BRIDGED_TYPES)
        if BRIDGED_STRUCTURES:
            OC_PythonObject.pythonifyStructTable().update(BRIDGED_STRUCTURES)
    except AttributeError:
        pass

_bridgePythonTypes()
