import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTProfessionalVideoWorkflow(TestCase):
    @min_os_level("10.10")
    def test_functions(self):
        VideoToolbox.VTRegisterProfessionalVideoWorkflowVideoDecoders
        VideoToolbox.VTRegisterProfessionalVideoWorkflowVideoEncoders
