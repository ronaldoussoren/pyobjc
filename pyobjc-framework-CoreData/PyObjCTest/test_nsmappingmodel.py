from PyObjCTools.TestSupport import *
from CoreData import *

class TestNSMappingModel (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsOut(NSMappingModel.inferredMappingModelForSourceModel_destinationModel_error_, 2)

if __name__ == "__main__":
    main()
