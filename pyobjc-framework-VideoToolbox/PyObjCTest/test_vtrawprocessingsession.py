from PyObjCTools.TestSupport import TestCase, min_os_level

import VideoToolbox

VTRAWProcessingParameterChangeHandler = b"v@"
VTRAWProcessingOutputHandler = b"vi@"


class TestVTRAWProcessingSession(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_Key, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_Name, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_Description, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_Enabled, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_ValueType, str)
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterValueType_Boolean, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterValueType_Integer, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterValueType_Float, str
        )
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameterValueType_List, str)
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterValueType_SubGroup, str
        )
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_ListArray, str)
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterListElement_Label, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterListElement_Description, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTRAWProcessingParameterListElement_ListElementID, str
        )
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_SubGroup, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_MaximumValue, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_MinimumValue, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_InitialValue, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_NeutralValue, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_CameraValue, str)
        self.assertIsInstance(VideoToolbox.kVTRAWProcessingParameter_CurrentValue, str)

    @min_os_level("15.0")
    def test_types(self):
        self.assertIsCFType(VideoToolbox.VTRAWProcessingSessionRef)

    @min_os_level("15.0")
    def test_functions(self):
        self.assertArgIsOut(VideoToolbox.VTRAWProcessingSessionCreate, 4)
        self.assertArgIsAlreadyCFRetained(VideoToolbox.VTRAWProcessingSessionCreate, 4)

        VideoToolbox.VTRAWProcessingSessionInvalidate
        VideoToolbox.VTRAWProcessingSessionGetTypeID

        self.assertArgIsBlock(
            VideoToolbox.VTRAWProcessingSessionSetParameterChangedHander,
            1,
            VTRAWProcessingParameterChangeHandler,
        )

        self.assertArgIsBlock(
            VideoToolbox.VTRAWProcessingSessionProcessFrame,
            3,
            VTRAWProcessingOutputHandler,
        )

        VideoToolbox.VTRAWProcessingSessionCompleteFrames

        self.assertArgIsOut(
            VideoToolbox.VTRAWProcessingSessionCopyProcessingParameters, 1
        )
        self.assertArgIsAlreadyCFRetained(
            VideoToolbox.VTRAWProcessingSessionCopyProcessingParameters, 1
        )

        VideoToolbox.VTRAWProcessingSessionSetProcessingParameters
