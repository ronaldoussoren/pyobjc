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

        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftEarTop, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightEarTop, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftEarMiddle, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightEarMiddle, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftEarBottom, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightEarBottom, str
        )
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointNameLeftEye, str)
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointNameRightEye, str)
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointNameNose, str)
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointNameNeck, str)
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftFrontElbow, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightFrontElbow, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftFrontKnee, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightFrontKnee, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftFrontPaw, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightFrontPaw, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftBackElbow, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightBackElbow, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftBackKnee, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightBackKnee, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameLeftBackPaw, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameRightBackPaw, str
        )
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointNameTailTop, str)
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameTailMiddle, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointNameTailBottom, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointsGroupNameHead, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointsGroupNameTrunk, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointsGroupNameForelegs, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointsGroupNameHindlegs, str
        )
        self.assertIsInstance(
            Vision.VNAnimalBodyPoseObservationJointsGroupNameTail, str
        )
        self.assertIsInstance(Vision.VNAnimalBodyPoseObservationJointsGroupNameAll, str)
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameRoot, str)
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameRightHip, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameRightKnee, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameRightAnkle, str
        )
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameLeftHip, str)
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameLeftKnee, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameLeftAnkle, str
        )
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameSpine, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameCenterShoulder, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameCenterHead, str
        )
        self.assertIsInstance(Vision.VNHumanBodyPose3DObservationJointNameTopHead, str)
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameLeftShoulder, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameLeftElbow, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameLeftWrist, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameRightShoulder, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameRightElbow, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointNameRightWrist, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameHead, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameTorso, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameLeftArm, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameRightArm, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameLeftLeg, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameRightLeg, str
        )
        self.assertIsInstance(
            Vision.VNHumanBodyPose3DObservationJointsGroupNameAll, str
        )
