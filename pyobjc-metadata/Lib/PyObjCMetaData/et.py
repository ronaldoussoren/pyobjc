"""
ElementTree tools and imports

NOTE: _escape_attrib and ElementTree._write are copied from the ElementTree
source with minor modifications to generate single-quoted attributes because
that gives more pleasant output for this application.
"""
__all__ = ('ET', 'ElementTree')
import string

try:
    # Python 2.5
    import xml.etree.ElementTree as ET 
except ImportError:
    # And earlier (with separate install)
    try:
        import cElementTree as ET

    except ImportError:
        import elementtree.ElementTree as ET

def _escape_attrib(text, encoding=None, replace=string.replace):
    # escape attribute value
    try:
        if encoding:
            try:
                text = ET._encode(text, encoding)
            except UnicodeError:
                return ET._encode_entity(text)
        text = replace(text, "&", "&amp;")
        text = replace(text, "'", "&apos;") 
        #text = replace(text, "\"", "&quot;")
        text = replace(text, "<", "&lt;")
        text = replace(text, ">", "&gt;")
        return text
    except (TypeError, AttributeError):
        ET._raise_serialization_error(text)

class ElementTree (ET.ElementTree):
    """
    A subclass of ET.ElementTree that overrides the _write method to get
    a nicer output with single-quoted attributes (because our output contains
    attribute values with embedded double-quotes).
    """

    def _write(self, file, node, encoding, namespaces):
        # write XML to file
        tag = node.tag
        if tag is ET.Comment:
            file.write("<!-- %s -->" % ET._escape_cdata(node.text, encoding))
        elif tag is ET.ProcessingInstruction:
            file.write("<?%s?>" % ET._escape_cdata(node.text, encoding))
        else:
            items = node.items()
            xmlns_items = [] # new namespaces in this scope
            try:
                if isinstance(tag, ET.QName) or tag[:1] == "{":
                    tag, xmlns = ET.fixtag(tag, namespaces)
                    if xmlns: xmlns_items.append(xmlns)
            except TypeError:
                ET._raise_serialization_error(tag)
            file.write("<" + ET._encode(tag, encoding))
            if items or xmlns_items:
                items.sort() # lexical order
                for k, v in items:
                    try:
                        if isinstance(k, ET.QName) or k[:1] == "{":
                            k, xmlns = ET.fixtag(k, namespaces)
                            if xmlns: ET.xmlns_items.append(xmlns)
                    except TypeError:
                        ET._raise_serialization_error(k)
                    try:
                        if isinstance(v, ET.QName):
                            v, xmlns = ET.fixtag(v, namespaces)
                            if xmlns: xmlns_items.append(xmlns)
                    except TypeError:
                        ET._raise_serialization_error(v)
                    file.write(" %s=\'%s\'" % (ET._encode(k, encoding),
                                               _escape_attrib(v, encoding)))
                for k, v in xmlns_items:
                    file.write(" %s=\'%s\'" % (ET._encode(k, encoding),
                                               _escape_attrib(v, encoding)))
            if node.text or len(node):
                file.write(">")
                if node.text:
                    file.write(ET._escape_cdata(node.text, encoding))
                for n in node:
                    self._write(file, n, encoding, namespaces)
                file.write("</" + ET._encode(tag, encoding) + ">")
            else:
                file.write(" />")
            for k, v in xmlns_items:
                del namespaces[v]
        if node.tail:
            file.write(ET._escape_cdata(node.tail, encoding))
