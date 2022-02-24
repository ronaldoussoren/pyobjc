from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKAnnotationView(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(MapKit.MKAnnotationViewZPriority, float)
        self.assertIsTypedEnum(MapKit.MKFeatureDisplayPriority, float)

    def test_enum_types(self):
        self.assertIsEnumType(MapKit.MKAnnotationViewCollisionMode)
        self.assertIsEnumType(MapKit.MKAnnotationViewDragState)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(MapKit.MKAnnotationCalloutInfoDidChangeNotification, str)

        self.assertEqual(MapKit.MKAnnotationViewDragStateNone, 0)
        self.assertEqual(MapKit.MKAnnotationViewDragStateStarting, 1)
        self.assertEqual(MapKit.MKAnnotationViewDragStateDragging, 2)
        self.assertEqual(MapKit.MKAnnotationViewDragStateCanceling, 3)
        self.assertEqual(MapKit.MKAnnotationViewDragStateEnding, 4)

        self.assertEqual(MapKit.MKFeatureDisplayPriorityRequired, 1000)
        self.assertEqual(MapKit.MKFeatureDisplayPriorityDefaultHigh, 750)
        self.assertEqual(MapKit.MKFeatureDisplayPriorityDefaultLow, 250)

        self.assertEqual(MapKit.MKAnnotationViewCollisionModeRectangle, 0)
        self.assertEqual(MapKit.MKAnnotationViewCollisionModeCircle, 1)
        self.assertEqual(MapKit.MKAnnotationViewCollisionModeNone, 2)

        self.assertEqual(MapKit.MKAnnotationViewZPriorityMax, 1000.0)
        self.assertEqual(MapKit.MKAnnotationViewZPriorityDefaultSelected, 1000.0)
        self.assertEqual(MapKit.MKAnnotationViewZPriorityDefaultUnselected, 500.0)
        self.assertEqual(MapKit.MKAnnotationViewZPriorityMin, 0.0)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKAnnotationView, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultHasType(
            MapKit.MKAnnotationView.centerOffset, MapKit.CGPoint.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKAnnotationView.setCenterOffset_, 0, MapKit.CGPoint.__typestr__
        )

        self.assertResultHasType(
            MapKit.MKAnnotationView.calloutOffset, MapKit.CGPoint.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKAnnotationView.setCalloutOffset_, 0, MapKit.CGPoint.__typestr__
        )

        self.assertResultHasType(
            MapKit.MKAnnotationView.leftCalloutOffset, MapKit.CGPoint.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKAnnotationView.setLeftCalloutOffset_, 0, MapKit.CGPoint.__typestr__
        )

        self.assertResultHasType(
            MapKit.MKAnnotationView.rightCalloutOffset, MapKit.CGPoint.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKAnnotationView.setRightCalloutOffset_,
            0,
            MapKit.CGPoint.__typestr__,
        )

        self.assertResultIsBOOL(MapKit.MKAnnotationView.isEnabled)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setEnabled_, 0)

        self.assertResultIsBOOL(MapKit.MKAnnotationView.isHighlighted)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setHighlighted_, 0)

        self.assertResultIsBOOL(MapKit.MKAnnotationView.isSelected)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setSelected_, 0)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setSelected_animated_, 0)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setSelected_animated_, 1)

        self.assertResultIsBOOL(MapKit.MKAnnotationView.canShowCallout)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setCanShowCallout_, 0)

        self.assertResultIsBOOL(MapKit.MKAnnotationView.isDraggable)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setDraggable_, 0)
        self.assertArgIsBOOL(MapKit.MKAnnotationView.setDragState_animated_, 1)
