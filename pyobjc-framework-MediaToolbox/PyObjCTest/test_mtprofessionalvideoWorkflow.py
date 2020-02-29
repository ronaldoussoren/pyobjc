import MediaToolbox
from PyObjCTools.TestSupport import *


class TestMTProfessionalVideoWorkflow(TestCase):
    @min_os_level("10.10")
    def test_functions(self):
        MediaToolbox.MTRegisterProfessionalVideoWorkflowFormatReaders


if __name__ == "__main__":
    main()
