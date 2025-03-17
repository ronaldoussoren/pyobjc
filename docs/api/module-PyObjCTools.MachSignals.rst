================================================================
:mod:`PyObjCTools.MachSignals` -- signal handling in a CFRunLoop
================================================================

.. module:: PyObjCTools.MachSignals
   :synopsis: signal handling in a CFRunLoop

Substitute for the signal module when using a :class:`CFRunLoopRef`.

This module is generally only used to support :func:`PyObjCTools.AppHelper.installMachInterrupt`.

A mach port is opened and registered to the Run Loop.
When a signal occurs the signal number is sent in a mach
message to the Run Loop.  The handler then causes Python
code to get executed.

This is equivalent to the :mod:`signal` module, but that module
doesn't work promptly when a program is blocked waiting on
a Run Loop.

.. function:: getsignal(signum)

   Query the current signal handler for *signum*.

   :param int signum: Signal value to query,should be one of the ``SIG*`` constants from :mod:`signal`.
   :returns: :data:`None` when there is no signal handler, handler function otherwise.

.. function:: signal(signum, handler)

   Install a new signal handler for *signum*.

   :param int signum: Signal value to set,should be one of the ``SIG*`` constants from :mod:`signal`.
   :param handler: Signal handler callable, should accept a single positional parameter, the signal number.
   :returns: The previous signal handler, or :data:`None` when there is no previous handler.
