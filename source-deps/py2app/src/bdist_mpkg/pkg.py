import os, sys
import tools, plists
from StringIO import StringIO
from distutils.version import LooseVersion
try:
    from py2app.util import copy_tree
except ImportError:
    from distutils.dir_util import copy_tree
from distutils.dir_util import mkpath
from distutils.file_util import copy_file

def write_sizes(count, size, compressed, pkgdir):
    f = open(os.path.join(pkgdir, 'Contents', 'Resources', 'Archive.sizes'), 'w')
    f.write('NumFiles %d\nInstalledSize %d\nCompressedSize %d' % (count, size, compressed))
    f.close()

TEXT_EXTS = '.rtfd', '.rtf', '.html', '.txt' 
IMAGE_EXTS = '.tiff', '.png', '.jpg'

def write_pkginfo(pkgdir):
    f = open(os.path.join(pkgdir, 'Contents', 'PkgInfo'), 'w')
    f.write('pmkrpkg1')
    f.close()

def try_exts(path, exts=TEXT_EXTS):
    path = os.path.splitext(path)[0]
    for ext in exts:
        npath = path+ext
        if os.path.exists(npath):
            return npath
    return None

def copy_doc(path, name, pkgdir, exts=TEXT_EXTS, language=None, verbose=0, dry_run=0):
    if path is None:
        return
    is_string = hasattr(path, 'getvalue')
    if is_string:
        ext = '.txt'
    else:
        ext = os.path.splitext(path)[1].lower()
        if ext == '':
            ext = '.txt'
    if ext not in exts:
        raise ValueError, 'Invalid extension for %s' % (path,)
    destdir = os.path.join(pkgdir, 'Contents', 'Resources')
    if language is not None:
        destdir = os.path.join(destdir, language+'.lproj')
    mkpath(destdir, verbose=verbose, dry_run=dry_run)
    dest = os.path.join(destdir, name+ext)
    if is_string:
        if not dry_run:
            f = file(dest, 'wb')
            f.write(path.getvalue())
            f.close()
    elif ext == '.rtfd':
        copy_tree(path, dest, update=1, verbose=verbose, dry_run=dry_run)
    else:
        copy_file(path, dest, verbose=verbose, dry_run=dry_run)

def make_metapackage(cmd, name, version, packages, pkgdir, info=(), description=None):
    license = cmd.license
    readme = cmd.readme
    welcome = cmd.welcome
    background = cmd.background
    template = cmd.template

    verbose = cmd.verbose
    dry_run = cmd.dry_run

    dist = cmd.distribution

    if description is None:
        description = dist.get_description()
    if not description:
        description = u'%s %s' % (name, version)

    mkpath(os.path.join(pkgdir, 'Contents', 'Resources'), verbose=verbose, dry_run=dry_run)
    if not dry_run:
        write_pkginfo(pkgdir)
    
    ninfo = plists.mpkg_info(name, version, packages)
    ninfo.update(dict(info))
    if not dry_run:
        plists.write(ninfo, os.path.join(pkgdir, 'Contents', 'Info.plist'))

    desc = plists.common_description(name+' '+version, version)
    if description:
        desc['IFPkgDescriptionDescription'] = description
    if not dry_run:
        plists.write(desc, os.path.join(pkgdir, 'Contents', 'Resources', 'Description.plist'))

    if not os.path.exists(template):
        template = os.path.join(os.path.dirname(__file__), 'lib', template)
    
    copy_tree(
        template,
        os.path.join(pkgdir, 'Contents', 'Resources'),
        update=1, verbose=verbose, dry_run=dry_run,
    )

    if readme is None:
        readme_text = dist.get_long_description()
        if readme_text:
            readme = StringIO(readme_text)
    copy_doc(readme, 'ReadMe', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(license, 'License', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(welcome, 'Welcome', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(background, 'Background', pkgdir, exts=IMAGE_EXTS, verbose=verbose, dry_run=dry_run)

def make_package(cmd, name, version, files, common, prefix, pkgdir, info=(), description=None):
    license = cmd.license
    readme = cmd.readme
    welcome = cmd.welcome
    background = cmd.background
    template = cmd.template

    verbose = cmd.verbose
    dry_run = cmd.dry_run

    dist = cmd.distribution

    if description is None:
        description = dist.get_description()

    mkpath(os.path.join(pkgdir, 'Contents', 'Resources'), verbose=verbose, dry_run=dry_run)
    if not dry_run:
        write_pkginfo(pkgdir)
    
    tools.mkbom(common, pkgdir)
    count = len(files)
    admin = tools.admin_writable(prefix)
    size = tools.reduce_size(files)
    compressed = tools.pax(common, pkgdir)
    if not dry_run:
        write_sizes(count, size, compressed, pkgdir)
    
    if admin:
        auth = u'AdminAuthorization'
    else:
        auth = u'RootAuthorization'

    ninfo = plists.pkg_info(name, version)
    ninfo.update(dict(
        IFPkgFlagAuthorizationAction=auth,
        IFPkgFlagDefaultLocation=tools.unicode_path(prefix),
    ))
    ninfo.update(dict(info))
    if not dry_run:
        plists.write(ninfo, os.path.join(pkgdir, 'Contents', 'Info.plist'))

    desc = plists.common_description(name, version)
    if description is not None:
        desc['IFPkgDescriptionDescription'] = description
    if not dry_run:
        plists.write(desc, os.path.join(pkgdir, 'Contents', 'Resources', 'Description.plist'))

    if not os.path.exists(template):
        template = os.path.join(os.path.dirname(__file__), 'lib', template)
    
    copy_tree(
        template,
        os.path.join(pkgdir, 'Contents', 'Resources'),
        update=1, verbose=verbose, dry_run=dry_run,
    )

    copy_doc(readme, 'ReadMe', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(license, 'License', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(welcome, 'Welcome', pkgdir, exts=TEXT_EXTS, verbose=verbose, dry_run=dry_run)
    copy_doc(background, 'Background', pkgdir, exts=IMAGE_EXTS, verbose=verbose, dry_run=dry_run)
