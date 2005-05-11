import sys
from subprocess import Popen, PIPE
import select
from distutils.errors import DistutilsExecError
def runtasks(taskName, *commands, **kw):
    print "Performing task: %s" % (taskName,)
    for cmd in commands:
        print ' '.join(cmd)
        process = Popen(cmd, stdout=PIPE, stderr=PIPE, **kw)
        while True:
            try:
                stdout, stderr = process.communicate()
            except select.error:
                continue
            else:
                break
        res = process.wait()
        if res:
            for err in stderr:
                sys.stderr.write(err)
            raise DistutilsExecError("Task %r failed [%d]" % (taskName, res))
