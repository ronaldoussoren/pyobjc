=========================================================
:mod:`PyObjCTools.Signals` -- Debug signal handling
=========================================================

.. module:: PyObjCTools.Signals
   :synopsis: Debug signal handling

This module provides two functions that can be useful while investigating
random crashes of a PyObjC program. These crashes are often caused by 
Objective-C style weak references or incorrectly implemented protocols.

.. function:: dumpStackOnFatalSignal()

    This function will install signal handlers that print a stack trace and
    then re-raise the signal.

.. function:: resetFatalSignals()

    Restores the signal handlers to the state they had before the call to
    dumpStackOnFatalSignal.

This module is not designed to provide fine grained control over signal 
handling. Nor is it intended to be terribly robust. It may give useful
information when your program gets unexpected signals, but it might just
as easily cause a crash when such a signal gets in.