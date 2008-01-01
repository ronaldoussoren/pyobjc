import os
import distutils.sysconfig

def main():
    basepath = os.path.dirname(__file__)
    builddir = os.path.join(basepath, 'prebuilt')
    if not os.path.exists(builddir):
        os.makedirs(builddir)
    dest = os.path.join(builddir, 'main')
    src = os.path.join(basepath, 'src', 'main.m')
    if not os.path.exists(dest) or os.stat(dest).st_mtime < os.stat(src).st_mtime:
        cfg = distutils.sysconfig.get_config_vars()
        CC = cfg['CC']
        CFLAGS = cfg['CFLAGS'].replace(' -dynamic', '')
        LDFLAGS = cfg['LDFLAGS'] + ' -bundle -framework Foundation -framework AppKit'

        #CC = os.environ.get("CC", "cc")
        #CFLAGS = '-Os -Wall'
        #LDFLAGS = '-g -bundle -framework Foundation -framework AppKit'
        os.system('"%(CC)s" -o "%(dest)s" "%(src)s" %(CFLAGS)s %(LDFLAGS)s' % locals())
        os.system('strip -Sx "%(dest)s"' % locals())
    return dest

if __name__ == '__main__':
    main()
