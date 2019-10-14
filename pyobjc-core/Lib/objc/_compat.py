from objc import options as _options
import warnings


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
