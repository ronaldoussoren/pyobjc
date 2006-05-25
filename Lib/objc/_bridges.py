from _objc import *

__all__ = []

BRIDGED_STRUCTURES = {}
BRIDGED_TYPES = []

try:
    from array import array
    from Carbon.File import FSRef, FSSpec
except ImportError:
    pass
else:
    def struct_to_FSRef(s):
        return FSRef(rawdata=array('B', s[0]).tostring())
    BRIDGED_STRUCTURES['{FSRef=[80C]}'] = struct_to_FSRef

    def FSRef_to_struct(fsRef):
        return (tuple(array('B').fromstring(fsRef.data)),)
    BRIDGED_TYPES.append((FSRef, FSRef_to_struct))

    def struct_to_FSRef(s):
        return FSRef(rawdata=array('B', s[0]).tostring())
    BRIDGED_STRUCTURES['{FSRef=[80C]}'] = struct_to_FSRef

    def FSSpec_to_struct(fsSpec):
        return (tuple(array('B').fromstring(fsSpec.data)),)
    BRIDGED_TYPES.append((FSSpec, FSSpec_to_struct))

def _bridgePythonTypes():
    # python TO Obj-C
    OC_PythonObject = lookUpClass('OC_PythonObject')
    if BRIDGED_TYPES:
        OC_PythonObject.depythonifyTable().extend(BRIDGED_TYPES)
    if BRIDGED_STRUCTURES:
        OC_PythonObject.pythonifyStructTable().update(BRIDGED_STRUCTURES)
    
_bridgePythonTypes()
