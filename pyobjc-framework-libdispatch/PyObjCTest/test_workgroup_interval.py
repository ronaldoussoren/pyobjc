import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestWorkgroupIntervalAPI(TestCase):
    @min_os_level("11.0")
    def test_functions(self):
        self.assertResultHasType(dispatch.os_workgroup_interval_start, objc._C_INT)
        self.assertArgHasType(dispatch.os_workgroup_interval_start, 0, objc._C_ID)
        self.assertArgHasType(dispatch.os_workgroup_interval_start, 1, objc._C_ULNG_LNG)
        self.assertArgHasType(dispatch.os_workgroup_interval_start, 2, objc._C_ULNG_LNG)
        self.assertArgHasType(dispatch.os_workgroup_interval_start, 3, objc._C_ID)

        self.assertResultHasType(dispatch.os_workgroup_interval_update, objc._C_INT)
        self.assertArgHasType(dispatch.os_workgroup_interval_update, 0, objc._C_ID)
        self.assertArgHasType(
            dispatch.os_workgroup_interval_update, 1, objc._C_ULNG_LNG
        )
        self.assertArgHasType(dispatch.os_workgroup_interval_update, 2, objc._C_ID)

        self.assertResultHasType(dispatch.os_workgroup_interval_finish, objc._C_INT)
        self.assertArgHasType(dispatch.os_workgroup_interval_finish, 0, objc._C_ID)
        self.assertArgHasType(dispatch.os_workgroup_interval_finish, 1, objc._C_ID)
