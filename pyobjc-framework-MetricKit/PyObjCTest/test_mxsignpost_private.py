from PyObjCTools.TestSupport import TestCase
import MetricKit


class TestMXSignpost_Private(TestCase):
    # XXX: Alternatively expose custom bindings for the public part of the API
    def test_constants(self):
        self.assertEqual(MetricKit._METRICS_SIGNPOST_TYPE_TOKEN, b"signpost:metrics")
        self.assertEqual(
            MetricKit._MXSIGNPOST_METRICS_SNAPSHOT_FORMAT,
            "\n%{public, " + MetricKit._METRICS_SIGNPOST_TYPE_TOKEN + "}@",
        )

    def test_functions(self):
        # Mock os_signpost...
        MetricKit._MXSignpostEventEmit_guaranteed_args
        MetricKit._MXSignpostIntervalBegin_guaranteed_args
        MetricKit._MXSignpostAnimationIntervalBegin_guaranteed_args
        MetricKit._MXSignpostIntervalEnd_guaranteed_args
