"""
This file is a translation from Objective-C. The original
copy-right:

//  Copyright 2009 Matt Gallagher. All rights reserved.
//
//  Permission is given to use this source code file, free of charge, in any
//  project, commercial or otherwise, entirely at your risk, with the condition
//  that any redistribution (in part or whole) of source code must retain
//  this copyright and permission notice. Attribution in compiled projects is
//  appreciated but not required.
"""

import math

import Cocoa
import WebKit  # noqa: F401
import CoreLocation
import objc


class WhereIsMyMacAppDelegate(Cocoa.NSObject):
    window = objc.ivar()
    webView = objc.IBOutlet()
    locationManager = objc.ivar()
    locationLabel = objc.IBOutlet()
    accuracyLabel = objc.IBOutlet()

    def applicationDidFinishLaunching_(self, notification):
        self.locationManager = CoreLocation.CLLocationManager.alloc().init()
        self.locationManager.setDelegate_(self)
        self.locationManager.startUpdatingLocation()

    @classmethod
    def latitudeRangeForLocation_(self, location):
        M = 6_367_000.0
        # approximate average meridional radius of curvature of earth
        metersToLatitude = 1.0 / ((math.pi / 180.0) * M)
        accuracyToWindowScale = 2.0

        return location.horizontalAccuracy() * metersToLatitude * accuracyToWindowScale

    @classmethod
    def longitudeRangeForLocation_(self, location):
        latitudeRange = WhereIsMyMacAppDelegate.latitudeRangeForLocation_(location)

        return latitudeRange * math.cos(location.coordinate().latitude * math.pi / 180.0)

    @objc.IBAction
    def openInDefaultBrowser_(self, sender):
        currentLocation = self.locationManager.location()

        externalBrowserURL = Cocoa.NSURL.URLWithString_(
            "http://maps.google.com/maps?ll=%f,%f&amp;spn=%f,%f"
            % (
                currentLocation.coordinate().latitude,
                currentLocation.coordinate().longitude,
                WhereIsMyMacAppDelegate.latitudeRangeForLocation_(currentLocation),
                WhereIsMyMacAppDelegate.longitudeRangeForLocation_(currentLocation),
            )
        )

        Cocoa.NSWorkspace.sharedWorkspace().openURL_(externalBrowserURL)

    def locationManager_didUpdateToLocation_fromLocation_(
        self, manager, newLocation, oldLocation
    ):
        # Ignore updates where nothing we care about changed
        if newLocation is None:
            return
        if oldLocation is None:
            pass
        elif (
            newLocation.coordinate().longitude == oldLocation.coordinate().longitude
            and newLocation.coordinate().latitude == oldLocation.coordinate().latitude
            and newLocation.horizontalAccuracy() == oldLocation.horizontalAccuracy()
        ):
            return

        # Load the HTML for displaying the Google map from a file and replace the
        # format placeholders with our location data
        path = Cocoa.NSBundle.mainBundle().pathForResource_ofType_(
            "HTMLFormatString", "html"
        )
        with open(path) as fp:
            htmlString = fp.read() % (
                newLocation.coordinate().latitude,
                newLocation.coordinate().longitude,
                WhereIsMyMacAppDelegate.latitudeRangeForLocation_(newLocation),
                WhereIsMyMacAppDelegate.longitudeRangeForLocation_(newLocation),
            )

        # Load the HTML in the WebView and set the labels
        self.webView.mainFrame().loadHTMLString_baseURL_(htmlString, None)
        self.locationLabel.setStringValue_(
            "%f, %f"
            % (newLocation.coordinate().latitude, newLocation.coordinate().longitude)
        )
        self.accuracyLabel.setStringValue_(f"{newLocation.horizontalAccuracy():f}")

    def locationManager_didFailWithError_(self, manager, error):
        self.webView.mainFrame.loadHTMLString_baseURL_(
            Cocoa.NSLocalizedString("Location manager failed with error: %s", objc.nil)
            % (error.localizedDescription()),
            None,
        )
        self.locationLabel.setStringValue_("")
        self.accuracyLabel.setStringValue_("")

    def applicationWillTerminate_(self, aNotification):
        self.locationManager.stopUpdatingLocation()
