import objc as _objc

from _Foundation import *

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

_objc.loadBundle("Foundation", globals(), bundle_path="/System/Library/Frameworks/Foundation.framework")

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

NSConnectionDelegateMethods = _objc.informal_protocol(
    'NSConnectionDelegateMethods',
    [
# - (BOOL)makeNewConnection:(NSConnection *)conn sender:(NSConnection *)ancestor;
        _objc.selector(
            None, 
            selector='makeNewConnection:sender:',
            signature='c@:@@',
            isRequired=0
        ),
# - (BOOL)connection:(NSConnection *)ancestor shouldMakeNewConnection:(NSConnection *)conn;
        _objc.selector(
            None, 
            selector='connection:shouldMakeNewConnection:',
            signature='c@:@@',
            isRequired=0
        ),
# - (NSData *)authenticationDataForComponents:(NSArray *)components;
        _objc.selector(
            None, 
            selector='authenticationDataForComponents:',
            signature='@@:@',
            isRequired=0
        ),
# - (BOOL)authenticateComponents:(NSArray *)components withData:(NSData *)signature;
        _objc.selector(
            None, 
            selector='authenticateComponents:withData:',
            signature='@@:@@',
            isRequired=0
        ),
# - (id)createConversationForConnection:(NSConnection *)conn;
        _objc.selector(
            None, 
            selector='createConversationForConnection:',
            signature='@@:@',
            isRequired=0
        ),
        ]
    )

NSDistantObjectRequestMethods = _objc.informal_protocol(
    'NSDistantObjectRequestMethods',
    [
# - (BOOL)connection:(NSConnection *)connection handleRequest:(NSDistantObjectRequest *)doreq;
        _objc.selector(
            None, 
            selector='connection:handleRequest:',
            signature='c@:@@',
            isRequired=0
        ),
        ]
    )

NSCopyLinkMoveHandler = _objc.informal_protocol(
    'NSCopyLinkMoveHandler',
    [
# - (BOOL)fileManager:(NSFileManager *)fm shouldProceedAfterError:(NSDictionary *)errorInfo;
        _objc.selector(
            None, 
            selector='fileManager:shouldProceedAfterError:',
            signature='c@:@@',
            isRequired=0
        ),
# - (void)fileManager:(NSFileManager *)fm willProcessPath:(NSString *)path;
        _objc.selector(
            None, 
            selector='replacementObjectForArchiver:',
            signature='v@:@@',
            isRequired=0
        ),
        ]
    )

NSKeyedArchiverDelegate = _objc.informal_protocol(
    'NSKeyedArchiverDelegate',
    [
# - (id)archiver:(NSKeyedArchiver *)archiver willEncodeObject:(id)object;
        _objc.selector(
            None, 
            selector='archiver:willEncodeObject:',
            signature='@@:@@',
            isRequired=0
        ),
# - (void)archiver:(NSKeyedArchiver *)archiver didEncodeObject:(id)object;
        _objc.selector(
            None, 
            selector='archiver:didEncodeObject:',
            signature='v@:@@',
            isRequired=0
        ),
# - (void)archiver:(NSKeyedArchiver *)archiver willReplaceObject:(id)object withObject:(id)newObject;
        _objc.selector(
            None, 
            selector='archiver:willReplaceObject:willReplaceObject:',
            signature='v@:@@@',
            isRequired=0
        ),
# - (void)archiverWillFinish:(NSKeyedArchiver *)archiver;
        _objc.selector(
            None, 
            selector='archiverWillFinish:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)archiverDidFinish:(NSKeyedArchiver *)archiver;
        _objc.selector(
            None, 
            selector='archiverDidFinish:',
            signature='v@:@',
            isRequired=0
        ),
        ]
    )

NSKeyedUnarchiverDelegate = _objc.informal_protocol(
    'NSKeyedUnarchiverDelegate',
    [
# - (Class)unarchiver:(NSKeyedUnarchiver *)unarchiver cannotDecodeObjectOfClassName:(NSString *)name originalClasses:(NSArray *)classNames;
        _objc.selector(
            None, 
            selector='unarchiver:cannotDecodeObjectOfClassName:originalClasses:',
            signature='#@:@@@',
            isRequired=0
        ),
# - (id)unarchiver:(NSKeyedUnarchiver *)unarchiver didDecodeObject:(id)object;
        _objc.selector(
            None, 
            selector='unarchiver:didDecodeObject:',
            signature='@@:@@',
            isRequired=0
        ),
# - (void)unarchiver:(NSKeyedUnarchiver *)unarchiver willReplaceObject:(id)object withObject:(id)newObject;
        _objc.selector(
            None, 
            selector='unarchiver:willReplaceObject:withObject:',
            signature='v@:@@@',
            isRequired=0
        ),
# - (void)unarchiverWillFinish:(NSKeyedUnarchiver *)unarchiver;
        _objc.selector(
            None, 
            selector='unarchiverWillFinish:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)unarchiverDidFinish:(NSKeyedUnarchiver *)unarchiver;
        _objc.selector(
            None, 
            selector='unarchiverDidFinish:',
            signature='v@:@',
            isRequired=0
        ),
        ]
    )

NSNetServiceDelegateMethods = _objc.informal_protocol(
    'NSNetServiceDelegateMethods',
    [
# - (void)netServiceWillPublish:(NSNetService *)sender;
        _objc.selector(
            None, 
            selector='netServiceWillPublish:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)netServiceWillResolve:(NSNetService *)sender;
        _objc.selector(
            None, 
            selector='netServiceWillResolve:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)netService:(NSNetService *)sender didNotPublish:(NSDictionary *)errorDict;
        _objc.selector(
            None, 
            selector='netService:didNotPublish:',
            signature='v@:@@',
            isRequired=0
        ),
# - (void)netServiceDidResolveAddress:(NSNetService *)sender;
        _objc.selector(
            None, 
            selector='netServiceDidResolveAddress:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)netService:(NSNetService *)sender didNotResolve:(NSDictionary *)errorDict;
        _objc.selector(
            None, 
            selector='netService:didNotResolve:',
            signature='v@:@@',
            isRequired=0
        ),
# - (void)netServiceDidStop:(NSNetService *)sender;
        _objc.selector(
            None, 
            selector='netServiceDidStop:',
            signature='v@:@',
            isRequired=0
        ),
        ]
    )

NSNetServiceBrowserDelegateMethods = _objc.informal_protocol(
    'NSNetServiceBrowserDelegateMethods',
    [
# - (void)netServiceBrowserWillSearch:(NSNetServiceBrowser *)aNetServiceBrowser;
        _objc.selector(
            None, 
            selector='netServiceBrowserWillSearch:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindDomain:(NSString *)domainString moreComing:(BOOL)moreComing;
        _objc.selector(
            None, 
            selector='netServiceBrowser:didFindDomain:moreComing:',
            signature='v@:@@@',
            isRequired=0
        ),
# - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindService:(NSNetService *)aNetService moreComing:(BOOL)moreComing;
        _objc.selector(
            None, 
            selector='netServiceBrowser:didFindService:moreComing:',
            signature='v@:@@@',
            isRequired=0
        ),
# - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didNotSearch:(NSDictionary *)errorDict;
        _objc.selector(
            None, 
            selector='netServiceBrowser:didNotSearch:',
            signature='v@:@@',
            isRequired=0
        ),
# - (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser *)aNetServiceBrowser;
        _objc.selector(
            None, 
            selector='netServiceBrowserDidStopSearch:',
            signature='v@:@',
            isRequired=0
        ),
# - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveDomain:(NSString *)domainString moreComing:(BOOL)moreComing;
        _objc.selector(
            None, 
            selector='netServiceBrowser:didRemoveDomain:moreComing:',
            signature='v@:@@@',
            isRequired=0
        ),
# - (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveService:(NSNetService *)aNetService moreComing:(BOOL)moreComing;
        _objc.selector(
            None, 
            selector='netServiceBrowser:didRemoveService:moreComing:',
            signature='v@:@@@',
            isRequired=0
        ),
        ]
    )

NSPortDelegateMethods = _objc.informal_protocol(
    'NSPortDelegateMethods',
    [
# - (void)handlePortMessage:(NSPortMessage *)message;
        _objc.selector(
            None, 
            selector='handlePortMessage:',
            signature='v@:@',
            isRequired=0
        ),
        ]
    )

# NSMachPortDelegateMethods requires bridging of the Mach messaging structure(s).
