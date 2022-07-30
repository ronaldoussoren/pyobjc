import MediaToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTProfessionalVideoWorkflow(TestCase):
    @min_os_level("10.10")
    def test_functions(self):
        MediaToolbox.MTRegisterProfessionalVideoWorkflowFormatReaders
