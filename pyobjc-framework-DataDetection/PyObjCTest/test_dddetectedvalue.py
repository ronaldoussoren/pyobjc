from PyObjCTools.TestSupport import TestCase
import DataDetection


class TestDDDetectedValue(TestCase):
    def test_classes(self):
        DataDetection.DDDetectedValue
        DataDetection.DDDetectedValueLink
        DataDetection.DDDetectedValuePhoneNumber
        DataDetection.DDDetectedValueEmailAddress
        DataDetection.DDDetectedValuePostalAddress
        DataDetection.DDDetectedValueCalendarEvent
        DataDetection.DDDetectedValueShipmentTrackingNumber
        DataDetection.DDDetectedValueFlightNumber
        DataDetection.DDDetectedValueMoneyAmount
