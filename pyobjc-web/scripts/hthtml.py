# Author: Ollie Rutherfurd
# Contact: oliver@rutherfurd.net
# Revision: $Revision: 1.2 $
# Date: $Date: 2004/12/08 19:49:05 $
# Copyright: This module has been placed in the public domain.

"""
Simple .ht (HyperText Template) document tree Writer.

.ht tmeplate files are essentially normal HTML, with
an option set of RFC 2822-like headers at the top of
the file. There must be at least one blank line between
the last header and the start of the body HTML.

See http://ht2html.sf.net/ for more information on
.ht files and ht2html..
"""

__docformat__ = 'reStructuredText'

import os
from docutils import nodes
from docutils import writers
from docutils.writers.html4css1 import HTMLTranslator, utils


class Writer(writers.Writer):

    supported = ('ht',)
    """Formats this writer supports."""

    settings_spec = (
        '.ht template-Specific Options',
        None,
        (('Specify base section (i.e. if 3, a top-level section '
          'would be written as H3, 2nd level H4, etc...).  Default is 3.',
          ['--base-section'],
          {'choices': ['1','2','3','4'], 
            'default': '3', 
            'metavar': '<NUMBER>'}),
         ('Specify the initial header level.  Default is 1 for "<h1>".  '
          'Does not affect document title & subtitle (see --no-doc-title).',
          ['--initial-header-level'],
          {'choices': '1 2 3 4 5 6'.split(), 'default': '1',
           'metavar': '<level>'}),
         ('Specify a stylesheet URL, used verbatim.  Default is '
          '"default.css".',
          ['--stylesheet'],
          {'default': 'default.css', 'metavar': '<URL>'}),
         ('Specify a stylesheet file, relative to the current working '
          'directory.  The path is adjusted relative to the output HTML '
          'file.  Overrides --stylesheet.',
          ['--stylesheet-path'],
          {'metavar': '<file>'}),
         ('Format for footnote references: one of "superscript" or '
          '"brackets".  Default is "superscript".',
          ['--footnote-references'],
          {'choices': ['superscript', 'brackets'], 'default': 'superscript',
           'metavar': '<FORMAT>'}),
         ('Remove extra vertical whitespace between items of bullet lists '
          'and enumerated lists, when list items are "simple" (i.e., all '
          'items each contain one paragraph and/or one "simple" sublist '
          'only).  Default: enabled.',
          ['--compact-lists'],
          {'default': 1, 'action': 'store_true'}),
         ('Disable compact simple bullet and enumerated lists.',
          ['--no-compact-lists'],
          {'dest': 'compact_lists', 'action': 'store_false'}),
          ('Omit the XML declaration.  Use with caution.',
          ['--no-xml-declaration'], {'dest': 'xml_declaration', 'default': 1,
                                     'action': 'store_false'}),))

    relative_path_settings = ('stylesheet_path',)

    output = None

    def __init__(self):
        writers.Writer.__init__(self)
        self.translator_class = HTTranslator

    def translate(self):
        visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = visitor.astext()
        self.stylesheet = visitor.stylesheet
        self.body = visitor.body


class HTTranslator(HTMLTranslator):

    def __init__(self, document):

        # I don't believe we can embed any style content
        # the header, so always link to the stylesheet.
        document.settings.embed_stylesheet = 0
        document.settings.base_section = int(document.settings.base_section)

        HTMLTranslator.__init__(self, document)
        # ht2html likes having a title, so add a default one
        self.headers = {'title': 'None'}
        stylesheet = utils.get_stylesheet_reference(document.settings,
                os.path.join(os.getcwd(),'dummy'))
        if stylesheet:
            self.headers['stylesheet']= stylesheet
        # using first author found for .ht 'Author' header
        self.has_author = 0

    def astext(self):
        headers = ''.join(['%s: %s\n' % (k,v) \
            for (k,v) in self.headers.items()])
        # kludge! want footer, but not '</body></html>'
        body = self.body_pre_docinfo + self.docinfo + self.body + \
                self.body_suffix[:-1]

        return ''.join([headers + '\n'] + body)

    def visit_author(self, node):
        if not self.headers.has_key('author'):
            self.headers['author'] = self.encode(node.astext())
        HTMLTranslator.visit_author(self, node)

    def visit_contact(self, node):
        if not self.headers.has_key('author-email'):
            self.headers['author-email'] = self.encode(node.astext())
        HTMLTranslator.visit_contact(self, node)

    def visit_title(self, node):
        """Only 6 section levels are supported by HTML."""
        if isinstance(node.parent, nodes.topic):
            HTMLTranslator.visit_title(self, node)
        elif self.section_level == 0:
            HTMLTranslator.visit_title(self, node)
            # document title
            title = node.astext()
            self.headers['title'] = self.encode(title)
        else:
            # offset section level to account for ``base_section``.
            self.section_level += (self.settings.base_section - 1)
            HTMLTranslator.visit_title(self, node)
            self.section_level -= (self.settings.base_section - 1)


# :indentSize=4:lineSeparator=\n:noTabs=true:tabSize=4:
