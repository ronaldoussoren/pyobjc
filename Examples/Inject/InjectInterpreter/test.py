import sys
import os
import objc
if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit, "%s: You must specify the pid of a process to inject PyInterpreter into" % (sys.argv[0],)
    interp = os.path.abspath('dist/PyInterpreter.plugin/Contents/MacOS/PyInterpreter')
    if not os.path.exists(interp):
        if os.spawnl(os.P_WAIT, sys.executable, sys.executable, 'setup.py', 'py2app', '-A'):
            raise SystemExit, "Could not build PyInterpreter plugin?"
    objc.inject(int(sys.argv[1]), interp)
