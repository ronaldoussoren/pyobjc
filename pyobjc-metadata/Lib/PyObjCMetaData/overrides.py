"""
Create a PyObjCOverrides.bridgesupport file

This script creates a bridgesupport file that covers the deficiencies in system
metadata from said metadata and the normal PyObjC bridgesupport file.
"""
from PyObjCMetaData.et import *
import objc, sys, os, optparse
from scanframework import indentET, HEADER

def system_metadata_for(framework):
    """
    Return the path to the metadata file in a given framework
    """
    root = '/System/Library/Frameworks/%s.framework'%(framework,)
    if os.path.exists(root):
        p = os.path.join(root, 'Resources/BridgeSupport/%s.bridgesupport'%(
            framework,))
        if os.path.exists(p):
            return p
        else:
            return None

    for fwk in os.listdir('/System/Library/Frameworks'):
        root = '/System/Library/Framework/%s/Frameworks/%s.framework'%(
                fwk, framework)
        if os.path.exists(root):
            p = os.path.join(root, 'Resources/BridgeSupport/%s.bridgesupport'%(
                framework,))
            if os.path.exists(p):
                return p
            else:
                return None

    return None

def find_node(root, type, name, nameAttr='name'):
    for node in root.findall(type):
        if node.get(nameAttr) == name:
            return node
    return None

def copySimple(overrides, pyobjc, system, element):
    for p in pyobjc.findall(element):
        s = find_node(system, element, p.get('name'))
        if s is None or p.attrib != s.attrib:
            o = ET.SubElement(overrides, element)
            for k,v in p.attrib.items():
                o.set(k, v)

def copyFunction(overrides, pyobjc, system):
    if len(system.getchildren()) != len(pyobjc.getchildren()):
        overrides.append(pyobjc)
        return

    p = list(pyobjc.findall('retval'))
    s = list(system.findall('retval'))
    if len(p) != len(s):
        overrides.append(pyobjc)
        return

    if p:
        if p[0].attrib != s[0].attrib:
            overrides.append(pyobjc)
            return

    p = list(pyobjc.findall('arg'))
    s = list(system.findall('arg'))
    if len(p) != len(s):
        overrides.append(pyobjc)

    for arg_p, arg_s in zip(p, s):
        if arg_p.attrib != arg_s.attrib:
            overrides.append(pyobjc)
            return


def copyFunctionList(overrides, pyobjc, system):
    for p in pyobjc.findall('function'):
        s = find_node(system, 'function', p.get('name'))
        if s is None:
            overrides.append(p) 

        else:
            copyFunction(overrides, p, s)

def copyProtocol(overrides, pyobjc, system):
    classNode = None

    for p in pyobjc.findall('method'):
        s = find_node(system, 'method', p.get('selector'), nameAttr='selector')
        if s is None or p.attrib != s.attrib:
            if classNode is None:
                classNode = ET.SubElement(overrides, 'class', 
                        name=pyobjc.get('name'))
            classNode.append(p)
            continue

def copyInformalProtocolList(overrides, pyobjc, system):
    for p in pyobjc.findall('informal_protocol'):
        s = find_node(system, 'informal_protocol', p.get('name'))
        if s is None:
            overrides.append(p)
            continue

        copyProtocol(overrides, p, s)

def copyClass(overrides, pyobjc, system):
    classNode = None

    for p in pyobjc.findall('method'):
        s = find_node(system, 'method', p.get('selector'), nameAttr='selector')
        if s is None or p.attrib != s.attrib:
            if classNode is None:
                classNode = ET.SubElement(overrides, 'class', 
                        name=pyobjc.get('name'))
            classNode.append(p)
            continue
        
        retval_p = list(p.findall('retval'))
        retval_s = list(s.findall('retval'))

        arg_p = list(p.findall('arg'))
        arg_s = list(s.findall('arg'))

        if (retval_p == []) != (retval_s == []):
            if classNode is None:
                classNode = ET.SubElement(overrides, 'class', 
                        name=pyobjc.get('name'))
            classNode.append(p)
            continue

        if len(arg_p) != len(arg_s):
            if classNode is None:
                classNode = ET.SubElement(overrides, 'class', 
                        name=pyobjc.get('name'))
            classNode.append(p)
            continue

        for a_p, a_s in zip(arg_p, arg_s):
            if a_p.attrib != a_s.attrib:
                if classNode is None:
                    classNode = ET.SubElement(overrides, 'class', 
                            name=pyobjc.get('name'))
                classNode.append(p)
                continue

def copyClassList(overrides, pyobjc, system):
    for p in pyobjc.findall('class'):
        s = find_node(system, 'class', p.get('name'))
        if s is None:
            overrides.append(p)
            continue

        copyClass(overrides, p, s)


def main():
    parser = optparse.OptionParser(version="%prog 0.1")
    parser.add_option("-o", "--output-file", dest="outfile", metavar="FILE",
            help="write output to this file")
    parser.add_option("-p", "--pyobjc-metadata", dest="pyobjc", metavar="FILE",
            help="pyobjc metadata source file")
    parser.add_option("-s", "--system-metadata", dest="system", metavar="FILE",
            help="system metadata source file")
    parser.add_option("-F", "--framework", dest="framework", metavar="NAME",
                   help="use given framework")

    options, args = parser.parse_args()
    if args:
        parser.error("incorrect number of arguments")

    if options.framework is not None and options.system is not None:
        parser.error("Supply either -F or -s, not both")

    if options.system is None and options.framework is None:
        parser.error("no system metadata specified")

    if options.framework is not None:
        options.system = system_metadata_for(options.framework)

    if options.outfile is None:
        parser.error("-o is required")

    if options.pyobjc is None:
        parser.error("-p is required")

    elif not os.path.exists(options.pyobjc):
        parser.error("-p: file doesn't exist")


    elif options.system is None:
        # No system metadata at all, just copy all metadata
        data = open(options.pyobjc, 'rb').read()
        fp = open(options.outfile + '~', 'wb')
        fp.write(data)
        fp.close()
        os.rename(options.outfile + '~', options.outfile)

    else:
        system = ET.parse(options.system).getroot()
        pyobjc = ET.parse(options.pyobjc).getroot()
        overrides = ET.Element('signatures', version='1.0')

        for elt in (
            'struct', 'cftype', 'opaque', 'constant', 
            'string_constant', 'enum', 'null_constant' ):

            copySimple(overrides, pyobjc, system, elt)

        copyFunctionList(overrides, pyobjc, system)
        copyInformalProtocolList(overrides, pyobjc, system)
        copyClassList(overrides, pyobjc, system)


        if len(overrides.getchildren()) != 0:
            fp = open(options.outfile + '~', 'wb')
            print >>fp, HEADER
            indentET(overrides)
            tree = ElementTree(overrides)
            tree.write(fp)
            fp.write('\n')
            fp.close()
            os.rename(options.outfile + '~', options.outfile)
        else:
            if os.path.exists(options.outfile):
                os.unlink(options.outfile)

if __name__ == "__main__":
    main()
