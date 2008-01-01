import os
import plistlib
import shutil
import py2app.bundletemplate
from py2app.util import makedirs, mergecopy, mergetree, skipscm

def create_pluginbundle(destdir, name, extension='.plugin', module=py2app.bundletemplate,
        platform='MacOS', copy=mergecopy, mergetree=mergetree,
        condition=skipscm, plist={}):
    kw = module.plist_template.infoPlistDict(
        plist.get('CFBundleExecutable', name), plist)
    plugin = os.path.join(destdir, kw['CFBundleName'] + extension)
    contents = os.path.join(plugin, 'Contents')
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
    return plugin, plist

if __name__ == '__main__':
    import sys
    create_pluginbundle('build', sys.argv[1])
