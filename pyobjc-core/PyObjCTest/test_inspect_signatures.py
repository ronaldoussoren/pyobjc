import inspect
import types

import objc
from PyObjCTools.TestSupport import TestCase, min_python_release


class TestInspectSignatures(TestCase):
    @min_python_release("3.4")
    def test_module_functions_signature(self):
        for nm in dir(objc):
            with self.subTest(name=nm):
                obj = getattr(objc, nm)
                if isinstance(obj, types.BuiltinMethodType):
                    try:
                        value = inspect.signature(obj)

                    except ValueError:
                        value = None

                    if value is None:
                        self.fail(f"No inspect.signature for {nm}")

    @min_python_release("3.4")
    def test_class_signature(self):
        class_list = [
            objc.ObjCPointer,
            objc.objc_meta_class,
            objc.objc_class,
            objc.objc_object,
            objc.pyobjc_unicode,
            objc.selector,
            objc.FSRef,
            objc.ivar,
            objc.informal_protocol,
            objc.formal_protocol,
            objc.varlist,
            objc.function,
            objc.IMP,
            objc.super,
        ]
        if hasattr(objc, "WeakRef"):
            class_list.append(objc.WeakRef)
        for cls in class_list:
            for nm in dir(cls):
                if nm in (
                    "__new__",
                    "__subclasshook__",
                    "__abstractmethods__",
                    "__prepare__",
                    "__init_subclass__",
                    "__annotations__",
                    "__annotate__",
                ):
                    continue
                with self.subTest(classname=cls.__name__, attr=nm):
                    obj = getattr(cls, nm)
                    if isinstance(obj, types.BuiltinMethodType):
                        try:
                            value = inspect.signature(obj)
                        except ValueError:
                            value = None

                        if value is None and cls is objc.pyobjc_unicode:
                            if obj == getattr(str, nm):
                                # Don't fail for inherited methods
                                continue

                        if value is None:
                            self.fail(f"No inspect.signature for {cls.__name__}.{nm}")
