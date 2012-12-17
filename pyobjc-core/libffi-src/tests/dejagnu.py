#!/usr/bin/python
"""
A very crude emulator of dejagnu, just enough to integrate the libbfi
unittests into the pyobjc ones.
"""
import os
import re
import sys
import signal
from fnmatch import fnmatch
import unittest
from distutils.util import get_platform

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
            result.append(('expect', item[3].decode('string_escape')))
    return result


class DgTestCase (unittest.TestCase):
    def __init__(self, filename):
        unittest.TestCase.__init__(self)
        self.filename = filename

    #archOption = "-arch ppc"
    #archOption = "-arch ppc64"
    #archOption = "-arch i386"
    archOption = "-arch x86_64"
    #archOption = ""
    compileOptionsBase = "-g -DMACOSX -Iinclude -o /tmp/test.bin -lffi"
    compileOptionsList = ( # HACK ALERT: Yes, there are better ways to do this, but this is easy and extremely flexible
        "%s %s %s" % (compileOptionsBase, archOption, "-O0"),
        "%s %s %s" % (compileOptionsBase, archOption, "-O1"),
        "%s %s %s" % (compileOptionsBase, archOption, "-O2"),
        "%s %s %s" % (compileOptionsBase, archOption, "-O3"),
        "%s %s %s" % (compileOptionsBase, archOption, "-Os"),
        "%s %s %s" % (compileOptionsBase, archOption, "-Oz"),  # Note: Apple-Only, see gcc man page for details
        )
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

        for compileOptions in self.compileOptionsList:
            self.compileTestCase(compileOptions)
            data = self.runTestCase()

            if output != '':
                self.assertEquals(data.rstrip(), output.rstrip())
                os.unlink('/tmp/test.bin')


    def shortDescription(self):
        fn = os.path.basename(self.filename)[:-2]
        dn = os.path.basename(os.path.dirname(self.filename))
        return "dejagnu.%s.%s"%(dn, fn)

    def compileTestCase(self, compileOptions):
        # libdir = os.path.join('build', 'temp.%s-%d.%d'%(get_platform(), sys.version_info[0], sys.version_info[1]), 'libffi-src')
        # libffiobjects = self.object_files(libdir)

        commandline='cc %s %s 2>&1' % (compileOptions, self.filename)
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
        if not fn.endswith('.c'): continue
        tst = DgTestCase(os.path.join(dirname, fn))
        if alltests and tst.shortDescription() not in alltests:
            continue
        tests.append(tst)

    return unittest.TestSuite(tests)

alltests = []
if __name__ == "__main__":
    alltests = sys.argv[1:]
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testSuiteForDirectory('tests/testsuite/libffi.call'))
