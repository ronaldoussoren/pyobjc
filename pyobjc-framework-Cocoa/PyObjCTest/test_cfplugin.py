"""
No tests for CFPlugin: these API's are unsupported for the moment.
"""
from PyObjCTools.TestSupport import *
import CoreFoundation

symbols = [
        # From CFPluginCOM.h:
        'IUnknownVTbl',
        'IS_ERROR',
        'HRESULT_CODE',
        'HRESULT_FACILITY',
        'SEVERITY_SUCCESS',
        'SEVERITY_ERROR',
        'MAKE_HRESULT',
        'S_OK',
        'S_FALSE',
        'E_UNEXPECTED',
        'E_NOTIMPL',
        'E_OUTOFMEMORY',
        'E_INVALIDARG',
        'E_NOINTERFACE',
        'E_POINTER',
        'E_HANDLE',
        'E_ABORT',
        'E_FAIL',
        'E_ACCESSDENIED',

        # From CFPlugin.h:
        'kCFPlugInDynamicRegistrationKey',
        'kCFPlugInDynamicRegisterFunctionKey',
        'kCFPlugInUnloadFunctionKey',
        'kCFPlugInFactoriesKey',
        'kCFPlugInTypesKey',
        'CFPlugInGetTypeID',
        'CFPlugInCreate',
        'CFPlugInGetBundle',
        'CFPlugInSetLoadOnDemand',
        'CFPlugInIsLoadOnDemand',
        'CFPlugInFindFactoriesForPlugInType',
        'CFPlugInFindFactoriesForPlugInTypeInPlugIn',
        'CFPlugInInstanceCreate',
        'CFPlugInRegisterFactoryFunction',
        'CFPlugInRegisterFactoryFunctionByName',
        'CFPlugInUnregisterFactory',
        'CFPlugInRegisterPlugInType',
        'CFPlugInUnregisterPlugInType',
        'CFPlugInAddInstanceForFactory',
        'CFPlugInRemoveInstanceForFactory',
        'CFPlugInInstanceGetInterfaceFunctionTable',
        'CFPlugInInstanceGetFactoryName',
        'CFPlugInInstanceGetInstanceData',
        'CFPlugInInstanceGetTypeID',
        'CFPlugInInstanceCreateWithInstanceDataSize',
]

class  TestPluginNotSuppported( TestCase):
    def testUnsupported(self):
        for sym in symbols:
            if hasattr(CoreFoundation, sym):
                self.fail("Unsupported symbol present: %s"%(sym,))

if __name__ == "__main__":
    main()
