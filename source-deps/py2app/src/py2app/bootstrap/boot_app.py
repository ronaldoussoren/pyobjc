def _run(*scripts):
    import os, sys, site
    sys.frozen = 'macosx_app'
    base = os.path.dirname(os.path.abspath(__file__))
    site.addsitedir(base)
    site.addsitedir(os.path.join(base, 'Python', 'site-packages'))
    if not scripts:
        import __main__
    for script in scripts:
        execfile(os.path.join(base, 'Python', script), globals(), globals())
