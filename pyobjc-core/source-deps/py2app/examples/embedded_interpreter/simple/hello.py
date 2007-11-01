import sys, os
import pprint

def somefunc():
    print "Hello from py2app"

    print "frozen", repr(getattr(sys, "frozen", None))

    import __main__
    print __main__.__file__
    print "sys.path", sys.path
    print "sys.executable", sys.executable
    print "sys.prefix", sys.prefix
    print "sys.argv", sys.argv
    print "os.getcwd()", os.getcwd()
    pprint.pprint(dict(os.environ))

def innerbundle():
    import site
    import os
    site.addsitedir(os.path.expanduser('~/Library/Python/2.3/site-packages'))
    print '------------------------'
    somefunc()
    from AppKit import NSBeep
    NSBeep()

if __name__ == '__main__':
    if not sys.argv[1:]:
        somefunc()
        os.spawnv(os.P_WAIT, sys.executable, [sys.executable, __file__, 'arg'])
    else:
        innerbundle()
