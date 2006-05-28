# Author: Bill Bumgarner
# Contact: bbum@mac.com
# Copyright: 2002 - Bill Bumgarner - All Rights Reserved
# License: The MIT License -- see LICENSE.txt

"""
This is the DocArticle package.

This package provides a writer for DocUtils that spews HTML compliant
with O'Reilly's Dev Center article submission guidelines.
"""

try:
    x = True
except NameError:
    True = 1
    False = 0

__docformat__ = 'reStructuredText'

import sys
from warnings import warn
import re
from types import *

import docutils
from docutils import nodes, utils, writers, languages

from DocArticle import DocArticleText

class DocArticleWriter(writers.Writer):
    supported = ('html',)
    """Formats this writer supports."""

    output = None
    """Final translated form of `document`."""

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = HTMLDocArticleTranslator

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()

SpewNothing = 0
SpewParagraph = 1
SpewBreak = 2
SpewBreakBreak = 3
SpewNothingThenPara = 4

olTypeTranslator = {
    'arabic' : '1',
    'upperalpha' : 'A',
    'loweralpha' : 'a',
    'upperroman' : 'I',
    'lowerroman' : 'i'
    }

class HTMLDocArticleTranslator(nodes.NodeVisitor):
    named_tags = {'a': 1,
                  'applet': 1,
                  'form': 1,
                  'frame': 1,
                  'iframe': 1,
                  'img': 1,
                  'map': 1}

    words_and_spaces = re.compile(r'\S+| +|\n')

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.section_level = 0
        self.headerContent = []
        self.bodyContent = []
        self.bodySuffix = []
        self.metaContent = []
        self.context = []
        self.spewTextContext = [True]
        self.spewParaTag = [SpewParagraph]
        self.paraFormat = [(None,None)]
        self.colspecs = []

        self.body_pre_docinfo = []
        self.docinfo = []
        self.compact_simple = None
        self.compact_p = 1

        self.firstFootnoteVisited = False

        # lcode = settings.language_code
        lcode = 'en'
        self.language = languages.get_language(lcode)

    def astext(self):
        return ''.join([DocArticleText.contentStart, DocArticleText.headerStart] +
                       self.headerContent +
                       [DocArticleText.headerEnd, DocArticleText.bodyStart] +
                       self.body_pre_docinfo + self.docinfo + self.bodyContent + self.bodySuffix +
                       [DocArticleText.bodyEnd, DocArticleText.contentEnd])

    def encode(self, text):
        """Encode special characters in `text` & return."""
        # @@@ A codec to do these and all other HTML entities would be nice.
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('"', '&quot;')
        text = text.replace('>', '&gt;')
        return text

    def popAndAppend(self, node):
        possiblePoppedContent = self.context.pop()
        if possiblePoppedContent:
            self.bodyContent.append(possiblePoppedContent)

    def attval(self, text,
               whitespace=re.compile('[\n\r\t\v\f]')):
        """Cleanse, HTML encode, and return attribute value text."""
        return self.encode(whitespace.sub(' ', text))

    def emptytag(self, node, tagname, suffix='\n', **attributes):
        """Construct and return an XML-compatible empty tag."""
        return self.starttag(node, tagname, suffix, infix=' /', **attributes)

    def starttag(self, node, tagname, suffix='\n', infix='', **attributes):
        tagname = tagname.lower()
        atts = {}
        for (name, value) in attributes.items():
            atts[name.lower()] = value
        for att in ('id',):             # node attribute overrides
            if node.has_key(att):
                atts[att] = node[att]
        if atts.has_key('id') and self.named_tags.has_key(tagname):
            atts['name'] = atts['id']   # for compatibility with old browsers
        attlist = atts.items()
        attlist.sort()
        parts = [tagname]
        for name, value in attlist:
            if value is None:           # boolean attribute
                # According to the HTML spec, ``<element boolean>`` is good,
                # ``<element boolean="boolean">`` is bad.
                # (But the XHTML (XML) spec says the opposite.  <sigh>)
                parts.append(name.lower())
            elif isinstance(value, ListType):
                values = [str(v) for v in value]
                parts.append('%s="%s"' % (name.lower(),
                                          self.attval(' '.join(values))))
            else:
                parts.append('%s="%s"' % (name.lower(),
                                          self.attval(str(value))))
        return '<%s%s>%s' % (' '.join(parts), infix, suffix)

    def visit_Text(self, node):
        if self.spewTextContext[-1]:
            self.bodyContent.append(self.encode(node.astext()))

    def depart_Text(self, node):
        pass

    def visit_address(self, node):
        self.visit_docinfo_item(node, 'address', meta=None)
        self.bodyContent.append(self.starttag(node, 'pre'))

    def depart_address(self, node):
        self.bodyContent.append('\n</pre>\n')
        self.depart_docinfo_item(node)

    def visit_admonition(self, node, name='', admonitionCellAtts={}):
        baseAdmonitionCellAtts = {"width" : "15%"}
        baseAdmonitionCellAtts.update(admonitionCellAtts)
        self.bodyContent.append('<table width="90%" border="1" align="center">\n'
                                '<tbody><tr><td><table width="100%"><tbody><tr>\n')
        self.bodyContent.append(self.starttag(node, 'td', **baseAdmonitionCellAtts))
        if name:
            self.bodyContent.append(self.language.labels[name.lower()])
        self.bodyContent.append('</td><td>')


    def depart_admonition(self, node):
        self.bodyContent.append('</td></tr></tbody></table></td></tr></tbody></table>')

    attribution_formats = {'dash': ('&mdash;', ''),
                           'parentheses': ('(', ')'),
                           'parens': ('(', ')'),
                           'none': ('', '')}

    def visit_attribution(self, node):
        # prefix, suffix = self.attribution_formats[self.settings.attribution]
        prefix, suffix = ('(', ')')
        self.context.append(suffix)
        self.bodyContent.append(
            self.starttag(node, 'p', prefix))

    def depart_attribution(self, node):
        self.bodyContent.append(self.context.pop() + '</p>\n')


    def visit_author(self, node):
        self.visit_docinfo_item(node, 'Author')

    def depart_author(self, node):
        self.depart_docinfo_item(node)

    def visit_authors(self, node):
        pass

    def depart_authors(self, node):
        pass

    def visit_attention(self, node):
        self.visit_admonition(node, 'attention', admonitionCellAtts={"bgcolor":"#ffffcc"})

    def depart_attention(self, node):
        self.depart_admonition(node)

    def visit_block_quote(self, node):
        self.bodyContent.append(self.starttag(node, 'blockquote'))

    def depart_block_quote(self, node):
        self.bodyContent.append('</blockquote>\n')

    def visit_line_block(self, node):
        self.bodyContent.append(self.starttag(node, 'pre'))

    def depart_line_block(self, node):
        self.bodyContent.append('\n</pre>\n')

    def visit_bullet_list(self, node):
        self.bodyContent.append(self.starttag(node, 'ul'))
        self.spewParaTag.append(SpewNothing)

    def depart_bullet_list(self, node):
        self.bodyContent.append('</ul>\n')
        self.spewParaTag.pop()

    def visit_caption(self, node):
        self.bodyContent.append(self.starttag(node, 'p', ''))

    def depart_caption(self, node):
        self.bodyContent.append('</p>\n')

    def visit_caution(self, node):
        self.visit_admonition(node, 'caution', admonitionCellAtts={"bgcolor":"#ffff99"})

    def depart_caution(self, node):
        self.depart_admonition(node)

    def visit_citation(self, node):
        ##! verify col configuration
        self.bodyContent.append(self.starttag(node, 'table'))
        self.bodyContent.append('<colgroup><col /><col /></colgroup>\n'
                         '<col />\n'
                         '<tbody valign="top">\n'
                         '<tr>')
        self.footnote_backrefs(node)

    def depart_citation(self, node):
        self.bodyContent.append('</td></tr>\n'
                         '</tbody>\n</table>\n')

    def visit_citation_reference(self, node):
        href = ''
        if node.has_key('refid'):
            href = '#' + node['refid']
        elif node.has_key('refname'):
            href = '#' + self.document.nameids[node['refname']]
        self.bodyContent.append(self.starttag(node, 'a', '[', href=href))

    def depart_citation_reference(self, node):
        self.bodyContent.append(']</a>')

    def visit_classifier(self, node):
        pass
        
    def depart_classifier(self, node):
        pass

    def visit_colspec(self, node):
        self.colspecs.append(node)

    def depart_colspec(self, node):
        pass

    def write_colspecs(self):
        ##! verify
        width = 0
        for node in self.colspecs:
            width += node['colwidth']
        for node in self.colspecs:
            colwidth = int(node['colwidth'] * 100.0 / width + 0.5)
            self.bodyContent.append(self.emptytag(node, 'col', width='%i%%' % colwidth))
        self.colspecs = []

    def visit_comment(self, node, sub=re.compile('-(?=-)').sub):
        self.bodyContent.append('<!-- %s -->\n' % sub('- ', node.astext()))
        raise nodes.SkipNode

    def visit_contact(self, node):
        self.visit_docinfo_item(node, 'Contact')

    def depart_contact(self, node):
        self.depart_docinfo_item(node)

    def visit_copyright(self, node):
        self.visit_docinfo_item(node, 'copyright')

    def depart_copyright(self, node):
        self.depart_docinfo_item(node)

    def visit_danger(self, node):
        self.visit_admonition(node, 'danger', admonitionCellAtts={"bgcolor":"#ff6666"})

    def depart_danger(self, node):
        self.depart_admonition(node)

    def visit_date(self, node):
        self.visit_docinfo_item(node, 'date')

    def depart_date(self, node):
        self.depart_docinfo_item(node)

    def visit_decoration(self, node):
        pass

    def depart_decoration(self, node):
        pass

    def visit_definition(self, node):
        self.bodyContent.append('</dt>\n')
        self.bodyContent.append(self.starttag(node, 'dd', ''))

    def depart_definition(self, node):
        self.bodyContent.append('</dd>\n')

    def visit_definition_list(self, node):
        self.bodyContent.append(self.starttag(node, 'dl'))

    def depart_definition_list(self, node):
        self.bodyContent.append('</dl>\n')

    def visit_definition_list_item(self, node):
        pass

    def depart_definition_list_item(self, node):
        pass

    def visit_description(self, node):
        self.bodyContent.append(self.starttag(node, 'td', ''))

    def depart_description(self, node):
        self.bodyContent.append('</td>')

    def visit_docinfo(self, node):
        self.context.append(len(self.bodyContent))
        self.bodyContent.append(self.starttag(node, 'table'))
        self.bodyContent.append('<tbody valign="top">\n')
        self.in_docinfo = 1

    def depart_docinfo(self, node):
        self.bodyContent.append('</tbody>\n</table>\n')
        self.in_docinfo = None
        start = self.context.pop()
        self.body_pre_docinfo = self.bodyContent[:start]
        self.docinfo = self.bodyContent[start:]
        self.bodyContent = []

    def visit_docinfo_item(self, node, name, meta=1):
        if meta:
            self.headerContent.append('<meta name="%s" content="%s" />\n' %
                                      (name, self.attval(node.astext())))
        self.bodyContent.append(self.starttag(node, 'tr', ''))
        self.bodyContent.append('<th >%s:</th>\n<td>' % self.language.labels[name.lower()])

    def depart_docinfo_item(self, node):
        self.bodyContent.append('</td></tr>\n')

    def visit_doctest_block(self, node):
        self.bodyContent.append(self.starttag(node, 'pre'))

    def depart_doctest_block(self, node):
        self.bodyContent.append('\n</pre>\n')

    def visit_document(self, node):
        pass

    def depart_document(self, node):
        pass

    def visit_emphasis(self, node):
        self.bodyContent.append('<i>')

    def depart_emphasis(self, node):
        self.bodyContent.append('</i>')

    def visit_entry(self, node):
        if isinstance(node.parent.parent, nodes.thead):
            tagname = 'th'
        else:
            tagname = 'td'
        atts = {}
        if node.has_key('morerows'):
            atts['rowspan'] = node['morerows'] + 1
        if node.has_key('morecols'):
            atts['colspan'] = node['morecols'] + 1
        self.bodyContent.append(self.starttag(node, tagname, '', **atts))
        self.context.append('</%s>\n' % tagname.lower())
        if len(node) == 0:              # empty cell
            self.bodyContent.append('&nbsp;')

    def depart_entry(self, node):
        self.bodyContent.append(self.context.pop())

    def visit_enumerated_list(self, node):
        atts = {}
        if node.has_key('start'):
            atts['start'] = node['start']
        if node.has_key('enumtype'):
            atts['type'] = olTypeTranslator[node['enumtype']]
        self.bodyContent.append(self.starttag(node, 'ol', **atts))

    def depart_enumerated_list(self, node):
        self.bodyContent.append('</ol>\n')

    def visit_error(self, node):
        self.visit_admonition(node, 'error', admonitionCellAtts={"bgcolor":"#ff6666"})

    def depart_error(self, node):
        self.depart_admonition(node)

    def visit_field(self, node):
        self.bodyContent.append(self.starttag(node, 'tr', ''))

    def depart_field(self, node):
        self.bodyContent.append('</tr>\n')

    def visit_field_body(self, node):
        self.bodyContent.append(self.starttag(node, 'td', ''))
        self.spewParaTag.append(SpewBreak)

    def depart_field_body(self, node):
        self.bodyContent.append('</td>\n')
        self.spewParaTag.pop()

    def visit_field_list(self, node):
        self.bodyContent.append(self.starttag(node, 'table'))
        self.bodyContent.append('<tbody valign="top">\n')

    def depart_field_list(self, node):
        self.bodyContent.append('</tbody>\n</table>\n')

    def visit_field_name(self, node):
        atts = {}
        if len(node.astext()) > 14:
            atts['colspan'] = 2
            self.context.append('</tr>\n<tr><td>&nbsp;</td>')
        else:
            self.context.append('')
        self.bodyContent.append(self.starttag(node, 'th', '', **atts))

    def depart_field_name(self, node):
        self.bodyContent.append(':</th>')
        self.bodyContent.append(self.context.pop())

    def visit_figure(self, node):
        self.bodyContent.append(self.starttag(node, 'div'))

    def depart_figure(self, node):
        self.bodyContent.append('</div>\n')

    def visit_footer(self, node):
        self.context.append(len(self.body))

    def depart_footer(self, node):
        start = self.context.pop()
        footer = (['<hr/>\n',
                   self.starttag(node, 'div')]
                  + self.bodyContent[start:] + ['</div>\n'])
        self.bodySuffix[:0] = footer
        del self.bodyContent[start:]

    def check_simple_list(self, node):
        """Check for a simple list that can be rendered compactly."""
        visitor = SimpleListChecker(self.document)
        try:
            node.walk(visitor)
        except nodes.NodeFound:
            return None
        else:
            return 1

    def visit_footnote(self, node):
        if not self.firstFootnoteVisited:
            self.bodyContent.append('<hr />')
            self.firstFootnoteVisited = True
        self.bodyContent.append(self.starttag(node, 'table'))
        self.bodyContent.append('<tbody valign="top">\n<tr>')
        self.spewParaTag.append(SpewBreak)
        self.footnote_backrefs(node)

    def footnote_backrefs(self, node):
        # if self.settings.footnote_backlinks and node.hasattr('backrefs'):
        if node.hasattr('backrefs'):
            backrefs = node['backrefs']
            if len(backrefs) == 1:
                self.context.append('')
                self.context.append('<a href="#%s" name="%s">' % (backrefs[0], node['id']))
            else:
                i = 1
                backlinks = []
                for backref in backrefs:
                    backlinks.append('<a  href="#%s">%s</a>' % (backref, i))
                    i += 1
                self.context.append('<em>(%s)</em> ' % ', '.join(backlinks))
                self.context.append('<a name="%s">' % node['id'])
        else:
            self.context.append('')
            self.context.append('<a name="%s">' % node['id'])

    def depart_footnote(self, node):
        self.spewParaTag.pop()
        self.paraFormat.pop()
        self.bodyContent.append('</td></tr>\n</tbody>\n</table>\n')
        
    def visit_footnote_reference(self, node):
        href = ''
        if node.has_key('refid'):
            href = '#' + node['refid']
        elif node.has_key('refname'):
            href = '#' + self.document.nameids[node['refname']]
        # format = self.settings.footnote_references
        format = 'superscript'
        if format == 'brackets':
            suffix = '['
            self.context.append(']')
        elif format == 'superscript':
            suffix = '<sup>'
            self.context.append('</sup>')
        else:                           # shouldn't happen
            suffix = '???'
            self.content.append('???')
        self.bodyContent.append('<b>')
        self.bodyContent.append(suffix)
        self.bodyContent.append(self.starttag(node, 'a', '', href=href))

    def depart_footnote_reference(self, node):
        self.bodyContent.append('</a>')
        self.bodyContent.append(self.context.pop())
        self.bodyContent.append('</b>')

    def visit_rubric(self, node):
        self.bodyContent.append(self.starttag(node, 'p', ''))

    def depart_rubric(self, node):
        self.bodyContent.append('</p>\n')

    def visit_generated(self, node):
        pass

    def depart_generated(self, node):
        pass

    def visit_hint(self, node):
        self.visit_admonition(node, 'hint', admonitionCellAtts={"bgcolor":"#99ff99"})

    def depart_hint(self, node):
        self.depart_admonition(node)

    def visit_image(self, node):
        atts = node.attributes.copy()
        atts['src'] = atts['uri']
        del atts['uri']
        if not atts.has_key('alt'):
            atts['alt'] = atts['src']
        if isinstance(node.parent, nodes.TextElement):
            self.context.append(None)
        else:
            self.bodyContent.append('<p>')
            self.context.append('</p>\n')
        self.bodyContent.append(self.emptytag(node, 'img', '', **atts))

    depart_image = popAndAppend

    def visit_important(self, node):
        self.visit_admonition(node, 'important', admonitionCellAtts={"bgcolor":"#ffcccc"})

    def depart_important(self, node):
        self.depart_admonition(node)

    def visit_interpreted(self, node):
        ###! no idea what to do here
        pass

    def depart_interpreted(self, node):
        pass

    def visit_label(self, node):
        self.bodyContent.append(self.starttag(node, 'td', '<b>[%s' % self.context.pop()))

    def depart_label(self, node):
        self.paraFormat.append(('<font size=-1><i>', '</i></font>'))
        self.bodyContent.append('</a>]</b></td><td>%s' % self.context.pop())

    def visit_legend(self, node):
        self.bodyContent.append(self.starttag(node, 'div'))

    def depart_legend(self, node):
        self.bodyContent.append('</div>\n')

    def visit_list_item(self, node):
        self.bodyContent.append(self.starttag(node, 'li', ''))
        self.spewParaTag.append(SpewNothingThenPara)

    def depart_list_item(self, node):
        self.bodyContent.append('</li>\n')
        self.spewParaTag.pop()

    def visit_literal(self, node):
        self.bodyContent.append(self.starttag(node, 'code', ''))
        text = node.astext()
        for token in self.words_and_spaces.findall(text):
            if token.strip():
                # Protect text like "--an-option" from bad line wrapping:
                self.bodyContent.append('<span>%s</span>' % self.encode(token))
            elif token in ('\n', ' '):
                # Allow breaks at whitespace:
                self.bodyContent.append(token)
            else:
                # Protect runs of multiple spaces; the last space can wrap:
                self.bodyContent.append('&nbsp;' * (len(token) - 1) + ' ')
        self.bodyContent.append('</code>')
        # Content already processed:
        raise nodes.SkipNode

    def visit_literal_block(self, node):
        self.bodyContent.append(self.starttag(node, 'pre'))

    def depart_literal_block(self, node):
        self.bodyContent.append('\n</pre>\n')

    def visit_meta(self, node):
        self.headerContent.append(self.emptytag(node, 'meta', **node.attributes))

    def depart_meta(self, node):
        pass

    def visit_note(self, node):
        self.visit_admonition(node, 'note')

    def depart_note(self, node):
        self.depart_admonition(node)

    def visit_option(self, node):
        if self.context[-1]:
            self.bodyContent.append(', ')

    def depart_option(self, node):
        self.context[-1] += 1

    def visit_option_argument(self, node):
        self.bodyContent.append(node.get('delimiter', ' '))
        self.bodyContent.append(self.starttag(node, 'var', ''))

    def depart_option_argument(self, node):
        self.bodyContent.append('</var>')

    def visit_option_group(self, node):
        atts = {}
        if len(node.astext()) > 14:
            atts['colspan'] = 2
            self.context.append('</tr>\n<tr><td>&nbsp;</td>')
        else:
            self.context.append('')
        self.bodyContent.append(self.starttag(node, 'td', **atts))
        self.bodyContent.append('<kbd>')  ###! What tag is this?
        self.context.append(0)          # count number of options

    def depart_option_group(self, node):
        self.context.pop()
        self.bodyContent.append('</kbd></td>\n')
        self.bodyContent.append(self.context.pop())

    def visit_option_list(self, node):
        self.bodyContent.append(self.starttag(node, 'table'))
        self.bodyContent.append('<tbody valign="top">\n')

    def depart_option_list(self, node):
        self.bodyContent.append('</tbody>\n</table>\n')

    def visit_option_list_item(self, node):
        self.bodyContent.append(self.starttag(node, 'tr', ''))

    def depart_option_list_item(self, node):
        self.bodyContent.append('</tr>\n')

    def visit_option_string(self, node):
        self.bodyContent.append(self.starttag(node, 'span', ''))

    def depart_option_string(self, node):
        self.bodyContent.append('</span>')

    def visit_organization(self, node):
        self.visit_docinfo_item(node, 'organization')

    def depart_organization(self, node):
        self.depart_docinfo_item(node)

    def visit_paragraph(self, node):
        currentSpewParaTag = self.spewParaTag[-1]
        if currentSpewParaTag == SpewParagraph:
            self.bodyContent.append(self.starttag(node, 'p', ''))
            self.context.append('</p>\n')
        elif currentSpewParaTag == SpewBreak:
            self.context.append('<br />\n')
        elif currentSpewParaTag == SpewBreakBreak:
            self.context.append('<br /><br />\n')
        elif currentSpewParaTag == SpewNothingThenPara:
            self.context.append(None)
            self.spewParaTag[-1] = SpewParagraph
        else:
            self.context.append(None)

        start, end = self.paraFormat[-1]
        if start:
            self.bodyContent.append(start)
        if end:
            self.context.append(end)
        else:
            self.context.append(None)

    def depart_paragraph(self, node):
        self.popAndAppend(node) # pop end formatting tag, if any
        self.popAndAppend(node) # pop end paragraph tag, if any

    def visit_problematic(self, node):
        if node.hasattr('refid'):
            self.bodyContent.append('<a href="#%s" name="%s">' % (node['refid'], node['id']))
            self.context.append('</a>')
        else:
            self.context.append('')
        self.bodyContent.append(self.starttag(node, 'span', ''))

    def depart_problematic(self, node):
        self.bodyContent.append('</span>')
        self.bodyContent.append(self.context.pop())

    def visit_reference(self, node):
        if node.has_key('refuri'):
            href = node['refuri']
        elif node.has_key('refid'):
            href = '#' + node['refid']
        elif node.has_key('refname'):
            href = '#' + self.document.nameids[node['refname']]
        self.bodyContent.append(self.starttag(node, 'a', '', href=href))
        self.context.append('</a>')

    depart_reference = popAndAppend

    def visit_revision(self, node):
        self.visit_docinfo_item(node, 'revision')

    def depart_revision(self, node):
        self.depart_docinfo_item(node)

    def visit_row(self, node):
        self.bodyContent.append(self.starttag(node, 'tr', ''))

    def depart_row(self, node):
        self.bodyContent.append('</tr>\n')

    def visit_section(self, node):
        self.section_level += 1
        #hTag = 'h%s'% self.section_level
        #self.bodyContent.append(self.starttag(node, hTag))
        #self.bodyContent.append('</%s>\n' % hTag)

    def depart_section(self, node):
        self.section_level -= 1

    def visit_sidebar(self, node):
        self.bodyContent.append('<hr width="80%" align="center"/>')
        self.bodyContent.append('<table border="0" width="80%" align="center"><tbody><tr><td>')

    def depart_sidebar(self, node):
        self.bodyContent.append('</td></tr></tbody></table>\n')
        self.bodyContent.append('<hr width="80%" align="center"/>')

    def visit_status(self, node):
        self.visit_docinfo_item(node, 'status', meta=None)

    def depart_status(self, node):
        self.depart_docinfo_item(node)

    def visit_strong(self, node):
        self.bodyContent.append('<strong>')

    def depart_strong(self, node):
        self.bodyContent.append('</strong>')

    def visit_subscript(self, node):
        self.bodyContent.append(self.starttag(node, 'sub', ''))

    def depart_subscript(self, node):
        self.bodyContent.append('</sub>')

    def visit_substitution_definition(self, node):
        raise nodes.SkipNode # internal

    def visit_substitution_reference(self, node):
        pass

    def visit_subtitle(self, node):
        self.bodyContent.append(self.starttag(node, 'h3', ''))

    def depart_subtitle(self, node):
        self.bodyContent.append('</h3>\n')

    def visit_superscript(self, node):
        self.bodyContent.append(self.starttag(node, 'sup', ''))

    def depart_superscript(self, node):
        self.bodyContent.append('</sup>')

    def visit_table(self, node):
        self.bodyContent.append(self.starttag(node, 'table'))

    def depart_table(self, node):
        self.bodyContent.append('</table>\n')

    def visit_target(self, node):
        if not (node.has_key('refuri') or node.has_key('refid') or node.has_key('refname')):
            self.bodyContent.append(self.starttag(node, 'a', ''))
            self.context.append('</a>')
        else:
            self.context.append(None)

    depart_target = popAndAppend

    def visit_tbody(self, node):
        self.write_colspecs()
        self.bodyContent.append(self.context.pop()) # '</colgroup>\n' or ''
        self.bodyContent.append(self.starttag(node, 'tbody', valign='top'))

    def depart_tbody(self, node):
        self.bodyContent.append('</tbody>\n')

    def visit_term(self, node):
        self.bodyContent.append(self.starttag(node, 'dt', ''))

    def depart_term(self, node):
        pass

    def visit_tgroup(self, node):
        ###! verify
        # Mozilla needs <colgroup>:
        self.bodyContent.append(self.starttag(node, 'colgroup'))
        # Appended by thead or tbody:
        self.context.append('</colgroup>\n')

    def depart_tgroup(self, node):
        pass

    def visit_thead(self, node):
        self.write_colspecs()
        self.bodyContent.append(self.context.pop()) # '</colgroup>\n'
        # There may or may not be a <thead>; this is for <tbody> to use:
        self.context.append('')
        self.bodyContent.append(self.starttag(node, 'thead', valign='bottom'))

    def depart_thead(self, node):
        self.bodyContent.append('</thead>\n')

    def visit_tip(self, node):
        self.visit_admonition(node, 'tip')

    def depart_tip(self, node):
        self.depart_admonition(node)

    def visit_title(self, node):
        if isinstance(node.parent, nodes.topic) and (node.parent.attributes.get('name', None) != 'contents'):
            self.bodyContent.append('<i><center>')
            if node.parent.hasattr('id'):
                self.bodyContent.append(self.starttag({},'a','',name=node.parent['id']))
                self.context.append('</a></center></i><br />\n')
            else:
                self.context.append('</center></i><br />\n')
        elif self.section_level == 0:
            self.headerContent.append(DocArticleText.titleStart)
            self.headerContent.append(self.encode(node.astext()))
            self.headerContent.append(DocArticleText.titleEnd)
            self.bodyContent.append(self.starttag(node, 'h2', ''))
            self.context.append('</h2>\n')
        else:
            ### O'Reilly uses h2 to denote title and h3 for all sections.  In theory,
            ### nothing should hang below h3.  In practice, we leave it up to the
            ### author.
            level = self.section_level + 1
            self.bodyContent.append(self.starttag(node, 'h%s' % level, ''))
            atts = {}
            if node.parent.hasattr('id'):
                atts['name'] = node.parent['id']
            if node.hasattr('refid'):
                atts['href'] = '#' + node['refid']
            self.bodyContent.append(self.starttag({}, 'a', '', **atts))
            self.context.append('</a></h%s>\n' % level)

    def depart_title(self, node):
        self.popAndAppend(node)

    def visit_title_reference(self, node):
        self.bodyContent.append(self.starttag(node, 'cite', ''))

    def depart_title_reference(self, node):
        self.bodyContent.append('</cite>')
    
    def visit_topic(self, node):
        if node.attributes.get('name', None) != 'contents':
            self.spewParaTag.append(SpewNothingThenPara)
            self.bodyContent.append('<table border="1" width="80%" align="center"><tbody><tr><td>')
        
    def depart_topic(self, node):
        if node.attributes.get('name', None) != 'contents':
            self.bodyContent.append('</td></tr></tbody></table>\n')
            self.spewParaTag.pop()

    def visit_transition(self, node):
        self.bodyContent.append(self.emptytag(node, 'hr'))

    def depart_transition(self, node):
        pass

    def visit_version(self, node):
        self.visit_docinfo_item(node, 'version')

    def depart_version(self, node):
        self.depart_docinfo_item(node)

    def visit_warning(self, node):
        self.visit_admonition(node, 'warning', admonitionCellAtts={"bgcolor":"#ffff33"})

    def depart_warning(self, node):
        self.depart_admonition(node)

    def unknown_visit(self, node):
        print 'Node: %s' % node.__class__.__name__
        print "Failure processing at line (%s) of node:\n %s" % (node.line, node.pformat())
        raise NotImplementedError('visiting unknown node type: %s'
                                  % node.__class__.__name__)

    def visit_system_message(self, node):
        if node['level'] < self.document.reporter['writer'].report_level:
            # Level is too low to display:
            raise nodes.SkipNode
        self.bodyContent.append(self.starttag(node, 'div'))
        self.bodyContent.append('<p>')
        attr = {}
        backref_text = ''
        if node.hasattr('id'):
            attr['name'] = node['id']
        if node.hasattr('backrefs'):
            backrefs = node['backrefs']
            if len(backrefs) == 1:
                backref_text = ('; <em><a href="#%s">backlink</a></em>'
                                % backrefs[0])
            else:
                i = 1
                backlinks = []
                for backref in backrefs:
                    backlinks.append('<a href="#%s">%s</a>' % (backref, i))
                    i += 1
                backref_text = ('; <em>backlinks: %s</em>'
                                % ', '.join(backlinks))
        if node.hasattr('line'):
            line = ', line %s' % node['line']
        else:
            line = ''
        if attr:
            a_start = self.starttag({}, 'a', '', **attr)
            a_end = '</a>'
        else:
            a_start = a_end = ''
        self.bodyContent.append('System Message: %s%s/%s%s (<tt>%s</tt>%s)%s</p>\n'
                         % (a_start, node['type'], node['level'], a_end,
                            node['source'], line, backref_text))

    def depart_system_message(self, node):
        self.bodyContent.append('</div>\n')

