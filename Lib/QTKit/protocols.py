# generated from '/System/Library/Frameworks/QTKit.framework'
import objc as _objc


QTMovieDelegate = _objc.informal_protocol(
    "QTMovieDelegate",
    [
# (QTMovie *)externalMovie:(NSDictionary *)dictionary
        _objc.selector(
            None,
            selector='externalMovie:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)movie:(QTMovie *)movie linkToURL:(NSURL *)url
        _objc.selector(
            None,
            selector='movie:linkToURL:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)movie:(QTMovie *)movie shouldContinueOperation:(NSString *)op withPhase:(QTMovieOperationPhase)phase atPercent:(NSNumber *)percent withAttributes:(NSDictionary *)attributes
        _objc.selector(
            None,
            selector='movie:shouldContinueOperation:withPhase:atPercent:withAttributes:',
            signature='c@:@@i@@',
            isRequired=0,
        ),
# (BOOL)movieShouldLoadData:(id)sender
        _objc.selector(
            None,
            selector='movieShouldLoadData:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)movieShouldTask:(id)movie
        _objc.selector(
            None,
            selector='movieShouldTask:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

