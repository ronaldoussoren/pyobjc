from PyObjCTools.TestSupport import TestCase
import MetricKit


class TestMXSignpost_Private(TestCase):
    # XXX: Alternatively expose custom bindings for the public part of the API
    def test_constants(self):
        self.assertEqual(MetricKit._METRICS_SIGNPOST_TYPE_TOKEN, b"signpost:metrics")
        self.assertEqual(
            MetricKit._MXSIGNPOST_METRICS_SNAPSHOT_FORMAT,
            b"\n%{public, " + MetricKit._METRICS_SIGNPOST_TYPE_TOKEN + b"}@",
        )

    def test_function_macros(self):
        # These function macros use _MXSignpostMetricsSnapshot() which
        # is not available on macOS, hence these should not be exposed:
        self.assertNotHasAttr(MetricKit, "_MXSignpostEventEmit_guaranteed_args")
        self.assertNotHasAttr(MetricKit, "_MXSignpostIntervalBegin_guaranteed_args")
        self.assertNotHasAttr(
            MetricKit, "_MXSignpostAnimationIntervalBegin_guaranteed_args"
        )
        self.assertNotHasAttr(MetricKit, "_MXSignpostIntervalEnd_guaranteed_args")
