# generated from '/System/Library/Frameworks/ExceptionHandling.framework'
import objc as _objc


NSExceptionHandlerDelegate = _objc.informal_protocol(
    "NSExceptionHandlerDelegate",
    [
# (BOOL)exceptionHandler:(NSExceptionHandler *)sender shouldHandleException:(NSException *)exception mask:(unsigned int)aMask
        _objc.selector(
            None,
            selector='exceptionHandler:shouldHandleException:mask:',
            signature='c@:@@I',
            isRequired=0,
        ),
# (BOOL)exceptionHandler:(NSExceptionHandler *)sender shouldLogException:(NSException *)exception mask:(unsigned int)aMask
        _objc.selector(
            None,
            selector='exceptionHandler:shouldLogException:mask:',
            signature='c@:@@I',
            isRequired=0,
        ),
    ]
)

