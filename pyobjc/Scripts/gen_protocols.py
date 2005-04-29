#!/usr/bin/env python

"""This script/module generate Python code that defines (informal) protocols
by parsing header files from frameworks. It is used bu gen_all_protocols.py,
but can also be used separately, in which case you invoke it like this:

    ./gen_protocols.py <full_path_to_a_framework> > <outputfile>.py
"""

import sys
import os
import glob
import re
import objc

protoRE = re.compile(r"\n@interface\s+NSObject\s*\((.*?)\)|\n@protocol\s+(\w+)")

typeRE = re.compile(r"\s*\((oneway|in|out|inout|bycopy|byref)?\b\s*([^)]+)\)\s*")
selPartRE = re.compile(r"(\w+:?)\s*")
argNameRE = re.compile(r"(\w+)\s*")

def getSelector(line):
    types = []
    selParts = []
    m = typeRE.match(line)
    assert m is not None, "can't parse return type in {%s}" % line
    types.append(m.group(2).strip())
    pos = m.end()
    while 1:
        m = selPartRE.search(line, pos)
        if m is None:
            break
        part = m.group(1)
        selParts.append(part)
        if part[-1] != ":":
            break
        pos = m.end()
        m = typeRE.match(line, pos)
        if m is None and line[pos].isalpha():
            types.append('id')
        else:
            assert m is not None, "can't parse arg type"
            types.append(m.group(2).strip())
            pos = m.end()
        m = argNameRE.match(line, pos)
        assert m is not None, "can't parse arg name"
        pos = m.end()
    return "".join(selParts), types


def parseHeader(headerPath):
    header = file(headerPath).read()
    pos = 0
    protocols = {}
    while 1:
        m = protoRE.search(header, pos)
        if m is None:
            break
        name = m.group(1)
        if name is None:
            # @protocol
            name = m.group(2)
        end = header.find("@end", m.end())

        protocol = []
        rawProto = header[m.end():end]
        start = 0
        while 1:
            instanceStart = rawProto.find("\n- ",start)
            classStart = rawProto.find("\n+ ", start)
            isClass = 0
            if instanceStart < 0:
                if classStart < 0:
                    break
                else:
                    isClass = 1
                    start = classStart
            else:
                if classStart < 0:
                    isClass = 0
                    start = instanceStart
                else:
                    isClass = classStart < instanceStart
                    start = min(instanceStart, classStart)
            selend = rawProto.find(";", start)
            rawSelector = rawProto[start + 3:selend]
            selector, types = getSelector(rawSelector)
            protocol.append((selector, types, " ".join(rawSelector.split()), isClass))
            start = selend + 1
        protocol.sort()
        assert end >= 0
        pos = end + 5
        protocols[name] = protocol
    return protocols


template = r"""
%s
#import <%s/%s.h>
#include <stdio.h>

int main() {
    char *m;

    %s

    return 0;
}
"""

tempSource = "_makeTypeCodes.m"
tempExecutable = "_makeTypeCodes"

def makeTypeCodes(frameworkName, types, frameworkMain=None, extraStuff=""):
    if frameworkMain is None:
        frameworkMain = frameworkName
    lines = []
    keys = types.keys()
    keys.sort()
    for tp in keys:
        lines.append("m = @encode(%s);" % tp)
        lines.append(r'printf("%%s %s\n", m);' % tp)
    source = template % (extraStuff, frameworkName, frameworkMain, "\n    ".join(lines))
    file(tempSource, "w").write(source)
    if os.system("cc -o %s %s" % (tempExecutable, tempSource)):
        assert 0, "compile failed"
    output = os.popen("./" + tempExecutable).read().splitlines()
    assert len(output) == len(types)
    for line in output:
        typeCode, tp = line.split(" ", 1)
        assert tp in types
        types[tp] = typeCode
    # remove these lines when you're debugging:
    os.remove(tempSource)
    os.remove(tempExecutable)


def genProtocols(frameworkPath, outFile=None, specials={}, frameworkMain=None, extraStuff=""):
    """Generate protocol definitions for a framework. If outFile is None,
    the generated Python code will be printed to sys.stdout.
    """
    frameworkPath = os.path.normpath(frameworkPath)
    assert frameworkPath.endswith(".framework")
    frameworkName = os.path.basename(frameworkPath)
    frameworkName = frameworkName.split(".")[0]
    headersPath = os.path.join(frameworkPath, "Headers")
    headers = glob.glob1(headersPath, "*.h")
    allTypes = {}
    allProtocols = {}
    for header in headers:
        protocols = parseHeader(os.path.join(headersPath, header))
        allProtocols.update(protocols)
        items = protocols.items()
        items.sort()
        for protName, selectors in items:
            for sel, types, line, isClass in selectors:
                for tp in types:
                    allTypes[tp] = 0
    makeTypeCodes(frameworkName, allTypes, frameworkMain, extraStuff=extraStuff)
    protocols = allProtocols.items()
    protocols.sort()
    print >> outFile, "# generated from %r" % frameworkPath
    print >> outFile, "import objc as _objc\n\n"
    for protoName, selectors in protocols:
        print >> outFile, '%s = _objc.informal_protocol(' % protoName
        print >> outFile, '    "%s",' % protoName
        print >> outFile, '    ['
        for selector, types, line, isClass in selectors:
            types = [allTypes[tp] for tp in types]
            print >> outFile, "#", line.strip()
            print >> outFile, "        _objc.selector("
            print >> outFile, "            None,"
            print >> outFile, "            selector='%s'," % selector

            if selector in specials:
                print >> outFile, "            signature='%s'," % (specials[selector],)
            else:
                print >> outFile, "            signature='%s'," % (types[0] + "@:" + "".join(types[1:]))
            if isClass:
                print >> outFile, "            isClassMethod=1,"
            print >> outFile, "            isRequired=0,"
            print >> outFile, "        ),"
        print >> outFile, "    ]"
        print >> outFile, ")"
        print >> outFile

if __name__ == "__main__":
    if sys.argv[1:]:
        for frameworkPath in sys.argv[1:]:
            genProtocols(frameworkPath)
    else:
        print __doc__
