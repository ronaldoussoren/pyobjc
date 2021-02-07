import CoreData
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSMappingModel(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsOut(
            CoreData.NSMappingModel.inferredMappingModelForSourceModel_destinationModel_error_,
            2,
        )
