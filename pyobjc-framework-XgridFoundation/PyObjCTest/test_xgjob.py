from PyObjCTools.TestSupport import TestCase, min_os_level
import XgridFoundation


class TestXGJob(TestCase):
    def testConstants(self):
        self.assertIsInstance(XgridFoundation.XGJobSpecificationNameKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationTypeKey, str)
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationSubmissionIdentifierKey, str
        )
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationSchedulerParametersKey, str
        )
        self.assertIsInstance(XgridFoundation.XGJobSpecificationGridIdentifierKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationDependsOnJobsKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationInputFilesKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationFileDataKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationIsExecutableKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationTaskPrototypesKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationInputFileMapKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationCommandKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationArgumentsKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationArgumentTypeKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationPathIdentifierKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationEnvironmentKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationInputStreamKey, str)
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationTaskSpecificationsKey, str
        )
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationTaskPrototypeIdentifierKey, str
        )
        self.assertIsInstance(XgridFoundation.XGJobSpecificationDependsOnTasksKey, str)
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationNotificationEmailKey, str
        )
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationApplicationIdentifierKey, str
        )

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(XgridFoundation.XGJobSpecificationSchedulerHintsKey, str)
        self.assertIsInstance(
            XgridFoundation.XGJobSpecificationARTSpecificationsKey, str
        )
        self.assertIsInstance(XgridFoundation.XGJobSpecificationARTConditionsKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationARTDataKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationARTMinimumKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationARTMaximumKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationARTEqualKey, str)
        self.assertIsInstance(XgridFoundation.XGJobSpecificationTypeTaskListValue, str)
