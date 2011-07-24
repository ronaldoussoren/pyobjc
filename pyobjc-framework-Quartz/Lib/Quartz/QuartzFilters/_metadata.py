# Generated file, don't edit
# Source: BridgeSupport/QuartzFilters.bridgesupport
# Last update: Thu Jul 21 17:06:27 2011

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
constants = '''$kQuartzFilterApplicationDomain$kQuartzFilterManagerDidAddFilterNotification$kQuartzFilterManagerDidModifyFilterNotification$kQuartzFilterManagerDidRemoveFilterNotification$kQuartzFilterManagerDidSelectFilterNotification$kQuartzFilterPDFWorkflowDomain$kQuartzFilterPrintingDomain$'''
enums = '''$'''
misc.update({})
functions = {}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('QuartzFilter', b'applyToContext:', {'retval': {'type': b'Z'}, 'arguments': {2: {'type': b'^{CGContext=}'}}})
    r('QuartzFilter', b'removeFromContext:', {'arguments': {2: {'type': b'^{CGContext=}'}}})
    r('QuartzFilterView', b'selectFilter:', {'retval': {'type': b'Z'}})
    r('QuartzFilterManager', b'selectFilter:', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
protocols={'QuartzFilterManagerDelegate': objc.informal_protocol('QuartzFilterManagerDelegate', [objc.selector(None, 'quartzFilterManager:didAddFilter:', 'v@:@@', isRequired=False), objc.selector(None, 'quartzFilterManager:didModifyFilter:', 'v@:@@', isRequired=False), objc.selector(None, 'quartzFilterManager:didRemoveFilter:', 'v@:@@', isRequired=False), objc.selector(None, 'quartzFilterManager:didSelectFilter:', 'v@:@@', isRequired=False)])}
