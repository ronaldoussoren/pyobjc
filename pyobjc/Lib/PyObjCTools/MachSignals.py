"""
MachSignals - Integrating signal handling into the runloop
"""
import _machsignals
__all__ = ['getsignal', 'signal']

def getsignal(signum):
    """
    Return the signal handler for signal ``signum``. Returns ``None`` when
    there is no signal handler for the signal.
    """
    return _machsignals._signalmapping.get(signum)

def signal(signum, handler):
    """
    Install a new signal handler for ``signum``. Returns the old signal 
    handler (``None`` when there is no previous handler.
    """
    rval = getsignal(signum)
    _machsignals._signalmapping[signum] = handler
    _machsignals.handleSignal(signum)
    return rval
