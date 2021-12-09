import objc
from PyObjCTools.TestSupport import TestCase


class TestAPIImportingFailure(TestCase):
    # Test test case only tests error paths, the regular path
    # is tested implicitly by the rest of the test suite.

    def test_cannot_find_api_object(self):
        orig = objc.__C_API__
        try:
            del objc.__C_API__

            with self.assertRaisesRegex(
                AttributeError, "module 'objc' has no attribute '__C_API__'"
            ):
                import PyObjCTest.missing1  # noqa: F401

        finally:
            objc.__C_API__ = orig

    def test_bad_version(self):
        with self.assertRaisesRegex(
            RuntimeError, r"Wrong version of PyObjC C API \(got \d+, expected \d+\)"
        ):
            import PyObjCTest.missing2  # noqa: F401

    def test_too_small(self):
        with self.assertRaisesRegex(
            RuntimeError, r"Wrong struct-size of PyObjC C API \(got \d+, expected \d+\)"
        ):
            import PyObjCTest.missing3  # noqa: F401
