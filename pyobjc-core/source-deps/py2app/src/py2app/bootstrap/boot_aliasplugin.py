def _run(*scripts):
    global __file__
    import os, sys, site
    import Carbon.File
    sys.frozen = 'macosx_plugin'
    site.addsitedir(os.environ['RESOURCEPATH'])
    for (script, path) in scripts:
        alias = Carbon.File.Alias(rawdata=script)
        target, wasChanged = alias.ResolveAlias(None)
        if not os.path.exists(path):
            path = target.as_pathname()
        sys.path.append(os.path.dirname(path))
        __file__ = path
        execfile(path, globals(), globals())
