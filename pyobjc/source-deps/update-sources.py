#!/usr/bin/env python
import os, sys, shutil
try:
    set
except NameError:
    from sets import Set as set

# update the out-of-tree source distribution dependencies from CVS
# but don't clobber any local version control

CVS_TOOL = '/usr/bin/cvs'
SVN_TOOL = '/usr/local/bin/svn'
SOURCES = {
    'DocArticle': (CVS_TOOL, '-d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/docutils', 'export', '-r', 'HEAD', '-d', 'DocArticle_export', 'sandbox/bbum/DocArticle'),
    'subprocess': (CVS_TOOL, '-d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/python', 'export', '-r', 'HEAD', '-d', 'subprocess_export', 'python/dist/src/Lib/subprocess.py'),
    #'py2app': (SVN_TOOL, 'export', 'http://svn.red-bean.com/bob/py2app/trunk', 'py2app_export'),
}

def spawn(cmd, *args):
    return os.spawnv(os.P_WAIT, cmd, [cmd]+list(args))

def walker(path, ignores=set(('CVS', '.svn'))):
    skiplen = len(os.path.join(path, ''))
    for root, dirs, files in os.walk(path):
        root = root[skiplen:]
        if root:
            yield root
        for ignore in ignores:
            if ignore in dirs:
                dirs.remove(ignore)
            if ignore in files:
                files.remove(ignore)
        for fn in files:
            yield os.path.join(root, fn)
        
def update_source(name, command, update):
    export = name+'_export'
    shutil.rmtree(export, ignore_errors=True)
    res = spawn(*command)
    if res:
        print 'update of source %s failed with an exit code of %d' % (name, res)
        shutil.rmtree(export, ignore_errors=True)
        return False
    orig = set(walker(name))
    new  = set(walker(export))
    added = list(new - orig)
    added.sort()
    removed = list(orig - new)
    removed.sort()
    removed.reverse()
    new = list(new)
    new.sort()
    if update:
        do_svn_rm = []
        for fn in removed:
            fn = os.path.join(name, fn)
            if not os.path.exists(fn):
                continue
            elif os.path.isdir(fn) and not os.path.exists(os.path.join(fn, '.svn')):
                print 'removing unversioned %s' % (fn,)
                shutil.rmtree(fn, ignore_errors=True)
            else:
                do_svn_rm.append(fn)
        if do_svn_rm:
            spawn(SVN_TOOL, 'delete', '--force', *do_svn_rm)
    else:
        for fn in removed:
            fn = os.path.join(name, fn)
            try:
                if os.path.isdir(fn):
                    shutil.rmtree(fn, ignore_errors=True)
                else:
                    os.unlink(fn)
            except:
                print 'could not remove %s' % (fn,)
    for fn in new:
        src = os.path.join(export, fn)
        dest = os.path.join(name, fn)
        if os.path.isdir(src):
            try:
                os.makedirs(dest)
            except:
                pass
        else:
            shutil.copy2(src, dest)
            
    if update and added:
        spawn(SVN_TOOL, 'add', *[os.path.join(name, fn) for fn in added])
    shutil.rmtree(export, ignore_errors=True)

if __name__ == '__main__':
    if '-svn' in sys.argv:
        update=True
        sys.argv.remove('-svn')
    else:
        update=False
    for key in (sys.argv[1:] or SOURCES):
        update_source(key, SOURCES[key], update)
