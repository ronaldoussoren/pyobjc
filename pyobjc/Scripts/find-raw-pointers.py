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
import AppKit
import PreferencePanes
import ScreenSaver
import InterfaceBuilder
import AddressBook

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
    'NSBitmapImageRep_getBitmapDataPlanes_':1,
    'NSBitmapImageRep_getTIFFCompressionTypes_count_':1,
    'NSBitmapImageRep_initWithBitmapDataPlanes_pixelsWide_pixelsHigh_bitsPerSample_samplesPerPixel_hasAlpha_isPlanar_colorSpaceName_bytesPerRow_bitsPerPixel_':1,
    'NSFont_positionsForCompositeSequence_numberOfGlyphs_pointArray_':1,
    'NSSimpleHorizontalTypesetter_baseOfTypesetterGlyphInfo':1,
    'NSSimpleHorizontalTypesetter_layoutGlyphsInHorizontalLineFragment_baseline_':1,
    'NSWindow_graphicsPort':1,
    'NSWindow_initWithWindowRef_':1,
    'NSWindow_windowRef':1,
    'NSLayoutManager_getGlyphs_range_':1,
    'NSLayoutManager_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_':1,
    'NSLayoutManager_getGlyphsInRange_glyphs_characterIndexes_glyphInscriptions_elasticBits_bidiLevels_':1,
    'NSLayoutManager_rectArrayForCharacterRange_withinSelectedCharacterRange_inTextContainer_rectCount_':1,
    'NSLayoutManager_rectArrayForGlyphRange_withinSelectedGlyphRange_inTextContainer_rectCount_':1,
    'NSQuickDrawView_qdPort':1,
    'NSOpenGLContext_getValues_forParameter_':1,
    'NSOpenGLContext_setOffScreen_width_height_rowbytes_':1,
    'NSOpenGLPixelFormat_getValues_forAttribute_forVirtualScreen_':1,
    'NSOpenGLPixelFormat_initWithAttributes_':1,
    'NSView_sortSubviewsUsingFunction_context_':1,
    'NSGraphicsContext_focusStack':1,
    'NSGraphicsContext_graphicsPort':1,
    'NSGraphicsContext_initWithHostName_serverName_textProc_errorProc_timeout_secure_encapsulated_':1,
    'NSGraphicsContext_initWithMutableData_forDebugging_languageEncoding_nameEncoding_textProc_errorProc_':1,
    'NSGraphicsContext_setFocusStack_':1,
    'NSMovie_initWithMovie_':1,
    'NSMatrix_sortUsingFunction_context_':1,


    

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

    #<AddressBook>
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
    'IBObjCSourceParser_parseClass_':1,
    'NSView_objectAtPoint_rect_':1,
    'NSIBObjectData_restoreFromObjectDataInfo_':1,
    'NSIBObjectData_snapshotIntoObjectDataInfo_':1,
    'IBObjectContainer_decodeObjectToIntMapTableForKey_fromCoder_alwaysCreate_':1,
    'IBObjectContainer_decodeObjectToObjectMapTableForKey_fromCoder_alwaysCreate_':1,
    'IBXMLDecoder_allocObjectWithClassName_':1,
    'IBSplitScrollView_getMinimumX_maximumX_':1,

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

#print "--- SIGNATURES ----"
#sigs = PTRSIG.values()
#sigs.sort()
#print '\n'.join(sigs)
