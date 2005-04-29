# generated from '/System/Library/Frameworks/XgridFoundation.framework'
import objc as _objc


XGAuthenticatorDelegate = _objc.informal_protocol(
    "XGAuthenticatorDelegate",
    [
# (void)authenticatorDidAuthenticate:(XGAuthenticator *)authenticator
        _objc.selector(
            None,
            selector='authenticatorDidAuthenticate:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)authenticatorDidNotAuthenticate:(XGAuthenticator *)authenticator
        _objc.selector(
            None,
            selector='authenticatorDidNotAuthenticate:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

XGConnectionDelegate = _objc.informal_protocol(
    "XGConnectionDelegate",
    [
# (void)connectionDidClose:(XGConnection *)connection
        _objc.selector(
            None,
            selector='connectionDidClose:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)connectionDidNotOpen:(XGConnection *)connection withError:(NSError *)error
        _objc.selector(
            None,
            selector='connectionDidNotOpen:withError:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)connectionDidOpen:(XGConnection *)connection
        _objc.selector(
            None,
            selector='connectionDidOpen:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

XGFileDownloadDelegate = _objc.informal_protocol(
    "XGFileDownloadDelegate",
    [
# (void)fileDownload:(XGFileDownload *)fileDownload decideDestinationWithSuggestedPath:(NSString *)path
        _objc.selector(
            None,
            selector='fileDownload:decideDestinationWithSuggestedPath:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)fileDownload:(XGFileDownload *)fileDownload didCreateDestination:(NSString *)destination
        _objc.selector(
            None,
            selector='fileDownload:didCreateDestination:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)fileDownload:(XGFileDownload *)fileDownload didFailWithError:(NSError *)error
        _objc.selector(
            None,
            selector='fileDownload:didFailWithError:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)fileDownload:(XGFileDownload *)fileDownload didReceiveAttributes:(NSDictionary *)attributes
        _objc.selector(
            None,
            selector='fileDownload:didReceiveAttributes:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)fileDownload:(XGFileDownload *)fileDownload didReceiveData:(NSData *)data
        _objc.selector(
            None,
            selector='fileDownload:didReceiveData:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)fileDownloadDidBegin:(XGFileDownload *)fileDownload
        _objc.selector(
            None,
            selector='fileDownloadDidBegin:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)fileDownloadDidFinish:(XGFileDownload *)fileDownload
        _objc.selector(
            None,
            selector='fileDownloadDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

