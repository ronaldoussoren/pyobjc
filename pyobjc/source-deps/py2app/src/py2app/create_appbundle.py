import os
import plistlib
# XXX - plugins, prefpane, etc?
import py2app.apptemplate
from py2app.util import fsencoding, copy2

def makedirs(path):
    path = fsencoding(path)
    if not os.path.exists(path):
        os.makedirs(path)

def copy(src, dest):
    if os.path.exists(dest) and os.stat(dest).st_mtime >= os.stat(src).st_mtime:
        return
    copy2(src, dest)

def skipscm(ofn):
    fn = os.path.basename(ofn)
    if fn == 'CVS' or fn == '.svn':
        return False
    return True

def mergetree(src, dst, condition=None, copyfn=copy):
    """Recursively merge a directory tree using copy()."""
    # XXX - symlinks
    src = fsencoding(src)
    dst = fsencoding(dst)
    names = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        if condition is not None and not condition(srcname):
            continue
        try:
            if os.path.isdir(srcname):
                mergetree(srcname, dstname, condition=condition)
            else:
                copyfn(srcname, dstname)
        except (IOError, os.error), why:
            errors.append((srcname, dstname, why))
    if errors:
        raise Error, errors
    

def create_appbundle(destdir, name, module=py2app.apptemplate,
        platform='MacOS', copy=copy, mergetree=mergetree,
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
