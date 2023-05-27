from PyObjCTools.TestSupport import TestCase, min_os_level

import xpc
import objc

xpc_connection_handler_t = b"v@"
xpc_array_applier_t = b"BQ@"
xpc_dictionary_applier_t = b"Bn^t@"
xpc_handler_t = b"v@"


class TestXPC(TestCase):
    def test_metadata_sane(self):
        to_exclude = set()
        for class_name in (
            "XPC_TYPE_ACTIVITY",
            "XPC_TYPE_UUID",
            "XPC_TYPE_INT64",
            "XPC_TYPE_UINT64",
            "XPC_TYPE_DOUBLE",
            "XPC_TYPE_NULL",
            "XPC_TYPE_DATE",
            "XPC_TYPE_DICTIONARY",
            "XPC_TYPE_ARRAY",
            "XPC_TYPE_STRING",
            "XPC_TYPE_DATA",
            "XPC_TYPE_SHMEM",
            "XPC_TYPE_SESSION",
            "XPC_TYPE_FD",
            "XPC_TYPE_RICH_ERROR",
            "XPC_TYPE_ERROR",
            "XPC_TYPE_ENDPOINT",
            "XPC_TYPE_BOOL",
        ):
            to_exclude = to_exclude.union(
                {
                    (class_name, "utf8ValueSafe"),
                    (class_name, "utf8ValueSafe_"),
                    (class_name, "isKeyExcludedFromWebScript:"),
                    (class_name, "isKeyExcludedFromWebScript:"),
                    (class_name, "newTaggedNSStringWithASCIIBytes__length__"),
                    (class_name, "isKeyExcludedFromWebScript_"),
                }
            )

        self.assertCallableMetadataIsSane(xpc, exclude_attrs=to_exclude)

    def test_constants(self):
        self.assertNotHasAttr(xpc, "XPC_API_VERSION")

        self.assertIsInstance(xpc.XPC_TYPE_ENDPOINT, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_NULL, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_BOOL, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_INT64, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_UINT64, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_DOUBLE, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_DATE, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_DATA, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_STRING, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_UUID, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_FD, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_SHMEM, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_ARRAY, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_DICTIONARY, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_ERROR, objc.objc_class)

        self.assertIsInstance(xpc.XPC_BOOL_TRUE, objc.objc_object)
        self.assertIsInstance(xpc.XPC_BOOL_FALSE, objc.objc_object)

        self.assertIsInstance(xpc.XPC_ERROR_KEY_DESCRIPTION, bytes)
        self.assertIsInstance(xpc.XPC_EVENT_KEY_NAME, bytes)

        self.assertEqual(xpc.XPC_ARRAY_APPEND, 0xFFFFFFFFFFFFFFFF)

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(xpc.XPC_TYPE_SESSION, objc.objc_class)
        self.assertIsInstance(xpc.XPC_TYPE_RICH_ERROR, objc.objc_class)

    def test_functions(self):
        self.assertNotHasAttr(xpc, "xpc_retain")
        self.assertNotHasAttr(xpc, "xpc_release")

        xpc.xpc_get_type

        self.assertResultIsRetained(xpc.xpc_copy)

        xpc.xpc_equal
        xpc.xpc_hash

        self.assertResultIsNullTerminated(xpc.xpc_copy_description)

        self.assertResultIsRetained(xpc.xpc_null_create)
        self.assertResultIsRetained(xpc.xpc_bool_create)

        xpc.xpc_bool_get_value

        self.assertResultIsRetained(xpc.xpc_int64_create)

        xpc.xpc_int64_get_value

        self.assertResultIsRetained(xpc.xpc_uint64_create)

        xpc.xpc_uint64_get_value

        self.assertResultIsRetained(xpc.xpc_double_create)

        xpc.xpc_double_get_value

        self.assertResultIsRetained(xpc.xpc_date_create)
        self.assertResultIsRetained(xpc.xpc_date_create_from_current)

        xpc.xpc_date_get_value

        self.assertResultIsRetained(xpc.xpc_data_create)
        self.assertArgIsIn(xpc.xpc_data_create, 0)
        self.assertArgSizeInArg(xpc.xpc_data_create, 0, 1)

        self.assertResultIsRetained(xpc.xpc_data_create_with_dispatch_data)

        xpc.xpc_data_get_length

        self.assertResultIsVariableSize(xpc.xpc_data_get_bytes_ptr)

        self.assertArgIsOut(xpc.xpc_data_get_bytes, 1)
        self.assertArgSizeInArg(xpc.xpc_data_get_bytes, 1, 3)

        self.assertResultIsRetained(xpc.xpc_string_create)
        self.assertArgIsIn(xpc.xpc_string_create, 0)
        self.assertArgIsNullTerminated(xpc.xpc_string_create, 0)

        self.assertResultIsRetained(xpc.xpc_string_create_with_format)
        self.assertArgIsIn(xpc.xpc_string_create_with_format, 0)
        self.assertArgIsNullTerminated(xpc.xpc_string_create_with_format, 0)
        self.assertArgIsPrintf(xpc.xpc_string_create_with_format, 0)

        self.assertNotHasAttr(xpc, "xpc_string_create_with_format_and_arguments")

        xpc.xpc_string_get_length

        self.assertResultIsNullTerminated(xpc.xpc_string_get_string_ptr)

        self.assertResultIsRetained(xpc.xpc_uuid_create)
        self.assertArgIsIn(xpc.xpc_uuid_create, 0)
        self.assertArgIsFixedSize(xpc.xpc_uuid_create, 0, 16)

        self.assertResultHasType(xpc.xpc_uuid_get_bytes, b"^v")
        self.assertResultIsFixedSize(xpc.xpc_uuid_get_bytes, 16)

        self.assertResultIsRetained(xpc.xpc_fd_create)

        xpc.xpc_fd_dup

        self.assertResultIsRetained(xpc.xpc_shmem_create)

        self.assertArgIsOut(xpc.xpc_shmem_map, 1)

        self.assertResultIsRetained(xpc.xpc_array_create)
        self.assertArgIsIn(xpc.xpc_array_create, 0)
        self.assertArgSizeInArg(xpc.xpc_array_create, 0, 1)

        xpc.xpc_array_set_value
        xpc.xpc_array_append_value
        xpc.xpc_array_get_count
        xpc.xpc_array_get_value

        self.assertArgIsBlock(xpc.xpc_array_apply, 1, xpc_array_applier_t)

        self.assertArgIsIn(xpc.xpc_array_create, 0)
        self.assertArgSizeInArg(xpc.xpc_array_create, 0, 1)

        xpc.xpc_array_set_bool
        xpc.xpc_array_set_int64
        xpc.xpc_array_set_uint64
        xpc.xpc_array_set_double
        xpc.xpc_array_set_date

        self.assertArgIsIn(xpc.xpc_array_set_data, 2)
        self.assertArgSizeInArg(xpc.xpc_array_set_data, 2, 3)

        self.assertArgIsIn(xpc.xpc_array_set_string, 2)
        self.assertArgIsNullTerminated(xpc.xpc_array_set_string, 2)

        self.assertArgIsIn(xpc.xpc_array_set_uuid, 2)
        self.assertArgIsFixedSize(xpc.xpc_array_set_uuid, 2, 16)

        xpc.xpc_array_set_fd
        xpc.xpc_array_set_connection
        xpc.xpc_array_get_bool
        xpc.xpc_array_get_int64
        xpc.xpc_array_get_uint64
        xpc.xpc_array_get_double
        xpc.xpc_array_get_date

        self.assertResultSizeInArg(xpc.xpc_array_get_data, 2)
        self.assertArgIsOut(xpc.xpc_array_get_data, 2)

        self.assertResultIsNullTerminated(xpc.xpc_array_get_string)

        self.assertResultIsFixedSize(xpc.xpc_array_get_uuid, 16)
        self.assertResultHasType(xpc.xpc_array_get_uuid, b"^v")

        xpc.xpc_array_dup_fd

        self.assertResultIsRetained(xpc.xpc_array_create_connection)

        # Manual binding:
        # self.assertResultIsRetained(xpc.xpc_dictionary_create)
        # self.assertArgIsIn(xpc.xpc_dictionary_create, 0)
        # self.assertArgSizeInArg(xpc.xpc_dictionary_create, 0, 2)
        # self.assertArgIsIn(xpc.xpc_dictionary_create, 1)
        # self.assertArgSizeInArg(xpc.xpc_dictionary_create, 1, 2)

        value = xpc.xpc_dictionary_create(
            [b"key1", b"key2"], [xpc.XPC_BOOL_TRUE, xpc.XPC_BOOL_FALSE], 2
        )
        self.assertIs(xpc.xpc_dictionary_get_value(value, b"key1"), xpc.XPC_BOOL_TRUE)
        self.assertIs(xpc.xpc_dictionary_get_value(value, b"key2"), xpc.XPC_BOOL_FALSE)

        items = set()

        def applier(key, value):
            items.add((key, value))
            return True

        xpc.xpc_dictionary_apply(value, applier)
        self.assertEqual(
            items, {(b"key1", xpc.XPC_BOOL_TRUE), (b"key2", xpc.XPC_BOOL_FALSE)}
        )

        self.assertResultIsRetained(xpc.xpc_dictionary_create_reply)

        self.assertArgIsIn(xpc.xpc_dictionary_set_value, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_value, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_value, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_value, 1)

        xpc.xpc_dictionary_get_count

        self.assertArgIsBlock(xpc.xpc_dictionary_apply, 1, xpc_dictionary_applier_t)

        xpc.xpc_dictionary_get_remote_connection

        self.assertArgIsIn(xpc.xpc_dictionary_set_bool, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_bool, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_int64, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_int64, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_uint64, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_uint64, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_double, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_double, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_date, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_date, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_data, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_data, 1)
        self.assertArgIsIn(xpc.xpc_dictionary_set_data, 2)
        self.assertArgSizeInArg(xpc.xpc_dictionary_set_data, 2, 3)

        self.assertArgIsIn(xpc.xpc_dictionary_set_string, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_string, 1)
        self.assertArgIsIn(xpc.xpc_dictionary_set_string, 2)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_string, 2)

        self.assertArgIsIn(xpc.xpc_dictionary_set_uuid, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_uuid, 1)
        self.assertArgIsIn(xpc.xpc_dictionary_set_uuid, 2)
        self.assertArgIsFixedSize(xpc.xpc_dictionary_set_uuid, 2, 16)

        self.assertArgIsIn(xpc.xpc_dictionary_set_fd, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_fd, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_set_connection, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_set_connection, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_bool, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_bool, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_int64, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_int64, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_uint64, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_uint64, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_double, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_double, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_date, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_date, 1)

        self.assertResultSizeInArg(xpc.xpc_dictionary_get_data, 2)
        self.assertArgIsIn(xpc.xpc_dictionary_get_data, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_data, 1)
        self.assertArgIsOut(xpc.xpc_dictionary_get_data, 2)

        self.assertResultIsNullTerminated(xpc.xpc_dictionary_get_string)
        self.assertArgIsIn(xpc.xpc_dictionary_get_string, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_string, 1)

        self.assertResultIsFixedSize(xpc.xpc_dictionary_get_uuid, 16)
        self.assertResultHasType(xpc.xpc_dictionary_get_uuid, b"^v")
        self.assertArgIsIn(xpc.xpc_dictionary_get_uuid, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_uuid, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_dup_fd, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_dup_fd, 1)

        self.assertResultIsRetained(xpc.xpc_dictionary_create_connection)
        self.assertArgIsIn(xpc.xpc_dictionary_create_connection, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_create_connection, 1)

        xpc.xpc_main
        xpc.xpc_transaction_begin
        xpc.xpc_transaction_end

        self.assertArgIsIn(xpc.xpc_set_event_stream_handler, 0)
        self.assertArgIsNullTerminated(xpc.xpc_set_event_stream_handler, 0)
        self.assertArgIsBlock(xpc.xpc_set_event_stream_handler, 2, xpc_handler_t)

    @min_os_level("10.11")
    def test_functions10_11(self):
        xpc.xpc_array_get_dictionary
        xpc.xpc_array_get_array

        self.assertArgIsIn(xpc.xpc_dictionary_get_dictionary, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_dictionary, 1)

        self.assertArgIsIn(xpc.xpc_dictionary_get_array, 1)
        self.assertArgIsNullTerminated(xpc.xpc_dictionary_get_array, 1)

    @min_os_level("10.15")
    def test_functions10_15(self):
        self.assertResultIsNullTerminated(xpc.xpc_type_get_name)

    @min_os_level("11.0")
    def test_functions11_0(self):
        self.assertResultIsRetained(xpc.xpc_array_create_empty)
        self.assertResultIsRetained(xpc.xpc_dictionary_create_empty)
