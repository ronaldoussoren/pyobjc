import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestUTCUtils(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), "%r exposed in bindings" % (name,)
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("kUTCDefaultOptions")
        self.assert_not_wrapped("UTCDateTime")
        self.assert_not_wrapped("LocalDateTime")
        self.assert_not_wrapped("ConvertLocalTimeToUTC")
        self.assert_not_wrapped("ConvertUTCToLocalTime")
        self.assert_not_wrapped("ConvertUTCToLocalDateTime")
        self.assert_not_wrapped("ConvertLocalToUTCDateTime")
        self.assert_not_wrapped("GetUTCDateTime")
        self.assert_not_wrapped("SetUTCDateTime")
        self.assert_not_wrapped("GetLocalDateTime")
        self.assert_not_wrapped("SetLocalDateTime")
        self.assert_not_wrapped("")
