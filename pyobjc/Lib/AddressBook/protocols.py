# generated from '/System/Library/Frameworks/AddressBook.framework'
import objc as _objc


ABActionDelegate = _objc.informal_protocol(
    "ABActionDelegate",
    [
# (NSString *)actionProperty
        _objc.selector(
            None,
            selector='actionProperty',
            signature='@@:',
            isRequired=0,
        ),
# (void)performActionForPerson:(ABPerson *)person identifier:(NSString *)identifier
        _objc.selector(
            None,
            selector='performActionForPerson:identifier:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)shouldEnableActionForPerson:(ABPerson *)person identifier:(NSString *)identifier
        _objc.selector(
            None,
            selector='shouldEnableActionForPerson:identifier:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSString *)titleForPerson:(ABPerson *)person identifier:(NSString *)identifier
        _objc.selector(
            None,
            selector='titleForPerson:identifier:',
            signature='@@:@@',
            isRequired=0,
        ),
    ]
)

ABImageClient = _objc.informal_protocol(
    "ABImageClient",
    [
# (void)consumeImageData:(NSData *)data forTag:(int)tag
        _objc.selector(
            None,
            selector='consumeImageData:forTag:',
            signature='v@:@i',
            isRequired=0,
        ),
    ]
)

