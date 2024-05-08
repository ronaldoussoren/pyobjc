from PyObjCTools.TestSupport import TestCase

import contextlib
import objc

NSObject = objc.lookUpClass("NSObject")


@contextlib.contextmanager
def patch(function):
    orig_value = objc.options._processClassDict
    try:
        objc.options._processClassDict = function

        yield

    finally:
        objc.options._processClassDict = orig_value


class TestTransformerIntegrationErrors(TestCase):
    def tetst_unset(self):
        with patch(None):
            with self.assertRaisesRegex(
                objc.internal_error, "'objc.options._processClassDict' is not set"
            ):
                name = "OC_TransformIntegrationErrorNS"

                type(name, (NSObject,), {})

    def test_not_tuple(self):
        for idx, value in enumerate(
            (42, (True, (), (), (), (), False), [True, (), (), False])
        ):
            with self.subTest(value):

                def helper(
                    class_name,
                    class_dict,
                    meta_dict,
                    class_object,
                    protocols,
                    hidden_instance_methods,
                    hidden_class_methods,
                ):
                    return value  # noqa: B023

                with patch(helper):
                    with self.assertRaisesRegex(
                        objc.internal_error, "did not return a tuple of 3 items"
                    ):
                        name = f"OC_TransformIntegrationErrorNT{idx}"

                        type(name, (NSObject,), {})

    def test_invalid_ivar(self):
        for idx, value in enumerate(
            (
                42,
                "no",
            )
        ):
            with self.subTest(value):

                def helper(
                    class_name,
                    class_dict,
                    meta_dict,
                    class_object,
                    protocols,
                    hidden_instance_methods,
                    hidden_class_methods,
                ):
                    return (value,), (), (), False  # noqa: B023

                with patch(helper):
                    with self.assertRaisesRegex(
                        objc.internal_error,
                        "invalid instance_variables in result of class dict transformer",
                    ):
                        name = f"OC_TransformIntegrationErrorIV{idx}"
                        type(name, (NSObject,), {})

        idx += 1

        def helper(
            class_name,
            class_dict,
            meta_dict,
            class_object,
            protocols,
            hidden_instance_methods,
            hidden_class_methods,
        ):
            return (objc.ivar(),), (), (), False  # noqa: B023

        with patch(helper):
            with self.assertRaisesRegex(objc.error, "instance variable without a name"):
                name = f"OC_TransformIntegrationErrorIV{idx}"

                type(name, (NSObject,), {})

    def test_invalid_instance_methods(self):
        for idx, value in enumerate(
            (
                42,
                objc.selector(
                    lambda self: 42,
                    selector=b"answer",
                    signature=b"@@:",
                    isClassMethod=True,
                ),
                NSObject.pyobjc_instanceMethods.description,
            )
        ):
            with self.subTest(value):

                def helper(
                    class_name,
                    class_dict,
                    meta_dict,
                    class_object,
                    protocols,
                    hidden_instance_methods,
                    hidden_class_methods,
                ):
                    return (), (value,), (), False  # noqa: B023

                with patch(helper):
                    with self.assertRaisesRegex(
                        objc.internal_error,
                        "invalid instance_methods in result of class dict transformer",
                    ):
                        name = f"OC_TransformIntegrationErrorIM{idx}"

                        type(name, (NSObject,), {"answer": value})

    def test_invalid_class_methods(self):
        for idx, value in enumerate(
            (
                42,
                objc.selector(
                    lambda self: 42,
                    selector=b"answer",
                    signature=b"@@:",
                    isClassMethod=False,
                ),
                NSObject.pyobjc_classMethods.description,
            )
        ):
            with self.subTest(value):

                def helper(
                    class_name,
                    class_dict,
                    meta_dict,
                    class_object,
                    protocols,
                    hidden_instance_methods,
                    hidden_class_methods,
                ):
                    return (), (), (value,), False  # noqa: B023

                with patch(helper):
                    with self.assertRaisesRegex(
                        objc.internal_error,
                        "invalid class_methods in result of class dict transformer",
                    ):
                        name = f"OC_TransformIntegrationErrorCM{idx}"

                        type(name, (NSObject,), {"answer": value})

    def test_not_tuples(self):
        with self.subTest("ivars"):

            def helper(
                class_name,
                class_dict,
                meta_dict,
                class_object,
                protocols,
                hidden_instance_methods,
                hidden_class_methods,
            ):
                return 42, (), (), False  # noqa: B023

            with patch(helper):
                with self.assertRaisesRegex(
                    objc.internal_error,
                    "invalid instance_variables in result of class dict transformer",
                ):
                    name = "OC_TransformIntegrationErrorNT1"

                    type(name, (NSObject,), {})

        with self.subTest("instance methods"):

            def helper(
                class_name,
                class_dict,
                meta_dict,
                class_object,
                protocols,
                hidden_instance_methods,
                hidden_class_methods,
            ):
                return (), 42, (), False  # noqa: B023

            with patch(helper):
                with self.assertRaisesRegex(
                    objc.internal_error,
                    "invalid instance_methods in result of class dict transformer",
                ):
                    name = "OC_TransformIntegrationErrorNT2"

                    type(name, (NSObject,), {})

        with self.subTest("class methods"):

            def helper(
                class_name,
                class_dict,
                meta_dict,
                class_object,
                protocols,
                hidden_instance_methods,
                hidden_class_methods,
            ):
                return (), (), 42, False  # noqa: B023

            with patch(helper):
                with self.assertRaisesRegex(
                    objc.internal_error,
                    "invalid class_methods in result of class dict transformer",
                ):
                    name = "OC_TransformIntegrationErrorNT3"

                    type(name, (NSObject,), {})

    def test_without_processDict(self):
        with patch(None):
            with self.assertRaisesRegex(
                objc.internal_error,
                "Cannot create class because 'objc.options._processClassDict' is not set",
            ):

                class OC_TransformIntegrationErrorNoPD(NSObject):
                    def method(self):
                        pass
