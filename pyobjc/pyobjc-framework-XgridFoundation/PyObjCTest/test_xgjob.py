
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGJob (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(XGJobSpecificationNameKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationTypeKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationSubmissionIdentifierKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationSchedulerParametersKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationGridIdentifierKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationDependsOnJobsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationInputFilesKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationFileDataKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationIsExecutableKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationTaskPrototypesKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationInputFileMapKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationCommandKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationArgumentsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationArgumentTypeKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationPathIdentifierKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationEnvironmentKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationInputStreamKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationTaskSpecificationsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationTaskPrototypeIdentifierKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationDependsOnTasksKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationNotificationEmailKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationApplicationIdentifierKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationSchedulerHintsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTSpecificationsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTConditionsKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTDataKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTMinimumKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTMaximumKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationARTEqualKey,  unicode)
        self.failUnlessIsInstance(XGJobSpecificationTypeTaskListValue,  unicode)


if __name__ == "__main__":
    main()
