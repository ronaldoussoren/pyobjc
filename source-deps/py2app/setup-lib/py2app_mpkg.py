import os
import sys
from distutils.version import LooseVersion
from distutils import log
from distutils.command.bdist_mpkg import bdist_mpkg as _bdist_mpkg
from py2app.util import copy_tree, skipscm
try:
    set
except NameError:
    from sets import Set as set

JUNK = set(['.DS_Store', '.gdb_history', 'build', 'dist', 'NonFunctional'])
JUNK_EXTS = set(['.pbxuser', '.pyc', '.pyo', '.swp'])
def skipjunk(fn, junk=JUNK, junk_exts=JUNK_EXTS):
    if not skipscm(fn):
        return False
    elif os.path.basename(fn) in junk:
        return False
    elif os.path.splitext(fn)[1] in junk_exts:
        return False
    return True

PREFLIGHT_RM = """#!/usr/bin/env python
import shutil, os
for fn in %(files)r:
    if os.path.isdir(fn):
        shutil.rmtree(fn, ignore_errors=True)
    elif os.path.exists(fn):
        os.unlink(fn)
"""

def run_setup(*args, **kwargs):
    import distutils.core
    d = {
        '_setup_stop_after':None,
        '_setup_distribution':None,
    }
    for k in d:
        d[k] = getattr(distutils.core, k, None)
    try:
        return distutils.core.run_setup(*args, **kwargs)
    finally:
        for k,v in d.iteritems():
            setattr(distutils.core, k, v)
    
def write_preflight_rm(path, files):
    fobj = file(path, 'w')
    fobj.write(PREFLIGHT_RM % dict(files=map(os.path.normpath, files)))
    fobj.close()
    os.chmod(path, 0775)

OSX_VERSION = LooseVersion(os.popen('/usr/bin/sw_vers -productVersion').read().strip())
class bdist_mpkg(_bdist_mpkg):
    def initialize_options(self):
        _bdist_mpkg.initialize_options(self)
        self.preflight_rm = {}
        self.scheme_descriptions.update(dict(
            tools = u'(Optional) py2app tools\nInstalled to: /Developer/Applications/Python Tools/py2app',
            examples = u'(Optional) py2app example code\nInstalled to: /Developer/Python/py2app/Examples',
        ))

    def run_extra(self):
        _bdist_mpkg.run_extra(self)
        self.py2app_platlib_purelib()
        self.py2app_examples()
        self.py2app_tools()

    def scheme_hook(self, scheme, pkgname, version, files, common, prefix, pkgdir):
        _bdist_mpkg.scheme_hook(self, scheme, pkgname, version, files, common, prefix, pkgdir)
        rmfiles = self.preflight_rm.get(scheme)
        if rmfiles is None:
            return
        rmfiles = [os.path.normpath(os.path.join(prefix, fn)) for fn in rmfiles]
        preflight = os.path.join(pkgdir, 'Contents', 'Resources', 'preflight')
        write_preflight_rm(preflight, rmfiles)

    def py2app_platlib_purelib(self):
        for scheme in ('platlib', 'purelib'):
            schemedir = os.path.join(self.pkg_base, scheme)
            if os.path.exists(schemedir):
                self.preflight_rm[scheme] = os.listdir(schemedir)
        
    def py2app_examples(self):
        scheme = 'examples'
        schemedir = os.path.join(self.pkg_base, scheme)
        self.scheme_map[scheme] = '/Developer/Python/py2app/Examples'
        copy_tree('examples', schemedir,
            condition=skipjunk, dry_run=self.dry_run, verbose=self.verbose)
        self.preflight_rm[scheme] = ['.']

    def py2app_tools(self):
        scheme = 'tools'
        schemedir = os.path.abspath(os.path.join(self.pkg_base, scheme))
        builddir = os.path.abspath(os.path.join(self.bdist_base, 'tools'))
        self.scheme_map[scheme] = '/Developer/Applications/Python Tools/py2app'
        for tool in os.listdir('tools'):
            bdist = os.path.join(builddir, tool)
            setupdir = os.path.abspath(os.path.join('tools', tool))
            setup = os.path.join(setupdir, 'setup.py')
            if tool == '.svn' or not os.path.exists(setup):
                continue
            cwd = os.getcwd()
            os.chdir(setupdir)
            old_path = list(sys.path)
            sys.path.insert(0, setupdir)
            args = ['py2app', '--semi-standalone', '--strip', '--dist-dir=' + schemedir, '--bdist-base=' + bdist]
            try:
                run_setup(setup, args)
            finally:
                sys.path[:] = old_path
                os.chdir(cwd)
        self.preflight_rm[scheme] = ['.']

cmdclass = {'bdist_mpkg': bdist_mpkg}
