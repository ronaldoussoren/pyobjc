from PyObjCTools.TestSupport import TestCase
import AudioVideoBridging


class TestAVB17221EntityDiscovery(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221EntityDiscovery.discoverEntities
        )
        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221EntityDiscovery.discoverEntity_
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221EntityDiscovery.addLocalEntity_error_
        )
        self.assertArgIsOut(
            AudioVideoBridging.AVB17221EntityDiscovery.addLocalEntity_error_, 1
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221EntityDiscovery.removeLocalEntity_error_
        )
        self.assertArgIsOut(
            AudioVideoBridging.AVB17221EntityDiscovery.removeLocalEntity_error_, 1
        )

        self.assertResultIsBOOL(
            AudioVideoBridging.AVB17221EntityDiscovery.changeEntityWithEntityID_toNewGPTPGrandmasterID_error_
        )
        self.assertArgIsOut(
            AudioVideoBridging.AVB17221EntityDiscovery.changeEntityWithEntityID_toNewGPTPGrandmasterID_error_,
            2,
        )
