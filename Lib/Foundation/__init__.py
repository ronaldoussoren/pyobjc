import objc as _objc

from _Foundation import *

CLASSLIST=[
	"NSRecursiveLock",
	"NSintNumber",
	"NSRandomSpecifier",
	"NSFileURLHandle",
	"NSGetCommand",
	"NSPlaceholderValue",
	"NSCFDate",
	"NSCFData",
	"NSRelativeSpecifier",
	"NSCloneCommand",
	"NSCFDictionary__",
	"%NSCFSet",
	"NSAssertionHandler",
	"NSAppleEventManager",
	"%NSCFType",
	"NSMethodSignature",
	"Protocol",
	"NSScanner",
	"NSString",
	"%NSCFBoolean",
	"NSCountedSet",
	"_NSKeyForwardingSetBinding",
	"NSScriptObjectSpecifier",
	"NSTimer",
	"NSConditionLock",
	"NSNull__",
	"_NSSelectorSetBinding",
	"_NSUndoInvocation",
	"NSCFSet__",
	"NSWhoseSpecifier",
	"NSCFDictionary",
	"NSMutableAttributedString",
	"NSCFArray__",
	"NSKeyBinding",
	"NSMutableSet",
	"NSDate",
	"NSData",
	"NSAEDescriptorTranslator",
	"NSMutableStringProxyForMutableAttributedString",
	"NSMachPort__",
	"NSExpandedBuiltinCharacterSet",
	"NSLock",
	"NSMachBootstrapServer",
	"%NSCFArray",
	"NSBuiltinCharacterSet",
	"NSTimeZoneDetail",
	"NSTimeZone",
	"NSScriptCommandConstructionContext",
	"NSScriptSuiteRegistry",
	"%NSNull",
	"NSFileAttributes",
	"NSImmutableRangeCharacterSet",
	"NSunsignedLongLongNumber",
	"NSCFCharacterSet",
	"NSCondition",
	"NSLanguageContext",
	"NSThread",
	"NSlongLongNumber",
	"NSConcretePipe",
	"NSNotification",
	"NSValueDecoder",
	"NSSubrangeData",
	"NSCFArray",
	"NSMachPort",
	"NSMutableCharacterSet",
	"%NSMachPort",
	"NSArchiver",
	"NSPlaceholderString",
	"NSPortCoder",
	"NSHTTPURLHandle",
	"NSRunLoop",
	"NSCountCommand",
	"OC_PythonArray",
	"NSAutoreleasePool",
	"NSConcreteTask",
	"List",
	"NSSocketPortNameServer",
	"OC_PythonDictionaryEnumerator",
	"_NSMutableKnownKeyDictionary",
	"NSKeyedArchiver",
	"NSConcreteNotification",
	"NSURL",
	"NSPortNameServer",
	"NSInvocationBuilder",
	"NSAttributedString",
	"NSSimpleCString",
	"NSFileManager",
	"NSDeserializer",
	"NSCFType",
	"NSCFCharacterSet__",
	"NSProcessInfo",
	"%NSCFTimeZone",
	"NSConcreteMutableAttributedString",
	"NSPlaceholderArray",
	"NSConcretePortCoder",
	"NSMKKDKeyEnumerator",
	"_NSSelectorGetBinding",
	"NSInvocation",
	"NSCFType__",
	"NSLocalTimeZone",
	"NSSerializer",
	"%NSCFTimer",
	"NSConcreteProtocolChecker",
	"NSCFString",
	"NSBundle",
	"NSEnumerator",
	"NSParser",
	"NSCFNumber",
	"NSBigMutableString",
	"NSunsignedIntNumber",
	"NSException",
	"_NSMKKDSubsetMapping",
	"NSDistributedLock",
	"%NSCFDictionary",
	"NSKeySetBinding",
	"NSConcreteFileHandle",
	"%NSCFNumber",
	"NSArray",
	"NSCheapMutableString",
	"NSMutableArray",
	"NSunsignedShortNumber",
	"NSScriptCommand",
	"NSSet",
	"NSPipe",
	"NSFault",
	"NSDecimalNumberHandler",
	"NSPortMessage",
	"_NSLocalNotificationCenter",
	"NSCFDate__",
	"NSConcreteValue",
	"NSSimpleAttributeDictionaryEnumerator",
	"NSSimpleAttributeDictionary",
	"_NSUndoBeginMark",
	"NSTask",
	"_NSKVCPIvarSetBinding",
	"NSDistantObjectRequest",
	"NSCFTimeZone__",
	"NSFTPURLHandle",
	"NSSpellServer",
	"NSCFData__",
	"NSUserDefaults",
	"NSUnarchiver",
	"NSCFNumber__",
	"_NSZombie",
	"NSScriptingAppleEventHandler",
	"NSImmutableStringCharacterSet",
	"NSFileHandle",
	"NSIdEnumerator",
	"NSUniqueIDSpecifier",
	"NSNetServiceBrowser",
	"NSClassDescription",
	"NSMultiReadUniWriteLock",
	"NSValue",
	"NSCFString__",
	"NSPlaceholderMutableArray",
	"NSPort",
	"NSNetService",
	"NSCFTimer__",
	"NSQuitCommand",
	"NSNull",
	"NSURLHandle",
	"NSNumber",
	"NSIndexSpecifier",
	"NSMutableString",
	"NSMutableDictionary",
	"NSMutableData",
	"NSPlaceholderDictionary",
	"_NSUndoLightInvocation",
	"NSMutableRLEArray",
	"NSPathStore2",
	"NSPositionalSpecifier",
	"NSCreateCommand",
	"NSCFSet",
	"NSKeyGetBinding",
	"NSStreamData",
	"%NSURL",
	"NSWhoseTest",
	"NSScriptExecutionContext",
	"NSPlaceholderMutableDictionary",
	"NSConcreteMutableData",
	"NSNumberFormatter",
	"NSDateFormatter",
	"NSAppleEventDescriptor",
	"NSCoercionHandler",
	"NSLogicalTest",
	"NSDeleteCommand",
	"NSDistributedNotificationCenter",
	"_NSMKKDGetBinding",
	"NSMiddleSpecifier",
	"NSDirectoryEnumerator",
	"NSPropertySpecifier",
	"NSCoder",
	"NSCalendarDate",
	"NSInvertedCharacterSet",
	"NSCFBoolean__",
	"NSConcreteDistantObjectRequest",
	"_NSCDBinderMaps",
	"NSRangeSpecifier",
	"_NSKVCPIvarGetBinding",
	"NSScriptClassDescription",
	"NSPlaceholderMutableString",
	"NSRefCountingNumber",
	"NSCFBoolean",
	"NSConstantString",
	"%NSCFDate",
	"%NSCFData",
	"NSPropertyListSerialization",
	"NSProtocolChecker",
	"NSAllDescendantPathsEnumerator",
	"_NSUndoEndMark",
	"Object",
	"NSDecimalNumberPlaceholder",
	"NSNullFileHandle",
	"NSdoubleNumber",
	"%NSCFCharacterSet",
	"NSPlaceholderNumber",
	"NSSetCommand",
	"_NSParserSyntaxNode",
	"NSScriptWhoseTest",
	"NSAbsoluteURL",
	"_NSMKKDInitializer",
	"NSProxy",
	"NSMutableStringProxy",
	"NSPlaceholderMutableSet",
	"NSCloseCommand",
	"NSConcreteAttributedString",
	"NSshortNumber",
	"NSDictionaryEntry",
	"NSKeyedUnarchiver",
	"NSRLEArray",
	"NSSocketPort",
	"_NSUndoObject",
	"NSURL__",
	"NSConnection",
	"_NSKeyForwardingGetBinding",
	"NSObjectSpecifier",
	"NSAppleScript",
	"NSFaultHandler",
	"NSTerminologyRegistry",
	"NSDistributedObjectsStatistics",
	"NSDebugString",
	"NSMessagePort",
	"NSHost",
	"NSNameSpecifier",
	"NSConcreteScanner",
	"NSConcreteMutableCharacterSet",
	"_NSKeyedCoderOldStyleArray",
	"NSCharacterSet",
	"_NSClassToBinderMaps",
	"NSFormatter",
	"NSSpecifierTest",
	"%NSCFString",
	"_NSUndoStack",
	"NSUndoManager",
	"NSDecimalNumber",
	"NSPlaceholderSet",
	"NSMoveCommand",
	"OC_PythonObject",
	"NSNotificationQueue",
	"NSScriptCommandDescription",
	"NSCFTimer",
	"NSExistsCommand",
	"NSConcreteData",
	"NSTimeZoneDetailDecoder",
	"NSScriptCoercionHandler",
	"NSNotificationCenter",
	"NSCFTimeZone",
	"OC_PythonDictionary",
	"NSObject",
	"NSDistantObject",
	"NSfloatNumber",
	"NSMessagePortNameServer",
	"NSDictionary",
]

NSClassFromString = _objc.lookUpClass

# Do something smart to collect Foundation classes...

NSBundle = _objc.lookUpClass('NSBundle')

# We use strings to represent selectors, therefore 
# NSSelectorFromString and NSStringFromSelector are no-ops (for now)

def NSSelectorFromString(aSelectorName):
    if not isinstance(aSelectorName, str):
        raise TypeError, "aSelector must be string"

    return aSelectorName

NSStringFromSelector = NSSelectorFromString

def NSStringFromClass(aClass):
    return aClass.__name__

_objc.loadBundle("Foundation", globals(), bundle_path="/System/Library/Frameworks/Foundation.framework", bundle_classes=CLASSLIST)

del CLASSLIST

import os
import sys
if 'PYOBJCFRAMEWORKS' in os.environ:
    paths = os.environ['PYOBJCFRAMEWORKS'].split(":")
    count = 0
    for path in paths:
        bundle = NSBundle.bundleWithPath_(path)
        bundle.principalClass()
        sys.path.insert(count, str(bundle.resourcePath()))
        count = count + 1

        initPath = bundle.pathForResource_ofType_( "Init", "py")
        if initPath:
            execfile(initPath, globals(), locals())


try:
    import autoGIL
except ImportError:
    pass
else:
    # Install an observer callback in the current CFRunLoop that will
    # automatically release and acquire the Global Interpreter Lock
    # when needed. This is needed so other Python threads get a chance
    # to run while we're inside the event loop.
    autoGIL.installAutoGIL()


import protocols  # no need to export these, just register with PyObjC

#
# (informal) protocols eported for b/w compatibility
#
from protocols import NSConnectionDelegateMethods, NSDistantObjectRequestMethods, \
                      NSCopyLinkMoveHandler, NSKeyedArchiverDelegate, \
                      NSKeyedUnarchiverDelegate, NSNetServiceDelegateMethods, \
                      NSNetServiceBrowserDelegateMethods, NSPortDelegateMethods
