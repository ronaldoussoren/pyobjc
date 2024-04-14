"""
No tests for CoreFoundation.CFPlugin: these API's are unsupported for the moment.
"""

import CoreFoundation
from PyObjCTools.TestSupport import TestCase

symbols = [
    # From CoreFoundation.CFPluginCOM.h:
    "IUnknownVTbl",
    "IS_ERROR",
    "HRESULT_CODE",
    "HRESULT_FACILITY",
    "SEVERITY_SUCCESS",
    "SEVERITY_ERROR",
    "MAKE_HRESULT",
    "S_OK",
    "S_FALSE",
    "E_UNEXPECTED",
    "E_NOTIMPL",
    "E_OUTOFMEMORY",
    "E_INVALIDARG",
    "E_NOINTERFACE",
    "E_POINTER",
    "E_HANDLE",
    "E_ABORT",
    "E_FAIL",
    "E_ACCESSDENIED",
    # From CoreFoundation.CFPlugin.h:
    "kCFPlugInDynamicRegistrationKey",
    "kCFPlugInDynamicRegisterFunctionKey",
    "kCFPlugInUnloadFunctionKey",
    "kCFPlugInFactoriesKey",
    "kCFPlugInTypesKey",
    "CFPlugInGetTypeID",
    "CFPlugInCreate",
    "CFPlugInGetBundle",
    "CFPlugInSetLoadOnDemand",
    "CFPlugInIsLoadOnDemand",
    "CFPlugInFindFactoriesForPlugInType",
    "CFPlugInFindFactoriesForPlugInTypeInPlugIn",
    "CFPlugInInstanceCreate",
    "CFPlugInRegisterFactoryFunction",
    "CFPlugInRegisterFactoryFunctionByName",
    "CFPlugInUnregisterFactory",
    "CFPlugInRegisterPlugInType",
    "CFPlugInUnregisterPlugInType",
    "CFPlugInAddInstanceForFactory",
    "CFPlugInRemoveInstanceForFactory",
    "CFPlugInInstanceGetInterfaceFunctionTable",
    "CFPlugInInstanceGetFactoryName",
    "CFPlugInInstanceGetInstanceData",
    "CFPlugInInstanceGetTypeID",
    "CFPlugInInstanceCreateWithInstanceDataSize",
]


class TestPluginNotSuppported(TestCase):
    def testUnsupported(self):
        for sym in symbols:
            with self.subTest(sym):
                if hasattr(CoreFoundation, sym):
                    self.fail(f"Unsupported symbol present: {sym}")
