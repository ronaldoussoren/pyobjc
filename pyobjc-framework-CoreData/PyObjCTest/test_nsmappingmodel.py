import CoreData
from PyObjCTools.TestSupport import TestCase


class TestNSMappingModel(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            CoreData.NSMappingModel.inferredMappingModelForSourceModel_destinationModel_error_,
            2,
        )
