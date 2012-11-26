__all__ = ['runtime', 'pluginBundle', 'registerPlugin', 'splitStruct', '_loadFunctionList']
import warnings

class Runtime:
    """
    Backward compatibility interface.

    This class provides (partial) support for the interface of
    older versions of PyObjC.
    """
    def __getattr__(self, name):
        warnings.warn("Deprecated: use objc.lookUpClass",
            DeprecationWarning)
        import objc
        if name == '__objc_classes__':
            return objc.getClassList()
        elif name == '__kind__':
            return 'python'

        try:
            return objc.lookUpClass(name)
        except objc.nosuchclass_error:
            raise AttributeError(name)

    def __repr__(self):
        return "objc.runtime"

runtime = Runtime()

_PLUGINS = {}
def registerPlugin(pluginName):
    """
    Deprecated: use currentBundle()

    Register the current py2app plugin by name and return its bundle
    """
    warnings.warn("Deprecated: use objc.currentBundle()", DeprecationWarning)
    import os
    import sys
    path = os.path.dirname(os.path.dirname(os.environ['RESOURCEPATH']))
    if sys.version_info[0] == 2 and not isinstance(path, unicode):
        path = unicode(path, sys.getfilesystemencoding())
    _PLUGINS[pluginName] = path
    return pluginBundle(pluginName)

def pluginBundle(pluginName):
    """
    Deprecated: use currentBundle()

    Return the main bundle for the named plugin. This should be used
    only after it has been registered with registerPlugin
    """
    warnings.warn("Deprecated: use currentBundle()", DeprecationWarning)
    import objc
    NSBundle = objc.lookUpClass('NSBundle')
    return NSBundle.bundleWithPath_(_PLUGINS[pluginName])

def splitStruct(value):
    warnings.warn("Deprecated: use splitStructSignature()", DeprecationWarning)
    import objc
    return objc.splitStructSignature(value)

def _loadFunctionList(*args, **kwds):
    warnings.warn("Deprecated: use loadFunctionList()", DeprecationWarning)
    import objc
    objc.loadFunctionList(*args, **kwds)
