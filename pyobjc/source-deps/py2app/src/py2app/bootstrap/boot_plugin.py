def _run(*scripts):
    import os, sys, site
    sys.frozen = 'macosx_plugin'
    base = os.environ['RESOURCEPATH']
    site.addsitedir(base)
    site.addsitedir(os.path.join(base, 'Python', 'site-packages'))
    for script in scripts:
        execfile(os.path.join(base, 'Python', script), globals(), globals())
