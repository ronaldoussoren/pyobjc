"""
This is a plugin that is used to give a live interface to the 
Example code stored in the PyObjC repository.

The plugin makes a number of assumptions:
* The toplevel directory for an example contains a setup.py file
* Projects with examples are named 'pyobjc-framework-NAME' (for
  various names)
* Examples are in an "Examples" directory of a project, that
  directory will not be empty.
* Examples are either direct subdirectories of this folder, or
  in a subfolder.
* Examples, or folders containing examples, can contain a file
  named 'summary.txt'. This summary is a reStructuredText file
  and is shown on the summary pages.
* Examples should also contain a file 'readme.txt', also a
  reStructuredText file. The readme contains a longer description
  of the example.

TODO:
* All HTML and zipfiles are currently recalculated for every request,
  it might be a better idea to cache generated files.
* The code needs to be audited to check for security issues, as the
  plugin is intended to be used on the Internet.
"""

import re, zipfile
from StringIO import StringIO

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_stylesheet

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

from docutils.core import publish_parts


import os

# We know paths in the example tree contain only characters from
# the regexp below. This is used as an initial filter for invalid 
# requests.
gValidPath=re.compile('^[-A-Za-z0-9./ ]*$')

# Suffix for files that we show as source files.
# Other files are surpressed in the web interface, but will be present
# in the downloadable ZIP file.
gSourceSuffix = ('.py', '.pyw', '.m', '.h')


class Examples(Component):
    implements(INavigationContributor, ITemplateProvider, IRequestHandler)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        """
        Name that can be used in configuration to add the plugin
        to a navigation menu.
        """
        return 'examples'

    def get_navigation_items(self, req):
        """
        Yield a record that adds the plugin to the main
        navigation menu.
        """
        yield ('mainnav', 'examples',
               tag.a('Examples', href=req.href.examples()))



    def match_request(self, req):
        """
        Return True iff the request is intented for this plugin.
        """
        return re.match(r'/examples(?:/.*)?$', req.path_info)



    def process_request(self, req):
        """
        Process a web request.
        """

        # Initial security check: only allow requests where the
        # URL contains known-good characters.
        if gValidPath.match(req.path_info)  is None:
            raise TracError("invalid path: %r"%(req.path_info,))
        
        if req.path_info in ('/examples', '/examples/'):
            # Root of the tree that's served by this plugin.
            #
            # This renders a list off all projects that contain examples. 
            # Entries in the list link to a second-level index.
            #

            menu = []
            for label, path in sorted(self._get_projects_containing_examples()):
                menu.append((label, req.href.examples() + '/' + path))

            return 'sample-global-index.html', dict(bottommenu=menu), None

        parts = req.path_info[10:].split('/')
        if '.' in parts or '..' in parts:
            # Another security check, ensure that the user doesn't
            # try to walk outside of our environment using '..' in the
            # request path.
            raise TracError("Invalid path")

        if len(parts) == 1:
            # "/examples/foo"
            #
            # This is the per-project index. This page shows a list
            # of all examples in the project. Examples in subdirectories
            # are shown with additional section headers.
            #
            # The name of an example is a link to the detail page for
            # that example.

            framework = parts[0]
            samples = []
            for subdir, name, summary in self._get_samples(framework):
                if summary is not None:
                    summary = self._restToHTML(summary)

                if subdir is not None:
                    samples.append([
                        req.href.examples() + '/%s/%s/index.html'%(framework, subdir),
                        name,
                        summary
                    ])
                else:
                    samples.append([
                        None,
                        name,
                        summary
                    ])

            data = {
                'title': 'Framework: %s'%(framework.split('-')[-1]),
                'samples': samples,
            }
            return 'sample-framework-index.html', data, None

        elif parts[-1].endswith('.zip'):
            # "/examples/foo/bar.zip"
            #
            # Returns a zipfile for a single example. 
            #
            # NOTE: self._sample_zip will bail out if the
            # path doesn't refer to a directory containing
            # a setup.py.
            #

            data = self._sample_zip(parts[:-1])

            req.send_response()
            req.send_header('Content-Type', 'application/octet-stream; name="%s"'%(parts[-1],))
            req.end_headers()
            req.write(data)
            return 

        elif parts[-1] == 'index.html':
            # Starting page for an example. This contains the readme for
            # the example and links to colorized source code files.
            #
            # NOTE: self._sample_index bails out if the path doesn't
            # refer to a directory containing a setup.py
            #

            data = self._sample_index(parts[:-1])
            return 'sample-index.html', data, None

        else:
            # Last chance: this must be a request of a source file.
            # Show the file as an HTML file with syntax coloring.
            #
            # NOTE: self._sample_source will bail out if the file
            # is not a valid source file.
            #

            data = self._sample_source(parts)
            return 'sample-source.html', data, None
            

    def get_templates_dirs(self):
        """
        Return the directory that contains template files.
        """
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]


    def _get_projects_containing_examples(self):
        """
        Yields (label, name), where the label is a
        label that should be shown to the user and name
        is the PyObjC project name.

        All yielded records correspond to projects that
        have example code in them.
        """
        repos = self.env.get_repository()
        path = '/trunk/pyobjc'
        try:
            node = repos.get_node(path)
            for e in node.get_entries():
                if not e.isdir: continue
                name = e.get_name()
                if not name.startswith('pyobjc-framework'): continue

                have_samples = False
                for sn in e.get_entries():
                    if sn.get_name() == 'Examples':
                        have_samples = True
                        break

                if not have_samples: continue

                label = 'Framework: ' + name.split('-')[-1]

                yield (label, name)


        finally:
            repos.close()


    def _search_samples(self, result, node, path=''):
        """
        Look for examples in ``node`` and add
        descriptions for them to ``result``.

        There are two major cases:

        * The node represents a sample, add
          ``(None, sampleName, summary)``
          to the result list.

        * The node represents a directory that
          contains examples. Add 
          ``(nodeName, None, summary)`` to the 
          list and also add the samples in subdirectories
          to the list (recursively).
        """
        is_sample = False
        summary_node = None

        for e in node.get_entries():

            if e.get_name() == 'setup.py':
                is_sample = True
            elif e.get_name().lower() == 'summary.txt':
                summary_node = e


        if is_sample:
            if summary_node is not None:
                summary = summary_node.get_content().read()
            else:
                summary = None


            result.append((os.path.join(path, node.get_name()), node.get_name(), summary))

        else:
            my_result = []
            for e in sorted(node.get_entries(), key=lambda n: n.get_name()):
                if not e.isdir: continue

                self._search_samples(my_result, e, os.path.join(path, node.get_name()))

            if my_result:
                if summary_node is not None:
                    summary = summary_node.get_content()
                else:
                    summary = None


                result.append((None, node.get_name(), summary))
                result.extend(my_result)



    def _get_samples(self, framework):
        """
        Return the list of examples in a given framework.

        The result contains tuples in two flavors:

        * (None, label, summary): Heading for a group of examples

        * (path, label, summary): A specific example
        """

        repos = self.env.get_repository()
        path = '/trunk/pyobjc/' + framework + '/Examples'
        try:
            node = repos.get_node(path)
            if node is None:
                raise TracError("Couldn't find repository path: %s" % path)

            result = []
            for e in sorted(node.get_entries(), key=lambda n: n.get_name()):
                self._search_samples(result, e)

            return result

        finally:
            repos.close()


    def _gather_sources(self, result, node, base=''):
        """
        Look for paths for source files below ``node``.

        The paths get added to ``result``.
        """

        if base is None:
            base = ''
        else:
            base = os.path.join(base, node.get_name())
        for e in node.get_entries():
            if os.path.splitext(e.get_name())[-1] in gSourceSuffix:
                fn = "source--%s.html"%( os.path.join(base, e.get_name()).replace('/', '-'))
                result.append((os.path.join(base, e.get_name()), fn))
            elif e.isdir:
                self._gather_sources(result, e, base)

    def _sample_index(self, parts):
        """
        Return information for the index page of an example:

        * Name of the example
        * List of sources
        * ReadMe information (as HTML fragment)
        * Name of the zipfile containing the entire example.
        """
        repos = self.env.get_repository()
        try:
            path = os.path.join('/trunk/pyobjc', parts[0], 'Examples', *parts[1:])
            node = repos.get_node(path)
            if node is None:
                raise TrackError("Couldn't find repository path: %s" % path)

            setup_node = repos.get_node(path + '/setup.py')
            if setup_node is None:
                # Path doesn't refer to an example, bail out.
                raise TrackError("Couldn't find repository path: %s" % path)

            readme_node = None
            sources = []
            for e in node.get_entries():
                if e.get_name().lower() == "readme.txt":
                    readme_node = e
                elif e.get_name().lower() == "summary.txt" and readme_node is None:
                    readme_node = e

                elif os.path.splitext(e.get_name())[-1] in ('.py', '.pyw', '.m', '.h'):
                    fn = "source--%s.html"%(e.get_name())

                    sources.append((e.get_name(), fn))

                elif e.isdir:
                    self._gather_sources(sources, e)
                    

            if readme_node is None:
                readme = "Example without a readme file"

            else:
                readme = self._restToHTML(readme_node.get_content().read())

            title = node.get_name()
            zipname = node.get_name() + ".zip"

            sources.sort(key=lambda x: x[-1])

            return dict(
                title=node.get_name(),
                zipname=node.get_name() + ".zip",
                sources=sources,
                readme=readme
            )

        finally:
            repos.close()
        

    def _sample_source(self, parts):
        """
        Return the HTML rendering of a source file
        """

        bn = parts[-1]
        if not bn.startswith('source--') or not bn.endswith('.html'):
            # The link isn't of the form that this plugin generated, and
            # therefore cannot refer to a valid source file.
            raise TrackError("Path doesn't refer to source file: %s" % path)

        repos = self.env.get_repository()
        try:
            sourcefn = parts[-1].replace('-', '/')[8:-5]

            suffix = os.path.splitext(sourcefn)[-1]
            if suffix not in gSourceSuffix:
                # File is not one of the types of sources we want to deal
                # with.
                raise TrackError("Path doesn't refer to source file: %s" % path)


            fullpath = '/'.join(parts[1:-1] + [sourcefn])
            path = '/trunk/pyobjc/' + parts[0] + '/Examples/' + fullpath

            node = repos.get_node(path)
            if node is None:
                raise TrackError("Couldn't find repository path: %s" % path)
                
            src = node.get_content().read()

            sources=[]
            rootnode = repos.get_node(os.path.dirname(path))
            self._gather_sources(sources, rootnode, base=None)
            sources.sort(key=lambda x: x[-1])
            sources = [(a, b, (((b==parts[-1]) or None) and 'selected')) for a, b in sources ]

            lexer = get_lexer_for_filename(sourcefn)
            formatter = HtmlFormatter(linenoes=False, cssclass='source')
            body = highlight(src, lexer, formatter)
            style=formatter.get_style_defs()

            return dict(
                    filename=sourcefn,
                    zipname=os.path.basename(parts[-2]) + '.zip',
                    body=body,
                    style=style,
                    sources=sources,
                   )

        finally:
            repos.close()


    def _zip_node(self, zf, node, path=''):
        """
        Add the contents of ``node`` to the zipfile in
        the directory with path ``path``. 

        If ``node`` refers to a directory that directory
        is added recursively.
        """
        path = os.path.join(path, node.get_name())
        if node.isfile:
            info = zipfile.ZipInfo(path.encode('utf-8'))
            info.external_attr = 0444 << 16
            zf.writestr(info, node.get_content().read())

        else:
            for node in node.get_entries():
                self._zip_node(zf, node, path)


    def _sample_zip(self, parts):
        """
        Return a byte-string that contains a zipfile containing
        all files in an example.
        """

        repos = self.env.get_repository()
        try:
            fp = StringIO()
            zf = zipfile.ZipFile(fp, 'w', zipfile.ZIP_DEFLATED)
            path = os.path.join('/trunk/pyobjc', parts[0], 'Examples', *parts[1:])


            root = repos.get_node(path)
            if root is None:
                raise TrackError("Couldn't find repository path: %s" % path)

            setup_node = repos.get_node(path + '/setup.py')
            if setup_node is None:
                # Path doesn't refer to an example, bail out.
                raise TrackError("Couldn't find repository path: %s" % path)

            self._zip_node(zf, root)

            zf.close()
            return fp.getvalue()

        finally:
            repos.close()

    def _restToHTML(self, input):
        """
        Return the body HTML that is the translation of
        ``input``. The input is assumed to be reStructuredText.
        """
        output = publish_parts(
            source=input,
            source_path='pyobjc.txt',
            writer_name='html',
            settings_overrides=dict(
            input_encoding='utf-8',
            initial_header_level=2,
        ))

        return output['html_body']


