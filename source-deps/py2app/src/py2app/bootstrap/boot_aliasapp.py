def _run(*scripts):
    import os, sys, site
    import Carbon.File
    sys.frozen = 'macosx_app'
    site.addsitedir(os.path.dirname(os.path.abspath(__file__)))
    for script in scripts:
        alias = Carbon.File.Alias(rawdata=script)
        target, wasChanged = alias.ResolveAlias(None)
        path = target.as_pathname()
        sys.path.append(os.path.dirname(path))
        execfile(path, globals(), globals())
