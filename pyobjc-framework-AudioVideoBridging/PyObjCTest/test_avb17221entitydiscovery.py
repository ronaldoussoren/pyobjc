from PyObjCTools.TestSupport import TestCase, min_os_level
import AudioVideoBridging


class TestAVB17221EntityDiscovery(TestCase):
    @min_os_level("10.8")
    def test_methods10_8(self):
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
