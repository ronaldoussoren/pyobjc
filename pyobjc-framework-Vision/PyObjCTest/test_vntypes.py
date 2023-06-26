from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTypes(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Vision.VNBarcodeSymbology, str)
        self.assertIsTypedEnum(Vision.VNVideoProcessingOption, str)
        self.assertIsTypedEnum(Vision.VNComputeStage, str)
        self.assertIsTypedEnum(Vision.VNRecognizedPointKey, str)
        self.assertIsTypedEnum(Vision.VNRecognizedPointGroupKey, str)
        self.assertIsTypedEnum(Vision.VNAnimalBodyPoseObservationJointName, str)
        self.assertIsTypedEnum(Vision.VNAnimalBodyPoseObservationJointsGroupName, str)
        self.assertIsTypedEnum(Vision.VNHumanBodyPose3DObservationJointName, str)
        self.assertIsTypedEnum(Vision.VNHumanBodyPose3DObservationJointsGroupName, str)

    def test_enum_types(self):
        self.assertIsEnumType(Vision.VNElementType)
        self.assertIsEnumType(Vision.VNImageCropAndScaleOption)
        self.assertIsEnumType(Vision.VNPointsClassification)

    def testConstants(self):
        self.assertEqual(Vision.VNImageCropAndScaleOptionCenterCrop, 0)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFit, 1)
        self.assertEqual(Vision.VNImageCropAndScaleOptionScaleFill, 2)
        self.assertEqual(
            Vision.VNImageCropAndScaleOptionScaleFitRotate90CCW,
            0x100 + Vision.VNImageCropAndScaleOptionScaleFit,
        )
        self.assertEqual(
            Vision.VNImageCropAndScaleOptionScaleFillRotate90CCW,
            0x100 + Vision.VNImageCropAndScaleOptionScaleFill,
        )

        self.assertEqual(Vision.VNElementTypeUnknown, 0)
        self.assertEqual(Vision.VNElementTypeFloat, 1)
        self.assertEqual(Vision.VNElementTypeDouble, 2)

        self.assertEqual(Vision.VNChiralityUnknown, 0)
        self.assertEqual(Vision.VNChiralityLeft, -1)
        self.assertEqual(Vision.VNChiralityRight, 1)

        self.assertEqual(Vision.VNPointsClassificationDisconnected, 0)
        self.assertEqual(Vision.VNPointsClassificationOpenPath, 1)
        self.assertEqual(Vision.VNPointsClassificationClosedPath, 2)

        self.assertIsEnumType(Vision.VNBarcodeCompositeType)
        self.assertEqual(Vision.VNBarcodeCompositeTypeNone, 0)
        self.assertEqual(Vision.VNBarcodeCompositeTypeLinked, 1)
        self.assertEqual(Vision.VNBarcodeCompositeTypeGS1TypeA, 2)
        self.assertEqual(Vision.VNBarcodeCompositeTypeGS1TypeB, 3)
        self.assertEqual(Vision.VNBarcodeCompositeTypeGS1TypeC, 4)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Vision.VNBarcodeSymbologyAztec, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39Checksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39FullASCII, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode39FullASCIIChecksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode93, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode93i, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyCode128, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyDataMatrix, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyEAN8, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyEAN13, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyI2of5, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyI2of5Checksum, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyITF14, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyPDF417, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyQR, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyUPCE, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Vision.VNVideoProcessingOptionFrameCadence, str)
        self.assertIsInstance(Vision.VNVideoProcessingOptionTimeInterval, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(Vision.VNBarcodeSymbologyCodabar, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBar, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBarExpanded, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyGS1DataBarLimited, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyMicroPDF417, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyMicroQR, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(Vision.VNComputeStageMain, str)
        self.assertIsInstance(Vision.VNComputeStagePostProcessing, str)
        self.assertIsInstance(Vision.VNBarcodeSymbologyMSIPlessey, str)

        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftEarTop, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightEarTop, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftEarMiddle, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightEarMiddle, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftEarBottom, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightEarBottom, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftEye, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightEye, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameNose, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameNeck, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftFrontElbow, str)
        self.assertEqual(
            Vision.VNAnimalBodyPoseObservationJointNameRightFrontElbow, str
        )
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftFrontKnee, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightFrontKnee, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftFrontPaw, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightFrontPaw, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftBackElbow, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightBackElbow, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftBackKnee, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightBackKnee, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameLeftBackPaw, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameRightBackPaw, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameTailTop, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameTailMiddle, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointNameTailBottom, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameHead, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameTrunk, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameForelegs, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameHindlegs, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameTail, str)
        self.assertEqual(Vision.VNAnimalBodyPoseObservationJointsGroupNameAll, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRoot, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightHip, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightKnee, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightAnkle, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftHip, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftKnee, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftAnkle, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameSpine, str)
        self.assertEqual(
            Vision.VNHumanBodyPose3DObservationJointNameCenterShoulder, str
        )
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameCenterHead, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameTopHead, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftShoulder, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftElbow, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameLeftWrist, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightShoulder, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightElbow, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointNameRightWrist, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointsGroupNameHead, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointsGroupNameTorso, str)
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointsGroupNameLeftArm, str)
        self.assertEqual(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameRightArm, str
        )
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointsGroupNameLeftLeg, str)
        self.assertEqual(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameRightLeg, str
        )
        self.assertEqual(Vision.VNHumanBodyPose3DObservationJointsGroupNameAll, str)
