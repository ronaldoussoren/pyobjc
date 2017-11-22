from PyObjCTools.TestSupport import *

import libdispatch

dispatch_data_applier_t = b'B@Ln^vL'

class TestDataAPI (TestCase):

    @min_os_level('10.7')
    def test_constants(self):
        self.assertIsInstance(libdispatch.dispatch_data_empty, objc.objc_object)
        self.assertIsInstance(libdispatch.DISPATCH_DATA_DESTRUCTOR_FREE, objc.objc_object)

        self.assertIs(libdispatch.DISPATCH_DATA_DESTRUCTOR_DEFAULT, None)

    @min_os_level('10.7')
    def test_functions(self):
        self.assertResultHasType(libdispatch.dispatch_data_create, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create, 0, objc._C_IN + objc._C_PTR + objc._C_VOID)
        self.assertArgSizeInArg(libdispatch.dispatch_data_create, 0, 1)
        self.assertArgHasType(libdispatch.dispatch_data_create, 1, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_data_create, 2, objc._C_ID) # dispatch_queue_t
        self.assertArgIsBlock(libdispatch.dispatch_data_create, 3, b'v')

        self.assertResultHasType(libdispatch.dispatch_data_get_size, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_data_get_size, 0, objc._C_ID)

        # FIXME: dispatch_data_create_map

        self.assertResultHasType(libdispatch.dispatch_data_create_concat, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_concat, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_concat, 1, objc._C_ID)

        self.assertResultHasType(libdispatch.dispatch_data_create_subrange, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_subrange, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_create_subrange, 1, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_data_create_subrange, 2, objc._C_ULNG)

        self.assertResultHasType(libdispatch.dispatch_data_apply, objc._C_BOOL)
        self.assertArgHasType(libdispatch.dispatch_data_apply, 0, objc._C_ID)
        self.assertArgIsBlock(libdispatch.dispatch_data_apply, 1, dispatch_data_applier_t)

        self.assertResultHasType(libdispatch.dispatch_data_copy_region, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_copy_region, 0, objc._C_ID)
        self.assertArgHasType(libdispatch.dispatch_data_copy_region, 1, objc._C_ULNG)
        self.assertArgHasType(libdispatch.dispatch_data_copy_region, 2, objc._C_OUT + objc._C_PTR + objc._C_ULNG)

if __name__ == "__main__":
    main()
