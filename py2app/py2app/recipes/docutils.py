def check(cmd, mf):
    m = mf.findNode('docutils')
    if m is None or m.filename is None:
        return None
    for pkg in [
            'languages', 'parsers', 'readers', 'writers',
            'parsers.rst.directives', 'parsers.rst.languages']:
        mf.import_hook('docutils.' + pkg, m, ['*'])
    return dict()
