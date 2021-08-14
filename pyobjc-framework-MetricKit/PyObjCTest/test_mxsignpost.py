from PyObjCTools.TestSupport import TestCase
import MetricKit


class TestMXSignpost(TestCase):
    def test_functions_macros(self):
        # Functin macros using _MXSignpostEventEmit_guaranteed_args, which
        # is not available on macOS.

        self.assertNotHasAttr(MetricKit, "MXSignpostEventEmit")
        self.assertNotHasAttr(MetricKit, "MXSignpostIntervalBegin")
        self.assertNotHasAttr(MetricKit, "MXSignpostAnimationIntervalBegin")
        self.assertNotHasAttr(MetricKit, "MXSignpostIntervalEnd")
