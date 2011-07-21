# Generated file, don't edit
# Source: BridgeSupport/InstallerPlugins.bridgesupport
# Last update: Thu Jul 21 08:46:11 2011

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
constants = '''$InstallerState_Choice_CustomLocation$InstallerState_Choice_Identifier$InstallerState_Choice_Installed$'''
enums = '''$InstallerDirectionBackward@1$InstallerDirectionForward@0$InstallerDirectionUndefined@2$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('InstallerPane', b'gotoNextPane', {'retval': {'type': b'Z'}})
    r('InstallerPane', b'gotoPreviousPane', {'retval': {'type': b'Z'}})
    r('InstallerPane', b'nextEnabled', {'retval': {'type': b'Z'}})
    r('InstallerPane', b'previousEnabled', {'retval': {'type': b'Z'}})
    r('InstallerPane', b'setNextEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('InstallerPane', b'setPreviousEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r('InstallerPane', b'shouldExitPane:', {'retval': {'type': b'Z'}})
    r('InstallerSection', b'gotoPane:', {'retval': {'type': b'Z'}})
    r('InstallerSection', b'shouldLoad', {'retval': {'type': b'Z'}})
    r('InstallerState', b'installStarted', {'retval': {'type': b'Z'}})
    r('InstallerState', b'installSucceeded', {'retval': {'type': b'Z'}})
    r('InstallerState', b'licenseAgreed', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
