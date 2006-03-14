#!/usr/bin/env python
"""
Script for finding methods whose signature contains pointer arguments that have
not been annotated or wrapped. This script is used to find those methods that
require further investigation before they can be used from Python.

If you write a custom wrapper for a method you should add it to the list below,
likewise for methods that won't be supported by the bridge.

Don't forget to add unittests for methods that are wrapped, or whose signature
you change.

XXX:
- The data should be stored in a seperate file, to make it possible to use the
  data for other purposes
- The new annotation possibilities should be used, add a comment possibility
  as well.
- Write tools for editing the data, and creating HTML reports (for the website)
"""

import objc
import Foundation

if 1:
    try:
        import AppKit
    except ImportError:
        pass

if 0:
    try:
        import PreferencePanes
    except ImportError:
        pass

if 0:
    try:
        import ScreenSaver
    except ImportError:
        pass

if 0:
    try:
        import InterfaceBuilder
    except ImportError:
        pass

if 0:
    try:
        import AddressBook
    except ImportError:
        pass

if 0:
    try:
        import WebKit
    except ImportError:
        pass

if 0:
    try:
        import SecurityInterface
    except ImportError:
        pass

if 0:
    try:
        import ExceptionHandlers
    except ImportError:
        pass

if 0:
    try:
        import CoreData
    except ImportError:
        pass

PTRSIG={}


REL_OSX_10_2 = 'MacOS X 10.2'
REL_OSX_10_3 = 'MacOS X 10.3'
REL_OSX_10_4 = 'MacOS X 10.4'

TP_SUPPORTED = 'supported'
TP_UNSUPPORTED = 'unsupported'
TP_DEPRECATED = 'deprecated' # Unsupported because the method is deprecated in Cocoa
TP_UNDOCUMENTED = 'undocumented' #  Unsupported because there is no documentation for the method/class

# Keys are 'Class_MethodName' value is ( initial-release, entrytype+)

# XXX: This should be a data file, need to add framework info and comments.
WRAPPED_METHODS={
    'NSKeyValueIvarSetter_initWithContainerClassID_key_containerIsa_ivar_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueIvarGetter_initWithContainerClassID_key_ivar_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueAccessor_initWithContainerClassID_key_implementation_selector_extraArguments_count_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueIvarMutableCollectionGetter_initWithContainerClassID_key_containerIsa_ivar_proxyClass_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueIvarMutableCollectionGetter_ivar': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueMethodSetter_initWithContainerClassID_key_method_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSKeyValueMethodGetter_initWithContainerClassID_key_method_': (REL_OSX_10_4, TP_UNDOCUMENTED),

    # All of these would require libxml2 wrappers:
    'NSXMLTreeReader_createNamedNodeFromNode_reader_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processCDATA_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processComment_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processDocumentFragment_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processDocumentType_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processDocument_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processElement_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processEndElement_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processEndEntity_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processEntityReference_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processEntity_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processNode_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processNotation_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processProcessingInstruction_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processRealDocument_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processSignificantWhitespace_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processText_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processWhitespace_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLTreeReader_processXMLDeclaration_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLElementDeclarationContent_XMLStringSequenceStarted_choiceStarted_appendingToString_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLElementDeclarationContent_createElementContent_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLElementDeclarationContent_libxml2Content': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLElement_validateName_error_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSXMLSAXParser_context': (REL_OSX_10_4, TP_UNDOCUMENTED),



    # WebKit related
    'NSHTTPAuthenticator_addCredentialsToInitialHTTPRequest_proxyURL_protocol_': (REL_OSX_10_4, TP_UNSUPPORTED),
    'NSHTTPAuthenticator_addCredentialsToRetryHTTPRequest_proxyURL_afterFailureResponse_nsFailureResponse_failureCount_protocol_withCallback_context_': (REL_OSX_10_4, TP_UNSUPPORTED),
    'NSHTTPAuthenticator_checkForAuthenticationFailureInHTTPResponse_withURL_proxyURL_': (REL_OSX_10_4, TP_UNSUPPORTED),
    'NSPortMessage_initWithMachMessage_': (REL_OSX_10_4, TP_UNSUPPORTED),
    'NSSet_initWithObjects_ex_count_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSDictionary_initWithObjects_ex_forKeys_count_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSArray_initWithObjects_ex_count_': (REL_OSX_10_4, TP_UNDOCUMENTED),

    'NSConnectionHTTPURLProtocol_createStream_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSConnectionHTTPURLProtocol_retryAfterAuthenticationFailure_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSConnectionHTTPURLProtocol_setResponseHeaderUsingHTTPResponse_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSConnectionHTTPURLProtocol_updateConnectionForResponse_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_addConnection_forKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_connectionsForKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_dequeueRequestForKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_enqueueRequest_forKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_removeConnection_forKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_setUseSSLOnly_forKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),
    'NSHTTPConnectionCache_useSSLOnlyForKey_': (REL_OSX_10_4, TP_UNDOCUMENTED),




    # Internal methods
    'OC_PythonArray_getObjects_inRange_': (REL_OSX_10_3, TP_UNSUPPORTED),

    #<Foundation>
    'NSBinHexDecoder_decodeAllIntoBuffer_size_useZeroBytesForCRC_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSBinHexDecoder_decodeIntoBuffer_size_useZeroBytesForCRC_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueAccessor_extraArgument1': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueAccessor_extraArgument2': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueAccessor_initWithContainerClass_key_implementation_selector_extraArgument1_extraArgument2_extraArgument3_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueMethodSetter_method': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueIvarMutableArrayGetter_initWithContainerClass_key_ivar_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueIvarMutableArrayGetter_ivar': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSKeyValueIvarSetter_ivar': (REL_OSX_10_3, TP_UNDOCUMENTED),


    'NSIndexSet_getIndexes_maxCount_inIndexRange_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSInputStream_getBuffer_length_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSString_getCString_maxLength_range_remainingRange_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSString_getCharacters_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSString_getCharacters_range_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_getBytes_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_getBytes_length_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_getBytes_range_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSValue_getValue_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSValue_pointerValue': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableData_mutableBytes': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableData_serializeAlignedBytes_length_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableData_serializeInts_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableData_serializeInts_count_atIndex_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_decodeBytesForKey_returnedLength_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_decodeBytesWithReturnedLength_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSSet_initWithObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSSet_setWithObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSScriptObjectSpecifier_indicesOfObjectsByEvaluatingWithContainer_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSArray_arrayByAddingObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSArray_arrayWithObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSArray_initWithObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSArray_sortedArrayUsingFunction_context_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSArray_sortedArrayUsingFunction_context_hint_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBezierPath_appendBezierPathWithGlyphs_count_inFont_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBezierPath_appendBezierPathWithPoints_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBezierPath_elementAtIndex_associatedPoints_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBezierPath_setAssociatedPoints_atIndex_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBezierPath_setLineDash_count_phase_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMovie_QTMovie': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMovie_initWithMovie': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_encodeValueOfObjCType_at_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_decodeValueOfObjCType_at_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_encodeArrayOfObjCType_count_at_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSCoder_decodeArrayOfObjCType_count_at_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_initWithBytes_length_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_bytes': (REL_OSX_10_2, TP_SUPPORTED),
    'NSData_mutableBytes': (REL_OSX_10_2, TP_SUPPORTED),
    'NSDictionary_initWithObjects_forKeys_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSDictionary_dictionaryWithObjects_forKeys_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableArray_removeObjectsFromIndices_numIndices_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableArray_replaceObjectsInRange_withObjects_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableArray_sortUsingFunction_context_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMutableArray_sortUsingFunction_context_range_': (REL_OSX_10_2, TP_SUPPORTED),

    #<AppKit>
    'NSATSUStyleObject_initWithStyle_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_mergeInVariations_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_merge_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_setAttributes_Values_ValueSizes_Count_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_setFeatures_selectors_count_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_setVariations_Values_Count_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSATSUStyleObject_style': (REL_OSX_10_3, TP_UNDOCUMENTED),

    # XX: selectionMode is a pointer
    'NSArrayDetailBinder_addObjectToMasterArrayRelationship_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArrayDetailBinder_addObjectsToMasterArrayRelationship_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArrayDetailBinder_insertObjectIntoMasterArrayRelationship_atIndex_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArrayDetailBinder_insertObjectsIntoMasterArrayRelationship_atIndexes_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArrayDetailBinder_removeObjectFromMasterArrayRelationshipAtIndex_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArrayDetailBinder_removeObjectsFromMasterArrayRelationshipAtIndexes_selectionMode_': (REL_OSX_10_3, TP_UNDOCUMENTED),

    'NSFontEffectsBox_carbonNotificationProc': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSValueBinder_handleValidationError_description_inEditor_errorUserInterfaceHandled_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSValueBinder_validateAndCommitValueInEditor_editingIsEnding_errorUserInterfaceHandled_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSToolTipStringDrawingLayoutManager_sizeForDisplayingAttributedString_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSAATAttributes_fillPlatformStyle_': (REL_OSX_10_3, TP_UNDOCUMENTED),


    'NSATSTypesetter_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSATSTypesetter_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSATSTypesetter_substituteGlyphsInRange_withGlyphs_': (REL_OSX_10_2, TP_SUPPORTED),

    'NSOpenGLContext_CGLContextObj': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBitmapImageRep_getBitmapDataPlanes_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBitmapImageRep_getTIFFCompressionTypes_count_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSBitmapImageRep_initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSSimpleHorizontalTypesetter_baseOfTypesetterGlyphInfo': (REL_OSX_10_2, TP_SUPPORTED),
    'NSSimpleHorizontalTypesetter_layoutGlyphsInHorizontalLineFragment_baseline_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSWindow_graphicsPort': (REL_OSX_10_2, TP_SUPPORTED),
    'NSWindow_initWithWindowRef_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSWindow_windowRef': (REL_OSX_10_2, TP_SUPPORTED),
    'NSLayoutManager_getGlyphs_range_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSLayoutManager_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSLayoutManager_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSLayoutManager_rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSLayoutManager_rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSQuickDrawView_qdPort': (REL_OSX_10_2, TP_SUPPORTED),
    'NSOpenGLContext_getValues_forParameter_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSOpenGLContext_setOffScreen_width_height_rowbytes_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSOpenGLPixelFormat_getValues_forAttribute_forVirtualScreen_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSOpenGLPixelFormat_initWithAttributes_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSView_sortSubviewsUsingFunction_context_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSGraphicsContext_focusStack': (REL_OSX_10_2, TP_SUPPORTED),
    'NSGraphicsContext_graphicsPort': (REL_OSX_10_2, TP_SUPPORTED),
    'NSGraphicsContext_initWithHostName_serverName_textProc_errorProc_timeout_secure_encapsulated_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSGraphicsContext_initWithMutableData_forDebugging_languageEncoding_nameEncoding_textProc_errorProc_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSGraphicsContext_setFocusStack_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMovie_initWithMovie_': (REL_OSX_10_2, TP_SUPPORTED),
    'NSMatrix_sortUsingFunction_context_': (REL_OSX_10_2, TP_SUPPORTED),

# Depricated methods

    #<Foundation>
    'NSData_deserializeAlignedBytesLengthAtCursor_':1,
    'NSData_deserializeBytes_length_atCursor_':1,
    'NSData_deserializeDataAt_ofObjCType_atCursor_context_':1,
    'NSData_deserializeIntAtCursor_':1,
    'NSData_deserializeInts_count_atCursor_':1,
    'NSData_deserializeInts_count_atIndex_':1,

    #<AppKit>
    'NSPageLayout_convertOldFactor_newFactor_':1,

# Unsupported methods:

    #<objc>
    'Protocol_descriptionForClassMethod_':1,

    #<Foundation>
    'NSString_initWithBytesNoCopy_length_encoding_freeWhenDone_':1,
    'NSData_dataWithBytesNoCopy_length_':1,
    'NSData_dataWithBytesNoCopy_length_freeWhenDone_':1,
    'NSData_initWithBytesNoCopy_length_':1,
    'NSData_initWithBytesNoCopy_length_freeWhenDone_':1,
    'NSBezierPath_getLineDash_count_phase_':1,
    'NSFault_forward__':1,
    'NSResurrectedObject_forward__':1,
    'NSDeallocatedObject_forward__':1,
    'NSInvocationBuilder_forward__':1,
    'NSObject_forward__':1,
    'NSProxy_forward__':1,
    'NSArray_getObjects_':1,
    'NSArray_getObjects_range_':1,
    'NSObject_performv__':1,
    'NSString_initWithCharactersNoCopy_length_freeWhenDone_':1,

    #<AppKit>
    'NSLeafProxy_forward__':1,

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
    # from 'WebKit'
    'WebCoreBridge_adjustPageHeightNew_top_bottom_limit_':1,
    'WebCoreBridge_copyDOMNode_copier_':1,
    'WebCoreBridge_copyRenderNode_copier_':1,
    'WebCoreBridge_drawRect_withPainter_':1,
    'WebCoreBridge_part':1,
    'WebCoreBridge_renderPart':1,
    'WebCoreBridge_setRenderPart_':1,
    'WebCoreTextRendererFactory_fontWithFamilies_traits_size_':1,
    'KWQResourceLoader_initWithLoader_job_':1,
    'KWQTextAreaTextView_setWidget_':1,
    'KWQTextAreaTextView_widget':1,
    'WebCoreDOMImplementation_DOMImplementationImpl':1,
    'WebCoreDOMImplementation_implementionatWithImpl_':1,
    'KWQComboBoxAdapter_initWithQComboBox_':1,
    'WebCoreDOMAttr_attrImpl':1,
    'WebCoreDOMAttr_attrWithImpl_':1,
    'WebCoreSettings_settings':1,
    'KWQObjectTimerTarget_initWithQObject_timerId_':1,
    'WebBridge_runJavaScriptTextInputPanelWithPrompt_defaultText_returningText_':1,
    'KWQPopUpButton_widget':1,
    'KWQScrollBar_initWithQScrollBar_':1,
    'KWQPageState_URL':1,
    'KWQPageState_document':1,
    'KWQPageState_initWithDocument_URL_windowProperties_locationProperties_interpreterBuiltins_':1,
    'KWQPageState_interpreterBuiltins':1,
    'KWQPageState_locationProperties':1,
    'KWQPageState_pausedActions':1,
    'KWQPageState_renderer':1,
    'KWQPageState_setPausedActions_':1,
    'KWQPageState_windowProperties':1,
    'WebNSView_initWithQButton_':1,
    'KWQSingleShotTimerTarget_targetWithQObject_member_':1,
    'NSWindowGraphicsContext_setCGContext_':1,
    'WebHistoryPrivate_findIndex_forDay_':1,
    'WebHistoryPrivate_loadFromURL_error_':1,
    'WebHistoryPrivate_saveToURL_error_':1,
    'KWQButton_initWithQButton_':1,
    'WebTextRenderer_convertCharacters_length_toGlyphs_skipControlCharacters_':1,
    'WebTextRenderer_convertUnicodeCharacters_length_toGlyphs_':1,
    'WebTextRenderer_extendGlyphToWidthMapToInclude_font_':1,
    'WebTextRenderer_floatWidthForCharacters_stringLength_fromCharacterPosition_numberOfCharacters_withPadding_applyRounding_attemptFontSubstitution_widths_letterSpacing_wordSpacing_smallCaps_fontFamilies_':1,
    'WebTextRenderer_floatWidthForRun_style_applyRounding_attemptFontSubstitution_widths_':1,
    'WebTextRenderer_substituteFontForCharacters_length_families_':1,
    'WebTextRenderer_substituteFontForString_families_':1,
    'NSTextView_completionsForPartialWordRange_indexOfSelectedItem_':1,
    'NSTextView_dragImageForSelectionWithEvent_origin_':1,
    'NSTextView_smartInsertForString_replacingRange_beforeString_afterString_':1,
    'WebHistory_loadFromURL_error_':1,
    'WebHistory_saveToURL_error_':1,
    'KWQTextField_initWithQLineEdit_':1,
    'KWQTextField_widget':1,
    'KWQView_initWithWidget_':1,
    'KWQView_widget':1,
    'WebCoreDOMNamedNodeMap_implWebCoreDOMNamedNodeMap_initWithImpl_':1,
    'WebCoreDOMNamedNodeMap_namedNodeMapWithImpl_WebBaseNetscapePluginStream_setPluginPointer_HIViewAdapter_bindHIViewToNSView_nsView_':1,
    'HIViewAdapter_getHIViewForNSView_HIViewAdapter_initWithFrame_view_':1,
    'WebBaseNetscapePluginView_destroyStream_reason_':1,
    'WebBaseNetscapePluginView_getCarbonEvent_':1,
    'WebBaseNetscapePluginView_getCarbonEvent_withEvent_':1,
    'WebBaseNetscapePluginView_getURLNotify_target_notifyData_':1,
    'WebBaseNetscapePluginView_invalidateRect_':1,
    'WebBaseNetscapePluginView_invalidateRegion_':1,
    'WebBaseNetscapePluginView_loadRequest_inTarget_withNotifyData_':1,
    'WebBaseNetscapePluginView_newStream_target_stream_':1,
    'WebBaseNetscapePluginView_pluginPointer':1,
    'WebBaseNetscapePluginView_postURLNotify_target_len_buf_file_notifyData_':1,
    'WebBaseNetscapePluginView_sendEvent_':1,
    'WebBaseNetscapePluginView_write_len_buffer_WebCoreDOMText_textImpl':1,
    'CarbonWindowAdapter_initWithCarbonWindowRef_takingOwnership_':1,
    'CarbonWindowAdapter_initWithCarbonWindowRef_takingOwnership_disableOrdering_carbon_':1,
    'CarbonWindowAdapter_sendCarbonUpdateHICommandStatusEvent_withMenuRef_andMenuItemIndex_':1,
    'WebCoreDOMText_textWithImpl_':1,
    'WebDownloadInternal_download_shouldBeginChildDownloadOfSource_delegate_':1,
    'WebCoreDOMDocumentFragment_documentFragmentImpl':1,
    'WebCoreDOMDocumentFragment_documentFragmentWithImpl_':1,
    'WebCoreDOMCharacterData_characterDataImpl':1,
    'WebCoreDOMCharacterData_commentWithImpl_':1,
    'KWQTableView_initWithListBox_items_':1,
    'KWQTableView_widget':1,
    'KWQTextArea_getCursorPositionAsIndex_inParagraph_':1,
    'KWQTextArea_initWithQTextEdit_':1,
    'KWQTextArea_widget':1,
    'WebAuthenticationPanel_sheetDidEnd_returnCode_contextInfo_':1,
    'WebCoreDOMNodeList_impl':1,
    'WebCoreDOMNodeList_initWithImpl_':1,
    'WebCoreDOMNodeList_nodeListWithImpl_':1,
    'WebCoreDOMElement_elementImpl':1,
    'WebCoreDOMElement_elementWithImpl_':1,
    'WebNetscapePluginPackage_NPP_Destroy':1,
    'WebNetscapePluginPackage_NPP_DestroyStream':1,
    'WebNetscapePluginPackage_NPP_GetValue':1,
    'WebNetscapePluginPackage_NPP_HandleEvent':1,
    'WebNetscapePluginPackage_NPP_New':1,
    'WebNetscapePluginPackage_NPP_NewStream':1,
    'WebNetscapePluginPackage_NPP_Print':1,
    'WebNetscapePluginPackage_NPP_SetValue':1,
    'WebNetscapePluginPackage_NPP_SetWindow':1,
    'WebNetscapePluginPackage_NPP_StreamAsFile':1,
    'WebNetscapePluginPackage_NPP_URLNotify':1,
    'WebNetscapePluginPackage_NPP_Write':1,
    'WebNetscapePluginPackage_NPP_WriteReady':1,
    'KWQFileButtonAdapter_initWithKWQFileButton_':1,
    'WebCoreDOMDocument_documentImpl':1,
    'WebCoreDOMDocument_documentWithImpl_':1,
    'KWQSecureTextField_widget':1,
    'WebCoreDOMEntityReference_entityReferenceImpl':1,
    'WebCoreDOMEntityReference_entityReferenceWithImpl_':1,
    'WebPluginRequest_initWithRequest_frameName_notifyData_':1,
    'WebPluginRequest_notifyData':1,
    'WebCoreDOMCDATASection_CDATASectionImpl':1,
    'WebCoreDOMCDATASection_CDATASectionWithImpl_':1,
    'KWQPopUpButtonCell_initWithWidget_':1,
    'KWQPopUpButtonCell_widget':1,
    'WebGlyphBuffer_addGlyphs_advances_count_at__':1,
    'KWQTimerTarget_targetWithQTimer_':1,
    'WebCoreDOMNode_impl':1,
    'WebCoreDOMNode_initWithImpl_':1,
    'WebCoreDOMNode_nodeWithImpl_':1,
    'WebCoreDOMDocumentType_documentTypeImpl':1,
    'WebCoreDOMDocumentType_documentTypeWithImpl_':1,
    'WebCoreDOMProcessingInstruction_processingInstructionImpl':1,
    'WebCoreDOMProcessingInstruction_processingInstructionWithImpl_':1,
    'WebNetscapePluginStream_initWithRequest_pluginPointer_notifyData_':1,
    'WebCoreDOMComment_commentImpl':1,
    'WebCoreDOMNamedNodeMap_impl':1,
    'WebCoreDOMNamedNodeMap_initWithImpl_':1,
    'WebCoreDOMNamedNodeMap_namedNodeMapWithImpl_':1,
    'WebBaseNetscapePluginStream_setPluginPointer_':1,
    'HIViewAdapter_bindHIViewToNSView_nsView_':1,
    'HIViewAdapter_getHIViewForNSView_':1,
    'HIViewAdapter_initWithFrame_view_':1,
    'WebBaseNetscapePluginView_write_len_buffer_':1,
    'WebCoreDOMText_textImpl':1,
    'KWQResourceLoader_initWithJob_': 1,
    'KWQSecureTextField_initWithQLineEdit_':1,
    'KWQAccObject_anchorElement':1,
    'KWQAccObject_initWithRenderer_':1,
    'WebBridge_pollForAppletInView_':1,
    'WebBridge_syncLoadResourceWithURL_customHeaders_postData_finalURL_responseHeaders_statusCode_':1,
    'WebTextRenderer_floatWidthForRun_style_widths_':1,
    'WebBaseNetscapePluginStream_setNotifyData_':1,




    # From 'import PreferencePanes', some undocumented framework?
    'SFCertificateData_parseGeneralNames_indent_':(REL_OSX_10_2, TP_UNDOCUMENTED),
    'SFCertificateTrustPanel_beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_trust_message_':1,
    'SFCertificateTrustPanel_runModalForTrust_message_':1,
    'SFKeychainSavePanel_keychain':1,
    'SFAuthorizationView_authorizationRights':1,
    'SFPasswordAsstModel_calculateSetSize___':1,
    'SFPasswordAsstModel_calculate___':1,
    'SFAuthorization_authorizationRef':1,
    'SFAuthorization_permitWithRights_flags_environment_authorizedRights_':1,
    'SFCertificateData_certData':1,
    'SFCertificateData_certificate':1,
    'SFCertificateData_data':1,
    'SFCertificateData_initWithCertData_':1,
    'SFCertificateData_initWithCertificate_':1,
    'SFCertificateData_initWithData_':1,
    'SFCertificateData_issuer':1,
    'SFCertificateData_parseGeneralNames_':1,
    'SFCertificateData_setCertData_':1,
    'SFCertificateData_setCertificate_':1,
    'SFCertificateData_setData_':1,
    'SFCertificateData_subject':1,
    'SFCertificateView_certificate':1,
    'SFCertificateView_setCertificate_':1,
    'SFCertificatePanel_beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_certificates_showGroup_':1,
    'SFChooseIdentityPanel_beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_identities_message_':1,
    'SFChooseIdentityPanel_identity':1,
    'SFKeychainSettingsPanel_beginSheetForWindow_modalDelegate_didEndSelector_contextInfo_settings_keychain_':1,
    'SFKeychainSettingsPanel_runModalForSettings_keychain_':1,

    #<AddressBook>

       # Panther
    'DSoBuffer_dsDataBuffer':1,
    'DSoBuffer_grow_':1,
    'DSoDataList_dsDataList':1,
    'DSoDataList_initWithDir_dsDataList_':1,
    'DSoRecord_getAttrValuePtrForTypeNode_value_':1,
    'DSoDataNode_dsDataNode':1,
    'DSoDataNode_initWithDir_copyOfDsDataNode_':1,
    'DSoDataNode_initWithDir_dsDataNode_':1,
    'ABPeoplePickerView_carbonDelegate':1,
    'ABPeoplePickerView_setCarbonDelegate_':1,
    'ABUIController_resizeWindow_animate_fromLayout_toLayout_paneWidths_numberOfPanes_':1,
    'ABAuthenticationInfo_authenticationInfoWithAuthentication_forUser_andPass_':1,
    'ABAuthenticationInfo_initWithAuthentication_forUser_andPass_':1,
    'NSString_abEscapeStringForUnichar_and_advance_':1,
    'ABIndexer_filelock':1,
    'ABPerson_firstLastSortingNamePart1_part2_':1,
    'ABPerson_lastFirstSortingNamePart1_part2_':1,
    'ABPerson_propertyLineForGenericABProperty_vCardProperty_is21_groupCount_':1,
    'ABPerson_slowFirstLastSortingNamePart1_part2_':1,
    'ABPerson_slowLastFirstSortingNamePart1_part2_':1,
    'ABVCardParser_nextPersonWithLength_':1,
    'ABCardItemRuler_view_stringForToolTip_point_userData_':1,
    'ABTableController_dragImageForRows_event_dragImageOffset_':1,
    'ABRemoteImageLoader_nts_BeginLoadingImageForPerson_forClient_orCallback_withRefcon_':1,
    'ABInputController_textView_completions_forPartialWordRange_indexOfSelectedItem_':1,
    'ABRecord_createFirstLastSortingNamePart1_part2_':1,
    'ABRecord_createLastFirstSortingNamePart1_part2_':1,
    'ABTextView_view_stringForToolTip_point_userData_':1,
    'ABDBCache_databaseChangedForUserInfo_groupsChanged_peopleChanged_':1,
    'ABSeparatedButtonsCell_view_stringForToolTip_point_userData_':1,
    'ABWindow_setFrame_animate_fromLayout_toLayout_paneWidths_numberOfPanes_':1,
    'ABMembersController_deleteConfirmSheetDidEnd_returnCode_contextInfo_':1,
    'ABMembersController_removeConfirmSheetDidEnd_returnCode_contextInfo_':1,
    'ABVCardLexer_nextBase64Line_':1,
    'ABVCardLexer_nextSingleByteBase64Line_':1,
    'ABVCardLexer_nextUnicodeBase64Line_':1,



      # Januar
    'ABLDAP_ConfigController_editorDidEnd_returnCode_contextInfo_':1,
    'ABGroupsController_deleteConfirmSheetDidEnd_returnCode_contextInfo_':1,
    'ABCustomLabelEditor_sheetDidEnd_returnCode_contextInfo_':1,
    'ABRemoteImageLoader_beginLoadingImageForPerson_forClient_orCallback_withRefcon_':1,
    'ABLayoutManager_rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_forCursorPosition_':1,
    'ABLDAP_Manager_queryAttributes':1,
    'ABPersonImageView_savePanelDidEnd_returnCode_contextInfo_':1,
    'ABVCard_initWithVCardRef_':1,
    'ABVCardEnumerator_initWithVCardRef_':1,
    'ABRecord_firstLastSortingNamePart1_part2_':1,
    'ABRecord_lastFirstSortingNamePart1_part2_':1,
    'AB_AFDataFile_info':1,
    'ABPeopleController_deleteConfirmSheetDidEnd_returnCode_contextInfo_':1,
    'ABPeopleController_removeConfirmSheetDidEnd_returnCode_contextInfo_':1,


    #<Foundation>
      # .. Panther ..
    'NSKeyValueAccessor_initWithContainerClass_key_implementation_selector_extraArgumentCount_extraArgument1_extraArgument2_':1,
    'NSCFNetworkHTTPURLProtocol_retryAfterAuthenticationFailure_':1,
    'NSCFNetworkHTTPURLProtocol_setResponseHeaderUsingHTTPResponse_andCall_context_':1,
    'NSURLAuthenticationChallengeState_initWithProtocol_httpRequest_challenge_callback_context_':1,
    'NSURLAuthenticationChallengeState_initWithProtocol_httpRequest_proxyURL_challenge_callback_context_': 1,
    'NSHTTPURLProtocol_didAddCredentials_toRequest_context_':1,
    'NSURLQueue_newNode':1,
    'NSUndoManager_registerUndoWithTarget_selector_arguments_argumentCount_':1,
    'NSKeyValueIvarGetter_initWithContainerClass_key_ivar_':1,
    'NSKeyValueMethodGetter_initWithContainerClass_key_getMethod_':1,
    'NSKeyValueIvarSetter_initWithContainerClass_key_ivar_':1,
    'NSKeyValueMethodSetter_initWithContainerClass_key_setMethod_':1,
    'NSSSLProxyWrapperStream_initWithURL_httpStream_readStreamToProxy_writeStreamToProxy_':1,
    'NSGZipDecoder_decodeData_dataForkData_resourceForkData_':1,
    'NSGZipDecoder_decodeHeader_headerLength_modificationTime_filename_':1,
    'NSURLKeychainCredentialInternal_initWithKeychainItem_':1,
    'NSURLKeychainCredential_credentialWithKeychainItem_':1,
    'NSURLKeychainCredential_initWithKeychainItem_':1,
    'NSHTTPAuthenticator_addCredentialsToInitialHTTPRequest_protocol_':1,
    'NSHTTPAuthenticator_addCredentialsToRetryHTTPRequest_afterFailureResponse_nsFailureResponse_failureCount_protocol_withCallback_context_':1,
    'NSHTTPAuthenticator_cancelAddCredentialsToRetryHTTPRequest_':1,
    'NSHTTPAuthenticator_checkForAuthenticationFailureInHTTPResponse_withURL_':1,
    'NSMacBinaryDecoder_decodeData_dataForkData_resourceForkData_':1,
    'NSMacBinaryDecoder_decodeDownloadData_dataForkData_resourceForkData_':1,
    'NSBinHexDecoder_decodeAllIntoBuffer_size_':1,
    'NSBinHexDecoder_decodeData_dataForkData_resourceForkData_':1,
    'NSBinHexDecoder_decodeForkWithData_count_CRCCheckFlag_':1,
    'NSBinHexDecoder_decodeIntoBuffer_size_':1,

      ## NSAppleEventManagerSuspensionID is an opaque pointer (TODO)
    'NSAppleEventManager_appleEventForSuspensionID_':1,
    'NSAppleEventManager_replyAppleEventForSuspensionID_':1,
    'NSAppleEventManager_resumeWithSuspensionID_':1,
    'NSAppleEventManager_setCurrentAppleEventAndReplyEventWithSuspensionID_':1,
    'NSAppleEventManager_suspendCurrentAppleEvent':1,
    'NSGZipDecoder_decodeDownloadData_dataForkData_resourceForkData_':1,
    'NSGZipDecoder_decodeDownloadHeader_headerLength_modificationTime_filename_':1,
    'NSBinHexDecoder_decodeDownloadData_dataForkData_resourceForkData_':1,


      ## This looks doable
    'NSURLHostNameAddressInfo_addrinfo':1,


      # .. Jaguar ..
    'NSString_escapeStringForUnichar_and_advance_':1,
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
       # .. Panther ..
    'NSGlyphGenerator_generateGlyphsForGlyphStorage_desiredNumberOfCharacters_glyphIndex_characterIndex_':1,
    'NSMatrix_textView_completions_forPartialWordRange_indexOfSelectedItem_':1,
    'NSSavePanel_control_textView_completions_forPartialWordRange_indexOfSelectedItem_':1,
    'NSTableView_textView_completions_forPartialWordRange_indexOfSelectedItem_':1,
    'NSTextField_textView_completions_forPartialWordRange_indexOfSelectedItem_':1,

    'NSBinder_invokeSelector_withArguments_forBinding_atIndex_error_':1,
    'NSBinder_invokeSelector_withArguments_forBinding_error_':1,
    'NSBinder_setValue_forBinding_atIndex_error_':1,
    'NSBinder_setValue_forBinding_error_':1,
    'NSGrayFrame_drawWindowBackgroundRegion_level_':1,
    'NSNavOutlineView_cellAtPoint_row_column_loaded_':1,
    'NSNavFBEContainerNode_eventQueue':1,
    'NSColorPickerPageableNameListView_selectedIndexAndQuality_':1,
    'NSSpeechSynthesizerVars_findVoiceByIdentifier_returningCreator_returningID_':1,
    'NSSpeechSynthesizerVars_speechChannel':1,
    'NSSpeechRecognizerVars_setSRRecognitionSystem_':1,
    'NSSpeechRecognizerVars_setSRRecognizer_':1,
    'NSSpeechRecognizerVars_srRecognitionSystem':1,
    'NSSpeechRecognizerVars_srRecognizer':1,
    'NSDocFormatReader_attributesAtIndex_effectiveRange_inRange_':1,
    'NSDocFormatReader_paragraphAttributesAtIndex_effectiveRange_inRange_':1,
    'NSFontOptions_sheetDidEnd_returnCode_contextInfo_':1,
    'NSNavVirtualNode_copyIcon':1,
    'NSNavVirtualNode_setIconRef_':1,
    'NSNavFBENode_copyIcon':1,
    'NSNavFBENode_fbeNode':1,
    'NSNavFBENode_initWithFBENode_':1,
    'NSNavFBENode_nodeWithFBENode_':1,
    'NSColorPickerPageableNameList_attachColorList_systemList_makeSelected_':1,
    'NSColorPickerPageableNameList_removeColorSheetDidEnd_returnCode_context_':1,
    'NSColorPickerPageableNameList_removeListSheetDidEnd_returnCode_context_':1,
    'NSColorPickerPageableNameList_renameColorSheetDidEnd_returnCode_context_':1,
    'NSColorPickerPageableNameList_renameListSheetDidEnd_returnCode_context_':1,
    'NSColorPickerPageableNameList_tryNewColorListNameSheetDidEnd_returnCode_context_':1,
    'NSRegion_cgsRegionObj':1,
    'NSRegion_getRects_count_':1,
    'NSRegion_initWithCGSRegionObj_':1,
    'NSCGImageRep_CGImage':1,
    'NSCGImageRep_initWithCGImage_':1,
    'NSView_getRectsBeingDrawn_count_':1,
    'NSNavFileListDelegate_getSnapToWidthList_snapRadiusList_count_':1,
    'NSNavMatrix_cellAtPoint_row_column_':1,
    'NSNavSidebarView_getSnapToWidthList_snapRadiusList_count_':1,



     # PyOpenGL integration?
     'NSOpenGLPixelFormat_CGLPixelFormatObj':1,




       # .. Jaguar ..
    'NSCGSContext_windowID':1,
    'NSPreferences_confirmCloseSheetIsDone_returnCode_contextInfo_':1,
    'NSPasteboard_readDocumentFromPbtype_filename_':1,
    'NSView_knowsPagesFirst_last_':1,
    'NSTitledFrame_constrainResizeEdge_withDelta_elapsedTime_':1,
    'NSTextView_getMarkedText_selectedRange_':1,
    'NSTableView_dragImageForRows_event_dragImageOffset_':1,
    'NSStringDrawingTextStorage_fastDrawAttributedString_containerSize_padding_inRect_onView_pinToTop_sizeOnly_size_':1,
    'NSStringDrawingTextStorage_fastDrawString_attributes_containerSize_padding_inRect_onView_pinToTop_sizeOnly_size_':1,
    'NSStorage_addElement_':1,
    'NSStorage_elementAtIndex_':1,
    'NSStorage_insertElement_atIndex_':1,
    'NSStorage_insertElements_count_atIndex_':1,
    'NSStorage_pointerToElement_directlyAccessibleElements_':1,
    'NSStorage_replaceElementAtIndex_withElement_':1,
    'NSStatusBar_drawBackgroundInRect_inView_highlight_':1,
    'NSServiceListener_invokeServiceIn_msg_pb_userData_error_':1,
    'NSRunStorage_elementAtIndex_effectiveRange_':1,
    'NSRunStorage_insertElement_range_coalesceRuns_':1,
    'NSRunStorage_replaceElementsInRange_withElement_coalesceRuns_':1,
    'NSRulebookSetObject_initWithSetHeader_':1,
    'NSRulebookSetObject_setHeader':1,
    'NSRulebook_codeSegment':1,
    'NSRulebook_findEntryListFor_':1,
    'NSRulebook_propertyTableAtIndex_':1,
    'NSRulebook_testStructArrayAtIndex_':1,
    'NSQuickDrawPort_port':1,
    'NSPageData_stream':1,
    'NSMovieView_movieController':1,
    'NSPPDParse_growBuffer_current_end_factor_':1,
    'NSPPDParse_openInclude_':1,
    'NSPPDParse_readFromStream_':1,
    'NSPPDParse_startInputStream_closeOnEnd_':1,
    'NSAKDeserializerStream_readData_length_':1,
    'NSAKSerializerStream_copySerializationInto_':1,
    'NSAKSerializerStream_writeRoomForInt_':1,
    'NSATSTypesetter_charIndexToBreakLineByWordWrappingAtIndex_inRange_hyphenate_glyphVector_':1,
    'NSATSTypesetter_fillPlatformTextStyle_forLayoutManager_withAttributes_':1,
    'NSApplication_msgPrint_ok_':1,
    'SCGSContext_windowID':1,
    'NSCarbonWindow_handleMouseDownEvent_at_inPart_withMods_':1,
    'NSCarbonWindow_initWithCarbonWindowRef_takingOwnership_':1,
    'NSCarbonWindow_initWithCarbonWindowRef_takingOwnership_disableOrdering_':1,
    'NSCarbonWindow_sendCarbonUpdateHICommandStatusEvent_withMenuRef_andMenuItemIndex_':1,
    'NSCell_heartBeat_':1,
    'NSWindow_heartBeat_':1,
    'NSView_heartBeat_':1,
    'NSCharacterProperty_initWithRulebookSet_':1,
    'NSCollatorElement_entryState_':1,
    'NSCollatorElement_stepKey_elements_number_state_':1,
    'NSColorSwatch_getSavedNumVisibleRows_':1,
    'NSDefaultSpellServerDelegate_spellServer_findMisspelledWordInString_language_wordCount_countOnly_':1,
    'NSDocInfo_initFromInfo_':1,
    'NSFocusState_clip_':1,
    'NSFocusState_setInitialGState_':1,
    'NSFont_metrics':1,
    'NSFrameView_drawWindowBackgroundRegion_':1,
    'NSGlyphGenerator_generateGlyphsForLayoutManager_range_desiredNumberOfCharacters_startingAtGlyphIndex_completedRange_nextGlyphIndex_':1,
    'NSGraphicsContext_DPSContext':1,
    'NSGraphicsContext_contextID':1,
    'NSGraphicsContext_errorProc':1,
    'NSGraphicsContext_sendTaggedMsg_':1,
    'NSGraphicsContext_setErrorProc_':1,
    'NSGraphicsContext_setTextProc_':1,
    'NSGraphicsContext_textProc':1,
    'NSHFSBrowserCell_setIconRef_label_':1,
    'NSHFSContainer_iconRef_label_forObjectName_':1,
    'NSHFSObject_iconRef_label_':1,
    'NSHFSObject_initWithRawCatalogInfo_name_parentRef_ref_hfsName_hidden_':1,
    'NSHyphenator_getHyphenLocations_inString_':1,
    'NSHyphenator_getHyphenLocations_inString_wordAtIndex_':1,
    'NSImageReader_bitmapDataPlanes':1,
    'NSImageReader_loadImage_':1,
    'NSImageReader_loadImage_forImageRep_':1,
    'NSImageWriter_initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_size_':1,
    'NSImage_getImage_rect_':1,
    'NSInputContext_keyBindingState':1,
    'NSJPEGImageReader_extractHeaderInfo_':1,


    #<InterfaceBuilder>
    'NSImage_getGlobalWindowNum_frame_':1,
    'IBIncompatibleProperty_incompatiblePropertiesForDocument_version_criticalCount_':1,
    'IBIncompatibleProperty_incompatiblePropertiesForDocument_version_criticalCount_longestMessageIndex_':1,
    'IBObjCSourceParser_parseClass_':1,
    'NSView_objectAtPoint_rect_':1,
    'NSIBObjectData_restoreFromObjectDataInfo_':1,
    'NSIBObjectData_snapshotIntoObjectDataInfo_':1,
    'IBObjectContainer_decodeObjectToIntMapTableForKey_fromCoder_alwaysCreate_':1,
    'IBObjectContainer_decodeObjectToObjectMapTableForKey_fromCoder_alwaysCreate_':1,
    'IBXMLDecoder_allocObjectWithClassName_':1,
    'IBSplitScrollView_getMinimumX_maximumX_':1,

    # XXX: Loads of 10.3 stuff
    'PBXReference_pruneReferencesBySendingBooleanSelector_toObject_withContext_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXObject_copyWithZone_getUnretainedObjectMappings_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXFileType_bestFileTypeForRepresentingFileAtPath_withFileAttributes_withLessSpecificFileType_getExtraFileProperties_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXFileType_fileTypeForPath_getExtraFileProperties_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXFileType_guessFileTypeForGenericFileAtPath_withFileAttributes_getExtraFileProperties_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXCStringStorage_applyFunction_context_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXCStringStorage_offsetsOfStringsMatching_ignoreCase_matchStyle_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXThreadableWorkQueueOperation_launchExecutableAtPath_arguments_environment_workingDirectoryPath_keepStdinOpen_getErrorString_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTypeDescriptor_typeRecord':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXLexicalRules_isNumber_withRange_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXProject_expandedValueForString_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXProject_expandedValueForString_getRecursiveSettingName_options_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBTree_initMaxWidth_lookupFailedValue_keepUnique_comparisonFunction_comparisonContext_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBTree_initWithContentsOfFile_comparisonFunction_comparisonContext_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBTree_printValueFunction':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBTree_setPrintValueFunction_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXCodeSenseManager_getProjectInfo_forReference_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_expandedCurrentValueForBuildSetting_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_expandedValueForString_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_getLiteralStringValue_currentExpandedStringValue_isCurrentlyShadowed_recursiveSettingName_forBuildSettingKeyPath_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_hasOriginalForCopiedReference_usingCopiesToOriginalsMappings_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_moveBuildPhasesFromIndices_numIndices_toIndex_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXTarget_moveBuildRulesFromIndices_numIndices_toIndex_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildOperation_expandedValueForString_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildContext_expandedValueForString_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildContext_expandedValueForString_getRecursiveSettingName_options_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXSymbol_symbolRecord':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXSymbol_symbolWithSymbolRecord_projectIndex_location_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildOptionDefinition_initWithName_type_allowedValues_defaultValue_isCommon_commandLineArguments_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildSettingsDictionary_buildSettingForKeyPath_getOperation_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildSettingsDictionary_expandedBuildSettingForString_withExpansionDictionaries_getRecursiveSettingName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildSettingsDictionary_expandedBuildSettingForString_withExpansionDictionaries_getRecursiveSettingName_options_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXBuildOutputParseRule_getBuildLogMessageItem_andBuildMessage_byMatchingAgainstString_withContext_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXMemberContainerSymbol_memberSymbolsOfType_withMapTable_includingInherited_includingCategories_projectOnly_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_currentRecord':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_firstRecord':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_getCurrentRecord_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_getNextRecord_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_getPreviousRecord_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_getRecord_atRow_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_lastRecord':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_recordAtRow_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_records':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'PBXRecordVector_rowForRecord_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_dictionaryByParsingAsSimpleAssignmentsAndGetLocalizedErrorString_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_getLineStartOffsets_count_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_initWithContentsOfFile_defaultCStringEncoding_getStringEncoding_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_initWithPotentiallyMalformedUTF8Bytes_length_stopAtTrailingIncompleteUTF8Sequence_getUsedLength_getNumberOfMalformedSequences_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_initWithUnicodeOrMacOSRomanContentsOfFile_getStringEncoding_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_stringByExpandingBuildSettingsUsingDictionaries_getRecursiveSettingName_percentMacroDelegate_options_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSString_stringFromOSType_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaExceptionsAttribute_initWithName_byteStream_constantPool_': (REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaSourceAttribute_initWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaUnknownAttribute_initWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaCodeExceptionAttribute_initWithByteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSArray_arrayByRecursivelyExpandingStringValuesWithExpansionDictionaries_getRecursiveSettingName_applyStringPostprocessingSelector_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSMutableArray_correctlyRemoveObjectsFromIndices_numIndices_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSMutableArray_moveObjectsFromIndices_numIndices_toIndex_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'TSCachedFileManager_registerFileInfoDerivationFunction_forKeyName_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaInnerClassesAttribute_initWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'TSStackBacktrace_initWithStackFramesNoCopy_count_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaAttribute_attributeWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaMethod_parseMethodSignature_methodReturnType_methodArguments_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'TSMergedSortedArray_arrayWithArray_array_usingFunction_context_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'TSMergedSortedArray_initWithArray_array_usingFunction_context_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'XCStringList_initWithStrings_count_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'TSLineDataBuffer_processCompleteLinesUsingFunction_context_andRemove_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaCodeAttribute_initWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'NSDictionary_dictionaryByRecursivelyExpandingStringValuesWithExpansionDictionaries_getRecursiveSettingName_applyStringPostprocessingSelector_':(REL_OSX_10_3, TP_UNDOCUMENTED),
    'JKJavaConstantAttribute_initWithName_byteStream_constantPool_':(REL_OSX_10_3, TP_UNDOCUMENTED),


    #<PreferencePanes>
    "NSAuthorization_authorizationRef":1,
    "NSAuthorization_authorizationWithRights_flags_env_":1,
    "NSAuthorization_freeRights_":1,
    "NSAuthorization_permitRights_flags_env_rights_":1,
    "ChangeKCSettings_chSheetDidEnd_returnCode_contextInfo_":1,
    "ChangeKCSettings_prepPanel_keychain_":1,
    "ChangeKCSettings_secKeychainRef":1,
    "ChangeKCSettings_setKeychainRef_":1,
    "ChangeKCSettings_setSettings_":1,
    "CreateKeychainSavePanel_saveSheetDidEnd_returnCode_contextInfo_":1,
    "CreateKeychainSavePanel_setSaveType_":1,
    "CreateKeychainSavePanel_setUpPanelKindAndID_":1,
    "NSKeychain_beginSaveSheetForDirectory_file_password_modalForWindow_modalDelegate_didEndSelector_contextInfo_":1,
    "NSKeychain_beginSettingsSheet_modalForWindow_modalDelegate_didEndSelector_contextInfo_":1,
    "NSKeychain_copySettings_":1,
    "NSKeychain_initWithSecKeychainRef_":1,
    "NSKeychain_secKeychainRef":1,
    "NSKeychain_setSettings_":1,
    "DialogController_beginChooseIdentitySheetForWindow_modalDelegate_didEndSelector_contextInfo_displayInfo_identities_":1,
    "DialogController_beginDisplayCertGroupSheetForWindow_modalDelegate_didEndSelector_contextInfo_certificates_keychains_":1,
    "DialogController_beginDisplayCertificateSheetForWindow_modalDelegate_didEndSelector_contextInfo_certificate_keychains_":1,
    "DialogController_changeSettingsPanel_keychain_":1,
    "DialogController_changeSettingsSheet_keychain_modalForWindow_modalDelegate_didEndSelector_contextInfo_":1,
    "DialogController_chooseIdentityPanel_identities_":1,
    "DialogController_contextInfo":1,
    "DialogController_displayCertificatePanel_keychains_":1,
    "DialogController_editTrustPanel_trust_":1,
    "DialogController_editTrustSheetForWindow_modalDelegate_didEndSelector_contextInfo_displayInfo_trust_":1,
    "DialogController_keychainSavePanelForDirectory_file_attrList_":1,
    "DialogController_keychainSaveSheetForDirectory_file_password_attrs_modalForWindow_modalDelegate_didEndSelector_contextInfo_":1,
    "DialogController_setContextInfo_":1,
    "NSCertificateData_certificate":1,
    "NSCertificateData_data":1,
    "NSCertificateData_initWithCertificate_":1,
    "NSCertificateData_initWithData_":1,
    "NSCertificateData_issuer":1,
    "NSCertificateData_parseGeneralNames_":1,
    "NSCertificateData_setCertificate_":1,
    "NSCertificateData_setData_":1,
    "NSCertificateData_subject":1,
    "NSChooseIdentityPanel_chooseIdentityWithInfo_identities_":1,
    "NSChooseIdentityPanel_chosenIdentity":1,
    "NSCertDisplayPanel_displayCertificate_keychains_":1,
    "NSKeychainItem_initGenericPasswordWithServiceName_accountName_access_keychain_passwordData_":1,
    "NSKeychainItem_initInternetPasswordWithServerName_securityDomain_account_path_port_protocol_authType_access_keychain_passwordData_":1,
    "NSKeychainItem_initWithClass_attrList_access_keychain_data_":1,
    "NSKeychainItem_initWithSecKeychainItemRef_":1,
    "NSKeychainItem_secKeychainItemRef":1,
    "NSEditTrustPanel_beginEditTrustSheetForWindow_modalDelegate_didEndSelector_contextInfo_displayInfo_trust_":1,
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
    '^{_NSModalSession':1,
}


for cls in objc.getClassList():
    if cls.__name__.startswith('_'): continue
    if cls.__name__.startswith('%'): continue
    if cls.__name__ == 'Object': continue

    if cls.__name__.startswith('OC_'): continue

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
                print r, sel.signature

#print "--- SIGNATURES ----"
#sigs = PTRSIG.values()
#sigs.sort()
#print '\n'.join(sigs)
