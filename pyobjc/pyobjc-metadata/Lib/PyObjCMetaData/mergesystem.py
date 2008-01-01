#!/usr/bin/env python
"""
This script merges information from the system's BridgeSupport.xml documents
into our own exception files.

NOTE: This is mostly for bootstrapping, in the long run our own metadata 
should be at least as good as the system version.

XXX: also have to to verify the output of the merger, some CF metadata seems
dodgy to me (either that or metadata for Tiger and Leopard will be incompatible)
"""
from PyObjCMetaData.et import *
import sys
from scanframework import indentET, HEADER

def find_node(root, type, name):
    for node in root.findall(type):
        if node.get('name') == name:
            return node
    return None


gExceptionAttributes = dict(
    struct = [ 'type', 'type64' ],

    retval = [ 
            'type', 'type64', 
            'already_retained' 
            'c_array_length_in_arg',
            'c_array_of_fixed_length',
            'c_array_delimited_by_null',
            'c_array_delimited_by_arg', # XXX: currently used in rubycocoa
        ],
    argument = [ 
            'type', 'type64', 
            'type_modifier', 
            'null_accepted', 
            'c_array_length_in_arg',
            'c_array_delimited_by_arg', # XXX: currently used in rubycocoa
            'c_array_of_fixed_length',
            'c_array_delimited_by_null',
            'printf_format',
        ],

    cftype = [ 'gettypeid_func', 'tollfree', ],

    method = [ 'suggestion' ],
)
gExceptionAttributes[None] = [ 'ignore', 'comment' ]

def have_meta(node):
    for attrname in gExceptionAttributes.get(None, ()):
        value = node.get(attrname)
        if value:
            return True

    for attrname in gExceptionAttributes.get(node.tag, ()):
        value = node.get(attrname)
        if value:
            return True
    return False

def copy_meta(dst, src):
    if src is None:
        return

    for attrname in gExceptionAttributes.get(None, ()):
        value = src.get(attrname)
        if value:
            dst.set(attrname, value)

    for attrname in gExceptionAttributes.get(dst.tag, ()):
        value = src.get(attrname)
        if value:
            dst.set(attrname, value)

def main():
    framework = sys.argv[1]
    exceptions = sys.argv[2]

    sysmeta = ET.parse(framework).getroot()
    exception = ET.parse(exceptions).getroot()

    for node in sysmeta.findall('cftype'):
        nm = node.get('name')
        exc = find_node(exception, 'cftype', nm)
        if exc is None:
            exc = find_node(exception, 'opaque', nm)
            if exc is not None:
                exc.tag = 'cftype'
            else:
                exc = ET.SubElement(exception, 'cftype', name=nm)
        copy_meta(exc, node)

    for node in sysmeta.findall('opaque'):
        nm = node.get('name')
        exc = find_node(exception, 'opaque', nm)
        if exc is None:
            exc = find_node(exception, 'cftype', nm)
            if exc is not None:
                exc.tag = 'opaque'
            else:
                exc = ET.SubElement(exception, 'opaque', name=nm)
        copy_meta(exc, node)

    for node in sysmeta.findall('function'):
        copy = False
        for child in node:
            if have_meta(child):
                copy = True
                break

        if copy:
            exc = find_node(exception, 'function', function.get('name'))
            if not exc:
                exc = ET.SubElement(exception, 'function', name=function.get('name'))
            copy_meta(exc, node)

            argIdx = 0
            for child in node:
                if not have_meta(child):
                    if child.tag == 'argument':
                        argIdx += 1
                    continue

                if child.tag == 'retval':
                    try:
                        e = iter(exc.findall('retval')).next()
                    except:
                        e = ET.SubElement(exc, 'retval')
                    copy_meta(e, child)

                if child.tag == 'argument':
                    for e in exc.findall('argument'):
                        if int(e.get('index')) == argIdx:
                            break
                    else:
                        e = ET.SubElement(exc, 'argument', index=str(argIdx))
                    copy_meta(e, child)

    for node in sysmeta.findall('class'):
        for method in node.findall('method'):
            copy = have_meta(method)
            for child in method:
                if have_meta(child):
                    copy = True
                    break

            if copy:
                clsExc = find_node(exception, 'class', node.get('name'))
                
                for methodExc in clsExc.findall('method'):
                    if methodExc.get('selector') == method.get('selector'):
                        break
                else:
                    methodExc = ET.SubElement(clsExc, 'method', selector=method.sget('selector'))

                for child in method:
                    if not have_meta(child):
                        continue

                    if child.tag == 'retval':
                        try:
                            e = iter(methodExc.findall('retval')).next()
                        except:
                            e = ET.SubElement(methodExc, 'retval')
                        copy_meta(e, child)

                    if child.tag == 'argument':
                        for e in exc.findall('argument'):
                            if e.get('index') == chid.get('index'):
                                break
                        else:
                            e = ET.SubElement(exc, 'argument', index=child.get('index'))
                        copy_meta(e, child)

    indentET(exception)
    tree = ElementTree(exception)

    fp = open(sys.argv[2], 'w')
    print >>fp, HEADER
    tree.write(fp)
    fp.write('\n')
    fp.close()

if __name__ == "__main__":
    main()
