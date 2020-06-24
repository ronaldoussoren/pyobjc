import Security
from PyObjCTools.TestSupport import TestCase


class Testcssmspi(TestCase):
    def test_unsuppported(self):
        self.assertFalse(hasattr(Security, "CSSM_CONTEXT_EVENT_CREATE"))
        self.assertFalse(hasattr(Security, "CSSM_CONTEXT_EVENT_DELETE"))
        self.assertFalse(hasattr(Security, "CSSM_CONTEXT_EVENT_UPDATE"))
        self.assertFalse(hasattr(Security, "CSSM_MODULE_FUNCS"))
        self.assertFalse(hasattr(Security, "CSSM_UPCALLS"))
        self.assertFalse(hasattr(Security, "CSSM_SPI_ModuleLoad"))
        self.assertFalse(hasattr(Security, "CSSM_SPI_ModuleUnload"))
        self.assertFalse(hasattr(Security, "CSSM_SPI_ModuleAttach"))
        self.assertFalse(hasattr(Security, "CSSM_SPI_ModuleDetach"))
