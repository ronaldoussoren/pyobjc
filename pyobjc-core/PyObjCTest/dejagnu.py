"""
A very crude emulator of dejagnu, just enough to integrate the libbfi 
unittests into the pyobjc ones.
"""
import os
import re
import sys
import signal
import codecs
from fnmatch import fnmatch
import unittest
from distutils.util import get_platform
from distutils.sysconfig import get_config_var

gDgCommands=re.compile(r'''
        (?:{\s*(dg-do)\s*run\s*({[^}]*})?\s*})
        |
        (?:{\s*(dg-output)\s*"([^"]*)"\s*})
        ''',
            re.VERBOSE|re.MULTILINE)

def signame(code):
    for nm in dir(signal):
        if nm.startswith('SIG') and nm[3] != '_' \
                and getattr(signal, nm) == code:
            return nm
    return code

def exitCode2Description(code):
    """
    Convert the exit code as returned by os.popen().close() to a string
    """
    if os.WIFEXITED(code):
        return 'exited with status %s'%(os.WEXITSTATUS(code),)
    
    elif os.WIFSIGNALED(code):
        sig = os.WTERMSIG(code)
        return 'crashed with signal %s [%s]'%(signame(sig), sig)

    else:
        return 'exit code %s'%(code,)

def platform_matches(matchstr):
    # This is a hack
    if sys.byteorder == 'little':
        platform = 'i386-apple-darwin'
    else:
        platform = 'powerpc-apple-darwin'

    return fnmatch(platform, matchstr)

def parseDG(fdata):
    result = []
    for  item in gDgCommands.findall(fdata):
        if item[0] == 'dg-do':
            result.append(('run', item[1]))
        elif item[2] == 'dg-output':
            if sys.version_info[0] == 3:
                value = codecs.decode(item[3], 'unicode_escape')
            else:
                value = item[3].decode('string_escape')
            result.append(('expect', value))

    return result


class DgTestCase (unittest.TestCase):
    def __init__(self, filename):
        unittest.TestCase.__init__(self)
        self.filename = filename

    def runTest(self):
        script = parseDG(open(self.filename).read())
        output = []

        for command, data in script:
            if command == 'run':
                action = 'run'
                action_data = data
            if command == 'expect':
                output.append(data)
        output = ''.join(output)
        output = output.replace('\\', '')

        d = action_data.split()
        if d and d[1] == 'target':
            for item in d[2:]:
                if platform_matches(item):
                    break

            else:
                # Test shouldn't be run on this platform
                return

        # NOTE: We're ignoring the xfail data for now, none of the
        # testcases are supposed to fail on darwin.
        
        self.compileTestCase()
        data = self.runTestCase()

        if output != '':
            self.assertEquals(data.rstrip(), output.rstrip())
        os.unlink('/tmp/test.bin')


    def shortDescription(self):
        fn = os.path.basename(self.filename)[:-2]
        dn = os.path.basename(os.path.dirname(self.filename))
        return "dejagnu.%s.%s"%(dn, fn)

    def compileTestCase(self):
        libdir = os.path.join('build', 'temp.%s-%d.%d'%(get_platform(), sys.version_info[0], sys.version_info[1]))
        if hasattr(sys, 'gettotalrefcount'):
            libdir += "-pydebug"
        libdir = os.path.join(libdir, 'libffi-src')

        libffiobjects = self.object_files(libdir)


        if self.filename.endswith('.m'):
            extra_link = '-framework Foundation'
        else:
            extra_link = ''

        commandline='MACOSX_DEPLPOYMENT_TARGET=%s %s %s -g -DMACOSX -Ilibffi-src/include -Ilibffi-src/powerpc -o /tmp/test.bin %s %s %s 2>&1'%(
                get_config_var('MACOSX_DEPLOYMENT_TARGET'),
                get_config_var('CC'),
                get_config_var('CFLAGS'), self.filename, ' '.join(libffiobjects),
		extra_link)

        fp = os.popen(commandline)
        data = fp.read()
        xit = fp.close()
        if xit != None:
            self.fail("Compile failed[%s]:\n%s"%(xit, data))


    def runTestCase(self):
        os.environ['DYLD_BIND_AT_LAUNCH'] = '1'
        fp = os.popen('/tmp/test.bin', 'r')
        del os.environ['DYLD_BIND_AT_LAUNCH']
        data = fp.read()
        xit = fp.close()
        if xit != None:
            self.fail("Running failed (%s)"%(exitCode2Description(xit),))
        return data


    def object_files(self, basedir):
        result = []
        for dirpath, dirnames, filenames in os.walk(basedir):
            for fn in filenames:
                if fn.endswith('.o'):
                    result.append(os.path.join(dirpath, fn))
        return result
            

def testSuiteForDirectory(dirname):
    tests = []
    for fn in os.listdir(dirname):
        if not fn.endswith('.c') and not fn.endswith('.m'): continue
        tst = DgTestCase(os.path.join(dirname, fn))
        if alltests and tst.shortDescription() not in alltests:
            continue
        tests.append(tst)

    return unittest.TestSuite(tests)


alltests = []
if __name__ == "__main__":
    alltests = sys.argv[1:]
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuiteForDirectory('libffi-src/tests/testsuite/libffi.call'))
