import sys
from subprocess import Popen, PIPE
from distutils.errors import DistutilsExecError
def runtasks(taskName, *commands, **kw):
    print "Performing task: %s" % (taskName,)
    for cmd in commands:
        print ' '.join(cmd)
        process = Popen(cmd, stdout=PIPE, stderr=PIPE, **kw)
        stdout, stderr = process.communicate()
        res = process.wait()
        if res:
            for err in stderr:
                sys.stderr.write(err)
            raise DistutilsExecError("Task %r failed [%d]" % (taskName, res))
