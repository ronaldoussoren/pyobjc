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

if not os.path.isdir('Modules'):
    print "Run me from the root of the PyObjC source tree"
    sys.exit(1)

FRAMEWORKS="/System/Library/Frameworks"
FOUNDATION=os.path.join(FRAMEWORKS, "Foundation.framework")
APPKIT=os.path.join(FRAMEWORKS, "AppKit.framework")
ADDRESSBOOK=os.path.join(FRAMEWORKS, "AddressBook.framework")
PREFPANES=os.path.join(FRAMEWORKS, "PreferencePanes.framework")
WEBKIT=os.path.join(FRAMEWORKS, "WebKit.framework")
IB=os.path.join(FRAMEWORKS, "InterfaceBuilder.framework")
FOUNDATION_HDRS=os.path.join(FOUNDATION, 'Headers')
ADDRESSBOOK_HDRS=os.path.join(ADDRESSBOOK, 'Headers')
APPKIT_HDRS=os.path.join(APPKIT, 'Headers')
PREFPANES_HDRS=os.path.join(PREFPANES, 'Headers')
IB_HDRS=os.path.join(IB, 'Headers')
WEBKIT_HDRS=os.path.join(WEBKIT, 'Headers')

def filterAddressBookHeaders(fn):
    if fn[-3:] == 'C.h':
        return 0

    if fn == 'ABPeoplePickerView.h':
        return 0

    return 1

enum_generator.generate(FOUNDATION_HDRS, 'Modules/Foundation/_Fnd_Enum.inc')
enum_generator.generate(APPKIT_HDRS, 'Modules/AppKit/_App_Enum.inc')
enum_generator.generate(ADDRESSBOOK_HDRS,
                        'Modules/AddressBook/_Addr_Enum.inc',
                        filter=filterAddressBookHeaders)
enum_generator.generate(PREFPANES_HDRS, 'Modules/PreferencePanes/_PreferencePanes_Enum.inc')
enum_generator.generate(IB_HDRS, 'Modules/InterfaceBuilder/_InterfaceBuilder_Enum.inc')
enum_generator.generate(WEBKIT_HDRS, 'Modules/WebKit/_WebKit_Enum.inc')

strconst_generator.generate(FOUNDATION_HDRS, 'Modules/Foundation/_Fnd_Str.inc')
strconst_generator.generate(APPKIT_HDRS, 'Modules/AppKit/_App_Str.inc')
strconst_generator.generate(ADDRESSBOOK_HDRS,
                            'Modules/AddressBook/_Addr_Str.inc',
                            filter=filterAddressBookHeaders)
strconst_generator.generate(PREFPANES_HDRS, 'Modules/PreferencePanes/_PreferencePanes_Str.inc')
strconst_generator.generate(IB_HDRS, 'Modules/InterfaceBuilder/_InterfaceBuilder_Str.inc')

# The two items on the ignore-list cause link errors, to-be-investigated.
strconst_generator.generate(WEBKIT_HDRS,
                            'Modules/WebKit/_WebKit_Str.inc',
                            ignore=('WebElementImageAltStringKey', 'WebPreferencesChangedNotification')
)

FOUNDATION_PREFIX="FOUNDATION_EXPORT"
FOUNDATION_IGNORE_LIST=(
	# All have types that are not (yet) mapped to python
	'NSZeroPoint',
	'NSZeroSize',
	'NSZeroRect',
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

var_generator.generate(FOUNDATION_HDRS, 'Modules/Foundation/_Fnd_Var.inc', FOUNDATION_PREFIX, FOUNDATION_IGNORE_LIST)

APPKIT_PREFIX="APPKIT_EXTERN"
APPKIT_IGNORE_LIST=(
	# First two have types that are not yet mapped
	'NSIconSize', 
	'NSTokenSize', 

	# NSApp is a 'real' variable, will probably add get/set functions
	'NSApp')

var_generator.generate(APPKIT_HDRS, 'Modules/AppKit/_App_Var.inc', APPKIT_PREFIX, APPKIT_IGNORE_LIST)

FOUNDATION_IGNORE_LIST=(
	# Private functions in NSException.h 
	'_NSAddHandler2',
	'_NSRemoveHandler2',
	'_NSExceptionObjectFromHandler2'

        # List of functions that are not usefull from Python:

        # List of manually wrapped functions:
)
APPKIT_IGNORE_LIST=(

        # List of manually wrapped functions:
        'NSApplicationMain(',
        'NSCountWindows(',
        'NSCountWindowsForContext(',
        'NSAvailableWindowDepths(',
        'NSRectFillList(',
        'NSGetWindowServerMemory(',
)
func_collector.generate(FOUNDATION_HDRS, 'Modules/Foundation/Foundation.prototypes', 
	FOUNDATION_PREFIX, FOUNDATION_IGNORE_LIST)
func_collector.generate(APPKIT_HDRS, 'Modules/AppKit/AppKit.prototypes', 
	APPKIT_PREFIX, APPKIT_IGNORE_LIST)

# Add easy to handle types in Foundation:
#func_builder.SIMPLE_TYPES['NSHashTable*'] = (
#	'\tresult = PyCObject_New(%(varname)s);\n\t if (result == NULL) return NULL;',
#	'O&',
#	'convert_NSHashtable, &%(varname)s',
#)

func_builder.INT_ALIASES.extend([
	'NSSearchPathDomainMask', 'NSCalculationError',
	'NSComparisonResult', 'NSInsertionPosition',
	'NSNotificationCoalescing', 'NSNotificationCoalescing',
	'NSRectEdge', 'NSRelativePosition',
	'NSRoundingMode', 'NSSaveOptions', 'NSSearchPathDirectory',
	'NSSearchPathDomainMask', 'NSTestComparisonOperation',
	'NSURLHandleStatus', 'NSWhoseSubelementIdentifier']
)
func_builder.IGNORE_VARARGS.extend([
        # Some of these are Foundation some are AppKit
        'NSGetInformationalAlertPanel',
        'NSLog',
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

fd = file('Modules/Foundation/_Fnd_Functions.inc', 'w')
structs = ['NSPoint', 'NSSize', 'NSRect', 'NSRange']
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


func_builder.process_list(fd , file('Modules/Foundation/Foundation.prototypes'))
fd = None
for s in structs:
	del func_builder.SIMPLE_TYPES[s]

fd = file('Modules/AppKit/_App_Functions.inc', 'w')
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

func_builder.INT_ALIASES.extend([
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
])


func_builder.process_list(fd, file('Modules/AppKit/AppKit.prototypes'))
for s in structs:
	del func_builder.SIMPLE_TYPES[s]
