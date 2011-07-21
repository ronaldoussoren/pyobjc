# Generated file, don't edit
# Source: BridgeSupport/InterfaceBuilderKit.bridgesupport
# Last update: Thu Jul 21 08:47:20 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "IBDocumentStorage*": objc.createOpaquePointerType('IBDocumentStorage*', b'^{IBDocumentStorage=}'),
    "IBInset": objc.createStructType('IBInset', b'{IBInsetTag="left"f"top"f"right"f"bottom"f}', None),
}
constants = '''$IBAdditionalLocalizableKeyPaths$IBAttributeKeyPaths$IBLocalizableGeometryKeyPaths$IBLocalizableStringKeyPaths$IBToManyRelationshipKeyPaths$IBToOneRelationshipKeyPaths$'''
enums = '''$IBMaxXDirection@2$IBMaxXMaxYDirection@10$IBMaxXMinYDirection@6$IBMaxYDirection@8$IBMinXDirection@1$IBMinXMaxYDirection@9$IBMinXMinYDirection@5$IBMinYDirection@4$IBNoDirection@0$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('IBDocument', b'addObject:toParent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('IBDocument', b'childrenOfObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('IBDocument', b'connectAction:ofSourceObject:toDestinationObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('IBDocument', b'connectBinding:ofSourceObject:toDestinationObject:keyPath:options:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}, 5: {'type': b'@'}, 6: {'type': b'@'}}})
    r('IBDocument', b'connectOutlet:ofSourceObject:toDestinationObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('IBDocument', b'documentForObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('IBDocument', b'documentImageNamed:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('IBDocument', b'metadataForKey:ofObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('IBDocument', b'moveObject:toParent:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('IBDocument', b'objects', {'retval': {'type': b'@'}})
    r('IBDocument', b'parentOfObject:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('IBDocument', b'removeObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('IBDocument', b'setMetadata:forKey:ofObject:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('IBDocument', b'topLevelObjects', {'retval': {'type': b'@'}})
    r('IBInspector', b'document', {'retval': {'type': b'@'}})
    r('IBInspector', b'inspectedObjects', {'retval': {'type': b'@'}})
    r('IBInspector', b'inspectedObjectsController', {'retval': {'type': b'@'}})
    r('IBInspector', b'label', {'retval': {'type': b'@'}})
    r('IBInspector', b'refresh', {'retval': {'type': b'v'}})
    r('IBInspector', b'sharedInstance', {'retval': {'type': b'@'}})
    r('IBInspector', b'supportsMultipleObjectInspection', {'retval': {'type': b'Z'}})
    r('IBInspector', b'view', {'retval': {'type': b'@'}})
    r('IBInspector', b'viewNibName', {'retval': {'type': b'@'}})
    r('IBPlugin', b'didLoad', {'retval': {'type': b'v'}})
    r('IBPlugin', b'document:didAddDraggedObjects:fromDraggedLibraryView:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'type': b'@'}}})
    r('IBPlugin', b'label', {'retval': {'type': b'@'}})
    r('IBPlugin', b'libraryNibNames', {'retval': {'type': b'@'}})
    r('IBPlugin', b'pasteboardObjectsForDraggedLibraryView:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': b'@'}}})
    r('IBPlugin', b'preferencesView', {'retval': {'type': b'@'}})
    r('IBPlugin', b'requiredFrameworks', {'retval': {'type': b'@'}})
    r('IBPlugin', b'sharedInstance', {'retval': {'type': b'@'}})
    r('IBPlugin', b'willUnload', {'retval': {'type': b'v'}})
    r('NSObject', b'ibAwakeInDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibDefaultChildren', {'retval': {'type': b'@'}})
    r('NSObject', b'ibDefaultImage', {'retval': {'type': b'@'}})
    r('NSObject', b'ibDefaultLabel', {'retval': {'type': b'@'}})
    r('NSObject', b'ibDidAddToDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibDidRemoveFromDesignableDocument:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibIsChildInitiallySelectable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibRemoveChildren:', {'retval': {'type': b'Z'}})
    r('NSObject', b'ibIsChildViewUserMovable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibIsChildViewUserSizable:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibObjectAtLocation:inWindowController:', {'retval': {'type': b'@'}, 'arguments': {2: {'type': sel32or64(b'{_NSPoint=ff}', b'{CGPoint=dd}')}, 3: {'type': b'@'}}})
    r('NSObject', b'ibPopulateAttributeInspectorClasses:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibPopulateKeyPaths:', {'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}}})
    r('NSObject', b'ibRectForChild:inWindowController:', {'retval': {'type': sel32or64(b'{_NSRect={_NSPoint=ff}{_NSSize=ff}}', b'{CGRect={CGPoint=dd}{CGSize=dd}}')}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r('NSView', b'ibBaselineAtIndex:', {'retval': {'type': b'f'}, 'arguments': {2: {'type': b'i'}}})
    r('NSView', b'ibBaselineCount', {'retval': {'type': b'i'}})
    r('NSView', b'ibDesignableContentView', {'retval': {'type': b'@'}})
    r('NSView', b'ibLayoutInset', {'retval': {'type': b'{IBInsetTag=ffff}'}})
    r('NSView', b'ibMaximumSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r('NSView', b'ibMinimumSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r('NSView', b'ibPreferredDesignSize', {'retval': {'type': sel32or64(b'{_NSSize=ff}', b'{CGSize=dd}')}})
    r('NSView', b'ibPreferredResizeDirection', {'retval': {'type': b'i'}})
finally:
    objc._updatingMetadata(False)
protocols={'IBObjectIntegration': objc.informal_protocol('IBObjectIntegration', [objc.selector(None, 'ibAwakeInDesignableDocument:', 'v@:@', isRequired=False), objc.selector(None, 'ibDefaultChildren', '@@:', isRequired=False), objc.selector(None, 'ibDefaultImage', '@@:', isRequired=False), objc.selector(None, 'ibDefaultLabel', '@@:', isRequired=False), objc.selector(None, 'ibRemoveChildren:', 'Z@:@', isRequired=False), objc.selector(None, 'ibDidAddToDesignableDocument:', 'v@:@', isRequired=False), objc.selector(None, 'ibDidRemoveFromDesignableDocument:', 'v@:@', isRequired=False), objc.selector(None, 'ibIsChildInitiallySelectable:', 'Z@:@', isRequired=False), objc.selector(None, 'ibIsChildViewUserMovable:', 'Z@:@', isRequired=False), objc.selector(None, 'ibIsChildViewUserSizable:', 'Z@:@', isRequired=False), objc.selector(None, 'ibObjectAtLocation:inWindowController:', sel32or64('@@:{_NSPoint=ff}@', '@@:{CGPoint=dd}@'), isRequired=False), objc.selector(None, 'ibPopulateAttributeInspectorClasses:', 'v@:@', isRequired=False), objc.selector(None, 'ibPopulateKeyPaths:', 'v@:@', isRequired=False), objc.selector(None, 'ibRectForChild:inWindowController:', sel32or64('{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@@', '{CGRect={CGPoint=dd}{CGSize=dd}}@:@@'), isRequired=False)])}
