#!/usr/bin/env python
"""
Report about the differences in two metadata files.

The script is incomplete at the moment: it doesn't look inside nested
elements yet (function, class, informal_protocol).
"""
from PyObjCMetaData.et import *
import objc
import sys
import os
from scanframework import indentET, HEADER

def find_node(root, type, name, nameAttr='name'):
    for node in root.findall(type):
        if node.get(nameAttr) == name:
            return node
    return None

def filter64(value):
    result = {}
    for k in value:
        if k.endswith('64'): continue
        result[k] = value[k]

    # Make sure all irrelavant bits of the signature string get ignored
    if 'type' in value:
        result['type'] = ''.join(objc.splitSignature(value['type']))

    return result

def diffDict(first, second):
    first = filter64(first)
    second = filter64(second)
    result = []
    for k in sorted(first):
        if k not in second:
            result.append('<%s'%(k,))
        elif first[k] != second[k]:
            result.append('!%s[%s!=%s]'%(k, first[k], second[k]))
    for k in sorted(second):
        if k.endswith('64'): 
            # Ignore 64-bit variants for now
            continue
        if k not in first:
            result.append('>%s'%(k,))
    return ' '.join(result)

def diffSimple(first, second, tag):
    for f in first.findall(tag):
        s = find_node(second, tag, f.get('name'))
        if s is None:
            print "< %s %s"%(tag, f.get('name'))
        elif filter64(f.attrib)  != filter64(s.attrib):
            print "! %s %s"%(tag, f.get('name'))
            print "  ", diffDict(f.attrib, s.attrib)
    for s in second.findall(tag):
        f = find_node(first, tag, s.get('name'))
        if f is None:
            print "> %s %s"%(tag, s.get('name'))


def diffFunction(first, second, prefix='function', nameAttr='name'):
    if filter64(first.attrib) != filter64(second.attrib):
        print '! %s %s'%(prefix, first.get(nameAttr))
        print '  ', diffDict(first.attrib, second.attrib)

    f_r = None
    f_a = []
    s_r = None
    s_a = []

    for n in first:
        if n.tag == 'retval':
            if f_r is not None:
                print '** < %s.retval duplicate for %s'%(prefix, first.get(nameAttr))
            f_r = n
        elif n.tag == 'arg':
            f_a.append(n)

        else:
            print '** < %s.%s for %s: unknown tag'%(prefix, n.tag, first.get(nameAttr))

    for n in second:
        if n.tag == 'retval':
            if s_r is not None:
                print '** > %s.retval duplicate for %s'%(prefix, second.get(nameAttr))
            s_r = n
        elif n.tag == 'arg':
            s_a.append(n)

        else:
            print '** < %s.%s for %s: unknown tag'%(prefix, n.tag, first.get(nameAttr))

    if f_r is None:
        if s_r is not None and (s_r.get('type') != objc._C_VOID or len(s_r.attrib) != 1):
                print '> %s.retval %s'%(prefix, first.get(nameAttr))
    else:
        if s_r is None and (f_r.get('type') != objc._C_VOID or len(f_r.attrib) != 1):
                print '> %s.retval %s'%(prefix, first.get(nameAttr))
        elif s_r is not None:
            if filter64(s_r.attrib) != filter64(f_r.attrib):
                print '! %s.retval %s'%(prefix, first.get(nameAttr))
                print '  ', diffDict(f_r.attrib, s_r.attrib)

    for idx in range(max(len(f_a), len(s_a))):
        try:
            f = f_a[idx]
        except IndexError:
            f = None

        try:
            s = s_a[idx]
        except IndexError:
            s = None

        if s is None:
            print '< %s.argument[%d] %s'%(prefix, idx, first.get(nameAttr))
        elif f is None:
            print '> %s.argument[%d] %s'%(prefix, idx, first.get(nameAttr))
        else:
            if f.attrib != s.attrib:
                print '! %s.argument[%d] %s'%(prefix, idx, first.get(nameAttr))
                print '  ', diffDict(f.attrib, s.attrib)

def diffFunctionList(first, second, tag, nameAttr='name', prefix=None):
    if prefix is None:
        prefix = tag
    for f in first.findall(tag):
        s = find_node(second, tag, f.get(nameAttr), nameAttr=nameAttr)
        if s is None:
            print "< %s %s"%(prefix, f.get(nameAttr))
        else:
            diffFunction(f, s, prefix, nameAttr)
    for s in second.findall(tag):
        f = find_node(first, tag, s.get(nameAttr), nameAttr=nameAttr)
        if f is None:
            print "> %s %s"%(prefix, s.get(nameAttr))

def diffClassList(first, second):
    for f in first.findall('class'):
        s = find_node(second, 'class', f.get('name'))
        if s is None:
            print "< %s %s"%('class', f.get('name'))
        else:
            diffFunctionList(f, s, 'method', nameAttr='selector', prefix='class[%s].method'%(f.get('name')))
    for s in second.findall('class'):
        f = find_node(first, 'class', s.get('name'))
        if f is None:
            print "> %s %s"%('class', s.get('name'))

def diffProtocolList(first, second):
    for f in first.findall('informal_protocol'):
        s = find_node(second, 'informal_protocol', f.get('name'))
        if s is None:
            print "< %s %s"%('informal_protocol', f.get('name'))
        else:
            diffFunctionList(f, s, 'method', nameAttr='selector', prefix='informal_protocol[%s].method'%(f.get('name')))

    for s in second.findall('informal_protocol'):
        f = find_node(first, 'informal_protocol', s.get('name'))
        if f is None:
            print "> %s %s"%('informal_protocol', s.get('name'))

def main():
    if len(sys.argv) == 2:
        fwk = sys.argv[1]
    
        for dirpath, dirnames, filenames in os.walk(os.path.expanduser('~/Projects/pyobjc-leopard/BridgeSupport~dst')):
            if fwk + '.bridgesupport' in filenames:
                first = os.path.join(dirpath, fwk + '.bridgesupport')
                break
        else:
            raise RuntimeError("No Leopard data for %s"%(fwk,))

        second = os.path.join(os.path.expanduser('~'),
                'Projects', 'pyobjc-leopard', 'stable', 'pyobjc-framework-%s'%(fwk),
                'Lib', fwk, 'PyObjC.bridgesupport')

        if not os.path.exists(second):
            test = os.path.join(os.path.expanduser('~'),
                    'Projects', 'pyobjc-leopard', 'stable', 'pyobjc-framework-Cocoa',
                    'Lib', fwk, 'PyObjC.bridgesupport')

            if not os.path.exists(test):
                test = os.path.join(os.path.expanduser('~'),
                        'Projects', 'pyobjc-leopard', 'stable', 'pyobjc-framework-Quartz',
                        'Lib', fwk, 'PyObjC.bridgesupport')

                if os.path.exists(test):
                    second = test

            else:
                second = test

    elif len(sys.argv) == 3:
        first = sys.argv[1]
        second = sys.argv[2]

    else:
            print >>sys.stderr, "Usage: %s orig new"
            sys.exit(1)



    print "Comparing %s and %s"%(first, second)

    first = ET.parse(first).getroot()
    second = ET.parse(second).getroot()

    diffSimple(first, second, 'struct')
    diffSimple(first, second, 'cftype')
    diffSimple(first, second, 'opaque')
    diffSimple(first, second, 'constant')
    diffSimple(first, second, 'string_constant')
    diffSimple(first, second, 'enum')
    diffFunctionList(first, second, 'function')
    diffFunctionList(first, second, 'static_inline')
    diffClassList(first, second)
    diffProtocolList(first, second)


if __name__ == "__main__":
    main()
