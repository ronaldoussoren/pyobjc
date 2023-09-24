from PyObjCTools.TestSupport import TestCase, min_os_level
import MetricKit


class TestMXSignpostRecord(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(MetricKit.MXSignpostRecord.isInterval)
