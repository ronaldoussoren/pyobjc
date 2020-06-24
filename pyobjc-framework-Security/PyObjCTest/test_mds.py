import Security
from PyObjCTools.TestSupport import TestCase


class TestMDS(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "MDS_FUNCS"))
        self.assertFalse(hasattr(Security, "MDS_Initialize"))
        self.assertFalse(hasattr(Security, "MDS_Terminate"))
        self.assertFalse(hasattr(Security, "MDS_Install"))
        self.assertFalse(hasattr(Security, "MDS_Uninstall"))
