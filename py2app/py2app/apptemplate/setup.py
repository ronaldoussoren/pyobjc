import os
import distutils.sysconfig

def main():
    basepath = os.path.dirname(__file__)
    builddir = os.path.join(basepath, 'prebuilt')
    if not os.path.exists(builddir):
        os.makedirs(builddir)
    dest = os.path.join(builddir, 'main')
    src = os.path.join(basepath, 'src', 'main.c')
    if not os.path.exists(dest) or (
            os.stat(dest).st_mtime < os.stat(src).st_mtime):
        cfg = distutils.sysconfig.get_config_vars()
        CC = cfg['CC']
        CFLAGS = cfg['CFLAGS'].replace(' -dynamic', '')
        os.system('"%(CC)s" -o "%(dest)s" "%(src)s" %(CFLAGS)s' % locals())
        #os.system('strip "%(dest)s"' % locals())
    return dest

if __name__ == '__main__':
    main()
