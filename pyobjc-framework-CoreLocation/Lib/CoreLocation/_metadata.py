# Generated file, don't edit
# Source: BridgeSupport/CoreLocation.bridgesupport
# Last update: Mon Jul 18 19:28:08 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
    "CLLocationCoordinate2D": objc.createStructType('CLLocationCoordinate2D', b'{_CLLocationCoordinate2D="latitude"d"longitude"d}', None),
}
constants = '''$kCLDistanceFilterNone@d$kCLErrorDomain$kCLLocationAccuracyBest@d$kCLLocationAccuracyHundredMeters@d$kCLLocationAccuracyKilometer@d$kCLLocationAccuracyNearestTenMeters@d$kCLLocationAccuracyThreeKilometers@d$'''
enums = '''$kCLErrorDenied@1$kCLErrorLocationUnknown@0$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('CLLocation', b'initWithCoordinate:altitude:horizontalAccuracy:verticalAccuracy:timestamp:', {'arguments': {2: {'type': b'{_CLLocationCoordinate2D=dd}'}}})
    r('CLLocation', b'coordinate', {'retval': {'type': b'{_CLLocationCoordinate2D=dd}'}})
    r('CLLocationManager', b'locationServicesEnabled', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
