"""
A class that deals with generating the website.

TODO: add a way to syntax-color embedded source code, possibly based
on: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/252170
"""
import os, shutil

from genshi.template import MarkupTemplate, TemplateLoader

from docutils.core import publish_parts



gTemplateDir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'templates')
gTemplateIncludes = os.path.join(gTemplateDir, 'global')

gTopMenu=[
    ('Home',            '/index.html'),
    ('Documentation',   '/documentation/index.html'),
    ('Development',     '/development.html'),
    ('Download',        '/downloads.html'),
    ('Examples',        '/examples/index.html'),
    ('Mailing lists',   'http://sourceforge.net/mail/?group_id=14534'),
]

gBottomMenu=[
]


class SiteGenerator (object):

    def __init__(self, templateRoot, siteRoot):
        self.templateRoot = templateRoot
        self.siteRoot = siteRoot


    def _makeGlobals(self, outputpath):
        """
        Return the dictionary of global functions/constants
        for the template. The output of the template
        will be written als 'outputpath' (relative to
        the site root). 

        Note that this function does *not* write to the
        filesystem
        """

        def url(path):
            """
            Return 'path' as a relative URL. 'Path' is supposed to
            be site-relative (that is '/some/path') and this function
            returns a path relative to the current page.
            """
            if path.startswith('http://') or path.startswith('https://'):
                return path

            if not path.startswith('/'):
                return path

            while path.startswith('/'):
                 path = path[1:]

            dirpath = os.path.dirname(outputpath)
            if dirpath == '.' or dirpath == '':
                return path

            else:
                rootpath = os.path.sep.join(['..'] * (1+dirpath.count(os.path.sep)))
                return os.path.join(rootpath, path)

        return dict(
                url=url,
                topmenu=gTopMenu,
                bottommenu=gBottomMenu,
               )

    def _makeLoader(self, _templateFn):
        #return TemplateLoader([ os.path.dirname(_templateFn), gTemplateIncludes, ])
        return TemplateLoader(gTemplateIncludes)

    def localPathForSitePath(self, sitePath):
        while sitePath.startswith(os.sep):
            sitePath = sitePath[1:]
        return os.path.join(self.siteRoot, sitePath)


    def emitHTML(self, _htmlpath, _templateFn, **kwds):
        """
        read the specified template, perform template
        instantantiation and write the result to _htmlpath.

        Any keyword arguments are used to fill in the blanks
        in the template.
        """
        while _htmlpath.startswith(os.sep):
            _htmlpath = _htmlpath[1:]

        outfn = os.path.join(self.siteRoot, _htmlpath)
        infn = os.path.join(gTemplateDir, _templateFn)

        outdn = os.path.dirname(outfn)
        if not os.path.exists(outdn):
            os.makedirs(outdn)

        tmpl = MarkupTemplate(open(infn, 'r').read(), loader=self._makeLoader(infn), lookup='strict')
        variables = self._makeGlobals(_htmlpath)
        variables.update(kwds)
        stream = tmpl.generate(**variables)
        fp = open(outfn, "w")
        fp.write(stream.render('html'))
        fp.close()

    def copyReST(self, _infn, _outfn, template='static-rest.html', **kwds):
        input = open(_infn, 'rU').read()
        output = publish_parts(
            source=input,
            source_path=_infn,
            writer_name='html',
            settings_overrides=dict(
                input_encoding='utf-8',
                initial_header_level=2,
            ))

        kwds.update(output)
        self.emitHTML(_outfn, template, **kwds)


    def copy(self, input, output):
        """
        Copy 'input' to 'output' (where 'output' is a path relative
        to the site root).

        If 'input' is a directory it is copied recursively, 
        version managment turds are ignored.
        """
        output = self.localPathForSitePath(output)
        if not os.path.exists(os.path.dirname(output)):
            os.makedirs(os.path.dirname(output))

        if os.path.isfile(input):
            data = open(input, 'rb')
            open(output, 'wb').write(data)
            data = None

        else:
            if os.path.exists(output):
                shutil.rmtree(output)
            os.mkdir(output)
            for dirpath, dirnames, filenames in os.walk(input):
                for dn in ('.svn', 'CVS'):
                    if dn in dirnames:
                        dirnames.remove(dn)

                if dirpath == input:
                    relpath = '.'
                else:
                    relpath = output[len(input):]

                for dn in dirnames:
                    os.mkdir(os.path.join(output, relpath, dn))

                for fn in filenames:
                    data = open(os.path.join(dirpath, fn), 'rb').read()
                    open(os.path.join(output, relpath, fn), 'wb').write(data)
                    data = None
