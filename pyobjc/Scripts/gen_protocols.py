#!/usr/bin/env python

"""This script will generate Python code that defines (informal) protocols
byparsing header files from frameworks.

Invoke it like this:
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
    assert line[:2] == "- "
    line = line[2:]
    end = line.find(";")
    assert end > 0
    line = line[:end]
    types = []
    selParts = []
    m = typeRE.match(line)
    assert m is not None, "can't parse return type"
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
        rawProto = header[m.end():end].splitlines()
        for line in rawProto:
            if line.startswith("- "):
                selector, types = getSelector(line)
                protocol.append((selector, types, line))
        protocol.sort()
        assert end >= 0
        pos = end + 5
        protocols[name] = protocol
    return protocols


template = r"""
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

def makeTypeCodes(frameworkName, types):
    lines = []
    keys = types.keys()
    keys.sort()
    for tp in keys:
        lines.append("m = @encode(%s);" % tp)
        lines.append(r'printf("%%s %s\n", m);' % tp)
    source = template % (frameworkName, frameworkName, "\n    ".join(lines))
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


def genProtocol(frameworkPath):
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
            for sel, types, line in selectors:
                for tp in types:
                    allTypes[tp] = 0
    makeTypeCodes(frameworkName, allTypes)
    protocols = allProtocols.items()
    protocols.sort()
    print "# generated from %r" % frameworkPath
    print "import objc as _objc\n\n"
    for protoName, selectors in protocols:
        print '%s = _objc.informal_protocol(' % protoName
        print '    "%s",' % protoName
        print '    ['
        for selector, types, line in selectors:
            types = [allTypes[tp] for tp in types]
            print "#", line.strip()
            print "        _objc.selector("
            print "            None,"
            print "            selector='%s'," % selector
            print "            signature='%s'," % (types[0] + "@:" + "".join(types[1:]))
            print "            isRequired=0,"
            print "        ),"
        print "    ]"
        print ")"
        print

if __name__ == "__main__":
    if sys.argv[1:]:
        for frameworkPath in sys.argv[1:]:
            genProtocol(frameworkPath)
    else:
        print __doc__
