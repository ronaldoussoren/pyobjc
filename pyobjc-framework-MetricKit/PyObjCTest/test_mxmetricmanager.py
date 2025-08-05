from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import MetricKit


class TestMXMetricManager(TestCase):
    def test_classes(self):
        MetricKit.MXMetricManager

    def test_enum(self):
        self.assertIsTypedEnum(MetricKit.MXLaunchTaskID, str)

    @min_sdk_level("12.0")
    def test_protocol(self):
        self.assertProtocolExists("MXMetricManagerSubscriber")

    @min_os_level("12.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetricKit.MXMetricManager.extendLaunchMeasurementForTaskID_error_
        )
        self.assertArgIsOut(
            MetricKit.MXMetricManager.extendLaunchMeasurementForTaskID_error_, 1
        )

        self.assertResultIsBOOL(
            MetricKit.MXMetricManager.finishExtendedLaunchMeasurementForTaskID_error_
        )
        self.assertArgIsOut(
            MetricKit.MXMetricManager.finishExtendedLaunchMeasurementForTaskID_error_, 1
        )
