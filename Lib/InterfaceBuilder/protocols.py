# generated from '/System/Library/Frameworks/InterfaceBuilder.framework'
import objc as _objc


IB = _objc.informal_protocol(
    "IB",
    [
# (id <IBDocuments>)activeDocument
        _objc.selector(
            None,
            selector='activeDocument',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBDocuments>) documentForObject:(id)object
        _objc.selector(
            None,
            selector='documentForObject:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)isTestingInterface
        _objc.selector(
            None,
            selector='isTestingInterface',
            signature='c@:',
            isRequired=0,
        ),
# (id)selectedObject
        _objc.selector(
            None,
            selector='selectedObject',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBEditors>)selectionOwner
        _objc.selector(
            None,
            selector='selectionOwner',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBCellProtocol = _objc.informal_protocol(
    "IBCellProtocol",
    [
# (BOOL)acceptsColor:(NSColor *)color
        _objc.selector(
            None,
            selector='acceptsColor:',
            signature='c@:@',
            isRequired=0,
        ),
# (void)cellWillAltDragWithSize:(NSSize)cellSize
        _objc.selector(
            None,
            selector='cellWillAltDragWithSize:',
            signature='v@:{_NSSize=ff}',
            isRequired=0,
        ),
# (void)depositColor:(NSColor *)color
        _objc.selector(
            None,
            selector='depositColor:',
            signature='v@:@',
            isRequired=0,
        ),
# (float)ibAlternateMinimumHeight
        _objc.selector(
            None,
            selector='ibAlternateMinimumHeight',
            signature='f@:',
            isRequired=0,
        ),
# (float)ibAlternateMinimumWidth
        _objc.selector(
            None,
            selector='ibAlternateMinimumWidth',
            signature='f@:',
            isRequired=0,
        ),
# (float)ibBaseLineForCellSize:(NSSize)cellSize
        _objc.selector(
            None,
            selector='ibBaseLineForCellSize:',
            signature='f@:{_NSSize=ff}',
            isRequired=0,
        ),
# (BOOL)ibHasAlternateMinimumHeight
        _objc.selector(
            None,
            selector='ibHasAlternateMinimumHeight',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibHasAlternateMinimumWidth
        _objc.selector(
            None,
            selector='ibHasAlternateMinimumWidth',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibHasBaseLine
        _objc.selector(
            None,
            selector='ibHasBaseLine',
            signature='c@:',
            isRequired=0,
        ),
# (void)ibMatchPrototype:(NSCell*)prototype
        _objc.selector(
            None,
            selector='ibMatchPrototype:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSString*)ibWidgetType
        _objc.selector(
            None,
            selector='ibWidgetType',
            signature='@@:',
            isRequired=0,
        ),
# (NSSize)maximumSizeForCellSize:(NSSize)cellSize knobPosition:(IBKnobPosition)knobPosition
        _objc.selector(
            None,
            selector='maximumSizeForCellSize:knobPosition:',
            signature='{_NSSize=ff}@:{_NSSize=ff}i',
            isRequired=0,
        ),
# (NSSize)minimumSizeForCellSize:(NSSize)cellSize knobPosition:(IBKnobPosition)knobPosition
        _objc.selector(
            None,
            selector='minimumSizeForCellSize:knobPosition:',
            signature='{_NSSize=ff}@:{_NSSize=ff}i',
            isRequired=0,
        ),
    ]
)

IBConnectors = _objc.informal_protocol(
    "IBConnectors",
    [
# (id)destination
        _objc.selector(
            None,
            selector='destination',
            signature='@@:',
            isRequired=0,
        ),
# (void)establishConnection
        _objc.selector(
            None,
            selector='establishConnection',
            signature='v@:',
            isRequired=0,
        ),
# (NSString *)label
        _objc.selector(
            None,
            selector='label',
            signature='@@:',
            isRequired=0,
        ),
# (id)nibInstantiate
        _objc.selector(
            None,
            selector='nibInstantiate',
            signature='@@:',
            isRequired=0,
        ),
# (void)replaceObject:(id)oldObject withObject:(id)newObject
        _objc.selector(
            None,
            selector='replaceObject:withObject:',
            signature='v@:@@',
            isRequired=0,
        ),
# (id)source
        _objc.selector(
            None,
            selector='source',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBDocuments = _objc.informal_protocol(
    "IBDocuments",
    [
# (void)addConnector:(id <IBConnectors>)connector
        _objc.selector(
            None,
            selector='addConnector:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSArray *)allConnectors
        _objc.selector(
            None,
            selector='allConnectors',
            signature='@@:',
            isRequired=0,
        ),
# (void)attachObject:(id)object toParent:(id)parent
        _objc.selector(
            None,
            selector='attachObject:toParent:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)attachObjects:(NSArray *)objects toParent:(id)parent
        _objc.selector(
            None,
            selector='attachObjects:toParent:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSArray *)connectorsForDestination:(id)destination
        _objc.selector(
            None,
            selector='connectorsForDestination:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)connectorsForDestination:(id)destination ofClass:(Class)connnectorClass
        _objc.selector(
            None,
            selector='connectorsForDestination:ofClass:',
            signature='@@:@#',
            isRequired=0,
        ),
# (NSArray *)connectorsForSource:(id)source
        _objc.selector(
            None,
            selector='connectorsForSource:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)connectorsForSource:(id)source ofClass:(Class)connnectorClass
        _objc.selector(
            None,
            selector='connectorsForSource:ofClass:',
            signature='@@:@#',
            isRequired=0,
        ),
# (BOOL)containsObject:(id)object
        _objc.selector(
            None,
            selector='containsObject:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)containsObjectWithName:(NSString *)name forParent:(id)parent
        _objc.selector(
            None,
            selector='containsObjectWithName:forParent:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)copyObject:(id)object type:(NSString *)type toPasteboard:(NSPasteboard *)pasteboard
        _objc.selector(
            None,
            selector='copyObject:type:toPasteboard:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (BOOL)copyObjects:(NSArray *)objects type:(NSString *)type toPasteboard:(NSPasteboard *)pasteboard
        _objc.selector(
            None,
            selector='copyObjects:type:toPasteboard:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (void)detachObject:(id)object
        _objc.selector(
            None,
            selector='detachObject:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)detachObjects:(NSArray *)objects
        _objc.selector(
            None,
            selector='detachObjects:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSString *)documentPath
        _objc.selector(
            None,
            selector='documentPath',
            signature='@@:',
            isRequired=0,
        ),
# (void)drawObject:(id)object
        _objc.selector(
            None,
            selector='drawObject:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)editor:(id <IBEditors>)editor didCloseForObject:(id)object
        _objc.selector(
            None,
            selector='editor:didCloseForObject:',
            signature='v@:@@',
            isRequired=0,
        ),
# (id <IBEditors>)editorForObject:(id)object create:(BOOL)createIt
        _objc.selector(
            None,
            selector='editorForObject:create:',
            signature='@@:@c',
            isRequired=0,
        ),
# (NSInterfaceStyle)interfaceStyle
        _objc.selector(
            None,
            selector='interfaceStyle',
            signature='i@:',
            isRequired=0,
        ),
# (BOOL)isUntitled
        _objc.selector(
            None,
            selector='isUntitled',
            signature='c@:',
            isRequired=0,
        ),
# (NSString *)nameForObject:(id)object
        _objc.selector(
            None,
            selector='nameForObject:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)objects
        _objc.selector(
            None,
            selector='objects',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBEditors>)openEditorForObject:(id)object
        _objc.selector(
            None,
            selector='openEditorForObject:',
            signature='@@:@',
            isRequired=0,
        ),
# (id <IBEditors>)parentEditorForEditor:(id <IBEditors>)editor
        _objc.selector(
            None,
            selector='parentEditorForEditor:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)parentOfObject:(id)object
        _objc.selector(
            None,
            selector='parentOfObject:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)pasteType:(NSString *)type fromPasteboard:(NSPasteboard *)pasteboard parent:(id)parent
        _objc.selector(
            None,
            selector='pasteType:fromPasteboard:parent:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (id <IBProjects>)project
        _objc.selector(
            None,
            selector='project',
            signature='@@:',
            isRequired=0,
        ),
# (void)removeConnector:(id <IBConnectors>)connector
        _objc.selector(
            None,
            selector='removeConnector:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)replaceObject:(id)oldObject withObject:(id)newObject
        _objc.selector(
            None,
            selector='replaceObject:withObject:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)resignSelectionForEditor:(id <IBEditors>)editor
        _objc.selector(
            None,
            selector='resignSelectionForEditor:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)setName:(NSString *)name forObject:(id)object
        _objc.selector(
            None,
            selector='setName:forObject:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)setSelectionFromEditor:(id <IBEditors>)editor
        _objc.selector(
            None,
            selector='setSelectionFromEditor:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)touch
        _objc.selector(
            None,
            selector='touch',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

IBEditors = _objc.informal_protocol(
    "IBEditors",
    [
# (BOOL)acceptsTypeFromPasteboard:(NSPasteboard *)pasteboard
        _objc.selector(
            None,
            selector='acceptsTypeFromPasteboard:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)activate
        _objc.selector(
            None,
            selector='activate',
            signature='c@:',
            isRequired=0,
        ),
# (void)closeEditor
        _objc.selector(
            None,
            selector='closeEditor',
            signature='v@:',
            isRequired=0,
        ),
# (void)closeSubeditors
        _objc.selector(
            None,
            selector='closeSubeditors',
            signature='v@:',
            isRequired=0,
        ),
# (void)copySelection
        _objc.selector(
            None,
            selector='copySelection',
            signature='v@:',
            isRequired=0,
        ),
# (void)deleteSelection
        _objc.selector(
            None,
            selector='deleteSelection',
            signature='v@:',
            isRequired=0,
        ),
# (id /*<IBDocuments>*/)document
        _objc.selector(
            None,
            selector='document',
            signature='@@:',
            isRequired=0,
        ),
# (id)editedObject
        _objc.selector(
            None,
            selector='editedObject',
            signature='@@:',
            isRequired=0,
        ),
# (id)initWithObject:(id)object inDocument:(id /*<IBDocuments>*/)document
        _objc.selector(
            None,
            selector='initWithObject:inDocument:',
            signature='@@:@@',
            isRequired=0,
        ),
# (void)makeSelectionVisible:(BOOL)showIt
        _objc.selector(
            None,
            selector='makeSelectionVisible:',
            signature='v@:c',
            isRequired=0,
        ),
# (id <IBEditors>)openSubeditorForObject:(id)object
        _objc.selector(
            None,
            selector='openSubeditorForObject:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)orderFront
        _objc.selector(
            None,
            selector='orderFront',
            signature='v@:',
            isRequired=0,
        ),
# (void)pasteInSelection
        _objc.selector(
            None,
            selector='pasteInSelection',
            signature='v@:',
            isRequired=0,
        ),
# (void)resetObject:(id)object
        _objc.selector(
            None,
            selector='resetObject:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)selectObjects:(NSArray *)objects
        _objc.selector(
            None,
            selector='selectObjects:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)shouldCopySelection
        _objc.selector(
            None,
            selector='shouldCopySelection',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)shouldDeleteSelection
        _objc.selector(
            None,
            selector='shouldDeleteSelection',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)shouldPasteInSelection
        _objc.selector(
            None,
            selector='shouldPasteInSelection',
            signature='c@:',
            isRequired=0,
        ),
# (void)validateEditing
        _objc.selector(
            None,
            selector='validateEditing',
            signature='v@:',
            isRequired=0,
        ),
# (BOOL)wantsSelection
        _objc.selector(
            None,
            selector='wantsSelection',
            signature='c@:',
            isRequired=0,
        ),
# (NSWindow *)window
        _objc.selector(
            None,
            selector='window',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBNibInstantiation = _objc.informal_protocol(
    "IBNibInstantiation",
    [
# (id)nibInstantiate
        _objc.selector(
            None,
            selector='nibInstantiate',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBObjectProtocol = _objc.informal_protocol(
    "IBObjectProtocol",
    [
# (void)awakeFromDocument:(id <IBDocuments>)document
        _objc.selector(
            None,
            selector='awakeFromDocument:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)canSubstituteForClass:(Class)originalObjectClass
        _objc.selector(
            None,
            selector='canSubstituteForClass:',
            signature='c@:#',
            isClassMethod=1,
            isRequired=0,
        ),
# (NSString *)classInspectorClassName
        _objc.selector(
            None,
            selector='classInspectorClassName',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)connectInspectorClassName
        _objc.selector(
            None,
            selector='connectInspectorClassName',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)editorClassName
        _objc.selector(
            None,
            selector='editorClassName',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)helpInspectorClassName
        _objc.selector(
            None,
            selector='helpInspectorClassName',
            signature='@@:',
            isRequired=0,
        ),
# (NSArray*)ibIncompatibleProperties
        _objc.selector(
            None,
            selector='ibIncompatibleProperties',
            signature='@@:',
            isRequired=0,
        ),
# (NSImage *)imageForViewer
        _objc.selector(
            None,
            selector='imageForViewer',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)inspectorClassName
        _objc.selector(
            None,
            selector='inspectorClassName',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)nibLabel:(NSString*)objectName
        _objc.selector(
            None,
            selector='nibLabel:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSString *)objectNameForInspectorTitle
        _objc.selector(
            None,
            selector='objectNameForInspectorTitle',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)sizeInspectorClassName
        _objc.selector(
            None,
            selector='sizeInspectorClassName',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBProjectFiles = _objc.informal_protocol(
    "IBProjectFiles",
    [
# (NSString *)fileName
        _objc.selector(
            None,
            selector='fileName',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)fileType
        _objc.selector(
            None,
            selector='fileType',
            signature='@@:',
            isRequired=0,
        ),
# (BOOL)isLocalized
        _objc.selector(
            None,
            selector='isLocalized',
            signature='c@:',
            isRequired=0,
        ),
# (NSString *)language
        _objc.selector(
            None,
            selector='language',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)path
        _objc.selector(
            None,
            selector='path',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBProjects>)project
        _objc.selector(
            None,
            selector='project',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBProjects = _objc.informal_protocol(
    "IBProjects",
    [
# (id)applicationIconForInterfaceStyle:(NSInterfaceStyle)style inLanguage:(NSString *)language
        _objc.selector(
            None,
            selector='applicationIconForInterfaceStyle:inLanguage:',
            signature='@@:i@',
            isRequired=0,
        ),
# (BOOL)containsFileAtPath:(NSString *)path
        _objc.selector(
            None,
            selector='containsFileAtPath:',
            signature='c@:@',
            isRequired=0,
        ),
# (NSArray *)filesForFileType:(NSString *)fileType
        _objc.selector(
            None,
            selector='filesForFileType:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)isAncestorOfProject:(id <IBProjects>)otherProject
        _objc.selector(
            None,
            selector='isAncestorOfProject:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isDescendantOfProject:(id <IBProjects>)otherProject
        _objc.selector(
            None,
            selector='isDescendantOfProject:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isLive
        _objc.selector(
            None,
            selector='isLive',
            signature='c@:',
            isRequired=0,
        ),
# (NSString *)languageForFileAtPath:(NSString *)path
        _objc.selector(
            None,
            selector='languageForFileAtPath:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)mainNibFileForInterfaceStyle:(NSInterfaceStyle)style inLanguage:(NSString *)language
        _objc.selector(
            None,
            selector='mainNibFileForInterfaceStyle:inLanguage:',
            signature='@@:i@',
            isRequired=0,
        ),
# (NSString*)pathForFilename:(NSString*)name
        _objc.selector(
            None,
            selector='pathForFilename:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSString *)projectDirectory
        _objc.selector(
            None,
            selector='projectDirectory',
            signature='@@:',
            isRequired=0,
        ),
# (id)projectManager
        _objc.selector(
            None,
            selector='projectManager',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)projectName
        _objc.selector(
            None,
            selector='projectName',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBProjects>)rootProject
        _objc.selector(
            None,
            selector='rootProject',
            signature='@@:',
            isRequired=0,
        ),
# (NSArray *)subprojects
        _objc.selector(
            None,
            selector='subprojects',
            signature='@@:',
            isRequired=0,
        ),
# (id <IBProjects>)superproject
        _objc.selector(
            None,
            selector='superproject',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

IBSelectionOwners = _objc.informal_protocol(
    "IBSelectionOwners",
    [
# (NSArray *)selection
        _objc.selector(
            None,
            selector='selection',
            signature='@@:',
            isRequired=0,
        ),
# (unsigned int)selectionCount
        _objc.selector(
            None,
            selector='selectionCount',
            signature='I@:',
            isRequired=0,
        ),
    ]
)

IBViewProtocol = _objc.informal_protocol(
    "IBViewProtocol",
    [
# (BOOL)acceptsColor:(NSColor *)color atPoint:(NSPoint)point
        _objc.selector(
            None,
            selector='acceptsColor:atPoint:',
            signature='c@:@{_NSPoint=ff}',
            isRequired=0,
        ),
# (BOOL)allowsAltDragging
        _objc.selector(
            None,
            selector='allowsAltDragging',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)canEditSelf
        _objc.selector(
            None,
            selector='canEditSelf',
            signature='c@:',
            isRequired=0,
        ),
# (void)depositColor:(NSColor *)color atPoint:(NSPoint)point
        _objc.selector(
            None,
            selector='depositColor:atPoint:',
            signature='v@:@{_NSPoint=ff}',
            isRequired=0,
        ),
# (void)editSelf:(NSEvent *)theEvent in:(NSView<IBEditors>*)viewEditor
        _objc.selector(
            None,
            selector='editSelf:in:',
            signature='v@:@@',
            isRequired=0,
        ),
# (float)ibAlternateMinimumHeight
        _objc.selector(
            None,
            selector='ibAlternateMinimumHeight',
            signature='f@:',
            isRequired=0,
        ),
# (float)ibAlternateMinimumWidth
        _objc.selector(
            None,
            selector='ibAlternateMinimumWidth',
            signature='f@:',
            isRequired=0,
        ),
# (float)ibBaseLineAtIndex:(int)index
        _objc.selector(
            None,
            selector='ibBaseLineAtIndex:',
            signature='f@:i',
            isRequired=0,
        ),
# (BOOL)ibDrawFrameWhileResizing
        _objc.selector(
            None,
            selector='ibDrawFrameWhileResizing',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibHasAlternateMinimumHeight
        _objc.selector(
            None,
            selector='ibHasAlternateMinimumHeight',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibHasAlternateMinimumWidth
        _objc.selector(
            None,
            selector='ibHasAlternateMinimumWidth',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibIsContainer
        _objc.selector(
            None,
            selector='ibIsContainer',
            signature='c@:',
            isRequired=0,
        ),
# (id)ibNearestTargetForDrag
        _objc.selector(
            None,
            selector='ibNearestTargetForDrag',
            signature='@@:',
            isRequired=0,
        ),
# (int)ibNumberOfBaseLine
        _objc.selector(
            None,
            selector='ibNumberOfBaseLine',
            signature='i@:',
            isRequired=0,
        ),
# (IBInset)ibShadowInset
        _objc.selector(
            None,
            selector='ibShadowInset',
            signature='{_IBInset=ffff}@:',
            isRequired=0,
        ),
# (BOOL)ibShouldShowContainerGuides
        _objc.selector(
            None,
            selector='ibShouldShowContainerGuides',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibSupportsInsideOutSelection
        _objc.selector(
            None,
            selector='ibSupportsInsideOutSelection',
            signature='c@:',
            isRequired=0,
        ),
# (BOOL)ibSupportsLiveResize
        _objc.selector(
            None,
            selector='ibSupportsLiveResize',
            signature='c@:',
            isRequired=0,
        ),
# (NSString*)ibWidgetType
        _objc.selector(
            None,
            selector='ibWidgetType',
            signature='@@:',
            isRequired=0,
        ),
# (float)lineFragmentPadding
        _objc.selector(
            None,
            selector='lineFragmentPadding',
            signature='f@:',
            isRequired=0,
        ),
# (NSSize)maximumFrameSizeFromKnobPosition:(IBKnobPosition)knobPosition
        _objc.selector(
            None,
            selector='maximumFrameSizeFromKnobPosition:',
            signature='{_NSSize=ff}@:i',
            isRequired=0,
        ),
# (NSSize)minimumFrameSizeFromKnobPosition:(IBKnobPosition)position
        _objc.selector(
            None,
            selector='minimumFrameSizeFromKnobPosition:',
            signature='{_NSSize=ff}@:i',
            isRequired=0,
        ),
# (void)placeView:(NSRect)newFrame
        _objc.selector(
            None,
            selector='placeView:',
            signature='v@:{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (NSString *)trackerClassNameForEvent:(NSEvent *)event
        _objc.selector(
            None,
            selector='trackerClassNameForEvent:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

IBViewResourceDraggingDelegates = _objc.informal_protocol(
    "IBViewResourceDraggingDelegates",
    [
# (BOOL)acceptsViewResourceFromPasteboard:(NSPasteboard *)pasteboard forObject:(id)object atPoint:(NSPoint)point
        _objc.selector(
            None,
            selector='acceptsViewResourceFromPasteboard:forObject:atPoint:',
            signature='c@:@@{_NSPoint=ff}',
            isRequired=0,
        ),
# (void)depositViewResourceFromPasteboard:(NSPasteboard *)pasteboard onObject:(id)object atPoint:(NSPoint)point
        _objc.selector(
            None,
            selector='depositViewResourceFromPasteboard:onObject:atPoint:',
            signature='v@:@@{_NSPoint=ff}',
            isRequired=0,
        ),
# (BOOL)shouldDrawConnectionFrame
        _objc.selector(
            None,
            selector='shouldDrawConnectionFrame',
            signature='c@:',
            isRequired=0,
        ),
# (NSArray *)viewResourcePasteboardTypes
        _objc.selector(
            None,
            selector='viewResourcePasteboardTypes',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

NSObject_IBObjectProtocol = _objc.informal_protocol(
    "NSObject_IBObjectProtocol",
    [
    ]
)
