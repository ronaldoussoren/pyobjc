import imp
try:
    imp.find_module('py2app', None)
    imp.find_module('bdist_mpkg', None)
except ImportError:
    import os, sys, site
    path = os.path.join(os.path.dirname(__file__), 'py2app', 'src')
    # shuffle to the beginning, there may be an old version installed
    pathlen = len(sys.path)
    site.addsitedir(path)
    newentries = sys.path[pathlen:]
    del sys.path[pathlen:]
    sys.path[1:1] = newentries
else:
    import bdist_mpkg
