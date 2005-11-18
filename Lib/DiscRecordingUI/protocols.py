# generated from '/System/Library/Frameworks/DiscRecordingUI.framework'
import objc as _objc


DRBurnProgressPanelDelegateMethods = _objc.informal_protocol(
    "DRBurnProgressPanelDelegateMethods",
    [
# (BOOL) burnProgressPanel:(DRBurnProgressPanel*)theBurnPanel burnDidFinish:(DRBurn*)burn
        _objc.selector(
            None,
            selector='burnProgressPanel:burnDidFinish:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void) burnProgressPanelDidFinish:(NSNotification*)aNotification
        _objc.selector(
            None,
            selector='burnProgressPanelDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) burnProgressPanelWillBegin:(NSNotification*)aNotification
        _objc.selector(
            None,
            selector='burnProgressPanelWillBegin:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

DREraseProgressPanelDelegateMethods = _objc.informal_protocol(
    "DREraseProgressPanelDelegateMethods",
    [
# (BOOL) eraseProgressPanel:(DREraseProgressPanel*)theErasePanel eraseDidFinish:(DRErase*)erase
        _objc.selector(
            None,
            selector='eraseProgressPanel:eraseDidFinish:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void) eraseProgressPanelDidFinish:(NSNotification*)aNotification
        _objc.selector(
            None,
            selector='eraseProgressPanelDidFinish:',
            signature='v@:@',
            isRequired=0,
        ),
# (void) eraseProgressPanelWillBegin:(NSNotification*)aNotification
        _objc.selector(
            None,
            selector='eraseProgressPanelWillBegin:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

DRSetupPanelDelegate = _objc.informal_protocol(
    "DRSetupPanelDelegate",
    [
# (BOOL) setupPanel:(DRSetupPanel*)aPanel deviceContainsSuitableMedia:(DRDevice*)device promptString:(NSString**)prompt
        _objc.selector(
            None,
            selector='setupPanel:deviceContainsSuitableMedia:promptString:',
            signature='c@:@@o^@',
            isRequired=0,
        ),
# (BOOL) setupPanel:(DRSetupPanel*)aPanel deviceCouldBeTarget:(DRDevice*)device
        _objc.selector(
            None,
            selector='setupPanel:deviceCouldBeTarget:',
            signature='c@:@@',
            isRequired=0,
        ),
# (void) setupPanelDeviceSelectionChanged:(NSNotification*)aNotification
        _objc.selector(
            None,
            selector='setupPanelDeviceSelectionChanged:',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL) setupPanelShouldHandleMediaReservations:(DRSetupPanel*)aPanel
        _objc.selector(
            None,
            selector='setupPanelShouldHandleMediaReservations:',
            signature='c@:@',
            isRequired=0,
        ),
    ]
)

