__all__ = ['runtime', 'pluginBundle', 'registerPlugin']

class Runtime:
    """
    Backward compatibility interface.

    This class provides (partial) support for the interface of
    older versions of PyObjC.
    """
    def __getattr__(self, name):
        import warnings
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
            raise AttributeError, name

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return "objc.runtime"

runtime = Runtime()

_PLUGINS = {}
def registerPlugin(pluginName):
    """
    Deprecated: use currentBundle()

    Register the current py2app plugin by name and return its bundle
    """
    import os
    import sys
    path = os.path.dirname(os.path.dirname(os.environ['RESOURCEPATH']))
    if not isinstance(path, unicode):
        path = unicode(path, sys.getfilesystemencoding())
    _PLUGINS[pluginName] = path
    return pluginBundle(pluginName)

def pluginBundle(pluginName):
    """
    Deprecated: use currentBundle()

    Return the main bundle for the named plugin. This should be used
    only after it has been registered with registerPlugin
    """
    import warnings
    warnings.warn("Deprecated: use currentBundle()", DeprecationWarning)
    from Foundation import NSBundle
    return NSBundle.bundleWithPath_(_PLUGINS[pluginName])
