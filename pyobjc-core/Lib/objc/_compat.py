import warnings

from objc import options as _options


def setVerbose(value):
    warnings.warn("Set objc.options.verbose instead", DeprecationWarning)
    _options.verbose = bool(value)


def getVerbose():
    warnings.warn("Read objc.options.verbose instead", DeprecationWarning)
    return _options.verbose


def setUseKVOForSetattr(value):
    warnings.warn("Set objc.options.use_kvo instead", DeprecationWarning, 2)
    _options.use_kvo = bool(value)


def getUseKVOForSetattr():
    warnings.warn("Read objc.options.use_kvo instead", DeprecationWarning)
    return _options.use_kvo


def _setClassExtender(value):
    warnings.warn("Set objc.options._class_extender instead", DeprecationWarning, 2)
    _options._class_extender = value


def allocateBuffer(length):
    """Allocate a read/write buffer of memory of the given size."""
    if not isinstance(length, int) or length <= 0:
        raise TypeError("length must be a positive integer")

    warnings.warn("Use bytearray instead", DeprecationWarning)

    return bytearray(length)
