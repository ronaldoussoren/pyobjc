import functools
import CoreFoundation  # noqa: F401
import re


def _parse(value):
    return re.findall(
        "(sources0|sources1|timers|observers) = (.*)$", value, re.MULTILINE
    )


def check_cfrunloop_side_effects(func):
    @functools.wraps(func)
    def testfunc(self):
        # before = _parse(str(CoreFoundation.CFRunLoopGetCurrent()))

        try:
            return func(self)
        finally:
            pass
            # after = _parse(str(CoreFoundation.CFRunLoopGetCurrent()))

            # if before != after:
            #    self.assertEqual(before, after, "CFRunLoop changed")

    testfunc.__name__ = func.__name__
    return testfunc
