# generated from '/System/Library/Frameworks/Foundation.framework'
import objc as _objc


NSArchiverCallback = _objc.informal_protocol(
    "NSArchiverCallback",
    [
# (Class)classForArchiver
        _objc.selector(
            None,
            selector='classForArchiver',
            signature='#@:',
            isRequired=0,
        ),
# (id)replacementObjectForArchiver:(NSArchiver *)archiver
        _objc.selector(
            None,
            selector='replacementObjectForArchiver:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSClassDescriptionPrimitives = _objc.informal_protocol(
    "NSClassDescriptionPrimitives",
    [
# (NSArray *)attributeKeys
        _objc.selector(
            None,
            selector='attributeKeys',
            signature='@@:',
            isRequired=0,
        ),
# (NSClassDescription *)classDescription
        _objc.selector(
            None,
            selector='classDescription',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)inverseForRelationshipKey:(NSString *)relationshipKey
        _objc.selector(
            None,
            selector='inverseForRelationshipKey:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSArray *)toManyRelationshipKeys
        _objc.selector(
            None,
            selector='toManyRelationshipKeys',
            signature='@@:',
            isRequired=0,
        ),
# (NSArray *)toOneRelationshipKeys
        _objc.selector(
            None,
            selector='toOneRelationshipKeys',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

NSCoding = _objc.informal_protocol(
    "NSCoding",
    [
# (void)encodeWithCoder:(NSCoder *)aCoder
        _objc.selector(
            None,
            selector='encodeWithCoder:',
            signature='v@:@',
            isRequired=0,
        ),
# (id)initWithCoder:(NSCoder *)aDecoder
        _objc.selector(
            None,
            selector='initWithCoder:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSComparisonMethods = _objc.informal_protocol(
    "NSComparisonMethods",
    [
# (BOOL)doesContain:(id)object
        _objc.selector(
            None,
            selector='doesContain:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isCaseInsensitiveLike:(NSString *)object
        _objc.selector(
            None,
            selector='isCaseInsensitiveLike:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isEqualTo:(id)object
        _objc.selector(
            None,
            selector='isEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isGreaterThan:(id)object
        _objc.selector(
            None,
            selector='isGreaterThan:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isGreaterThanOrEqualTo:(id)object
        _objc.selector(
            None,
            selector='isGreaterThanOrEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isLessThan:(id)object
        _objc.selector(
            None,
            selector='isLessThan:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isLessThanOrEqualTo:(id)object
        _objc.selector(
            None,
            selector='isLessThanOrEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isLike:(NSString *)object
        _objc.selector(
            None,
            selector='isLike:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isNotEqualTo:(id)object
        _objc.selector(
            None,
            selector='isNotEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSConnectionDelegateMethods = _objc.informal_protocol(
    "NSConnectionDelegateMethods",
    [
# (BOOL)authenticateComponents:(NSArray *)components withData:(NSData *)signature
        _objc.selector(
            None,
            selector='authenticateComponents:withData:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSData *)authenticationDataForComponents:(NSArray *)components
        _objc.selector(
            None,
            selector='authenticationDataForComponents:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)connection:(NSConnection *)ancestor shouldMakeNewConnection:(NSConnection *)conn
        _objc.selector(
            None,
            selector='connection:shouldMakeNewConnection:',
            signature='c@:@@',
            isRequired=0,
        ),
# (id)createConversationForConnection:(NSConnection *)conn
        _objc.selector(
            None,
            selector='createConversationForConnection:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)makeNewConnection:(NSConnection *)conn sender:(NSConnection *)ancestor
        _objc.selector(
            None,
            selector='makeNewConnection:sender:',
            signature='c@:@@',
            isRequired=0,
        ),
    ]
)

NSCopyLinkMoveHandler = _objc.informal_protocol(
    "NSCopyLinkMoveHandler",
    [
# (BOOL)fileManager:(NSFileManager *)fm shouldProceedAfterError:(NSDictionary *)errorInfo
        _objc.selector(
            None,
            selector='fileManager:shouldProceedAfterError:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void)fileManager:(NSFileManager *)fm willProcessPath:(NSString *)path
        _objc.selector(
            None,
            selector='fileManager:willProcessPath:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

NSCopying = _objc.informal_protocol(
    "NSCopying",
    [
# (id)copyWithZone:(NSZone *)zone
        _objc.selector(
            None,
            selector='copyWithZone:',
            signature='@@:^{_NSZone=}',
            isRequired=0,
        ),
    ]
)

NSDecimalNumberBehaviors = _objc.informal_protocol(
    "NSDecimalNumberBehaviors",
    [
# (NSDecimalNumber *)exceptionDuringOperation:(SEL)operation error:(NSCalculationError)error leftOperand:(NSDecimalNumber *)leftOperand rightOperand:(NSDecimalNumber *)rightOperand
        _objc.selector(
            None,
            selector='exceptionDuringOperation:error:leftOperand:rightOperand:',
            signature='@@::i@@',
            isRequired=0,
        ),
# (NSRoundingMode)roundingMode
        _objc.selector(
            None,
            selector='roundingMode',
            signature='i@:',
            isRequired=0,
        ),
# (short)scale
        _objc.selector(
            None,
            selector='scale',
            signature='s@:',
            isRequired=0,
        ),
    ]
)

NSDelayedPerforming = _objc.informal_protocol(
    "NSDelayedPerforming",
    [
# (void)performSelector:(SEL)aSelector withObject:(id)anArgument afterDelay:(NSTimeInterval)delay
        _objc.selector(
            None,
            selector='performSelector:withObject:afterDelay:',
            signature='v@::@d',
            isRequired=0,
        ),
# (void)performSelector:(SEL)aSelector withObject:(id)anArgument afterDelay:(NSTimeInterval)delay inModes:(NSArray *)modes
        _objc.selector(
            None,
            selector='performSelector:withObject:afterDelay:inModes:',
            signature='v@::@d@',
            isRequired=0,
        ),
    ]
)

NSDeprecatedKeyValueCoding = _objc.informal_protocol(
    "NSDeprecatedKeyValueCoding",
    [
# (id)handleQueryWithUnboundKey:(NSString *)key
        _objc.selector(
            None,
            selector='handleQueryWithUnboundKey:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)handleTakeValue:(id)value forUnboundKey:(NSString *)key
        _objc.selector(
            None,
            selector='handleTakeValue:forUnboundKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)takeValue:(id)value forKey:(NSString *)key
        _objc.selector(
            None,
            selector='takeValue:forKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)takeValue:(id)value forKeyPath:(NSString *)keyPath
        _objc.selector(
            None,
            selector='takeValue:forKeyPath:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)takeValuesFromDictionary:(NSDictionary *)properties
        _objc.selector(
            None,
            selector='takeValuesFromDictionary:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)unableToSetNilForKey:(NSString *)key
        _objc.selector(
            None,
            selector='unableToSetNilForKey:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSDictionary *)valuesForKeys:(NSArray *)keys
        _objc.selector(
            None,
            selector='valuesForKeys:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSDistantObjectRequestMethods = _objc.informal_protocol(
    "NSDistantObjectRequestMethods",
    [
# (BOOL)connection:(NSConnection *)connection handleRequest:(NSDistantObjectRequest *)doreq
        _objc.selector(
            None,
            selector='connection:handleRequest:',
            signature='c@:@@',
            isRequired=0,
        ),
    ]
)

NSDistributedObjects = _objc.informal_protocol(
    "NSDistributedObjects",
    [
# (Class)classForPortCoder
        _objc.selector(
            None,
            selector='classForPortCoder',
            signature='#@:',
            isRequired=0,
        ),
# (id)replacementObjectForPortCoder:(NSPortCoder *)coder
        _objc.selector(
            None,
            selector='replacementObjectForPortCoder:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSKeyValueCoding = _objc.informal_protocol(
    "NSKeyValueCoding",
    [
# (NSMutableArray *)mutableArrayValueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='mutableArrayValueForKey:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSMutableArray *)mutableArrayValueForKeyPath:(NSString *)keyPath
        _objc.selector(
            None,
            selector='mutableArrayValueForKeyPath:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)setNilValueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='setNilValueForKey:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)setValue:(id)value forKey:(NSString *)key
        _objc.selector(
            None,
            selector='setValue:forKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)setValue:(id)value forKeyPath:(NSString *)keyPath
        _objc.selector(
            None,
            selector='setValue:forKeyPath:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)setValue:(id)value forUndefinedKey:(NSString *)key
        _objc.selector(
            None,
            selector='setValue:forUndefinedKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)setValuesForKeysWithDictionary:(NSDictionary *)keyedValues
        _objc.selector(
            None,
            selector='setValuesForKeysWithDictionary:',
            signature='v@:@',
            isRequired=0,
        ),
# (id)storedValueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='storedValueForKey:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)takeStoredValue:(id)value forKey:(NSString *)key
        _objc.selector(
            None,
            selector='takeStoredValue:forKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)validateValue:(id *)ioValue forKey:(NSString *)inKey error:(NSError **)outError
        _objc.selector(
            None,
            selector='validateValue:forKey:error:',
            signature='c@:^@@^@',
            isRequired=0,
        ),
# (BOOL)validateValue:(id *)ioValue forKeyPath:(NSString *)inKeyPath error:(NSError **)outError
        _objc.selector(
            None,
            selector='validateValue:forKeyPath:error:',
            signature='c@:^@@^@',
            isRequired=0,
        ),
# (id)valueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='valueForKey:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)valueForKeyPath:(NSString *)keyPath
        _objc.selector(
            None,
            selector='valueForKeyPath:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)valueForUndefinedKey:(NSString *)key
        _objc.selector(
            None,
            selector='valueForUndefinedKey:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSKeyValueObserverNotification = _objc.informal_protocol(
    "NSKeyValueObserverNotification",
    [
# (void)didChange:(NSKeyValueChange)change valuesAtIndexes:(NSIndexSet *)indexes forKey:(NSString *)key
        _objc.selector(
            None,
            selector='didChange:valuesAtIndexes:forKey:',
            signature='v@:i@@',
            isRequired=0,
        ),
# (void)didChangeValueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='didChangeValueForKey:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)willChange:(NSKeyValueChange)change valuesAtIndexes:(NSIndexSet *)indexes forKey:(NSString *)key
        _objc.selector(
            None,
            selector='willChange:valuesAtIndexes:forKey:',
            signature='v@:i@@',
            isRequired=0,
        ),
# (void)willChangeValueForKey:(NSString *)key
        _objc.selector(
            None,
            selector='willChangeValueForKey:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSKeyValueObserverRegistration = _objc.informal_protocol(
    "NSKeyValueObserverRegistration",
    [
# (void)addObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath options:(NSKeyValueObservingOptions)options context:(void *)context
        _objc.selector(
            None,
            selector='addObserver:forKeyPath:options:context:',
            signature='v@:@@I^v',
            isRequired=0,
        ),
# (void)removeObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath
        _objc.selector(
            None,
            selector='removeObserver:forKeyPath:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

NSKeyValueObserving = _objc.informal_protocol(
    "NSKeyValueObserving",
    [
# (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(NSObject *)object change:(NSDictionary *)change context:(void *)context
        _objc.selector(
            None,
            selector='observeValueForKeyPath:ofObject:change:context:',
            signature='v@:@@@^v',
            isRequired=0,
        ),
    ]
)

NSKeyValueObservingCustomization = _objc.informal_protocol(
    "NSKeyValueObservingCustomization",
    [
# (void *)observationInfo
        _objc.selector(
            None,
            selector='observationInfo',
            signature='^v@:',
            isRequired=0,
        ),
# (void)setObservationInfo:(void *)observationInfo
        _objc.selector(
            None,
            selector='setObservationInfo:',
            signature='v@:^v',
            isRequired=0,
        ),
    ]
)

NSKeyedArchiverDelegate = _objc.informal_protocol(
    "NSKeyedArchiverDelegate",
    [
# (void)archiver:(NSKeyedArchiver *)archiver didEncodeObject:(id)object
        _objc.selector(
            None,
            selector='archiver:didEncodeObject:',
            signature='v@:@@',
            isRequired=0,
        ),
# (id)archiver:(NSKeyedArchiver *)archiver willEncodeObject:(id)object
        _objc.selector(
            None,
            selector='archiver:willEncodeObject:',
            signature='@@:@@',
            isRequired=0,
        ),
# (void)archiver:(NSKeyedArchiver *)archiver willReplaceObject:(id)object withObject:(id)newObject
        _objc.selector(
            None,
            selector='archiver:willReplaceObject:withObject:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)archiverDidFinish:(NSKeyedArchiver *)archiver
        _objc.selector(
            None,
            selector='archiverDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)archiverWillFinish:(NSKeyedArchiver *)archiver
        _objc.selector(
            None,
            selector='archiverWillFinish:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSKeyedArchiverObjectSubstitution = _objc.informal_protocol(
    "NSKeyedArchiverObjectSubstitution",
    [
# (Class)classForKeyedArchiver
        _objc.selector(
            None,
            selector='classForKeyedArchiver',
            signature='#@:',
            isRequired=0,
        ),
# (id)replacementObjectForKeyedArchiver:(NSKeyedArchiver *)archiver
        _objc.selector(
            None,
            selector='replacementObjectForKeyedArchiver:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

NSKeyedUnarchiverDelegate = _objc.informal_protocol(
    "NSKeyedUnarchiverDelegate",
    [
# (Class)unarchiver:(NSKeyedUnarchiver *)unarchiver cannotDecodeObjectOfClassName:(NSString *)name originalClasses:(NSArray *)classNames
        _objc.selector(
            None,
            selector='unarchiver:cannotDecodeObjectOfClassName:originalClasses:',
            signature='#@:@@@',
            isRequired=0,
        ),
# (id)unarchiver:(NSKeyedUnarchiver *)unarchiver didDecodeObject:(id)object
        _objc.selector(
            None,
            selector='unarchiver:didDecodeObject:',
            signature='@@:@@',
            isRequired=0,
        ),
# (void)unarchiver:(NSKeyedUnarchiver *)unarchiver willReplaceObject:(id)object withObject:(id)newObject
        _objc.selector(
            None,
            selector='unarchiver:willReplaceObject:withObject:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)unarchiverDidFinish:(NSKeyedUnarchiver *)unarchiver
        _objc.selector(
            None,
            selector='unarchiverDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)unarchiverWillFinish:(NSKeyedUnarchiver *)unarchiver
        _objc.selector(
            None,
            selector='unarchiverWillFinish:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSKeyedUnarchiverObjectSubstitution = _objc.informal_protocol(
    "NSKeyedUnarchiverObjectSubstitution",
    [
    ]
)

NSLocking = _objc.informal_protocol(
    "NSLocking",
    [
# (void)lock
        _objc.selector(
            None,
            selector='lock',
            signature='v@:',
            isRequired=0,
        ),
# (void)unlock
        _objc.selector(
            None,
            selector='unlock',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

NSMachPortDelegateMethods = _objc.informal_protocol(
    "NSMachPortDelegateMethods",
    [
# (void)handleMachMessage:(void *)msg
        _objc.selector(
            None,
            selector='handleMachMessage:',
            signature='v@:^v',
            isRequired=0,
        ),
    ]
)

NSMainThreadPerformAdditions = _objc.informal_protocol(
    "NSMainThreadPerformAdditions",
    [
# (void)performSelectorOnMainThread:(SEL)aSelector withObject:(id)arg waitUntilDone:(BOOL)wait
        _objc.selector(
            None,
            selector='performSelectorOnMainThread:withObject:waitUntilDone:',
            signature='v@::@c',
            isRequired=0,
        ),
# (void)performSelectorOnMainThread:(SEL)aSelector withObject:(id)arg waitUntilDone:(BOOL)wait modes:(NSArray *)array
        _objc.selector(
            None,
            selector='performSelectorOnMainThread:withObject:waitUntilDone:modes:',
            signature='v@::@c@',
            isRequired=0,
        ),
    ]
)

NSMutableCopying = _objc.informal_protocol(
    "NSMutableCopying",
    [
# (id)mutableCopyWithZone:(NSZone *)zone
        _objc.selector(
            None,
            selector='mutableCopyWithZone:',
            signature='@@:^{_NSZone=}',
            isRequired=0,
        ),
    ]
)

NSNetServiceBrowserDelegateMethods = _objc.informal_protocol(
    "NSNetServiceBrowserDelegateMethods",
    [
# (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindDomain:(NSString *)domainString moreComing:(BOOL)moreComing
        _objc.selector(
            None,
            selector='netServiceBrowser:didFindDomain:moreComing:',
            signature='v@:@@c',
            isRequired=0,
        ),
# (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindService:(NSNetService *)aNetService moreComing:(BOOL)moreComing
        _objc.selector(
            None,
            selector='netServiceBrowser:didFindService:moreComing:',
            signature='v@:@@c',
            isRequired=0,
        ),
# (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didNotSearch:(NSDictionary *)errorDict
        _objc.selector(
            None,
            selector='netServiceBrowser:didNotSearch:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveDomain:(NSString *)domainString moreComing:(BOOL)moreComing
        _objc.selector(
            None,
            selector='netServiceBrowser:didRemoveDomain:moreComing:',
            signature='v@:@@c',
            isRequired=0,
        ),
# (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveService:(NSNetService *)aNetService moreComing:(BOOL)moreComing
        _objc.selector(
            None,
            selector='netServiceBrowser:didRemoveService:moreComing:',
            signature='v@:@@c',
            isRequired=0,
        ),
# (void)netServiceBrowserDidStopSearch:(NSNetServiceBrowser *)aNetServiceBrowser
        _objc.selector(
            None,
            selector='netServiceBrowserDidStopSearch:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)netServiceBrowserWillSearch:(NSNetServiceBrowser *)aNetServiceBrowser
        _objc.selector(
            None,
            selector='netServiceBrowserWillSearch:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSNetServiceDelegateMethods = _objc.informal_protocol(
    "NSNetServiceDelegateMethods",
    [
# (void)netService:(NSNetService *)sender didNotPublish:(NSDictionary *)errorDict
        _objc.selector(
            None,
            selector='netService:didNotPublish:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)netService:(NSNetService *)sender didNotResolve:(NSDictionary *)errorDict
        _objc.selector(
            None,
            selector='netService:didNotResolve:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)netServiceDidResolveAddress:(NSNetService *)sender
        _objc.selector(
            None,
            selector='netServiceDidResolveAddress:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)netServiceDidStop:(NSNetService *)sender
        _objc.selector(
            None,
            selector='netServiceDidStop:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)netServiceWillPublish:(NSNetService *)sender
        _objc.selector(
            None,
            selector='netServiceWillPublish:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)netServiceWillResolve:(NSNetService *)sender
        _objc.selector(
            None,
            selector='netServiceWillResolve:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSObjCTypeSerializationCallBack = _objc.informal_protocol(
    "NSObjCTypeSerializationCallBack",
    [
# (void)deserializeObjectAt:(id *)object ofObjCType:(const char *)type fromData:(NSData *)data atCursor:(unsigned *)cursor
        _objc.selector(
            None,
            selector='deserializeObjectAt:ofObjCType:fromData:atCursor:',
            signature='v@:^@*@^I',
            isRequired=0,
        ),
# (void)serializeObjectAt:(id *)object ofObjCType:(const char *)type intoData:(NSMutableData *)data
        _objc.selector(
            None,
            selector='serializeObjectAt:ofObjCType:intoData:',
            signature='v@:^@*@',
            isRequired=0,
        ),
    ]
)

NSObject = _objc.informal_protocol(
    "NSObject",
    [
# (id)autorelease
        _objc.selector(
            None,
            selector='autorelease',
            signature='@@:',
            isRequired=0,
        ),
# (Class)class
        _objc.selector(
            None,
            selector='class',
            signature='#@:',
            isRequired=0,
        ),
# (BOOL)conformsToProtocol:(Protocol *)aProtocol
        _objc.selector(
            None,
            selector='conformsToProtocol:',
            signature='c@:@',
            isRequired=0,
        ),
# (NSString *)description
        _objc.selector(
            None,
            selector='description',
            signature='@@:',
            isRequired=0,
        ),
# (unsigned)hash
        _objc.selector(
            None,
            selector='hash',
            signature='I@:',
            isRequired=0,
        ),
# (BOOL)isEqual:(id)object
        _objc.selector(
            None,
            selector='isEqual:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)isKindOfClass:(Class)aClass
        _objc.selector(
            None,
            selector='isKindOfClass:',
            signature='c@:#',
            isRequired=0,
        ),
# (BOOL)isMemberOfClass:(Class)aClass
        _objc.selector(
            None,
            selector='isMemberOfClass:',
            signature='c@:#',
            isRequired=0,
        ),
# (BOOL)isProxy
        _objc.selector(
            None,
            selector='isProxy',
            signature='c@:',
            isRequired=0,
        ),
# (id)performSelector:(SEL)aSelector
        _objc.selector(
            None,
            selector='performSelector:',
            signature='@@::',
            isRequired=0,
        ),
# (id)performSelector:(SEL)aSelector withObject:(id)object
        _objc.selector(
            None,
            selector='performSelector:withObject:',
            signature='@@::@',
            isRequired=0,
        ),
# (id)performSelector:(SEL)aSelector withObject:(id)object1 withObject:(id)object2
        _objc.selector(
            None,
            selector='performSelector:withObject:withObject:',
            signature='@@::@@',
            isRequired=0,
        ),
# (oneway void)release
        _objc.selector(
            None,
            selector='release',
            signature='v@:',
            isRequired=0,
        ),
# (BOOL)respondsToSelector:(SEL)aSelector
        _objc.selector(
            None,
            selector='respondsToSelector:',
            signature='c@::',
            isRequired=0,
        ),
# (id)retain
        _objc.selector(
            None,
            selector='retain',
            signature='@@:',
            isRequired=0,
        ),
# (unsigned)retainCount
        _objc.selector(
            None,
            selector='retainCount',
            signature='I@:',
            isRequired=0,
        ),
# (id)self
        _objc.selector(
            None,
            selector='self',
            signature='@@:',
            isRequired=0,
        ),
# (Class)superclass
        _objc.selector(
            None,
            selector='superclass',
            signature='#@:',
            isRequired=0,
        ),
# (NSZone *)zone
        _objc.selector(
            None,
            selector='zone',
            signature='^{_NSZone=}@:',
            isRequired=0,
        ),
    ]
)

NSPortDelegateMethods = _objc.informal_protocol(
    "NSPortDelegateMethods",
    [
# (void)handlePortMessage:(NSPortMessage *)message
        _objc.selector(
            None,
            selector='handlePortMessage:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSScriptClassDescription = _objc.informal_protocol(
    "NSScriptClassDescription",
    [
# (unsigned long)classCode
        _objc.selector(
            None,
            selector='classCode',
            signature='L@:',
            isRequired=0,
        ),
# (NSString *)className
        _objc.selector(
            None,
            selector='className',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

NSScriptKeyValueCoding = _objc.informal_protocol(
    "NSScriptKeyValueCoding",
    [
# (id)coerceValue:(id)value forKey:(NSString *)key
        _objc.selector(
            None,
            selector='coerceValue:forKey:',
            signature='@@:@@',
            isRequired=0,
        ),
# (void)insertValue:(id)value atIndex:(unsigned)index inPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='insertValue:atIndex:inPropertyWithKey:',
            signature='v@:@I@',
            isRequired=0,
        ),
# (void)insertValue:(id)value inPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='insertValue:inPropertyWithKey:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)removeValueAtIndex:(unsigned)index fromPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='removeValueAtIndex:fromPropertyWithKey:',
            signature='v@:I@',
            isRequired=0,
        ),
# (void)replaceValueAtIndex:(unsigned)index inPropertyWithKey:(NSString *)key withValue:(id)value
        _objc.selector(
            None,
            selector='replaceValueAtIndex:inPropertyWithKey:withValue:',
            signature='v@:I@@',
            isRequired=0,
        ),
# (id)valueAtIndex:(unsigned)index inPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='valueAtIndex:inPropertyWithKey:',
            signature='@@:I@',
            isRequired=0,
        ),
# (id)valueWithName:(NSString *)name inPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='valueWithName:inPropertyWithKey:',
            signature='@@:@@',
            isRequired=0,
        ),
# (id)valueWithUniqueID:(id)uniqueID inPropertyWithKey:(NSString *)key
        _objc.selector(
            None,
            selector='valueWithUniqueID:inPropertyWithKey:',
            signature='@@:@@',
            isRequired=0,
        ),
    ]
)

NSScriptObjectSpecifiers = _objc.informal_protocol(
    "NSScriptObjectSpecifiers",
    [
# (NSArray *)indicesOfObjectsByEvaluatingObjectSpecifier:(NSScriptObjectSpecifier *)specifier
        _objc.selector(
            None,
            selector='indicesOfObjectsByEvaluatingObjectSpecifier:',
            signature='@@:@',
            isRequired=0,
        ),
# (NSScriptObjectSpecifier *)objectSpecifier
        _objc.selector(
            None,
            selector='objectSpecifier',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

NSScripting = _objc.informal_protocol(
    "NSScripting",
    [
# (NSDictionary *)scriptingProperties
        _objc.selector(
            None,
            selector='scriptingProperties',
            signature='@@:',
            isRequired=0,
        ),
# (void)setScriptingProperties:(NSDictionary *)properties
        _objc.selector(
            None,
            selector='setScriptingProperties:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSScriptingComparisonMethods = _objc.informal_protocol(
    "NSScriptingComparisonMethods",
    [
# (BOOL)scriptingBeginsWith:(id)object
        _objc.selector(
            None,
            selector='scriptingBeginsWith:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingContains:(id)object
        _objc.selector(
            None,
            selector='scriptingContains:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingEndsWith:(id)object
        _objc.selector(
            None,
            selector='scriptingEndsWith:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingIsEqualTo:(id)object
        _objc.selector(
            None,
            selector='scriptingIsEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingIsGreaterThan:(id)object
        _objc.selector(
            None,
            selector='scriptingIsGreaterThan:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingIsGreaterThanOrEqualTo:(id)object
        _objc.selector(
            None,
            selector='scriptingIsGreaterThanOrEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingIsLessThan:(id)object
        _objc.selector(
            None,
            selector='scriptingIsLessThan:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)scriptingIsLessThanOrEqualTo:(id)object
        _objc.selector(
            None,
            selector='scriptingIsLessThanOrEqualTo:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

NSSpellServerDelegate = _objc.informal_protocol(
    "NSSpellServerDelegate",
    [
# (void)spellServer:(NSSpellServer *)sender didForgetWord:(NSString *)word inLanguage:(NSString *)language
        _objc.selector(
            None,
            selector='spellServer:didForgetWord:inLanguage:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)spellServer:(NSSpellServer *)sender didLearnWord:(NSString *)word inLanguage:(NSString *)language
        _objc.selector(
            None,
            selector='spellServer:didLearnWord:inLanguage:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (NSRange)spellServer:(NSSpellServer *)sender findMisspelledWordInString:(NSString *)stringToCheck language:(NSString *)language wordCount:(int *)wordCount countOnly:(BOOL)countOnly
        _objc.selector(
            None,
            selector='spellServer:findMisspelledWordInString:language:wordCount:countOnly:',
            signature='{_NSRange=II}@:@@@^ic',
            isRequired=0,
        ),
# (NSArray *)spellServer:(NSSpellServer *)sender suggestCompletionsForPartialWordRange:(NSRange)range inString:(NSString *)string language:(NSString *)language
        _objc.selector(
            None,
            selector='spellServer:suggestCompletionsForPartialWordRange:inString:language:',
            signature='@@:@{_NSRange=II}@@',
            isRequired=0,
        ),
# (NSArray *)spellServer:(NSSpellServer *)sender suggestGuessesForWord:(NSString *)word inLanguage:(NSString *)language
        _objc.selector(
            None,
            selector='spellServer:suggestGuessesForWord:inLanguage:',
            signature='@@:@@@',
            isRequired=0,
        ),
    ]
)

NSStreamDelegateEventExtensions = _objc.informal_protocol(
    "NSStreamDelegateEventExtensions",
    [
# (void)stream:(NSStream *)aStream handleEvent:(NSStreamEvent)eventCode
        _objc.selector(
            None,
            selector='stream:handleEvent:',
            signature='v@:@i',
            isRequired=0,
        ),
    ]
)

NSURLAuthenticationChallengeSender = _objc.informal_protocol(
    "NSURLAuthenticationChallengeSender",
    [
# (void)cancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='cancelAuthenticationChallenge:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)continueWithoutCredentialForAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='continueWithoutCredentialForAuthenticationChallenge:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)useCredential:(NSURLCredential *)credential forAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='useCredential:forAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

NSURLClient = _objc.informal_protocol(
    "NSURLClient",
    [
# (void)URL:(NSURL *)sender resourceDataDidBecomeAvailable:(NSData *)newBytes
        _objc.selector(
            None,
            selector='URL:resourceDataDidBecomeAvailable:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URL:(NSURL *)sender resourceDidFailLoadingWithReason:(NSString *)reason
        _objc.selector(
            None,
            selector='URL:resourceDidFailLoadingWithReason:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLResourceDidCancelLoading:(NSURL *)sender
        _objc.selector(
            None,
            selector='URLResourceDidCancelLoading:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)URLResourceDidFinishLoading:(NSURL *)sender
        _objc.selector(
            None,
            selector='URLResourceDidFinishLoading:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSURLConnectionDelegate = _objc.informal_protocol(
    "NSURLConnectionDelegate",
    [
# (void)connection:(NSURLConnection *)connection didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='connection:didCancelAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)connection:(NSURLConnection *)connection didFailWithError:(NSError *)error
        _objc.selector(
            None,
            selector='connection:didFailWithError:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)connection:(NSURLConnection *)connection didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='connection:didReceiveAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data
        _objc.selector(
            None,
            selector='connection:didReceiveData:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response
        _objc.selector(
            None,
            selector='connection:didReceiveResponse:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSCachedURLResponse *)connection:(NSURLConnection *)connection willCacheResponse:(NSCachedURLResponse *)cachedResponse
        _objc.selector(
            None,
            selector='connection:willCacheResponse:',
            signature='@@:@@',
            isRequired=0,
        ),
# (NSURLRequest *)connection:(NSURLConnection *)connection willSendRequest:(NSURLRequest *)request redirectResponse:(NSURLResponse *)response
        _objc.selector(
            None,
            selector='connection:willSendRequest:redirectResponse:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (void)connectionDidFinishLoading:(NSURLConnection *)connection
        _objc.selector(
            None,
            selector='connectionDidFinishLoading:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSURLDownloadDelegate = _objc.informal_protocol(
    "NSURLDownloadDelegate",
    [
# (void)download:(NSURLDownload *)download decideDestinationWithSuggestedFilename:(NSString *)filename
        _objc.selector(
            None,
            selector='download:decideDestinationWithSuggestedFilename:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='download:didCancelAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didCreateDestination:(NSString *)path
        _objc.selector(
            None,
            selector='download:didCreateDestination:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didFailWithError:(NSError *)error
        _objc.selector(
            None,
            selector='download:didFailWithError:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='download:didReceiveAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didReceiveDataOfLength:(unsigned)length
        _objc.selector(
            None,
            selector='download:didReceiveDataOfLength:',
            signature='v@:@I',
            isRequired=0,
        ),
# (void)download:(NSURLDownload *)download didReceiveResponse:(NSURLResponse *)response
        _objc.selector(
            None,
            selector='download:didReceiveResponse:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)download:(NSURLDownload *)download shouldDecodeSourceDataOfMIMEType:(NSString *)encodingType
        _objc.selector(
            None,
            selector='download:shouldDecodeSourceDataOfMIMEType:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSURLRequest *)download:(NSURLDownload *)download willSendRequest:(NSURLRequest *)request redirectResponse:(NSURLResponse *)redirectResponse
        _objc.selector(
            None,
            selector='download:willSendRequest:redirectResponse:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (void)downloadDidBegin:(NSURLDownload *)download
        _objc.selector(
            None,
            selector='downloadDidBegin:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)downloadDidFinish:(NSURLDownload *)download
        _objc.selector(
            None,
            selector='downloadDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSURLHandleClient = _objc.informal_protocol(
    "NSURLHandleClient",
    [
# (void)URLHandle:(NSURLHandle *)sender resourceDataDidBecomeAvailable:(NSData *)newBytes
        _objc.selector(
            None,
            selector='URLHandle:resourceDataDidBecomeAvailable:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLHandle:(NSURLHandle *)sender resourceDidFailLoadingWithReason:(NSString *)reason
        _objc.selector(
            None,
            selector='URLHandle:resourceDidFailLoadingWithReason:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLHandleResourceDidBeginLoading:(NSURLHandle *)sender
        _objc.selector(
            None,
            selector='URLHandleResourceDidBeginLoading:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)URLHandleResourceDidCancelLoading:(NSURLHandle *)sender
        _objc.selector(
            None,
            selector='URLHandleResourceDidCancelLoading:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)URLHandleResourceDidFinishLoading:(NSURLHandle *)sender
        _objc.selector(
            None,
            selector='URLHandleResourceDidFinishLoading:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSURLProtocolClient = _objc.informal_protocol(
    "NSURLProtocolClient",
    [
# (void)URLProtocol:(NSURLProtocol *)protocol cachedResponseIsValid:(NSCachedURLResponse *)cachedResponse
        _objc.selector(
            None,
            selector='URLProtocol:cachedResponseIsValid:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='URLProtocol:didCancelAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol didFailWithError:(NSError *)error
        _objc.selector(
            None,
            selector='URLProtocol:didFailWithError:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol didLoadData:(NSData *)data
        _objc.selector(
            None,
            selector='URLProtocol:didLoadData:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge
        _objc.selector(
            None,
            selector='URLProtocol:didReceiveAuthenticationChallenge:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol didReceiveResponse:(NSURLResponse *)response cacheStoragePolicy:(NSURLCacheStoragePolicy)policy
        _objc.selector(
            None,
            selector='URLProtocol:didReceiveResponse:cacheStoragePolicy:',
            signature='v@:@@i',
            isRequired=0,
        ),
# (void)URLProtocol:(NSURLProtocol *)protocol wasRedirectedToRequest:(NSURLRequest *)request redirectResponse:(NSURLResponse *)redirectResponse
        _objc.selector(
            None,
            selector='URLProtocol:wasRedirectedToRequest:redirectResponse:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)URLProtocolDidFinishLoading:(NSURLProtocol *)protocol
        _objc.selector(
            None,
            selector='URLProtocolDidFinishLoading:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

NSXMLParserDelegateEventAdditions = _objc.informal_protocol(
    "NSXMLParserDelegateEventAdditions",
    [
# (void)parser:(NSXMLParser *)parser didEndElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName
        _objc.selector(
            None,
            selector='parser:didEndElement:namespaceURI:qualifiedName:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser didEndMappingPrefix:(NSString *)prefix
        _objc.selector(
            None,
            selector='parser:didEndMappingPrefix:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser didStartElement:(NSString *)elementName namespaceURI:(NSString *)namespaceURI qualifiedName:(NSString *)qName attributes:(NSDictionary *)attributeDict
        _objc.selector(
            None,
            selector='parser:didStartElement:namespaceURI:qualifiedName:attributes:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser didStartMappingPrefix:(NSString *)prefix toURI:(NSString *)namespaceURI
        _objc.selector(
            None,
            selector='parser:didStartMappingPrefix:toURI:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundAttributeDeclarationWithName:(NSString *)attributeName forElement:(NSString *)elementName type:(NSString *)type defaultValue:(NSString *)defaultValue
        _objc.selector(
            None,
            selector='parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundCDATA:(NSData *)CDATABlock
        _objc.selector(
            None,
            selector='parser:foundCDATA:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundCharacters:(NSString *)string
        _objc.selector(
            None,
            selector='parser:foundCharacters:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundComment:(NSString *)comment
        _objc.selector(
            None,
            selector='parser:foundComment:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundElementDeclarationWithName:(NSString *)elementName model:(NSString *)model
        _objc.selector(
            None,
            selector='parser:foundElementDeclarationWithName:model:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundExternalEntityDeclarationWithName:(NSString *)name publicID:(NSString *)publicID systemID:(NSString *)systemID
        _objc.selector(
            None,
            selector='parser:foundExternalEntityDeclarationWithName:publicID:systemID:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundIgnorableWhitespace:(NSString *)whitespaceString
        _objc.selector(
            None,
            selector='parser:foundIgnorableWhitespace:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundInternalEntityDeclarationWithName:(NSString *)name value:(NSString *)value
        _objc.selector(
            None,
            selector='parser:foundInternalEntityDeclarationWithName:value:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundNotationDeclarationWithName:(NSString *)name publicID:(NSString *)publicID systemID:(NSString *)systemID
        _objc.selector(
            None,
            selector='parser:foundNotationDeclarationWithName:publicID:systemID:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundProcessingInstructionWithTarget:(NSString *)target data:(NSString *)data
        _objc.selector(
            None,
            selector='parser:foundProcessingInstructionWithTarget:data:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser foundUnparsedEntityDeclarationWithName:(NSString *)name publicID:(NSString *)publicID systemID:(NSString *)systemID notationName:(NSString *)notationName
        _objc.selector(
            None,
            selector='parser:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser parseErrorOccurred:(NSError *)parseError
        _objc.selector(
            None,
            selector='parser:parseErrorOccurred:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSData *)parser:(NSXMLParser *)parser resolveExternalEntityName:(NSString *)name systemID:(NSString *)systemID
        _objc.selector(
            None,
            selector='parser:resolveExternalEntityName:systemID:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (void)parser:(NSXMLParser *)parser validationErrorOccurred:(NSError *)validationError
        _objc.selector(
            None,
            selector='parser:validationErrorOccurred:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)parserDidEndDocument:(NSXMLParser *)parser
        _objc.selector(
            None,
            selector='parserDidEndDocument:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)parserDidStartDocument:(NSXMLParser *)parser
        _objc.selector(
            None,
            selector='parserDidStartDocument:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

