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

from Cocoa import *
import WebKit
from CoreLocation import *
import math

class WhereIsMyMacAppDelegate (NSObject):
    window = objc.ivar()
    webView = objc.IBOutlet()
    locationManager = objc.ivar()
    locationLabel = objc.IBOutlet()
    accuracyLabel = objc.IBOutlet()



    def applicationDidFinishLaunching_(self, notification):
	self.locationManager = CLLocationManager.alloc().init()
	self.locationManager.setDelegate_(self)
	self.locationManager.startUpdatingLocation()

    @classmethod
    def latitudeRangeForLocation_(self, aLocation):
	M = 6367000.0; # approximate average meridional radius of curvature of earth
	metersToLatitude = 1.0 / ((math.pi / 180.0) * M);
	accuracyToWindowScale = 2.0;
	
	return aLocation.horizontalAccuracy() * metersToLatitude * accuracyToWindowScale;

    @classmethod
    def longitudeRangeForLocation_(self, aLocation):
	latitudeRange = WhereIsMyMacAppDelegate.latitudeRangeForLocation_(aLocation)
	
	return latitudeRange * math.cos(aLocation.coordinate().latitude * math.pi / 180.0)


    @objc.IBAction
    def openInDefaultBrowser_(self, sender):
	currentLocation = locationManager.location()
	
	externalBrowserURL = NSURL.URLWithString_(
		u"http://maps.google.com/maps?ll=%f,%f&amp;spn=%f,%f"%(
                    currentLocation.coordinate.latitude,
                    currentLocation.coordinate.longitude,
                    WhereIsMyMacAppDelegate.latitudeRangeForLocation_(currentLocation),
                    WhereIsMyMacAppDelegate.longitudeRangeForLocation_(currentLocation)))

	NSWorkspace.sharedWorkspace.openURL_(externalBrowserURL)

    def locationManager_didUpdateToLocation_fromLocation_(self, 
            manager, newLocation, oldLocation):

	# Ignore updates where nothing we care about changed
        if newLocation is None:
            return
        if oldLocation is None:
            pass
	elif (newLocation.coordinate().longitude == oldLocation.coordinate().longitude and
		newLocation.coordinate().latitude == oldLocation.coordinate().latitude and
                newLocation.horizontalAccuracy() == oldLocation.horizontalAccuracy()):
		return

	# Load the HTML for displaying the Google map from a file and replace the
	# format placeholders with our location data
        path = NSBundle.mainBundle().pathForResource_ofType_(u"HTMLFormatString", u"html")
        htmlString = open(path, 'r').read() % (
		newLocation.coordinate().latitude,
		newLocation.coordinate().longitude,
		WhereIsMyMacAppDelegate.latitudeRangeForLocation_(newLocation),
		WhereIsMyMacAppDelegate.longitudeRangeForLocation_(newLocation))
	
	# Load the HTML in the WebView and set the labels
	self.webView.mainFrame().loadHTMLString_baseURL_(htmlString, None)
	self.locationLabel.setStringValue_(u"%f, %f"%(
		newLocation.coordinate().latitude, newLocation.coordinate().longitude))
	self.accuracyLabel.setStringValue_(u"%f"%(newLocation.horizontalAccuracy(),))

    def locationManager_didFailWithError_(self, manager, error):
	self.webView.mainFrame.loadHTMLString_baseURL_(
                NSLocalizedString(u"Location manager failed with error: %s", nil) % (
                    error.localizedDescription()), None)
	self.locationLabel.setStringValue_(u"")
	self.accuracyLabel.setStringValue_(u"")

    def applicationWillTerminate_(self, aNotification):
	self.locationManager.stopUpdatingLocation()
