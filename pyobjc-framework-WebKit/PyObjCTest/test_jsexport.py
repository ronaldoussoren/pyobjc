import JavaScriptCore
from PyObjCTools.TestSupport import TestCase, min_sdk_level, expectedFailure

# import WebKit
import objc


class TestJSExport(TestCase):
    @min_sdk_level("10.9")
    def test_protocols(self):
        self.assertProtocolExists("JSExport")

    @expectedFailure
    def test_jsexportas(self):
        self.fail("Test crashes hard on macOS 10.9")

        export_proto = objc.formal_protocol(
            "ExportProto",
            (objc.protocolNamed("JSExport"),),
            [
                JavaScriptCore.JSExportAs(
                    "doFoo",
                    objc.selector(None, selector=b"doFoo:withBar:", signature=b"v@:@@"),
                ),
                objc.selector(None, selector=b"method1:", signature=b"v@:@"),
            ],
        )

        # XXX: The test fails with the protocol defined in
        #      Python, but passes with the same protocol defined
        #      in Objective-C.
        # export_proto = objc.protocolNamed("TestHelper")

        # Validate protocol shape:
        for item in export_proto.instanceMethods():
            if item["selector"] == b"doFoo:withBar:__JS_EXPORT_AS__doFoo:":
                break
        else:
            self.fail("Export alias not found")

        class Helper(JavaScriptCore.NSObject, protocols=[export_proto]):
            def doFoo_withBar_(self, first, second):
                return f"{first}<->{second}"

            def method1_(self, a):
                return a * 2

        context = JavaScriptCore.JSContext.alloc().init()
        helper = Helper.alloc().init()

        context.setObject_forKeyedSubscript_(helper, "helper")
        context.setObject_forKeyedSubscript_("x", "value")

        value = context.evaluateScript_("helper.doFoo(value, value)")
        self.assertEqual(value.toString(), "x<->x")
