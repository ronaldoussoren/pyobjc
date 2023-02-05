import dispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestWorkgroupParallelAPI(TestCase):
    @min_os_level("11.0")
    def test_functions(self):
        self.assertResultHasType(dispatch.os_workgroup_parallel_create, objc._C_ID)
        self.assertResultIsRetained(dispatch.os_workgroup_parallel_create)
        self.assertArgHasType(
            dispatch.os_workgroup_parallel_create, 0, b"n^" + objc._C_CHAR_AS_TEXT
        )
        self.assertArgIsNullTerminated(dispatch.os_workgroup_parallel_create, 0)
        self.assertArgHasType(dispatch.os_workgroup_parallel_create, 1, objc._C_ID)
