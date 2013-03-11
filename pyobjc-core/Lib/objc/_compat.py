from objc import options as _options
import warnings

def setVerbose(value):
    warnings.warn("Set objc.options.verbose instead", DeprecationWarning)
    _options.verbose = bool(value)

def getVerbose():
    warnings.warn("Read objc.options.verbose instead", DeprecationWarning)
    return _options.verbose

def setUseKVOForSetattr(value):
    warnings.warn("Set objc.options.use_kvo instead", DeprecationWarning)
    _options.use_kvo = bool(value)

def getUseKVOForSetattr(value):
    warnings.warn("Read objc.options.use_kvo instead", DeprecationWarning)
    return _options._use_kvo


if hasattr(_options, "strbridge_enabled"):
    def setStrBridgeEnabled(value):
        warnings.warn("Set objc.options.strbridge_enabled instead", DeprecationWarning)
        _options.strbridge_enabled = bool(value)

    def getStrBridgeEnabled():
        warnings.warn("Read objc.options.strbridge_enabled instead", DeprecationWarning)
        return _options.strbridge_enabled

