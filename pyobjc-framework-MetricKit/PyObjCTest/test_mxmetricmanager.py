from PyObjCTools.TestSupport import TestCase, min_sdk_level
import MetricKit
import objc


class TestMXMetricManager(TestCase):
    def test_classes(self):
        MetricKit.MXMetricManager

    @min_sdk_level("12.0")
    def test_protocol(self):
        objc.protocolNamed("MXMetricManagerSubscriber")
