import os
import plistlib
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
    return plugin, plist

if __name__ == '__main__':
    import sys
    create_pluginbundle('build', sys.argv[1])
