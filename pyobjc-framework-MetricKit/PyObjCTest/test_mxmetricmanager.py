from PyObjCTools.TestSupport import TestCase
import MetricKit
import objc


class TestMXMetricManager(TestCase):
    def test_classes(self):
        MetricKit.MXMetricManager

    def test_protocol(self):
        objc.protocolNamed("MXMetricManagerSubscriber")
