# generated from '/System/Library/Frameworks/SecurityInterface.framework'
import objc as _objc


SFAuthorizationViewDelegate = _objc.informal_protocol(
    "SFAuthorizationViewDelegate",
    [
# (void)authorizationViewCreatedAuthorization:(SFAuthorizationView *)view
        _objc.selector(
            None,
            selector='authorizationViewCreatedAuthorization:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)authorizationViewDidAuthorize:(SFAuthorizationView *)view
        _objc.selector(
            None,
            selector='authorizationViewDidAuthorize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)authorizationViewDidDeauthorize:(SFAuthorizationView *)view
        _objc.selector(
            None,
            selector='authorizationViewDidDeauthorize:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)authorizationViewReleasedAuthorization:(SFAuthorizationView *)view
        _objc.selector(
            None,
            selector='authorizationViewReleasedAuthorization:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)authorizationViewShouldDeauthorize:(SFAuthorizationView *)view
        _objc.selector(
            None,
            selector='authorizationViewShouldDeauthorize:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)
