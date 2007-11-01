import os
import plistlib
import shutil
# XXX - plugins, prefpane, etc?
import py2app.apptemplate
from py2app.util import makedirs, mergecopy, mergetree, skipscm

def create_appbundle(destdir, name, extension='.app', module=py2app.apptemplate,
        platform='MacOS', copy=mergecopy, mergetree=mergetree,
        condition=skipscm, plist={}):
    kw = module.plist_template.infoPlistDict(
        plist.get('CFBundleExecutable', name), plist)
    app = os.path.join(destdir, kw['CFBundleName'] + extension)
    contents = os.path.join(app, 'Contents')
    resources = os.path.join(contents, 'Resources')
    platdir = os.path.join(contents, platform)
    dirs = [contents, resources, platdir]
    plist = plistlib.Plist()
    plist.update(kw)
    plistPath = os.path.join(contents, 'Info.plist')
    if os.path.exists(plistPath):
        if plist != plistlib.Plist.fromFile(plistPath):
            for d in dirs:
                shutil.rmtree(d, ignore_errors=True)
    for d in dirs:
        makedirs(d)
    plist.write(plistPath)
    srcmain = module.setup.main()
    destmain = os.path.join(platdir, kw['CFBundleExecutable'])
    open(os.path.join(contents, 'PkgInfo'), 'w').write(
        kw['CFBundlePackageType'] + kw['CFBundleSignature']
    )
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
