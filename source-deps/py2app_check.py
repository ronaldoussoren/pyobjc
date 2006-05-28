import imp
import os, sys, site
path = os.path.join(os.path.dirname(__file__), 'py2app-source', 'src')
try:
    py2app_file = imp.find_module('py2app', None)[1]
    from findVersion import findVersion
    srcVersion = findVersion(os.path.join(path, 'py2app', '__init__.py'))
    locVersion = findVersion(os.path.join(py2app_file, '__init__.py'))
    from distutils.version import LooseVersion
    if LooseVersion(locVersion) < LooseVersion(srcVersion):
        raise ImportError, "Old version detected %s < %s" % (locVersion, srcVersion)
    # import local versions
    import py2app
    import bdist_mpkg
except (ImportError, ValueError):
    # shuffle to the beginning, there may be an old version installed
    print '** using pyobjc source-deps py2app for building'
    pathlen = len(sys.path)
    site.addsitedir(path)
    newentries = sys.path[pathlen:]
    del sys.path[pathlen:]
    sys.path[1:1] = newentries
