#!/usr/bin/env python
"""
Script for finding methods whose signature contains pointer arguments that have
not been annotated or wrapped. This script is used to find those methods that
require further investigation before they can be used from Python.

If you write a custom wrapper for a method you should add it to the list below,
likewise for methods that won't be supported by the bridge.

Don't forget to add unittests for methods that are wrapped, or whose signature 
you change.
"""

import objc
import Foundation

#import AppKit
#import PreferencePanes
#import ScreenSaver
#import InterfaceBuilder

PTRSIG={}

WRAPPED_METHODS={
# Supported methods:

    #<Foundation>
    'NSString_getCString_maxLength_range_remainingRange_':1,
    'NSString_getCharacters_':1,
    'NSString_getCharacters_range_':1,
    'NSData_getBytes_':1,
    'NSData_getBytes_length_':1,
    'NSData_getBytes_range_':1,
    'NSValue_getValue_':1,
    'NSValue_pointerValue':1,
    'NSMutableData_mutableBytes':1,
    'NSMutableData_serializeAlignedBytes_length_':1,
    'NSMutableData_serializeInts_count_':1,
    'NSMutableData_serializeInts_count_atIndex_':1,
    'NSCoder_decodeBytesForKey_returnedLength_':1,
    'NSCoder_decodeBytesWithReturnedLength_':1,
    'NSSet_initWithObjects_count_':1,
    'NSSet_setWithObjects_count_':1,
    'NSScriptObjectSpecifier_indicesOfObjectsByEvaluatingWithContainer_count_':1,
    'NSArray_arrayByAddingObjects_count_':1,
    'NSArray_arrayWithObjects_count_':1,
    'NSArray_initWithObjects_count_':1,
    'NSArray_sortedArrayUsingFunction_context_':1,
    'NSArray_sortedArrayUsingFunction_context_hint_':1,
    'NSBezierPath_appendBezierPathWithGlyphs_count_inFont_':1,
    'NSBezierPath_appendBezierPathWithPoints_count_':1,
    'NSBezierPath_elementAtIndex_associatedPoints_':1,
    'NSBezierPath_setAssociatedPoints_atIndex_':1,
    'NSBezierPath_setLineDash_count_phase_':1,
    'NSMovie_QTMovie':1,
    'NSMovie_initWithMovie':1,
    'NSCoder_encodeValueOfObjCType_at_':1,
    'NSCoder_decodeValueOfObjCType_at_':1,
    'NSCoder_encodeArrayOfObjCType_count_at_':1,
    'NSCoder_decodeArrayOfObjCType_count_at_':1,
    'NSData_initWithBytes_length_':1,
    'NSData_bytes':1,
    'NSData_mutableBytes':1,
    'NSDictionary_initWithObjects_forKeys_count_':1,
    'NSDictionary_dictionaryWithObjects_forKeys_count_':1,
    'NSMutableArray_removeObjectsFromIndices_numIndices_':1,
    'NSMutableArray_replaceObjectsInRange_withObjects_count_':1,
    'NSMutableArray_sortUsingFunction_context_':1,
    'NSMutableArray_sortUsingFunction_context_range_':1,    

    #<AppKit>
    

# Depricated methods

    #<Foundation>
    'NSData_deserializeAlignedBytesLengthAtCursor_':1,
    'NSData_deserializeBytes_length_atCursor_':1,
    'NSData_deserializeDataAt_ofObjCType_atCursor_context_':1,
    'NSData_deserializeIntAtCursor_':1,
    'NSData_deserializeInts_count_atCursor_':1,
    'NSData_deserializeInts_count_atIndex_':1,


# Unsupported methods:

    #<objc>
    'Protocol_descriptionForClassMethod_':1,

    #<Foundation>
    'NSData_dataWithBytesNoCopy_length_':1,
    'NSData_dataWithBytesNoCopy_length_freeWhenDone_':1,
    'NSData_initWithBytesNoCopy_length_':1,
    'NSData_initWithBytesNoCopy_length_freeWhenDone_':1,
    'NSBezierPath_getLineDash_count_phase_':1,
    'NSFault_forward__':1,
    'NSInvocationBuilder_forward__':1,
    'NSObject_forward__':1,
    'NSProxy_forward__':1,
    'NSArray_getObjects_':1,
    'NSArray_getObjects_range_':1,
    'NSObject_performv__':1,
    'NSString_initWithCharactersNoCopy_length_freeWhenDone_':1,

    #<AppKit>

# Methods that will be added in the future:

    #<Foundation>
    'NSObject_instanceMethodDescriptionForSelector_':1,
    'NSObject_instanceMethodForSelector_':1,
    'NSObject_methodDescriptionForSelector_':1,
    'NSObject_methodForSelector_':1,
    'NSObject_methodFor_':1,
    'NSObject_validateValue_forKey_':1,
    'NSInvocation_getArgument_atIndex_':1,
    'NSInvocation_getReturnValue_':1,
    'NSInvocation_setArgument_atIndex_':1,
    'NSInvocation_setReturnValue_':1,

    'NSFileAttributes_attributesWithStat_':1, # Undocumented, but doable.

    #<AppKit>


# Undocumented methods:

    #<Foundation>
    'NSSet_getObjects_':1,
    'NSData_initWithBytes_length_copy_freeWhenDone_bytesAreVM_':1,
    'NSMessagePort_sendBeforeTime_streamData_components_from_msgid_':1,
    'NSConnection_getReleasedProxies_length_':1,
    'NSSocketPort_sendBeforeTime_streamData_components_from_msgid_':1,
    'NSProtocolChecker_methodDescriptionForSelector_':1,
    'NSIdEnumerator_initWithObjects_count_target_reverse_freeWhenDone_':1,
    'NSParser_parseMetaSyntaxLeafResultShouldBeSkipped_':1,
    'NSString_getBytes_maxLength_filledLength_encoding_allowLossyConversion_range_remainingRange_':1,
    'NSArray_apply_context_':1,
    'NSCheapMutableString_setContentsNoCopy_length_freeWhenDone_isUnicode_':1,
    'NSDictionary_getKeys_':1,
    'NSDictionary_getObjects_':1,
    'NSDictionary_getObjects_andKeys_':1,

    'NSMutableStringProxy_getBytes_maxLength_filledLength_encoding_allowLossyConversion_range_remainingRange_':1,
    'NSMutableStringProxy_getCString_maxLength_range_remainingRange_':1,
    'NSMutableStringProxy_getCharacters_':1,
    'NSMutableStringProxy_getCharacters_range_':1,
    'NSRLEArray_initWithRefCountedRunArray_':1,
    'NSRLEArray_objectAtIndex_effectiveRange_':1,
    'NSRLEArray_objectAtIndex_effectiveRange_runIndex_':1,
    'NSRLEArray_objectAtRunIndex_length_':1,
    'NSConstantString_initWithCharactersNoCopy_length_':1,

    #<AppKit>


# PyObjC internal methods:

    'OC_PythonArray_initWithPythonObject_':1,
    'OC_PythonArray_newWithPythonObject_':1,
    'OC_PythonDictionaryEnumerator_initWithPythonObject_':1,
    'OC_PythonDictionaryEnumerator_newWithPythonObject_':1,
    'OC_PythonDictionary_initWithPythonObject_':1,
    'OC_PythonDictionary_newWithPythonObject_':1,
    'OC_PythonObject_initWithObject_':1,
    'OC_PythonObject_newWithObject_':1,
    'OC_PythonObject_pyObject':1,
}

OKPTR={
    '^{__CFURL': 1,
    '^{AEDesc': 1,
    '^{FSRef': 1,
    '^{_NSZone': 1,
    '^{__CFNetService': 1,
    '^{__CFReadStream': 1,
    '^{__CFRunLoop': 1,
    '^{__CFSet': 1,
}


for cls in objc.getClassList():
    if cls.__name__.startswith('_'): continue
    if cls.__name__.startswith('%'): continue
    if cls.__name__ == 'Object': continue

    for selName in dir(cls):
        try:
            sel = getattr(cls, selName)
        except AttributeError:
            continue

        if cls.__bases__[0] != 'Object' and hasattr(cls.__bases__[0], selName):
            continue

        if not isinstance(sel, objc.selector):
            continue

        if sel.selector.startswith('_'):
            continue


        m = 0
        elems = objc.splitSignature(sel.signature)
        for e in elems:
            if e.startswith('^'):
                u = e.split('}', 1)[0]
                u = u.split('=', 1)[0]
                if not OKPTR.has_key(u):
                    PTRSIG[u] = e
                    m = 1
                #else:
                #    print "XXX", e, '%s_%s'%(cls.__name__, sel.selector.replace(':', '_'))


        if m:
            r = '%s_%s'%(cls.__name__, sel.selector.replace(':', '_'))
            if not WRAPPED_METHODS.has_key(r):
                print r

print "--- SIGNATURES ----"
sigs = PTRSIG.values()
sigs.sort()
print '\n'.join(sigs)
