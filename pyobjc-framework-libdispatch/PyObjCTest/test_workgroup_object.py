import libdispatch
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestWorkgroupObjectAPI(TestCase):
    @min_os_level("11.0")
    def test_functions(self):
        self.assertResultHasType(libdispatch.os_workgroup_copy_port, objc._C_INT)
        self.assertArgHasType(libdispatch.os_workgroup_copy_port, 0, objc._C_ID)
        self.assertArgHasType(
            libdispatch.os_workgroup_copy_port,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_UINT,
        )

        self.assertResultHasType(libdispatch.os_workgroup_create_with_port, objc._C_ID)
        self.assertArgHasType(
            libdispatch.os_workgroup_create_with_port,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(libdispatch.os_workgroup_create_with_port, 0)
        self.assertArgHasType(
            libdispatch.os_workgroup_create_with_port, 1, objc._C_UINT
        )

        self.assertResultHasType(
            libdispatch.os_workgroup_create_with_workgroup, objc._C_ID
        )
        self.assertArgHasType(
            libdispatch.os_workgroup_create_with_workgroup,
            0,
            objc._C_IN + objc._C_PTR + objc._C_CHAR_AS_TEXT,
        )
        self.assertArgIsNullTerminated(
            libdispatch.os_workgroup_create_with_workgroup, 0
        )
        self.assertArgHasType(
            libdispatch.os_workgroup_create_with_workgroup, 1, objc._C_ID
        )

        self.assertResultHasType(libdispatch.os_workgroup_join, objc._C_INT)
        self.assertArgHasType(libdispatch.os_workgroup_join, 0, objc._C_ID)
        self.assertArgHasType(
            libdispatch.os_workgroup_join, 1, b"^{os_workgroup_join_token_opaque_s=}"
        )

        self.assertResultHasType(libdispatch.os_workgroup_leave, objc._C_VOID)
        self.assertArgHasType(libdispatch.os_workgroup_leave, 0, objc._C_ID)
        self.assertArgHasType(
            libdispatch.os_workgroup_leave, 1, b"^{os_workgroup_join_token_opaque_s=}"
        )

        self.assertResultHasType(
            libdispatch.os_workgroup_set_working_arena, objc._C_INT
        )
        self.assertArgHasType(libdispatch.os_workgroup_set_working_arena, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.os_workgroup_set_working_arena, 1, b"n^v")
        self.assertArgIsVariableSize(libdispatch.os_workgroup_set_working_arena, 1)
        self.assertArgHasType(
            libdispatch.os_workgroup_set_working_arena, 2, objc._C_UINT
        )
        self.assertArgIsBlock(libdispatch.os_workgroup_set_working_arena, 3, b"vn^v")

        self.assertResultHasType(libdispatch.os_workgroup_get_working_arena, b"^v")
        self.assertResultIsVariableSize(libdispatch.os_workgroup_get_working_arena)
        self.assertArgHasType(libdispatch.os_workgroup_get_working_arena, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.os_workgroup_get_working_arena, 1, b"o^I")

        self.assertResultHasType(libdispatch.os_workgroup_cancel, objc._C_VOID)
        self.assertArgHasType(libdispatch.os_workgroup_cancel, 0, objc._C_ID)

        self.assertResultHasType(libdispatch.os_workgroup_testcancel, objc._C_BOOL)
        self.assertArgHasType(libdispatch.os_workgroup_testcancel, 0, objc._C_ID)

        self.assertResultHasType(
            libdispatch.os_workgroup_max_parallel_threads, objc._C_INT
        )
        self.assertArgHasType(
            libdispatch.os_workgroup_max_parallel_threads, 0, objc._C_ID
        )
        self.assertArgHasType(
            libdispatch.os_workgroup_max_parallel_threads,
            1,
            b"^{os_workgroup_mpt_attr_s=}",
        )
