"""
A basic command-line tool that uses JavaScriptCore

See also <http://parmanoir.com/Taming_JavascriptCore_within_and_without_WebView>

TODO: This needs to be an example that does something useful
"""
import JavaScriptCore

with JavaScriptCore.autoreleasing(JavaScriptCore.JSGlobalContextCreate(None)) as ctx:

    script = JavaScriptCore.JSStringCreateWithUTF8CString(b"return new Array")
    fn = JavaScriptCore.JSObjectMakeFunction(ctx, None, 0, None, script, None, 1, None)
    result = JavaScriptCore.JSObjectCallAsFunction(ctx, fn, None, 0, None, None)
    JavaScriptCore.JSStringRelease(script)

    # Result is now a reference to a JavaScript array.
