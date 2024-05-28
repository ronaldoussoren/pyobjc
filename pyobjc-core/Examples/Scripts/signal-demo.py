#!/usr/bin/python
"""
This script demonstrates using the PyObjCTools.Signals
module to show a stacktrace when there's a fatal signal
when running a script.
"""

import os
import signal

from PyObjCTools import Signals

Signals.dumpStackOnFatalSignal()


# all this does is set up an interesting stack to
# to show that a backtrace really is being
# generated.  Try commenting out the
# Signals.dumpStackOnFatalSignal() line above and run
# the script again.


def badness():
    os.kill(os.getpid(), signal.SIGQUIT)


class Foo:
    def baz(self):
        badness()

    def bar(self):
        self.baz()


Foo().bar()
