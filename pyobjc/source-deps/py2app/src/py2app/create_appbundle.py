import os
import plistlib
# XXX - plugins, prefpane, etc?
import py2app.apptemplate
from py2app.util import makedirs, mergecopy, mergetree, skipscm

def create_appbundle(destdir, name, module=py2app.apptemplate,
        platform='MacOS', copy=mergecopy, mergetree=mergetree,
        condition=skipscm, plist={}):
    kw = module.plist_template.infoPlistDict(
        plist.get('CFBundleExecutable', name), plist)
    app = os.path.join(destdir, kw['CFBundleName']+'.app')
    contents = os.path.join(app, 'Contents')
    resources = os.path.join(contents, 'Resources')
    platdir = os.path.join(contents, platform)
    makedirs(contents)
    makedirs(resources)
    makedirs(platdir)
    open(os.path.join(contents, 'PkgInfo'), 'w').write(
        kw['CFBundlePackageType'] + kw['CFBundleSignature']
    )
    plist = plistlib.Plist()
    plist.update(kw)
    plist.write(os.path.join(contents, 'Info.plist'))
    srcmain = module.setup.main()
    destmain = os.path.join(platdir, kw['CFBundleExecutable'])
    copy(srcmain, destmain)
    mergetree(
        os.path.join(os.path.dirname(module.__file__), 'lib'),
        resources,
        condition=condition,
        copyfn=copy,
    )
    return app, plist

if __name__ == '__main__':
    import sys
    create_appbundle('build', sys.argv[1])
