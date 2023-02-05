from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc
import objc

xpc_activity_handler_t = b"v@"


class TestActivity(TestCase):
    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_REPEATING, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_DELAY, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_GRACE_PERIOD, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_PRIORITY, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_PRIORITY_MAINTENANCE, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_PRIORITY_UTILITY, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_ALLOW_BATTERY, bytes)
        self.assertIsInstance(xpc.XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP, bytes)
        self.assertNotHasAttr(xpc, "XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL")
        self.assertNotHasAttr(xpc, "XPC_ACTIVITY_REQUIRE_HDD_SPINNING")

        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_1_MIN, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_5_MIN, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_15_MIN, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_30_MIN, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_1_HOUR, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_4_HOURS, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_8_HOURS, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_1_DAY, int)
        self.assertIsInstance(xpc.XPC_ACTIVITY_INTERVAL_7_DAYS, int)

        self.assertIsInstance(xpc.XPC_ACTIVITY_CHECK_IN, objc.objc_object)

        self.assertIsEnumType(xpc.xpc_activity_state_t)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_CHECK_IN, 0)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_WAIT, 1)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_RUN, 2)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_DEFER, 3)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_CONTINUE, 4)
        self.assertEqual(xpc.XPC_ACTIVITY_STATE_DONE, 5)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(xpc.XPC_ACTIVITY_PREVENT_DEVICE_SLEEP, bytes)

    def test_functions(self):
        self.assertArgIsIn(xpc.xpc_activity_register, 0)
        self.assertArgIsNullTerminated(xpc.xpc_activity_register, 0)
        self.assertArgIsBlock(xpc.xpc_activity_register, 2, xpc_activity_handler_t)

        self.assertResultIsRetained(xpc.xpc_activity_copy_criteria)

        xpc.xpc_activity_set_criteria
        xpc.xpc_activity_set_state
        xpc.xpc_activity_should_defer

        self.assertArgIsIn(xpc.xpc_activity_unregister, 0)
        self.assertArgIsNullTerminated(xpc.xpc_activity_unregister, 0)
