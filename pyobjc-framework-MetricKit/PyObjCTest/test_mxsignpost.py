from PyObjCTools.TestSupport import TestCase
import MetricKit


class TestMXSignpost(TestCase):
    def test_functions(self):
        # XXX: Should mock _MXSignpostEventEmit_guaranteed_args
        MetricKit.MXSignpostEventEmit

        # XXX: Should mock _MXSignpostIntervalBegin_guaranteed_args
        MetricKit.MXSignpostIntervalBegin

        # XXX: Should mock _MXSignpostAnimationIntervalBegin_guaranteed_args
        MetricKit.MXSignpostAnimationIntervalBegin

        # XXX: Should mock _MXSignpostIntervalEnd_guaranteed_args
        MetricKit.MXSignpostIntervalEnd
