# generated from '/System/Library/Frameworks/WebKit.framework'
import objc as _objc


DOMEventListener = _objc.informal_protocol(
    "DOMEventListener",
    [
# (void)handleEvent:(DOMEvent *)event
        _objc.selector(
            None,
            selector='handleEvent:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

DOMEventTarget = _objc.informal_protocol(
    "DOMEventTarget",
    [
# (void)addEventListener:(NSString *)type :(id <DOMEventListener>)listener :(BOOL)useCapture
        _objc.selector(
            None,
            selector='addEventListener:id',
            signature='v@:@',
            isRequired=0,
        ),
# (BOOL)dispatchEvent:(DOMEvent *)event
        _objc.selector(
            None,
            selector='dispatchEvent:',
            signature='c@:@',
            isRequired=0,
        ),
# (void)removeEventListener:(NSString *)type :(id <DOMEventListener>)listener :(BOOL)useCapture
        _objc.selector(
            None,
            selector='removeEventListener:id',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

DOMNodeFilter = _objc.informal_protocol(
    "DOMNodeFilter",
    [
# (short)acceptNode:(DOMNode *)n
        _objc.selector(
            None,
            selector='acceptNode:',
            signature='s@:@',
            isRequired=0,
        ),
    ]
)

WebDocumentRepresentation = _objc.informal_protocol(
    "WebDocumentRepresentation",
    [
# (BOOL)canProvideDocumentSource
        _objc.selector(
            None,
            selector='canProvideDocumentSource',
            signature='c@:',
            isRequired=0,
        ),
# (NSString *)documentSource
        _objc.selector(
            None,
            selector='documentSource',
            signature='@@:',
            isRequired=0,
        ),
# (void)finishedLoadingWithDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='finishedLoadingWithDataSource:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)receivedData:(NSData *)data withDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='receivedData:withDataSource:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)receivedError:(NSError *)error withDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='receivedError:withDataSource:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)setDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='setDataSource:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSString *)title
        _objc.selector(
            None,
            selector='title',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

WebDocumentSearching = _objc.informal_protocol(
    "WebDocumentSearching",
    [
# (BOOL)searchFor:(NSString *)string direction:(BOOL)forward caseSensitive:(BOOL)caseFlag wrap:(BOOL)wrapFlag
        _objc.selector(
            None,
            selector='searchFor:direction:caseSensitive:wrap:',
            signature='c@:@ccc',
            isRequired=0,
        ),
    ]
)

WebDocumentText = _objc.informal_protocol(
    "WebDocumentText",
    [
# (NSAttributedString *)attributedString
        _objc.selector(
            None,
            selector='attributedString',
            signature='@@:',
            isRequired=0,
        ),
# (void)deselectAll
        _objc.selector(
            None,
            selector='deselectAll',
            signature='v@:',
            isRequired=0,
        ),
# (void)selectAll
        _objc.selector(
            None,
            selector='selectAll',
            signature='v@:',
            isRequired=0,
        ),
# (NSAttributedString *)selectedAttributedString
        _objc.selector(
            None,
            selector='selectedAttributedString',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)selectedString
        _objc.selector(
            None,
            selector='selectedString',
            signature='@@:',
            isRequired=0,
        ),
# (NSString *)string
        _objc.selector(
            None,
            selector='string',
            signature='@@:',
            isRequired=0,
        ),
# (BOOL)supportsTextEncoding
        _objc.selector(
            None,
            selector='supportsTextEncoding',
            signature='c@:',
            isRequired=0,
        ),
    ]
)

WebDocumentView = _objc.informal_protocol(
    "WebDocumentView",
    [
# (BOOL)allowsScrolling
        _objc.selector(
            None,
            selector='allowsScrolling',
            signature='c@:',
            isRequired=0,
        ),
# (NSView <WebDocumentView> *)documentView
        _objc.selector(
            None,
            selector='documentView',
            signature='@@:',
            isRequired=0,
        ),
# (void)setAllowsScrolling:(BOOL)flag
        _objc.selector(
            None,
            selector='setAllowsScrolling:',
            signature='v@:c',
            isRequired=0,
        ),
# (WebFrame *)webFrame
        _objc.selector(
            None,
            selector='webFrame',
            signature='@@:',
            isRequired=0,
        ),
    ]
)

WebDownloadDelegate = _objc.informal_protocol(
    "WebDownloadDelegate",
    [
# (NSWindow *)downloadWindowForAuthenticationSheet:(WebDownload *)download
        _objc.selector(
            None,
            selector='downloadWindowForAuthenticationSheet:',
            signature='@@:@',
            isRequired=0,
        ),
    ]
)

WebFrameLoadDelegate = _objc.informal_protocol(
    "WebFrameLoadDelegate",
    [
# (void)webView:(WebView *)sender didCancelClientRedirectForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didCancelClientRedirectForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didChangeLocationWithinPageForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didChangeLocationWithinPageForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didCommitLoadForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didCommitLoadForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didFailLoadWithError:(NSError *)error forFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didFailLoadWithError:forFrame:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didFailProvisionalLoadWithError:(NSError *)error forFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didFailProvisionalLoadWithError:forFrame:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didFinishLoadForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didFinishLoadForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didReceiveIcon:(NSImage *)image forFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didReceiveIcon:forFrame:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didReceiveServerRedirectForProvisionalLoadForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didReceiveServerRedirectForProvisionalLoadForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didReceiveTitle:(NSString *)title forFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didReceiveTitle:forFrame:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender didStartProvisionalLoadForFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:didStartProvisionalLoadForFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender willCloseFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:willCloseFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender willPerformClientRedirectToURL:(NSURL *)URL delay:(NSTimeInterval)seconds fireDate:(NSDate *)date forFrame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:willPerformClientRedirectToURL:delay:fireDate:forFrame:',
            signature='v@:@@d@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView windowScriptObjectAvailable:(WebScriptObject *)windowScriptObject
        _objc.selector(
            None,
            selector='webView:windowScriptObjectAvailable:',
            signature='v@:@@',
            isRequired=0,
        ),
    ]
)

WebJavaPlugIn = _objc.informal_protocol(
    "WebJavaPlugIn",
    [
# (jvalue)webPlugInCallJava:(jobject)object isStatic:(BOOL)isStatic returnType:(WebJNIReturnType)returnType method:(jmethodID)method arguments:(jvalue*)args callingURL:(NSURL *)url exceptionDescription:(NSString **)exceptionString
        _objc.selector(
            None,
            selector='webPlugInCallJava:isStatic:returnType:method:arguments:callingURL:exceptionDescription:',
            signature='(jvalue=CcSsiqfd^{_jobject})@:^{_jobject=}ci^{_jmethodID=}^(jvalue=CcSsiqfd^{_jobject})@^@',
            isRequired=0,
        ),
# (jobject)webPlugInGetApplet
        _objc.selector(
            None,
            selector='webPlugInGetApplet',
            signature='^{_jobject=}@:',
            isRequired=0,
        ),
    ]
)

WebOpenPanelResultListener = _objc.informal_protocol(
    "WebOpenPanelResultListener",
    [
# (void)cancel
        _objc.selector(
            None,
            selector='cancel',
            signature='v@:',
            isRequired=0,
        ),
# (void)chooseFilename:(NSString *)fileName
        _objc.selector(
            None,
            selector='chooseFilename:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

WebPlugIn = _objc.informal_protocol(
    "WebPlugIn",
    [
# (id)objectForWebScript
        _objc.selector(
            None,
            selector='objectForWebScript',
            signature='@@:',
            isRequired=0,
        ),
# (void)webPlugInDestroy
        _objc.selector(
            None,
            selector='webPlugInDestroy',
            signature='v@:',
            isRequired=0,
        ),
# (void)webPlugInInitialize
        _objc.selector(
            None,
            selector='webPlugInInitialize',
            signature='v@:',
            isRequired=0,
        ),
# (void)webPlugInSetIsSelected:(BOOL)isSelected
        _objc.selector(
            None,
            selector='webPlugInSetIsSelected:',
            signature='v@:c',
            isRequired=0,
        ),
# (void)webPlugInStart
        _objc.selector(
            None,
            selector='webPlugInStart',
            signature='v@:',
            isRequired=0,
        ),
# (void)webPlugInStop
        _objc.selector(
            None,
            selector='webPlugInStop',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

WebPlugInContainer = _objc.informal_protocol(
    "WebPlugInContainer",
    [
# (WebFrame *)webFrame
        _objc.selector(
            None,
            selector='webFrame',
            signature='@@:',
            isRequired=0,
        ),
# (void)webPlugInContainerLoadRequest:(NSURLRequest *)request inFrame:(NSString *)target
        _objc.selector(
            None,
            selector='webPlugInContainerLoadRequest:inFrame:',
            signature='v@:@@',
            isRequired=0,
        ),
# (NSColor *)webPlugInContainerSelectionColor
        _objc.selector(
            None,
            selector='webPlugInContainerSelectionColor',
            signature='@@:',
            isRequired=0,
        ),
# (void)webPlugInContainerShowStatus:(NSString *)message
        _objc.selector(
            None,
            selector='webPlugInContainerShowStatus:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

WebPlugInViewFactory = _objc.informal_protocol(
    "WebPlugInViewFactory",
    [
# (NSView *)plugInViewWithArguments:(NSDictionary *)arguments
        _objc.selector(
            None,
            selector='plugInViewWithArguments:',
            signature='@@:@',
            isClassMethod=1,
            isRequired=0,
        ),
    ]
)

WebPolicyDecisionListener = _objc.informal_protocol(
    "WebPolicyDecisionListener",
    [
# (void)download
        _objc.selector(
            None,
            selector='download',
            signature='v@:',
            isRequired=0,
        ),
# (void)ignore
        _objc.selector(
            None,
            selector='ignore',
            signature='v@:',
            isRequired=0,
        ),
# (void)use
        _objc.selector(
            None,
            selector='use',
            signature='v@:',
            isRequired=0,
        ),
    ]
)

WebPolicyDelegate = _objc.informal_protocol(
    "WebPolicyDelegate",
    [
# (void)webView:(WebView *)webView decidePolicyForMIMEType:(NSString *)type request:(NSURLRequest *)request frame:(WebFrame *)frame decisionListener:(id<WebPolicyDecisionListener>)listener
        _objc.selector(
            None,
            selector='webView:decidePolicyForMIMEType:request:frame:decisionListener:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView decidePolicyForNavigationAction:(NSDictionary *)actionInformation request:(NSURLRequest *)request frame:(WebFrame *)frame decisionListener:(id<WebPolicyDecisionListener>)listener
        _objc.selector(
            None,
            selector='webView:decidePolicyForNavigationAction:request:frame:decisionListener:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView decidePolicyForNewWindowAction:(NSDictionary *)actionInformation request:(NSURLRequest *)request newFrameName:(NSString *)frameName decisionListener:(id<WebPolicyDecisionListener>)listener
        _objc.selector(
            None,
            selector='webView:decidePolicyForNewWindowAction:request:newFrameName:decisionListener:',
            signature='v@:@@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView unableToImplementPolicyWithError:(NSError *)error frame:(WebFrame *)frame
        _objc.selector(
            None,
            selector='webView:unableToImplementPolicyWithError:frame:',
            signature='v@:@@@',
            isRequired=0,
        ),
    ]
)

WebResourceLoadDelegate = _objc.informal_protocol(
    "WebResourceLoadDelegate",
    [
# (id)webView:(WebView *)sender identifierForInitialRequest:(NSURLRequest *)request fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:identifierForInitialRequest:fromDataSource:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender plugInFailedWithError:(NSError *)error dataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:plugInFailedWithError:dataSource:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didCancelAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didCancelAuthenticationChallenge:fromDataSource:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didFailLoadingWithError:(NSError *)error fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didFailLoadingWithError:fromDataSource:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didFinishLoadingFromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didFinishLoadingFromDataSource:',
            signature='v@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didReceiveAuthenticationChallenge:fromDataSource:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didReceiveContentLength: (unsigned)length fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didReceiveContentLength:fromDataSource:',
            signature='v@:@@I@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender resource:(id)identifier didReceiveResponse:(NSURLResponse *)response fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:didReceiveResponse:fromDataSource:',
            signature='v@:@@@@',
            isRequired=0,
        ),
# (NSURLRequest *)webView:(WebView *)sender resource:(id)identifier willSendRequest:(NSURLRequest *)request redirectResponse:(NSURLResponse *)redirectResponse fromDataSource:(WebDataSource *)dataSource
        _objc.selector(
            None,
            selector='webView:resource:willSendRequest:redirectResponse:fromDataSource:',
            signature='@@:@@@@@',
            isRequired=0,
        ),
    ]
)

WebScripting = _objc.informal_protocol(
    "WebScripting",
    [
# (void)finalizeForWebScript
        _objc.selector(
            None,
            selector='finalizeForWebScript',
            signature='v@:',
            isRequired=0,
        ),
# (id)invokeDefaultMethodWithArguments:(NSArray *)args
        _objc.selector(
            None,
            selector='invokeDefaultMethodWithArguments:',
            signature='@@:@',
            isRequired=0,
        ),
# (id)invokeUndefinedMethodFromWebScript:(NSString *)name withArguments:(NSArray *)args
        _objc.selector(
            None,
            selector='invokeUndefinedMethodFromWebScript:withArguments:',
            signature='@@:@@',
            isRequired=0,
        ),
# (BOOL)isKeyExcludedFromWebScript:(const char *)name
        _objc.selector(
            None,
            selector='isKeyExcludedFromWebScript:',
            signature='c@:r*',
            isClassMethod=1,
            isRequired=0,
        ),
# (BOOL)isSelectorExcludedFromWebScript:(SEL)aSelector
        _objc.selector(
            None,
            selector='isSelectorExcludedFromWebScript:',
            signature='c@::',
            isClassMethod=1,
            isRequired=0,
        ),
# (NSString *)webScriptNameForKey:(const char *)name
        _objc.selector(
            None,
            selector='webScriptNameForKey:',
            signature='@@:r*',
            isClassMethod=1,
            isRequired=0,
        ),
# (NSString *)webScriptNameForSelector:(SEL)aSelector
        _objc.selector(
            None,
            selector='webScriptNameForSelector:',
            signature='@@::',
            isClassMethod=1,
            isRequired=0,
        ),
    ]
)

WebUIDelegate = _objc.informal_protocol(
    "WebUIDelegate",
    [
# (NSArray *)webView:(WebView *)sender contextMenuItemsForElement:(NSDictionary *)element defaultMenuItems:(NSArray *)defaultMenuItems
        _objc.selector(
            None,
            selector='webView:contextMenuItemsForElement:defaultMenuItems:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (WebView *)webView:(WebView *)sender createWebViewWithRequest:(NSURLRequest *)request
        _objc.selector(
            None,
            selector='webView:createWebViewWithRequest:',
            signature='@@:@@',
            isRequired=0,
        ),
# (unsigned)webView:(WebView *)webView dragDestinationActionMaskForDraggingInfo:(id <NSDraggingInfo>)draggingInfo
        _objc.selector(
            None,
            selector='webView:dragDestinationActionMaskForDraggingInfo:',
            signature='I@:@@',
            isRequired=0,
        ),
# (unsigned)webView:(WebView *)webView dragSourceActionMaskForPoint:(NSPoint)point
        _objc.selector(
            None,
            selector='webView:dragSourceActionMaskForPoint:',
            signature='I@:@{_NSPoint=ff}',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender makeFirstResponder:(NSResponder *)responder
        _objc.selector(
            None,
            selector='webView:makeFirstResponder:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender mouseDidMoveOverElement:(NSDictionary *)elementInformation modifierFlags:(unsigned int)modifierFlags
        _objc.selector(
            None,
            selector='webView:mouseDidMoveOverElement:modifierFlags:',
            signature='v@:@@I',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender runJavaScriptAlertPanelWithMessage:(NSString *)message
        _objc.selector(
            None,
            selector='webView:runJavaScriptAlertPanelWithMessage:',
            signature='v@:@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)sender runJavaScriptConfirmPanelWithMessage:(NSString *)message
        _objc.selector(
            None,
            selector='webView:runJavaScriptConfirmPanelWithMessage:',
            signature='c@:@@',
            isRequired=0,
        ),
# (NSString *)webView:(WebView *)sender runJavaScriptTextInputPanelWithPrompt:(NSString *)prompt defaultText:(NSString *)defaultText
        _objc.selector(
            None,
            selector='webView:runJavaScriptTextInputPanelWithPrompt:defaultText:',
            signature='@@:@@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender runOpenPanelForFileButtonWithResultListener:(id<WebOpenPanelResultListener>)resultListener
        _objc.selector(
            None,
            selector='webView:runOpenPanelForFileButtonWithResultListener:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setContentRect:(NSRect)contentRect
        _objc.selector(
            None,
            selector='webView:setContentRect:',
            signature='v@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setFrame:(NSRect)frame
        _objc.selector(
            None,
            selector='webView:setFrame:',
            signature='v@:@{_NSRect={_NSPoint=ff}{_NSSize=ff}}',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setResizable:(BOOL)resizable
        _objc.selector(
            None,
            selector='webView:setResizable:',
            signature='v@:@c',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setStatusBarVisible:(BOOL)visible
        _objc.selector(
            None,
            selector='webView:setStatusBarVisible:',
            signature='v@:@c',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setStatusText:(NSString *)text
        _objc.selector(
            None,
            selector='webView:setStatusText:',
            signature='v@:@@',
            isRequired=0,
        ),
# (void)webView:(WebView *)sender setToolbarsVisible:(BOOL)visible
        _objc.selector(
            None,
            selector='webView:setToolbarsVisible:',
            signature='v@:@c',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldPerformAction:(SEL)action fromSender:(id)sender
        _objc.selector(
            None,
            selector='webView:shouldPerformAction:fromSender:',
            signature='c@:@:@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView validateUserInterfaceItem:(id <NSValidatedUserInterfaceItem>)item defaultValidation:(BOOL)defaultValidation
        _objc.selector(
            None,
            selector='webView:validateUserInterfaceItem:defaultValidation:',
            signature='c@:@@c',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView willPerformDragDestinationAction:(WebDragDestinationAction)action forDraggingInfo:(id <NSDraggingInfo>)draggingInfo
        _objc.selector(
            None,
            selector='webView:willPerformDragDestinationAction:forDraggingInfo:',
            signature='v@:@i@',
            isRequired=0,
        ),
# (void)webView:(WebView *)webView willPerformDragSourceAction:(WebDragSourceAction)action fromPoint:(NSPoint)point withPasteboard:(NSPasteboard *)pasteboard
        _objc.selector(
            None,
            selector='webView:willPerformDragSourceAction:fromPoint:withPasteboard:',
            signature='v@:@i{_NSPoint=ff}@',
            isRequired=0,
        ),
# (BOOL)webViewAreToolbarsVisible:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewAreToolbarsVisible:',
            signature='c@:@',
            isRequired=0,
        ),
# (void)webViewClose:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewClose:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSRect)webViewContentRect:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewContentRect:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@',
            isRequired=0,
        ),
# (NSResponder *)webViewFirstResponder:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewFirstResponder:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)webViewFocus:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewFocus:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSRect)webViewFrame:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewFrame:',
            signature='{_NSRect={_NSPoint=ff}{_NSSize=ff}}@:@',
            isRequired=0,
        ),
# (BOOL)webViewIsResizable:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewIsResizable:',
            signature='c@:@',
            isRequired=0,
        ),
# (BOOL)webViewIsStatusBarVisible:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewIsStatusBarVisible:',
            signature='c@:@',
            isRequired=0,
        ),
# (void)webViewShow:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewShow:',
            signature='v@:@',
            isRequired=0,
        ),
# (NSString *)webViewStatusText:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewStatusText:',
            signature='@@:@',
            isRequired=0,
        ),
# (void)webViewUnfocus:(WebView *)sender
        _objc.selector(
            None,
            selector='webViewUnfocus:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

WebViewEditingDelegate = _objc.informal_protocol(
    "WebViewEditingDelegate",
    [
# (NSUndoManager *)undoManagerForWebView:(WebView *)webView
        _objc.selector(
            None,
            selector='undoManagerForWebView:',
            signature='@@:@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView doCommandBySelector:(SEL)selector
        _objc.selector(
            None,
            selector='webView:doCommandBySelector:',
            signature='c@:@:',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldApplyStyle:(DOMCSSStyleDeclaration *)style toElementsInDOMRange:(DOMRange *)range
        _objc.selector(
            None,
            selector='webView:shouldApplyStyle:toElementsInDOMRange:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldBeginEditingInDOMRange:(DOMRange *)range
        _objc.selector(
            None,
            selector='webView:shouldBeginEditingInDOMRange:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldChangeSelectedDOMRange:(DOMRange *)currentRange toDOMRange:(DOMRange *)proposedRange affinity:(NSSelectionAffinity)selectionAffinity stillSelecting:(BOOL)flag
        _objc.selector(
            None,
            selector='webView:shouldChangeSelectedDOMRange:toDOMRange:affinity:stillSelecting:',
            signature='c@:@@@ic',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldChangeTypingStyle:(DOMCSSStyleDeclaration *)currentStyle toStyle:(DOMCSSStyleDeclaration *)proposedStyle
        _objc.selector(
            None,
            selector='webView:shouldChangeTypingStyle:toStyle:',
            signature='c@:@@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldDeleteDOMRange:(DOMRange *)range
        _objc.selector(
            None,
            selector='webView:shouldDeleteDOMRange:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldEndEditingInDOMRange:(DOMRange *)range
        _objc.selector(
            None,
            selector='webView:shouldEndEditingInDOMRange:',
            signature='c@:@@',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldInsertNode:(DOMNode *)node replacingDOMRange:(DOMRange *)range givenAction:(WebViewInsertAction)action
        _objc.selector(
            None,
            selector='webView:shouldInsertNode:replacingDOMRange:givenAction:',
            signature='c@:@@@i',
            isRequired=0,
        ),
# (BOOL)webView:(WebView *)webView shouldInsertText:(NSString *)text replacingDOMRange:(DOMRange *)range givenAction:(WebViewInsertAction)action
        _objc.selector(
            None,
            selector='webView:shouldInsertText:replacingDOMRange:givenAction:',
            signature='c@:@@@i',
            isRequired=0,
        ),
# (void)webViewDidBeginEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='webViewDidBeginEditing:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)webViewDidChange:(NSNotification *)notification
        _objc.selector(
            None,
            selector='webViewDidChange:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)webViewDidChangeSelection:(NSNotification *)notification
        _objc.selector(
            None,
            selector='webViewDidChangeSelection:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)webViewDidChangeTypingStyle:(NSNotification *)notification
        _objc.selector(
            None,
            selector='webViewDidChangeTypingStyle:',
            signature='v@:@',
            isRequired=0,
        ),
# (void)webViewDidEndEditing:(NSNotification *)notification
        _objc.selector(
            None,
            selector='webViewDidEndEditing:',
            signature='v@:@',
            isRequired=0,
        ),
    ]
)

