from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVBInterface(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVBInterface.isAVBCapableInterfaceNamed_
        )
