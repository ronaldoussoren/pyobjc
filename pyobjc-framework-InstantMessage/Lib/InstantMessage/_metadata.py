# Generated file, don't edit
# Source: BridgeSupport/InstantMessage.bridgesupport
# Last update: Thu Jul 21 08:46:43 2011

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
}
constants = '''$IMAVManagerStateChangedNotification$IMAVManagerURLToShareChangedNotification$IMCapabilityAudioConference$IMCapabilityDirectIM$IMCapabilityFileSharing$IMCapabilityFileTransfer$IMCapabilityText$IMCapabilityVideoConference$IMMyStatusChangedNotification$IMPersonAVBusyKey$IMPersonCapabilitiesKey$IMPersonEmailKey$IMPersonFirstNameKey$IMPersonIdleSinceKey$IMPersonInfoChangedNotification$IMPersonLastNameKey$IMPersonPictureDataKey$IMPersonScreenNameKey$IMPersonServiceNameKey$IMPersonStatusChangedNotification$IMPersonStatusKey$IMPersonStatusMessageKey$IMServiceStatusChangedNotification$IMStatusImagesChangedAppearanceNotification$'''
enums = '''$IMAVInactive@0$IMAVPending@4$IMAVRequested@1$IMAVRunning@5$IMAVShuttingDown@2$IMAVStartingUp@3$IMPersonStatusAvailable@4$IMPersonStatusAway@3$IMPersonStatusIdle@2$IMPersonStatusNoStatus@5$IMPersonStatusOffline@1$IMPersonStatusUnknown@0$IMServiceStatusDisconnected@1$IMServiceStatusLoggedIn@4$IMServiceStatusLoggedOut@0$IMServiceStatusLoggingIn@3$IMServiceStatusLoggingOut@2$IMVideoOptimizationDefault@0$IMVideoOptimizationReplacement@2$IMVideoOptimizationStills@1$'''
misc.update({})
functions = {'IMComparePersonStatus': (sel32or64('iII', 'qII'),)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSObject', b'getOpenGLBufferContext:pixelFormat:', {'arguments': {2: {'type_modifier': b'o'}, 3: {'type_modifier': b'o'}}})
    r('NSObject', b'getPixelBufferPixelFormat:', {'arguments': {2: {'type_modifier': b'o'}}})
    r('NSObject', b'renderIntoOpenGLBuffer:onScreen:forTime:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{__CVBuffer=}'}, 3: {'type_modifier': b'n'}, 4: {'type_modifier': b'n'}}})
    r('NSObject', b'renderIntoPixelBuffer:forTime:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{__CVBuffer=}'}, 3: {'type_modifier': b'n'}}})
finally:
    objc._updatingMetadata(False)
protocols={'IMVideoDataSource': objc.informal_protocol('IMVideoDataSource', [objc.selector(None, 'getOpenGLBufferContext:pixelFormat:', 'v@:^^{_CGLContextObject}^^{_CGLPixelFormatObject}', isRequired=False), objc.selector(None, 'getPixelBufferPixelFormat:', 'v@:^I', isRequired=False), objc.selector(None, 'renderIntoOpenGLBuffer:onScreen:forTime:', 'Z@:^{__CVBuffer=}^i^{?=IiqQdq{CVSMPTETime=ssIIIssss}QQ}', isRequired=False), objc.selector(None, 'renderIntoPixelBuffer:forTime:', 'Z@:^{__CVBuffer=}^{?=IiqQdq{CVSMPTETime=ssIIIssss}QQ}', isRequired=False)])}
