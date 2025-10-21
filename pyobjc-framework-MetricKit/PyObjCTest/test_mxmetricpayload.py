from PyObjCTools.TestSupport import TestCase
import MetricKit


class TestMXMetricPayload(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            MetricKit.MXMetricPayload.includesMultipleApplicationVersions
        )
