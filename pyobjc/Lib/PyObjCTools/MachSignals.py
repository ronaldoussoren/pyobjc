import _machsignals
import signal as signalmodule
__all__ = ['getsignal', 'signal']

def getsignal(signum):
    return _machsignals._signalmapping.get(signum)

def signal(signum, handler):
    rval = getsignal(signum)
    _machsignals._signalmapping[signum] = handler
    _machsignals.handleSignal(signum)
    return rval
