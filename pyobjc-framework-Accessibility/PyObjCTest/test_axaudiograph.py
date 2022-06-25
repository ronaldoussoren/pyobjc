from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level

import Accessibility


class TestAXAudiograph(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Accessibility.AXChartDescriptorContentDirection)
        self.assertIsEnumType(Accessibility.AXNumericDataAxisDescriptorScale)

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("AXChart")
        self.assertProtocolExists("AXDataAxisDescriptor")

    def test_constants(self):
        self.assertEqual(Accessibility.AXScaleTypeLinear, 0)
        self.assertEqual(Accessibility.AXScaleTypeLog10, 1)
        self.assertEqual(Accessibility.AXScaleTypeLn, 2)

        self.assertEqual(Accessibility.AXChartContentDirectionLeftToRight, 0)
        self.assertEqual(Accessibility.AXChartContentDirectionRightToLeft, 1)
        self.assertEqual(Accessibility.AXChartContentDirectionTopToBottom, 2)
        self.assertEqual(Accessibility.AXChartContentDirectionBottomToTop, 3)
        self.assertEqual(Accessibility.AXChartContentDirectionRadialClockwise, 4)
        self.assertEqual(Accessibility.AXChartContentDirectionRadialCounterClockwise, 5)

    @min_os_level("12.0")
    def test_classes(self):
        self.assertClassIsFinal(Accessibility.AXNumericDataAxisDescriptor)
        self.assertClassIsFinal(Accessibility.AXDataPointValue)
        self.assertClassIsFinal(Accessibility.AXDataPoint)
        self.assertClassIsFinal(Accessibility.AXChartDescriptor)

    @min_os_level("12.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Accessibility.AXNumericDataAxisDescriptor.initWithTitle_lowerBound_upperBound_gridlinePositions_valueDescriptionProvider_,  # noqa: B950
            4,
            b"@d",
        )
        self.assertArgIsBlock(
            Accessibility.AXNumericDataAxisDescriptor.initWithAttributedTitle_lowerBound_upperBound_gridlinePositions_valueDescriptionProvider_,  # noqa: B950
            4,
            b"@d",
        )

        self.assertResultIsBOOL(Accessibility.AXDataSeriesDescriptor.isContinuous)
        self.assertArgIsBOOL(Accessibility.AXDataSeriesDescriptor.setIsContinuous_, 0)

        self.assertArgIsBOOL(
            Accessibility.AXDataSeriesDescriptor.initWithName_isContinuous_dataPoints_,
            1,
        )
        self.assertArgIsBOOL(
            Accessibility.AXDataSeriesDescriptor.initWithAttributedName_isContinuous_dataPoints_,
            1,
        )
