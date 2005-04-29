#
# This script generates part of the python-wrappers around Cocoa.
#
# This script is based on some (not to clever) regular expressions, and seems
# to work pretty well with the current version of the Cocoa headers.
#
# NOTES:
# - This script is probably MacOSX specific.
# - This script should be rewritten, it's getting unmaintainable.
#
import enum_generator
import strconst_generator
import var_generator
import func_collector
import func_builder
import os
import sys
from dupfile import dupfile

#
# This script contains some MacOS X version dependencies. Because uname
# doesn't tell anything usefull, we use sw_vers to find the actual OS version.
#
import os
import sys
VER=None

if sys.platform == "darwin":
    fd = os.popen('/usr/bin/sw_vers', 'r')
    for ln in fd.readlines():
        if ln.startswith('ProductVersion:'):
            VER=ln.split()[-1]
    fd.close()
    fd = None
    VER = 'MacOS X ' + '.'.join(VER.split('.')[:2])

    FRAMEWORKS="/System/Library/Frameworks"
    def pathjoin(*args):
        res = os.path.join(*args)
        if not os.path.exists(res):
            return None
        return res

    ADDRESSBOOK_HDRS=pathjoin(FRAMEWORKS, "AddressBook.framework", "Headers")
    APPKIT_HDRS=pathjoin(FRAMEWORKS, "AppKit.framework", "Headers")
    FOUNDATION_HDRS=pathjoin(FRAMEWORKS, "Foundation.framework", "Headers")
    FOUNDATION_FUNCTION_PREFIX="FOUNDATION_EXPORT"
    FOUNDATION_INLINE_PREFIX='FOUNDATION_STATIC_INLINE'
    FOUNDATION_VAR_PREFIX="FOUNDATION_EXPORT"

    IB_HDRS=pathjoin(FRAMEWORKS, "InterfaceBuilder.framework", "Headers")
    PREFPANES_HDRS=pathjoin(FRAMEWORKS, "PreferencePanes.framework", "Headers")
    SECINT_HDRS=pathjoin(FRAMEWORKS, "SecurityInterface.framework", "Headers")

    WEBKIT_HDRS=pathjoin(FRAMEWORKS, "WebKit.framework", "Headers")
    APPLESCRIPTKIT_HDRS=pathjoin(FRAMEWORKS, "AppleScriptKit.framework", "Headers")
    APPKITSCRIPTING_HDRS=pathjoin(FRAMEWORKS, "AppKitScripting.framework", "Headers")
    AUTOMATOR_HDRS=pathjoin(FRAMEWORKS, "Automator.framework", "Headers")
    COREDATA_HDRS=pathjoin(FRAMEWORKS, "CoreData.framework", "Headers")
    SYNCSERVICES_HDRS=pathjoin(FRAMEWORKS, "SyncServices.framework", "Headers")
    XGRIDFOUNDATION_HDRS=pathjoin(FRAMEWORKS, "XgridFoundation.framework", "Headers")

    EXCHND_HDRS=pathjoin(FRAMEWORKS, "ExceptionHandling.framework", "Headers")

else:
    # This is probably incorrect, and was added to help a future
    # port to GNUstep
    x = os.uname()
    VER = x[0] + ' ' + x[2]

    HDR_BASE=os.environ.get('GNUSTEP_SYSTEM_ROOT')
    HDR_BASE=os.path.join(HDR_BASE, "Library", "Headers")

    ADDRESSBOOK_HDRS=os.path.join(HDR_BASE, "AddressBook")
    if not os.path.exists(ADDRESSBOOK_HDRS):
        ADDRESSBOOK_HDRS=None

    APPKIT_HDRS=os.path.join(HDR_BASE, "AppKit")
    if not os.path.exists(APPKIT_HDRS):
        APPKIT_HDRS=None

    FOUNDATION_HDRS=os.path.join(HDR_BASE, "Foundation")
    FOUNDATION_FUNCTION_PREFIX="GS_EXPORT"
    FOUNDATION_INLINE_PREFIX='GS_GEOM_SCOPE'
    FOUNDATION_VAR_PREFIX="GS_EXPORT"
    if not os.path.exists(FOUNDATION_HDRS):
        FOUNDATION_HDRS=None

    IB_HDRS=os.path.join(HDR_BASE, "InterfaceBuilder")
    if not os.path.exists(IB_HDRS):
        IB_HDRS=None

    PREFPANES_HDRS=os.path.join(HDR_BASE, "PreferencePanes")
    if not os.path.exists(PREFPANES_HDRS):
        PREFPANES_HDRS=None

    WEBKIT_HDRS=os.path.join(HDR_BASE, "WebKit")
    if not os.path.exists(WEBKIT_HDRS):
        WEBKIT_HDRS=None

    EXCHND_HDRS=os.path.join(HDR_BASE, "ExceptionHandling")
    if not os.path.exists(EXCHND_HDRS):
        EXCHND_HDRS=None

    SECINT_HDRS=os.path.join(HDR_BASE, "SecurityInterface")
    if not os.path.exists(SECINT_HDRS):
        SECINT_HDRS=None

    APPLESCRIPTKIT_HDRS=None
    APPKITSCRIPTING_HDRS=None
    AUTOMATOR_HDRS=None
    COREDATA_HDRS=None
    SYNCSERVICES_HDRS=None
    XGRIDFOUNDATION_HDRS=None



if not os.path.isdir('Modules'):
    print "Run me from the root of the PyObjC source tree"
    sys.exit(1)

if not os.path.exists('build'):
    os.mkdir('build')

if not os.path.exists('build/codegen'):
    os.mkdir('build/codegen')



def filterAddressBookHeaders(fn):
    if fn[-3:] == 'C.h':
        return 0

    if fn == 'ABPeoplePickerView.h':
        return 0

    return 1

if FOUNDATION_HDRS is not None:
    enum_generator.generate(
            FOUNDATION_HDRS,
            'build/codegen/_Fnd_Enum.inc',
            ignore_files=['NSCompatibility.h', 'NSSerialization.h', 'NSUtilities.h'])
    strconst_generator.generate(
            FOUNDATION_HDRS,
            'build/codegen/_Fnd_Str.inc',
            ignore=(
                # Declared on GNUstep, but not actually inside the
                # shared lib?
                'ConnectionBecameInvalidNotification',
            )
    )
    FOUNDATION_IGNORE_LIST=(
        # All have types that are not (yet) mapped to python
        "NSNonOwnedPointerHashCallBacks",
        "NSNonRetainedObjectHashCallBacks",
        "NSObjectHashCallBacks",
        "NSOwnedObjectIdentityHashCallBacks",
        "NSOwnedPointerHashCallBacks",
        "NSPointerToStructHashCallBacks",
        "NSIntMapKeyCallBacks",
        "NSNonOwnedPointerMapKeyCallBacks",
        "NSNonOwnedPointerOrNullMapKeyCallBacks",
        "NSNonRetainedObjectMapKeyCallBacks",
        "NSObjectMapKeyCallBacks",
        "NSOwnedPointerMapKeyCallBacks",
        "NSIntMapValueCallBacks",
        "NSNonOwnedPointerMapValueCallBacks",
        "NSObjectMapValueCallBacks",
        "NSNonRetainedObjectMapValueCallBacks",
        "NSOwnedPointerMapValueCallBacks",
        "NSIntHashCallBacks",
        "NSHangOnMallocError",
    )

    var_generator.generate(
            FOUNDATION_HDRS,
            'build/codegen/_Fnd_Var.inc',
            FOUNDATION_VAR_PREFIX,
            FOUNDATION_IGNORE_LIST)

    FOUNDATION_IGNORE_LIST=(
        # Private functions
        '_NSAddHandler2(',
        '_NSRemoveHandler2(',
        '_NSExceptionObjectFromHandler2(',
        '_NSAutoreleaseNoPool(',
        '_NSAutoreleaseFreedObject(',
        '_NSAutoreleaseHighWaterLog(',
        'NXReadNSObjectFromCoder(',


        # List of functions that are not usefull from Python:
        'NSFrameAddress(',
        'NSReturnAddress(',
        'NSRecordAllocationEvent(',
        'NSCreateHashTableWithZone(',
        'NSCreateHashTable(',
        'NSFreeHashTable(',
        'NSResetHashTable(',
        'NSCompareHashTables(',
        'NSCopyHashTableWithZone(',
        'NSHashGet(',
        'NSHashInsert(',
        'NSHashInsertKnownAbsent(',
        'NSHashInsertIfAbsent(',
        'NSHashRemove(',
        'NSEnumerateHashTable(',
        'NSNextHashEnumeratorItem(',
        'NSEndHashTableEnumeration(',
        'NSCountHashTable(',
        'NSStringFromHashTable(',
        'NSAllHashTableObjects(',
        'NSJavaClassesFromPath(',
        'NSJavaClassesForBundle(',
        'NSCreateMapTableWithZone(',
        'NSCreateMapTable(',
        'NSFreeMapTable(',
        'NSResetMapTable(',
        'NSCompareMapTables(',
        'NSCopyMapTableWithZone(',
        'NSMapMember(',
        'NSMapGet(',
        'NSMapInsert(',
        'NSMapInsertKnownAbsent(',
        'NSMapInsertIfAbsent(',
        'NSMapRemove(',
        'NSEnumerateMapTable(',
        'NSNextMapEnumeratorPair(',
        'NSEndMapTableEnumeration(',
        'NSCountMapTable(',
        'NSStringFromMapTable(',
        'NSAllMapTableKeys(',
        'NSAllMapTableValues(',
        'NSGetSizeAndAlignment(', # Hmm, shouldn't we use this in the bridge?
        'NSLogv(',
        'NSLog(',
        'NSAllocateObject(',
        'NSCopyObject(',
        'NSShouldRetainWithZone(',
        'NSAllocateMemoryPages(',
        'NSDeallocateMemoryPages(',
        'NSCopyMemoryPages(',


        # List of manually wrapped functions:
        'NSFileTypeForHFSTypeCode(',
        'NSHFSTypeCodeFromFileType(',
        'NSStringFromPoint',
        'NSDivideRect(',

        # Zones might be usefull someday
        'NSCreateZone(',
        'NSRecycleZone(',
        'NSSetZoneName(',
        'NSZoneName(',
        'NSZoneFromPointer(',
        'NSZoneMalloc(',
        'NSZoneCalloc(',
        'NSZoneRealloc(',
        'NSZoneFree(',
        'NSDefaultMallocZone(',

        # TODO
        'NSUncaughtExceptionHandler(',
        'NSSetUncaughtExceptionHandler(',
        'NSGetUncaughtExceptionHandler(',

        # GNUstep functions
        'GSDebugAllocationClassList(',
        '_NSAddHandler(',
        '_NSRemoveHandler(',
        'NSStringFromMapTable(',
        'GSLogLock(',
        'NSLogv (',
        'NSLog (',
        'NSCreateZone (',
        'NSZoneFromPointer (',
        'NSZoneCalloc (',
        'NSSetZoneName (',
        'NSAllocateMemoryPages (',
        'NSDeallocateMemoryPages (',
        'NSCopyMemoryPages (',
        'GSDebugAllocation',
        'NSStringFromMapTable (',
        'NSDeallocateObject(',
        'GSDebugFunctionMsg(',
        'GSDebugMethodMsg(',
    )

    func_collector.generate(
            FOUNDATION_HDRS,
            'build/codegen/Foundation.prototypes',
            FOUNDATION_FUNCTION_PREFIX,
            FOUNDATION_IGNORE_LIST)

    func_collector.generate(
            FOUNDATION_HDRS,
            'build/codegen/Foundation.prototype2',
            FOUNDATION_INLINE_PREFIX,
            FOUNDATION_IGNORE_LIST)



    for arg in [
        'NSSearchPathDomainMask', 'NSCalculationError',
        'NSComparisonResult', 'NSInsertionPosition',
        'NSNotificationCoalescing', 'NSNotificationCoalescing',
        'NSRectEdge', 'NSRelativePosition',
        'NSRoundingMode', 'NSSaveOptions', 'NSSearchPathDirectory',
        'NSSearchPathDomainMask', 'NSTestComparisonOperation',
        'NSURLHandleStatus', 'NSWhoseSubelementIdentifier']:
        func_builder.TYPE_ALIASES[arg] = 'int'

    func_builder.TYPE_ALIASES['NSGlyph'] = 'unsigned int'

    func_builder.IGNORE_VARARGS.extend([
        # Some of these are Foundation some are AppKit
        'NSGetInformationalAlertPanel',
        'NSRunAlertPanel',
        'NSRunInformationalAlertPanel',
        'NSRunCriticalAlertPanel',
        'NSRunAlertPanelRelativeToWindow',
        'NSRunInformationalAlertPanelRelativeToWindow',
        'NSRunCriticalAlertPanelRelativeToWindow',
        'NSBeginAlertSheet',
        'NSBeginInformationalAlertSheet',
        'NSBeginCriticalAlertSheet',
        'NSGetAlertPanel',
        'NSGetCriticalAlertPanel',
    ])

    def BeginSheetMapper(funcname, args):
        new_args = []
        for tp, name in args:
            if name == 'contextInfo':
                tp = 'PYOBJC_VOIDPTR'
            new_args.append((tp, name))
        return tuple(new_args)

    func_builder.FUNC_MAP['NSBeginAlertSheet'] = BeginSheetMapper
    func_builder.FUNC_MAP['NSBeginInformationalAlertSheet'] = BeginSheetMapper
    func_builder.FUNC_MAP['NSBeginCriticalAlertSheet'] = BeginSheetMapper

    fd = dupfile('build/codegen/_Fnd_Functions.inc', 'w')

    func_builder.SIMPLE_TYPES['NSDecimal*'] = (
            '\tresult = Decimal_New(%(varname)s);\n\tif (result == NULL) return NULL;',
            'O&',
            'Decimal_Convert, &%(varname)s'
        )

    structs = ['NSPoint', 'NSSize', 'NSRect', 'NSRange', 'NSSwappedFloat', 'NSSwappedDouble']
    if sys.platform == 'darwin':
        structs.append('NSTimeInterval')
    for s in structs:
        func_builder.SIMPLE_TYPES[s] = (
            '\tresult = PyObjC_ObjCToPython(@encode(%s), (void*)&%%(varname)s); \n\tif (result == NULL) return NULL;'%s,
            'O&',
            'convert_%s, &%%(varname)s'%s
        )
        fd.write('''\

    static inline int convert_%(type)s(PyObject* object, void* pvar)
    {
            int err;

            err = PyObjC_PythonToObjC(@encode(%(type)s), object, pvar);
            if (err == -1) {
                    return 0;
            }
            return 1;
    }
    '''%{'type': s })

    fd.write('typedef void* PYOBJC_VOIDPTR;\n')

    funcs = func_builder.process_list(fd , file('build/codegen/Foundation.prototypes'))
    funcs2 = func_builder.process_list(fd , file('build/codegen/Foundation.prototype2'))

    # These are macro's
    funcs3 = func_builder.process_list(fd, [
        'NSString* NSLocalizedString(NSString* key, NSString* comment);',
        'NSString* NSLocalizedStringFromTable(NSString* key, NSString* tableName, NSString* comment);',
        'NSString* NSLocalizedStringFromTableInBundle(NSString* key, NSString* tableName, NSString* comment, NSBundle* bunlde);',
    ])
    func_builder.gen_method_table_entries(fd, funcs + funcs2 + funcs3)
    fd = None
    for s in structs:
        del func_builder.SIMPLE_TYPES[s]


if APPKIT_HDRS is not None:
    enum_generator.generate(
            APPKIT_HDRS,
            'build/codegen/_App_Enum.inc')

    strconst_generator.generate(
            APPKIT_HDRS,
            'build/codegen/_App_Str.inc')
    APPKIT_PREFIX="APPKIT_EXTERN"
    APPKIT_IGNORE_LIST=(
        # First two have types that are not yet mapped
        'NSIconSize',
        'NSTokenSize',

        # NSApp is a 'real' variable, will probably add get/set functions
        'NSApp')

    var_generator.generate(
            APPKIT_HDRS,
            'build/codegen/_App_Var.inc',
            APPKIT_PREFIX,
            APPKIT_IGNORE_LIST)

    APPKIT_IGNORE_LIST=(
        # List of manually wrapped functions:
        'NSApplicationMain(',
        'NSCountWindows(',
        'NSCountWindowsForContext(',
        'NSAvailableWindowDepths(',
        'NSRectFillList(',
        'NSGetWindowServerMemory(',
        'NSDrawTiledRects(',
        'NSDrawColorTiledRects(',
        'NSRectFillListWithGrays(',
        'NSRectFillListWithColors(',
        'NSRectFillListUsingOperation(',
        'NSRectFillListWithColorsUsingOperation(',
        'NSRectClipList(',
        'NSWindowList(',
        'NSWindowListForContext(',
        'NSBestDepth (',
        'NSAvailableWindowDepths (',

        #TODO:
        'NSDrawBitmap(',
    )

    if VER == "MacOS X 10.1":
        APPKIT_IGNORE_LIST = APPKIT_IGNORE_LIST + ('NSCopyBitmapFromGState',)

    func_collector.generate(
            APPKIT_HDRS,
            'build/codegen/AppKit.prototypes',
            APPKIT_PREFIX,
            APPKIT_IGNORE_LIST)

    func_builder.FUNC_MAP['NSShowAnimationEffect'] = BeginSheetMapper

    fd = dupfile('build/codegen/_App_Functions.inc', 'w')
    structs = ['NSAffineTransformStruct', 'NSRect', 'NSPoint']
    for s in structs:
        func_builder.SIMPLE_TYPES[s] = (
            '\tresult = PyObjC_ObjCToPython(@encode(%s), (void*)&%%(varname)s); \n\tif (result == NULL) return NULL;'%s,
            'O&',
            'convert_%s, &%%(varname)s'%s
        )
        fd.write('''\
    static inline int convert_%(type)s(PyObject* object, void* pvar)
    {
            int err;

            err = PyObjC_PythonToObjC(@encode(%(type)s), object, pvar);
            if (err == -1) {
                    return 0;
            }
            return 1;
    }
    '''%{'type': s })

    for arg in [
        'NSApplicationTerminateReply', 'NSBackingStoreType',
        'NSBezelStyle', 'NSBezierPathElement',
        'NSBitmapImageFileType', 'NSBorderType', 'NSBoxType',
        'NSButtonType', 'NSCellAttribute', 'NSCellImagePosition',
        'NSCellStateValue', 'NSCellType', 'NSCompositingOperation',
        'NSControlSize', 'NSControlTint', 'NSDocumentChangeType',
        'NSDragOperation', 'NSDrawerState', 'NSEventType',
        'NSFocusRingPlacement', 'NSFontAction', 'NSFontTraitMask',
        'NSGlyph', 'NSGlyphInscription', 'NSGlyphLayoutMode',
        'NSGlyphRelation', 'NSGradientType', 'NSImageAlignment',
        'NSImageFrameStyle', 'NSImageInterpolation', 'NSImageScaling',
        'NSInterfaceStyle', 'NSLayoutDirection', 'NSLayoutStatus',
        'NSLineBreakMode', 'NSLineCapStyle', 'NSLineJoinStyle',
        'NSLineMovementDirection', 'NSLineSweepDirection',
        'NSMatrixMode', 'NSMultibyteGlyphPacking', 'NSOpenGLContextParameter',
        'NSOpenGLGlobalOption', 'NSOpenGLPixelFormatAttribute',
        'NSPopUpArrowPosition', 'NSPrinterTableStatus',
        'NSPrintingOrientation', 'NSPrintingPageOrder',
        'NSPrintingPaginationMode', 'NSProgressIndicatorThickness',
        'NSQTMovieLoopMode', 'NSRequestUserAttentionType',
        'NSRulerOrientation', 'NSSaveOperationType',
        'NSScrollArrowPosition', 'NSScrollerArrow',
        'NSScrollerPart', 'NSSelectionAffinity',
        'NSSelectionDirection', 'NSSelectionGranularity',
        'NSTabState', 'NSTabViewState', 'NSTableViewDropOperation',
        'NSTextAlignment', 'NSTextTabType', 'NSTickMarkPosition',
        'NSTIFFCompression', 'NSTitlePosition', 'NSToolbarDisplayMode',
        'NSToolTipTag', 'NSTrackingRectTag', 'NSUsableScrollerParts',
        'NSWindingRule', 'NSWindowDepth', 'NSWindowOrderingMode',
        ]:
        func_builder.TYPE_ALIASES[arg] = 'int'


    fd.write('typedef void* PYOBJC_VOIDPTR;\n')
    funcs = func_builder.process_list(fd, file('build/codegen/AppKit.prototypes'))

    funcs2 = func_builder.process_list(fd, [

            # This is a very ugly macro, it access 'glyphs' in the enclosing
            # block ???
            #'void NSGlyphInfoAtIndex(int IX);',
        ])

    func_builder.gen_method_table_entries(fd, funcs + funcs2)
    for s in structs:
        del func_builder.SIMPLE_TYPES[s]


if ADDRESSBOOK_HDRS is not None:
    enum_generator.generate(
            ADDRESSBOOK_HDRS,
            'build/codegen/_Addr_Enum.inc',
            filter=filterAddressBookHeaders)
    strconst_generator.generate(
            ADDRESSBOOK_HDRS,
                'build/codegen/_Addr_Str.inc',
                filter=filterAddressBookHeaders)

if PREFPANES_HDRS is not None:
    enum_generator.generate(
            PREFPANES_HDRS,
            'build/codegen/_PreferencePanes_Enum.inc')
    strconst_generator.generate(
            PREFPANES_HDRS,
            'build/codegen/_PreferencePanes_Str.inc')

if IB_HDRS is not None:
    enum_generator.generate(
            IB_HDRS,
            'build/codegen/_InterfaceBuilder_Enum.inc')
    strconst_generator.generate(
            IB_HDRS,
            'build/codegen/_InterfaceBuilder_Str.inc')

if WEBKIT_HDRS is not None:
    enum_generator.generate(
            WEBKIT_HDRS,
            'build/codegen/_WebKit_Enum.inc',
                ignore_files=['npapi.h', 'npruntime.h', 'npfunctions.h'])

    # The two items on the ignore-list cause link errors,
    # to-be-investigated.
    strconst_generator.generate(WEBKIT_HDRS,
                                'build/codegen/_WebKit_Str.inc',
                                ignore=('WebElementImageAltStringKey',
                                        'WebPreferencesChangedNotification')
    )

if APPLESCRIPTKIT_HDRS is not None:
    enum_generator.generate(
            APPLESCRIPTKIT_HDRS,
            'build/codegen/_AppleScriptKit_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(APPLESCRIPTKIT_HDRS,
                                'build/codegen/_AppleScriptKit_Str.inc',
                                ignore=())

if APPKITSCRIPTING_HDRS is not None:
    enum_generator.generate(
            APPKITSCRIPTING_HDRS,
            'build/codegen/_AppKitScripting_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(APPKITSCRIPTING_HDRS,
                                'build/codegen/_AppKitScripting_Str.inc',
                                ignore=())

if AUTOMATOR_HDRS is not None:
    enum_generator.generate(
            AUTOMATOR_HDRS,
            'build/codegen/_Automator_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(AUTOMATOR_HDRS,
                                'build/codegen/_Automator_Str.inc',
                                ignore=())

if COREDATA_HDRS is not None:
    enum_generator.generate(
            COREDATA_HDRS,
            'build/codegen/_CoreData_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(COREDATA_HDRS,
                                'build/codegen/_CoreData_Str.inc',
                                ignore=())

if SYNCSERVICES_HDRS is not None:
    enum_generator.generate(
            SYNCSERVICES_HDRS,
            'build/codegen/_SyncServices_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(SYNCSERVICES_HDRS,
                                'build/codegen/_SyncServices_Str.inc',
                                ignore=())


if XGRIDFOUNDATION_HDRS is not None:
    enum_generator.generate(
            XGRIDFOUNDATION_HDRS,
            'build/codegen/_XgridFoundation_Enum.inc',
                ignore_files=[])

    strconst_generator.generate(XGRIDFOUNDATION_HDRS,
                                'build/codegen/_XgridFoundation_Str.inc',
                                ignore=())



if EXCHND_HDRS is not None:
    enum_generator.generate(
            EXCHND_HDRS,
            'build/codegen/_ExceptionHandling_Enum.inc')

    # The two items on the ignore-list cause link errors,
    # to-be-investigated.
    strconst_generator.generate(
        EXCHND_HDRS,
        'build/codegen/_ExceptionHandling_Str.inc')


if SECINT_HDRS is not None:
    enum_generator.generate(
            SECINT_HDRS,
            'build/codegen/_SecInt_Enum.inc')
    strconst_generator.generate(
            SECINT_HDRS,
            'build/codegen/_SecInt_Str.inc')
