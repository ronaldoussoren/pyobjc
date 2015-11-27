
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGJob (TestCase):
    def testConstants(self):
        self.assertIsInstance(XGJobSpecificationNameKey,  unicode)
        self.assertIsInstance(XGJobSpecificationTypeKey,  unicode)
        self.assertIsInstance(XGJobSpecificationSubmissionIdentifierKey,  unicode)
        self.assertIsInstance(XGJobSpecificationSchedulerParametersKey,  unicode)
        self.assertIsInstance(XGJobSpecificationGridIdentifierKey,  unicode)
        self.assertIsInstance(XGJobSpecificationDependsOnJobsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationInputFilesKey,  unicode)
        self.assertIsInstance(XGJobSpecificationFileDataKey,  unicode)
        self.assertIsInstance(XGJobSpecificationIsExecutableKey,  unicode)
        self.assertIsInstance(XGJobSpecificationTaskPrototypesKey,  unicode)
        self.assertIsInstance(XGJobSpecificationInputFileMapKey,  unicode)
        self.assertIsInstance(XGJobSpecificationCommandKey,  unicode)
        self.assertIsInstance(XGJobSpecificationArgumentsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationArgumentTypeKey,  unicode)
        self.assertIsInstance(XGJobSpecificationPathIdentifierKey,  unicode)
        self.assertIsInstance(XGJobSpecificationEnvironmentKey,  unicode)
        self.assertIsInstance(XGJobSpecificationInputStreamKey,  unicode)
        self.assertIsInstance(XGJobSpecificationTaskSpecificationsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationTaskPrototypeIdentifierKey,  unicode)
        self.assertIsInstance(XGJobSpecificationDependsOnTasksKey,  unicode)
        self.assertIsInstance(XGJobSpecificationNotificationEmailKey,  unicode)
        self.assertIsInstance(XGJobSpecificationApplicationIdentifierKey,  unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(XGJobSpecificationSchedulerHintsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTSpecificationsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTConditionsKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTDataKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTMinimumKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTMaximumKey,  unicode)
        self.assertIsInstance(XGJobSpecificationARTEqualKey,  unicode)
        self.assertIsInstance(XGJobSpecificationTypeTaskListValue,  unicode)


if __name__ == "__main__":
    main()
