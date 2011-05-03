"""
Low level debugging helper for PyObjC.

Allows you to log Python and ObjC (via atos) stack traces for NSExceptions
raised.

General guidelines for use:

- It's typically only useful when you log EVERY exception, because Foundation
  and AppKit will swallow most of them.  This means that you should never
  use this module in a release build.

- Typical use involves only calling installDebuggingHandler or
  installVerboseDebuggingHandler.  It may be removed at any time by calling
  removeDebuggingHandler.
"""

from Foundation import NSObject, NSLog
import objc
import os
import sys

import traceback
from ExceptionHandling import NSExceptionHandler, NSLogUncaughtExceptionMask, NSLogAndHandleEveryExceptionMask, NSStackTraceKey

DEFAULTMASK = NSLogUncaughtExceptionMask
EVERYTHINGMASK = NSLogAndHandleEveryExceptionMask


__all__ = [
    'LOGSTACKTRACE', 'DEFAULTVERBOSITY', 'DEFAULTMASK', 'EVERYTHINGMASK',
    'installDebuggingHandler', 'installVerboseDebuggingHandler',
    'installPythonExceptionHandler', 'removeDebuggingHandler',
    'handlerInstalled',
]

def isPythonException(exception):
    return (exception.userInfo() or {}).get(u'__pyobjc_exc_type__') is not None

def nsLogPythonException(exception):
    userInfo = exception.userInfo()
    NSLog(u'*** Python exception discarded!\n' +
        ''.join(traceback.format_exception(
        userInfo[u'__pyobjc_exc_type__'],
        userInfo[u'__pyobjc_exc_value__'],
        userInfo[u'__pyobjc_exc_traceback__'],
    )).decode('utf8'))
    # we logged it, so don't log it for us
    return False

def nsLogObjCException(exception):
    userInfo = exception.userInfo()
    stack = userInfo.get(NSStackTraceKey)
    if not stack or not os.path.exists('/usr/bin/atos'):
        return True
    pipe = os.popen('/usr/bin/atos -p %d %s' % (os.getpid(), stack))
    stacktrace = pipe.readlines()
    stacktrace.reverse()
    NSLog(u"%@", u"*** ObjC exception '%s' (reason: '%s') discarded\n" % (
            exception.name(), exception.reason(),
        ) +
        u'Stack trace (most recent call last):\n' +
        ''.join([('  '+line) for line in stacktrace]).decode('utf8')
    )
    return False

LOGSTACKTRACE = 1 << 0
DEFAULTVERBOSITY = 0

class PyObjCDebuggingDelegate(NSObject):
    verbosity = objc.ivar('verbosity', 'i')
    
    def initWithVerbosity_(self, verbosity):
        self = self.init()
        self.verbosity = verbosity
        return self

    def exceptionHandler_shouldLogException_mask_(self, sender, exception, aMask):
        try:
            if isPythonException(exception):
                if self.verbosity & LOGSTACKTRACE:
                    nsLogObjCException(exception)
                return nsLogPythonException(exception)
            elif self.verbosity & LOGSTACKTRACE:
                return nsLogObjCException(exception)
            else:
                return False
        except:
            print >>sys.stderr, "*** Exception occurred during exception handler ***"
            traceback.print_exc(sys.stderr)
            return True
    exceptionHandler_shouldLogException_mask_ = objc.selector(exceptionHandler_shouldLogException_mask_, signature='c@:@@I')

    def exceptionHandler_shouldHandleException_mask_(self, sender, exception, aMask):
        return False
    exceptionHandler_shouldHandleException_mask_ = objc.selector(exceptionHandler_shouldHandleException_mask_, signature='c@:@@I')

def installExceptionHandler(verbosity=DEFAULTVERBOSITY, mask=DEFAULTMASK):
    """
    Install the exception handling delegate that will log every exception
    matching the given mask with the given verbosity.
    """
    # we need to retain this, cause the handler doesn't
    global _exceptionHandlerDelegate
    delegate = PyObjCDebuggingDelegate.alloc().initWithVerbosity_(verbosity)
    NSExceptionHandler.defaultExceptionHandler().setExceptionHandlingMask_(mask)
    NSExceptionHandler.defaultExceptionHandler().setDelegate_(delegate)
    _exceptionHandlerDelegate = delegate

def installPythonExceptionHandler():
    """
    Install a verbose exception handling delegate that logs every exception
    raised.

    Will log only Python stack traces, if available.
    """
    installExceptionHandler(verbosity=DEFAULTVERBOSITY, mask=EVERYTHINGMASK)

def installVerboseExceptionHandler():
    """
    Install a verbose exception handling delegate that logs every exception
    raised.

    Will log both Python and ObjC stack traces, if available.
    """
    installExceptionHandler(verbosity=LOGSTACKTRACE, mask=EVERYTHINGMASK)

def removeExceptionHandler():
    """
    Remove the current exception handler delegate
    """
    NSExceptionHandler.defaultExceptionHandler().setDelegate_(None)
    NSExceptionHandler.defaultExceptionHandler().setExceptionHandlingMask_(0)

def handlerInstalled():
    """
    Is an exception handler delegate currently installed?
    """
    return NSExceptionHandler.defaultExceptionHandler().delegate() is not None
