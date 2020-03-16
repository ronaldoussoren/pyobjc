import libdispatch
from PyObjCTools.TestSupport import TestCase


class TestIntrospectionAPI(TestCase):
    def test_function(self):
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_create")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_destroy")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_item_enqueue")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_item_dequeue")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_item_complete")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_callout_begin")
        )
        self.assertFalse(
            hasattr(libdispatch, "dispatch_introspection_hook_queue_callout_end")
        )
