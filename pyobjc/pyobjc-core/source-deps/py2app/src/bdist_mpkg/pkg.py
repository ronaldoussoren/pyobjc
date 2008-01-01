import os, sys
import tools, plists
from StringIO import StringIO
from py2app.util import copy_tree
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

def copy_doc(path, name, pkgdir, exts=TEXT_EXTS, language=None, dry_run=0, copy_tree=copy_tree, copy_file=copy_file, mkpath=mkpath):
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
    mkpath(destdir)
    dest = os.path.join(destdir, name+ext)
    if is_string:
        if not dry_run:
            f = file(dest, 'wb')
            f.write(path.getvalue())
            f.close()
    elif ext == '.rtfd':
        copy_tree(path, dest)
    else:
        copy_file(path, dest)

def make_metapackage(cmd, name, version, packages, pkgdir, info=(), description=None):
    license = cmd.license
    readme = cmd.readme
    welcome = cmd.welcome
    background = cmd.background
    template = cmd.template
    dry_run = cmd.dry_run
    dist = cmd.distribution
    copy_tree = cmd.copy_tree
    copy_file = cmd.copy_file
    mkpath = cmd.mkpath

    if description is None:
        description = dist.get_description()
    if not description:
        description = u'%s %s' % (name, version)

    mkpath(os.path.join(pkgdir, 'Contents', 'Resources'))
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
    )

    if readme is None:
        readme_text = dist.get_long_description()
        if readme_text:
            readme = StringIO(readme_text)

    def doc(path, name, exts=TEXT_EXTS):
        copy_doc(path, name, pkgdir, exts=exts, dry_run=dry_run,
            mkpath=mkpath, copy_tree=copy_tree, copy_file=copy_file,
        )

    doc(readme, 'ReadMe')
    doc(license, 'License')
    doc(welcome, 'Welcome')
    doc(background, 'Background', exts=IMAGE_EXTS)

def make_package(cmd, name, version, files, common, prefix, pkgdir, info=(), description=None):
    license = cmd.license
    readme = cmd.readme
    welcome = cmd.welcome
    background = cmd.background
    template = cmd.template
    dry_run = cmd.dry_run
    dist = cmd.distribution
    copy_tree = cmd.copy_tree
    copy_file = cmd.copy_file
    mkpath = cmd.mkpath

    if description is None:
        description = dist.get_description()

    mkpath(os.path.join(pkgdir, 'Contents', 'Resources'))
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
    )

    def doc(path, name, exts=TEXT_EXTS):
        copy_doc(path, name, pkgdir, exts=exts, dry_run=dry_run,
            mkpath=mkpath, copy_tree=copy_tree, copy_file=copy_file,
        )

    doc(readme, 'ReadMe')
    doc(license, 'License')
    doc(welcome, 'Welcome')
    doc(background, 'Background', exts=IMAGE_EXTS)
