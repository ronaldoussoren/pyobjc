def _disable_linecache():
    import linecache
    def fake_getline(filename, lineno):
        return ''
    linecache.orig_getline = linecache.getline
    linecache.getline = fake_getline
_disable_linecache()
