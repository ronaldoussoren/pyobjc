:mod:`PyObjCTools.AppHelper` -- Work with AppKit
================================================

.. module:: PyObjCTools.AppHelper
   :synopsis: Work with AppKit

This module exports functions that are useful when working with the
:mod:`AppKit` framework (or more generally, run loops).

.. function:: callAfter(func, *args, **kwargs) -> None

    Call *function* on the main thread.  Returns immediately.

    :arg func: The callable to invoke on the main thread.
    :arg \*args: Positional arguments for *func*.
    :arg \*\*kwds: Keyword arguments for *func*.

.. function:: callLater(delay, func, *args, **kwargs) -> None

    Call a function on the main thread after a delay.  Returns immediately.

    :arg delay: The delay in sectonds before invoking *func*
    :arg func: The callable to invoke on the main thread.
    :arg \*args: Positional arguments for *func*.
    :arg \*\*kwds: Keyword arguments for *func*.

.. function:: endSheetMethod(method) -> objc.selector

    Convert a method to a form that is suitable to use as the delegate callback
    for sheet methods.

    :arg method: Callable with 3 arguments (the source object, return code and context)
    :returns: Callable wrapped in a selector with the correct signature

.. function:: stopEventLoop() -> None

    Stops the event loop (if started by :func:`runConsoleEventLoop`) or sends the
    ``NSApplication`` a ``terminate:`` message.

.. function:: runConsoleEventLoop(argv=None, installInterrupt=False, mode=NSDefaultRunLoopMode, maxTimeout=3.0) -> None

    Run a ``NSRunLoop`` in a stoppable way (with ``stopEventLoop``).

    :param argv: Program argument vector, defaults to :data:`sys.argv`.
    :param installInterrupt: If true install a signal handler that will handle "CTRL+C".
    :param mode: The runloop mode
    :param maxTimeout: The maximum delay between calling :func:`stopEventLoop` and actually stopping the run loop.

    .. versionadded: 3.1
       The *maxTimeout* parameter

.. function:: runEventLoop(argv=None, unexpectedErrorAlert=None, installInterrupt=None, pdb=None, main=NSApplicationMain) -> None

    Run the event loop using ``NSApplicationMain`` and ask the user if we should
    continue if an exception is caught.

    .. note:: This function doesn't return unless it throws an exception.

    :param argv: Program argument vector, defaults to :data:`sys.argv`.
    :param unexpectedErrorAlert: Callable without arguments that will be invoked when uncaught exception is detected. Defaults to dropping into :mod:`pdb` when *pdb* is true
                                 and to showing an alert panel otherwise.
    :param installInterrupt: If true install a signal handler that will handle "CTRL+C".
    :param pdb: If true assume we're running with a debugger, default is False unless "USE_PDB" is set in the environment
    :param main: Main function to use, defaults to *NSApplicationMain*
