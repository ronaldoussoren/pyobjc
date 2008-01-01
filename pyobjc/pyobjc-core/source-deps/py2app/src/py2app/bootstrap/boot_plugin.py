def _run(*scripts):
    global __file__
    import os, sys, site
    sys.frozen = 'macosx_plugin'
    base = os.environ['RESOURCEPATH']
    site.addsitedir(base)
    site.addsitedir(os.path.join(base, 'Python', 'site-packages'))
    for script in scripts:
        path = os.path.join(base, script)
        __file__ = path
        execfile(path, globals(), globals())
