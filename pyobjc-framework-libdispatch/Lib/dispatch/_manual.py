__all__ = ("dispatch_notify",)
import dispatch


def dispatch_notify(obj, queue, notification_block, /):
    if callable(obj):
        return dispatch.dispatch_block_notify(obj, queue, notification_block)
    else:
        return dispatch.dispatch_queue_notify(obj, queue, notification_block)
