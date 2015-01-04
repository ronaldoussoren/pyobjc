// objective.metadata exceptions file, see its document
// for information on how to update this file.
{
 "definitions": {
  "classes": {},
  "formal_protocols": {},
  "functions": {
   "AXIsProcessTrustedWithOptions": {
    "args": {
     "0": { "type_modifier": "o" }
    }
   },
   "AXMakeProcessTrusted": {
    "args": {
     "0": {}
    }
   },
   "AXObserverAddNotification": {
    "args": {
     "0": {},
     "1": {},
     "2": {},
     "3": {}
    }
   },
   "AXObserverCreate": {
    "args": {
     "1": {
      "function": {
       "args": [
        {
         "typestr": "^{__AXObserver=}"
        },
        {
         "typestr": "^{__AXUIElement=}"
        },
        {
         "typestr": "^{__CFString=}"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "v"
       }
      }
     },
     "2": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXObserverCreateWithInfoCallback": {
    "args": {
     "1": {
      "function": {
       "args": [
        {
         "typestr": "^{__AXObserver=}"
        },
        {
         "typestr": "^{__AXUIElement=}"
        },
        {
         "typestr": "^{__CFString=}"
        },
        {
         "typestr": "^{__CFDictionary=}"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "v"
       }
      }
     },
     "2": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXObserverGetRunLoopSource": {
    "args": {
     "0": {}
    },
    "retval": {}
   },
   "AXObserverRemoveNotification": {
    "args": {
     "0": {},
     "1": {},
     "2": {}
    }
   },
   "AXUIElementCopyActionDescription": {
    "args": {
     "0": {},
     "1": {},
     "2": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyActionNames": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyAttributeNames": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyAttributeValue": {
    "args": {
     "0": {},
     "1": {},
     "2": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyAttributeValues": {
    "args": {
     "0": {},
     "1": {},
     "4": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyElementAtPosition": {
    "args": {
     "0": {},
     "3": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyMultipleAttributeValues": {
    "args": {
     "0": {},
     "1": {},
     "3": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyParameterizedAttributeNames": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCopyParameterizedAttributeValue": {
    "args": {
     "0": {},
     "1": {},
     "3": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "AXUIElementCreateApplication": {
    "retval": {
     "already_cfretained": true
    }
   },
   "AXUIElementCreateSystemWide": {
    "retval": {
     "already_cfretained": true
    }
   },
   "AXUIElementGetAttributeValueCount": {
    "args": {
     "0": {},
     "1": {},
     "2": { "type_modifier": "o" }
    }
   },
   "AXUIElementGetPid": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o" }
    }
   },
   "AXUIElementIsAttributeSettable": {
    "args": {
     "0": {},
     "1": {},
     "2": { "type_modifier": "o" }
    }
   },
   "AXUIElementPerformAction": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "AXUIElementPostKeyboardEvent": {
    "args": {
     "0": {}
    }
   },
   "AXUIElementSetAttributeValue": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "AXUIElementSetMessagingTimeout": {
    "args": {
     "0": {}
    }
   },
   "AXValueCreate": {
    "args": {
     "1": {}
    },
    "retval": {
     "already_cfretained": true
    }
   },
   "AXValueGetType": {
    "args": {
     "0": {}
    }
   },
   "AXValueGetTypeID": {
    "variadic": false
   },
   "AXValueGetValue": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "AddIconToSuite": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "CopyProcessName": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "DisposeCIcon": {
    "args": {
     "0": {}
    }
   },
   "DisposeIconActionUPP": {
    "args": {
     "0": {}
    }
   },
   "DisposeIconGetterUPP": {
    "args": {
     "0": {}
    }
   },
   "DisposeIconSuite": {
    "args": {
     "0": {}
    }
   },
   "ForEachIconDo": {
    "args": {
     "0": {},
     "2": {},
     "3": {}
    }
   },
   "GetCIcon": {
    "retval": {}
   },
   "GetCurrentProcess": {
    "args": {
     "0": {}
    }
   },
   "GetFrontProcess": {
    "args": {
     "0": {}
    }
   },
   "GetIcon": {
    "retval": {}
   },
   "GetIconCacheData": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetIconCacheProc": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetIconFamilyData": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "GetIconFromSuite": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetIconRefVariant": {
    "args": {
     "0": {},
     "2": {}
    },
    "retval": {}
   },
   "GetIconSizesFromIconRef": {
    "args": {
     "1": {},
     "3": {}
    }
   },
   "GetIconSuite": {
    "args": {
     "0": {}
    }
   },
   "GetLabel": {
    "args": {
     "1": {}
    }
   },
   "GetNextProcess": {
    "args": {
     "0": {}
    }
   },
   "GetProcessBundleLocation": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetProcessForPID": {
    "args": {
     "1": {}
    }
   },
   "GetProcessInformation": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetProcessPID": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "GetSuiteLabel": {
    "args": {
     "0": {}
    }
   },
   "HIShapeContainsPoint": {
    "args": {
     "1": { "type_modifier": "n" }
    }
   },
   "HIShapeCreateMutableWithRect": {
    "args": {
     "0": { "type_modifier": "n" }
    }
   },
   "HIShapeCreateWithQDRgn": { "ignore": true },
   "HIShapeCreateWithRect": {
    "args": {
     "0": { "type_modifier": "n" }
    }
   },
   "HIShapeEnumerate": {
    "args": {
     "2": {
      "function_retained": False,
      "function": {
       "args": [
        {
         "typestr": "i"
        },
        {
         "typestr": "^{__HIShape=}"
        },
        {
         "typestr": [ "^{CGRect={CGPoint=ff}{CGSize=ff}}", "^{CGRect={CGPoint=dd}{CGSize=dd}}"  ],
	 "type_modifier": "n"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "i"
       }
      }
     },
    }
   },
   "HIShapeGetAsQDRgn": { "ignore": true },
   "HIShapeGetBounds": {
    "args": {
     "1": { "type_modifier": "n" }
    },
   },
   "HIShapeIntersectsRect": {
    "args": {
     "1": { "type_modifier": "n" }
    }
   },
   "HIShapeSetQDClip": { "ignore": true },
   "HIShapeUnionWithRect": {
    "args": {
     "1": { "type_modifier": "n"}
    }
   },
   "ICAddMapEntry": { "ignore": true },
   "ICAddProfile": { "ignore": true },
   "ICBegin": { "ignore": true },
   "ICCountMapEntries": { "ignore": true },
   "ICCountPref": { "ignore": true },
   "ICCountProfiles": { "ignore": true },
   "ICCreateGURLEvent": { "ignore": true },
   "ICDeleteMapEntry": { "ignore": true },
   "ICDeletePref": { "ignore": true },
   "ICDeleteProfile": { "ignore": true },
   "ICEditPreferences": { "ignore": true },
   "ICEnd": { "ignore": true },
   "ICFindPrefHandle": { "ignore": true },
   "ICGetConfigName": { "ignore": true },
   "ICGetCurrentProfile": { "ignore": true },
   "ICGetDefaultPref": { "ignore": true },
   "ICGetIndMapEntry": { "ignore": true },
   "ICGetIndPref": { "ignore": true },
   "ICGetIndProfile": { "ignore": true },
   "ICGetMapEntry": { "ignore": true },
   "ICGetPerm": { "ignore": true },
   "ICGetPref": { "ignore": true },
   "ICGetPrefHandle": { "ignore": true },
   "ICGetProfileName": { "ignore": true },
   "ICGetSeed": { "ignore": true },
   "ICGetVersion": { "ignore": true },
   "ICLaunchURL": { "ignore": true },
   "ICMapEntriesFilename": { "ignore": true },
   "ICMapEntriesTypeCreator": { "ignore": true },
   "ICMapFilename": { "ignore": true },
   "ICMapTypeCreator": { "ignore": true },
   "ICParseURL": { "ignore": true },
   "ICSendGURLEvent": { "ignore": true },
   "ICSetCurrentProfile": { "ignore": true },
   "ICSetMapEntry": { "ignore": true },
   "ICSetPref": { "ignore": true },
   "ICSetPrefHandle": { "ignore": true },
   "ICSetProfileName": { "ignore": true },
   "ICStart": { "ignore": true },
   "ICStop": { "ignore": true },
   "IconFamilyToIconSuite": {},
   "IconIDToRgn": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "IconMethodToRgn": {
    "args": {
     "0": {},
     "1": {},
     "3": {},
     "4": {}
    }
   },
   "IconRefContainsCGPoint": {
    "args": {
     "0": {},
     "1": {},
     "4": {}
    }
   },
   "IconRefIntersectsCGRect": {
    "args": {
     "0": {},
     "1": {},
     "4": {}
    }
   },
   "IconRefToHIShape": {
    "args": {
     "0": {},
     "3": {}
    },
    "retval": {}
   },
   "IconRefToIconFamily": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "IconRefToRgn": {
    "args": {
     "0": {},
     "1": {},
     "4": {}
    }
   },
   "IconSuiteToIconFamily": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "IconSuiteToRgn": {
    "args": {
     "0": {},
     "1": {},
     "3": {}
    }
   },
   "InvokeIconActionUPP": {
    "args": {
     "1": {},
     "2": {},
     "3": {}
    }
   },
   "InvokeIconGetterUPP": {
    "args": {
     "1": {},
     "2": {}
    },
    "retval": {}
   },
   "IsIconRefMaskEmpty": {
    "args": {
     "0": {}
    }
   },
   "IsProcessVisible": {
    "args": {
     "0": {}
    }
   },
   "KillProcess": {
    "args": {
     "0": {}
    }
   },
   "LaunchApplication": {
    "args": {
     "0": {}
    }
   },
   "LoadIconCache": {
    "args": {
     "0": {},
     "3": {}
    }
   },
   "MakeIconCache": {
    "args": {
     "0": {},
     "1": {},
     "2": {}
    }
   },
   "NewIconActionUPP": {
    "args": {
     "0": {
      "function": {
       "args": [
        {
         "typestr": "I"
        },
        {
         "typestr": "^^^c"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "s"
       }
      }
     }
    },
    "retval": {}
   },
   "NewIconGetterUPP": {
    "args": {
     "0": {
      "function": {
       "args": [
        {
         "typestr": "I"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "^^c"
       }
      }
     }
    },
    "retval": {}
   },
   "NewIconSuite": {
    "args": {
     "0": {}
    }
   },
   "PasteboardClear": {
    "args": {
     "0": {}
    }
   },
   "PasteboardCopyItemFlavorData": {
    "args": {
     "0": {},
     "1": {},
     "2": {},
     "3": {}
    }
   },
   "PasteboardCopyItemFlavors": {
    "args": {
     "0": {},
     "1": {},
     "2": {}
    }
   },
   "PasteboardCopyName": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PasteboardCopyPasteLocation": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PasteboardCreate": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PasteboardGetItemCount": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PasteboardGetItemFlavorFlags": {
    "args": {
     "0": {},
     "1": {},
     "2": {},
     "3": {}
    }
   },
   "PasteboardGetItemIdentifier": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "PasteboardPutItemFlavor": {
    "args": {
     "0": {},
     "1": {},
     "2": {},
     "3": {}
    }
   },
   "PasteboardResolvePromises": {
    "args": {
     "0": {}
    }
   },
   "PasteboardSetPasteLocation": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PasteboardSetPromiseKeeper": {
    "args": {
     "0": {},
     "1": {
      "function": {
       "args": [
        {
         "typestr": "^{OpaquePasteboardRef=}"
        },
        {
         "typestr": "^v"
        },
        {
         "typestr": "^{__CFString=}"
        },
        {
         "typestr": "^v"
        }
       ],
       "retval": {
        "typestr": "i"
       }
      }
     },
     "2": {}
    }
   },
   "PasteboardSynchronize": {
    "args": {
     "0": {}
    }
   },
   "PlotCIcon": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PlotCIconHandle": {
    "args": {
     "0": {},
     "3": {}
    }
   },
   "PlotIcon": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "PlotIconHandle": {
    "args": {
     "0": {},
     "3": {}
    }
   },
   "PlotIconID": {
    "args": {
     "0": {}
    }
   },
   "PlotIconMethod": {
    "args": {
     "0": {},
     "3": {},
     "4": {}
    }
   },
   "PlotIconRef": {
    "args": {
     "0": {},
     "4": {}
    }
   },
   "PlotIconRefInContext": {
    "args": {
     "0": {},
     "1": {},
     "4": {},
     "6": {}
    }
   },
   "PlotIconSuite": {
    "args": {
     "0": {},
     "3": {}
    }
   },
   "PlotSICNHandle": {
    "args": {
     "0": {},
     "3": {}
    }
   },
   "ProcessInformationCopyDictionary": {
    "args": {
     "0": {}
    },
    "retval": {
     "already_cfretained": true
    }
   },
   "PtInIconID": {
    "args": {
     "1": {}
    }
   },
   "PtInIconMethod": {
    "args": {
     "1": {},
     "3": {},
     "4": {}
    }
   },
   "PtInIconRef": {
    "args": {
     "0": {},
     "1": {},
     "4": {}
    }
   },
   "PtInIconSuite": {
    "args": {
     "1": {},
     "3": {}
    }
   },
   "RectInIconID": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "RectInIconMethod": {
    "args": {
     "0": {},
     "1": {},
     "3": {},
     "4": {}
    }
   },
   "RectInIconRef": {
    "args": {
     "0": {},
     "1": {},
     "4": {}
    }
   },
   "RectInIconSuite": {
    "args": {
     "0": {},
     "1": {},
     "3": {}
    }
   },
   "SameProcess": {
    "args": {
     "0": {},
     "1": {},
     "2": {}
    }
   },
   "SetFrontProcess": {
    "args": {
     "0": {}
    }
   },
   "SetFrontProcessWithOptions": {
    "args": {
     "0": {}
    }
   },
   "SetIconCacheData": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "SetIconCacheProc": {
    "args": {
     "0": {},
     "1": {}
    }
   },
   "SetIconFamilyData": {
    "args": {
     "0": {},
     "2": {}
    }
   },
   "SetSuiteLabel": {
    "args": {
     "0": {}
    }
   },
   "ShowHideProcess": {
    "args": {
     "0": {}
    }
   },
   "TransformProcessType": {
    "args": {
     "0": {}
    }
   },
   "TranslationCopyDestinationType": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "TranslationCopySourceType": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "TranslationCreate": {
    "args": {
     "0": {},
     "1": {},
     "3": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "TranslationCreateWithSourceArray": {
    "args": {
     "0": {},
     "2": { "type_modifier": "o", "already_cfretained": true },
     "3": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "TranslationGetTranslationFlags": {
    "args": {
     "0": {},
     "1": { "type_modifier": "o" }
    }
   },
   "TranslationPerformForData": {
    "args": {
     "0": {},
     "1": {},
     "2": { "type_modifier": "o", "already_cfretained": true }
    }
   },
   "TranslationPerformForFile": {
    "args": {
     "0": {},
     "1": { "type_modifier": "n" },
     "2": { "type_modifier": "n" },
     "3": {},
     "4": { "type_modifier": "o" }
    }
   },
   "TranslationPerformForURL": {
    "args": {
     "0": {},
     "1": {},
     "2": {},
     "3": { "type_modifier": "o", "already_cfretained": true}
    }
   },
   "UAZoomChangeFocus": {
    "args": {
     "0": { "type_modifier": "n" },
     "1": { "type_modifier": "n" }
    }
   },
   "WakeUpProcess": {
    "args": {
     "0": {}
    }
   }
  },
  "informal_protocols": {},
  "structs": {
   "ICDirSpec": { "ignore": true },
   "ICFontRecord": { "ignore": true },
   "ICCharTable": { "ignore": true },
   "ICAppSpec": { "ignore": true },
   "ICAppSpecList": { "ignore": true },
   "ICFileSpec": { "ignore": true },
   "ICMapEntry": { "ignore": true },
   "ICServiceEntry": { "ignore": true },
   "ICServices": { "ignore": true }
  },
  "enum": {
   "icPrefNotFoundErr": { "ignore": true },
   "icPermErr": { "ignore": true },
   "icPrefDataErr": { "ignore": true },
   "icInternalErr": { "ignore": true },
   "icTruncatedErr": { "ignore": true },
   "icNoMoreWritersErr": { "ignore": true },
   "icNothingToOverrideErr": { "ignore": true },
   "icNoURLErr": { "ignore": true },
   "icConfigNotFoundErr": { "ignore": true },
   "icConfigInappropriateErr": { "ignore": true },
   "icProfileNotFoundErr": { "ignore": true },
   "icTooManyProfilesErr": { "ignore": true },
   "kICComponentInterfaceVersion0": { "ignore": true },
   "kICComponentInterfaceVersion1": { "ignore": true },
   "kICComponentInterfaceVersion2": { "ignore": true },
   "kICComponentInterfaceVersion3": { "ignore": true },
   "kICComponentInterfaceVersion4": { "ignore": true },
   "kICComponentInterfaceVersion": { "ignore": true },
   "kICAttrLockedBit": { "ignore": true },
   "kICAttrVolatileBit": { "ignore": true },
   "kICAttrNoChange": { "ignore": true },
   "kICAttrLockedMask": { "ignore": true },
   "kICAttrVolatileMask": { "ignore": true },
   "icNoPerm": { "ignore": true },
   "icReadOnlyPerm": { "ignore": true },
   "icReadWritePerm": { "ignore": true },
   "kICNilProfileID": { "ignore": true },
   "kICNoUserInteractionBit": { "ignore": true },
   "kICNoUserInteractionMask": { "ignore": true },
   "kICFileType": { "ignore": true },
   "kICCreator": { "ignore": true },
   "kICFileSpecHeaderSize": { "ignore": true },
   "kInternetEventClass": { "ignore": true },
   "kAEGetURL": { "ignore": true },
   "kAEFetchURL": { "ignore": true },
   "keyAEAttaching": { "ignore": true },
   "kICEditPreferenceEventClass": { "ignore": true },
   "kICEditPreferenceEvent": { "ignore": true },
   "keyICEditPreferenceDestination": { "ignore": true },
   "kICComponentVersion": { "ignore": true },
   "kICNumVersion": { "ignore": true },
   "kICMapFixedLength": { "ignore": true },
   "kICServicesTCPBit": { "ignore": true },
   "kICServicesUDPBit": { "ignore": true },
   "kICServicesTCPMask": { "ignore": true },
   "kICServicesUDPMask": { "ignore": true },
   "kICMapBinaryBit": { "ignore": true },
   "kICMapResourceForkBit": { "ignore": true },
   "kICMapDataForkBit": { "ignore": true },
   "kICMapPostBit": { "ignore": true },
   "kICMapNotIncomingBit": { "ignore": true },
   "kICMapNotOutgoingBit": { "ignore": true },
   "kICMapBinaryMask": { "ignore": true },
   "kICMapResourceForkMask": { "ignore": true },
   "kICMapDataForkMask": { "ignore": true },
   "kICMapPostMask": { "ignore": true },
   "kICMapNotIncomingMask": { "ignore": true },
   "kICMapNotOutgoingMask": { "ignore": true }
  },
  "literals": {
   "kICArchieAll": { "ignore": true },
   "kICArchiePreferred": { "ignore": true },
   "kICCharacterSet": { "ignore": true },
   "kICDocumentFont": { "ignore": true },
   "kICDownloadFolder": { "ignore": true },
   "kICEmail": { "ignore": true },
   "kICFTPHost": { "ignore": true },
   "kICFTPProxyAccount": { "ignore": true },
   "kICFTPProxyHost": { "ignore": true },
   "kICFTPProxyPassword": { "ignore": true },
   "kICFTPProxyUser": { "ignore": true },
   "kICFingerHost": { "ignore": true },
   "kICGopherHost": { "ignore": true },
   "kICGopherProxy": { "ignore": true },
   "kICHTTPProxyHost": { "ignore": true },
   "kICHelper": { "ignore": true },
   "kICHelperDesc": { "ignore": true },
   "kICHelperList": { "ignore": true },
   "kICIRCHost": { "ignore": true },
   "kICInfoMacAll": { "ignore": true },
   "kICInfoMacPreferred": { "ignore": true },
   "kICLDAPSearchbase": { "ignore": true },
   "kICLDAPServer": { "ignore": true },
   "kICListFont": { "ignore": true },
   "kICMacSearchHost": { "ignore": true },
   "kICMailAccount": { "ignore": true },
   "kICMailHeaders": { "ignore": true },
   "kICMailPassword": { "ignore": true },
   "kICMapping": { "ignore": true },
   "kICNNTPHost": { "ignore": true },
   "kICNTPHost": { "ignore": true },
   "kICNewMailDialog": { "ignore": true },
   "kICNewMailFlashIcon": { "ignore": true },
   "kICNewMailPlaySound": { "ignore": true },
   "kICNewMailSoundName": { "ignore": true },
   "kICNewsAuthPassword": { "ignore": true },
   "kICNewsAuthUsername": { "ignore": true },
   "kICNewsHeaders": { "ignore": true },
   "kICNoProxyDomains": { "ignore": true },
   "kICOrganization": { "ignore": true },
   "kICPhHost": { "ignore": true },
   "kICPlan": { "ignore": true },
   "kICPrinterFont": { "ignore": true },
   "kICQuotingString": { "ignore": true },
   "kICRTSPProxyHost": { "ignore": true },
   "kICRealName": { "ignore": true },
   "kICReservedKey": { "ignore": true },
   "kICSMTPHost": { "ignore": true },
   "kICScreenFont": { "ignore": true },
   "kICServices": { "ignore": true },
   "kICSignature": { "ignore": true },
   "kICSnailMailAddress": { "ignore": true },
   "kICSocksHost": { "ignore": true },
   "kICTelnetHost": { "ignore": true },
   "kICUMichAll": { "ignore": true },
   "kICUMichPreferred": { "ignore": true },
   "kICUseFTPProxy": { "ignore": true },
   "kICUseGopherProxy": { "ignore": true },
   "kICUseHTTPProxy": { "ignore": true },
   "kICUsePassiveFTP": { "ignore": true },
   "kICUseRTSPProxy": { "ignore": true },
   "kICUseSocks": { "ignore": true },
   "kICWAISGateway": { "ignore": true },
   "kICWWWHomePage": { "ignore": true },
   "kICWebBackgroundColour": { "ignore": true },
   "kICWebReadColor": { "ignore": true },
   "kICWebSearchPagePrefs": { "ignore": true },
   "kICWebTextColor": { "ignore": true },
   "kICWebUnderlineLinks": { "ignore": true },
   "kICWebUnreadColor": { "ignore": true },
   "kICWhoisHost": { "ignore": true }
  },
  "cftypes": {
   "AXObserverRef": {
    "gettypeid_func": "AXObserverGetTypeID",
    "typestr": "^{__AXObserver=}"
   },
   "AXUIElementRef": {
    "gettypeid_func": "AXUIElementGetTypeID",
    "typestr": "^{__AXUIElement=}"
   },
   "AXValueRef": {
    "gettypeid_func": "AXValueGetTypeID",
    "typestr": "^{__AXValue=}"
   },
   "HIShapeRef": {
    "gettypeid_func": "HIShapeGetTypeID",
    "typestr": "^{__HIShape=}"
   },
   "TranslationRef": {
    "gettypeid_func": "TranslationGetTypeID",
    "typestr": "^{OpaqueTranslationRef=}"
   }
  }
 }
}
