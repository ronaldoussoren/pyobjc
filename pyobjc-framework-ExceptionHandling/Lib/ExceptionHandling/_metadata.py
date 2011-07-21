# Generated file, don't edit
# Source: BridgeSupport/ExceptionHandling.bridgesupport
# Last update: Thu Jul 21 08:43:15 2011

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
constants = '''$NSStackTraceKey$NSUncaughtRuntimeErrorException$NSUncaughtSystemExceptionException$'''
enums = '''$NSHandleOtherExceptionMask@512$NSHandleTopLevelExceptionMask@128$NSHandleUncaughtExceptionMask@2$NSHandleUncaughtRuntimeErrorMask@32$NSHandleUncaughtSystemExceptionMask@8$NSHangOnEveryExceptionMask@31$NSHangOnOtherExceptionMask@16$NSHangOnTopLevelExceptionMask@8$NSHangOnUncaughtExceptionMask@1$NSHangOnUncaughtRuntimeErrorMask@4$NSHangOnUncaughtSystemExceptionMask@2$NSLogAndHandleEveryExceptionMask@1023$NSLogOtherExceptionMask@256$NSLogTopLevelExceptionMask@64$NSLogUncaughtExceptionMask@1$NSLogUncaughtRuntimeErrorMask@16$NSLogUncaughtSystemExceptionMask@4$'''
misc.update({})
functions = {'NSExceptionHandlerResume': ('v',)}
cftypes = []
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
    r('NSObject', b'exceptionHandler:shouldHandleException:mask:', {'retval': {'type': b'Z'}})
    r('NSObject', b'exceptionHandler:shouldLogException:mask:', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
protocols={'NSExceptionHandlerDelegate': objc.informal_protocol('NSExceptionHandlerDelegate', [objc.selector(None, 'exceptionHandler:shouldHandleException:mask:', sel32or64('Z@:@@I', 'Z@:@@Q'), isRequired=False), objc.selector(None, 'exceptionHandler:shouldLogException:mask:', sel32or64('Z@:@@I', 'Z@:@@Q'), isRequired=False)])}
