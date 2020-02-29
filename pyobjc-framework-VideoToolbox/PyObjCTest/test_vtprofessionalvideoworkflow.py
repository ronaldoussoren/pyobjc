import VideoToolbox
from PyObjCTools.TestSupport import *


class TestVTProfessionalVideoWorkflow(TestCase):
    @min_os_level("10.10")
    def test_functions(self):
        VideoToolbox.VTRegisterProfessionalVideoWorkflowVideoDecoders
        VideoToolbox.VTRegisterProfessionalVideoWorkflowVideoEncoders


if __name__ == "__main__":
    main()
