"""
A very crude emulator of dejagnu, just enough to integrate the libbfi 
unittests into the pyobjc ones.
"""
import os
import re
import sys
from fnmatch import fnmatch
import unittest
from distutils.util import get_platform

gDgCommands=re.compile(r'''
        (?:{\s*(dg-do)\s*run\s*({[^}]*})?\s*})
        |
        (?:{\s*(dg-output)\s*"([^"]*)"\s*})
        ''',
            re.VERBOSE|re.MULTILINE)

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

        #print "TODO: run the output if it compiled"
        #print "TODO: check if output equals expected output"

    def shortDescription(self):
        fn = os.path.basename(self.filename)[:-2]
        dn = os.path.basename(os.path.dirname(self.filename))
        return "dejagnu.%s.%s"%(dn, fn)

    def compileTestCase(self):
        libdir = os.path.join('build', 'temp.%s-%d.%d'%(get_platform(), sys.version_info[0], sys.version_info[1]), 'libffi-src')
        libffiobjects = self.object_files(libdir)

        commandline='cc -g -DMACOSX -Ilibffi-src/include -o /tmp/test.bin %s %s 2>&1'%(
                self.filename, ' '.join(libffiobjects))

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
            self.fail("Running failed[%s]"%(xit,))
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
    runner.run(testSuiteForDirectory('libffi-src/testsuite/libffi.call'))
