"""Signals.py -- Automatically dump a python stacktrace if something bad happens.

This module is not designed to provide fine grained control over signal handling.
Nor is it intended to be terribly robust.
"""

import signal
import traceback # go ahead an import now -- don't know what state we'll be in later
import os

__all__ = ["dumpStackOnFatalSignal", "resetFatalSignals"]

originalHandlers = None

def dumpHandler(signum, frame):
    resetFatalSignals()
    print "*** Handling fatal signal '%d'." % signum
    traceback.print_stack(frame)
    print "*** Restored handlers and resignaling."
    os.kill(os.getpid(), signum)

def installHandler(sig):
    originalHandlers[sig] = signal.signal(sig, dumpHandler)

def dumpStackOnFatalSignal():
    global originalHandlers
    if not originalHandlers:
        originalHandlers = {}
        installHandler(signal.SIGQUIT)
        installHandler(signal.SIGILL)
        installHandler(signal.SIGTRAP)
        installHandler(signal.SIGABRT)
        installHandler(signal.SIGEMT)
        installHandler(signal.SIGFPE)
        installHandler(signal.SIGBUS)
        installHandler(signal.SIGSEGV)
        installHandler(signal.SIGSYS)

def resetFatalSignals():
    global originalHandlers
    if originalHandlers:
        for sig in originalHandlers:
            signal.signal(sig, originalHandlers[sig])
        originalHandlers = None
