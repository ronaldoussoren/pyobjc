import os
import sys
import time
import tempfile

SCRIPT = """#!%s
import os
import sys
if os.getuid() and os.geteuid():
    print '''
***

easy_install may need root permission, re-executing under sudo.
You may need to enter your password at the prompt below.

***
'''
    cmd = ['/usr/bin/sudo', sys.executable] + sys.argv
    os.execv(cmd[0], cmd)
os.unlink(sys.argv[0])
sys.argv[1:] = %r
print ''
print '$ easy_install ' + ' '.join(sys.argv[1:])
if __name__ == '__main__':
    from setuptools.command.easy_install import main
    main()
"""

def log(*args):
    print '[EggInstaller]', ' '.join(map(str, args))

def main():
    fd, name = tempfile.mkstemp(suffix='.py', prefix='EggInstaller')
    script = os.fdopen(fd, 'w+b')
    script.write(SCRIPT % (sys.executable, ['--'] + sys.argv[1:]))
    script.flush()
    script.close()
    os.chmod(name, 0700)
    cmd = ['/usr/bin/open', '-a', 'Terminal', name]
    os.spawnv(os.P_WAIT, cmd[0], cmd)
    log('waiting for', name)
    while os.path.exists(name):
        time.sleep(0.1)
    log('done')
    
if __name__ == '__main__':
    main()
