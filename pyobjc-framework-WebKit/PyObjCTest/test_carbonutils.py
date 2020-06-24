import Cocoa  # noqa: F401
from PyObjCTools.TestSupport import TestCase

try:
    import Quartz  # noqa: F401
except ImportError:
    Quartz = None  # noqa: F401


class TestCarbonUtils(TestCase):
    pass
