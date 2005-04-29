# generated from '/System/Library/Frameworks/SyncServices.framework'
import objc as _objc


ISyncFiltering = _objc.informal_protocol(
    "ISyncFiltering",
    [
# (BOOL)isEqual:(id)anotherFilter
        _objc.selector(
            None,
            selector='isEqual:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)shouldApplyRecord:(NSDictionary *)record withRecordIdentifier:(NSString *)recordId
        _objc.selector(
            None,
            selector='shouldApplyRecord:withRecordIdentifier:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSArray /* NSString */ *)supportedEntityNames
        _objc.selector(
            None,
            selector='supportedEntityNames',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

