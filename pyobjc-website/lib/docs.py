"""
docs - generating the online documentation

This parses the documentation in the PyObjC 
repository and generates the online documentation
from that.

TODO:
- Cleanup and enhance the documentation

- Update the inline documentation in the 
  pyobjc Objective-C sources and include that 
  as well.

- Start a project to parse Apple's documentation
  and transform that into PyObjC documentation for
  the corresponding framework.
"""
import os, zipfile

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

from genshi.core import Markup

from docutils.core import publish_parts

from distutils import log
import source_directive

def nameForProject(project):
    if project == 'pyobjc-core':
        name = 'PyObjC Core'

    elif project == 'pyobjc-metadata':
        name = 'Metadata Generator'

    elif project.startswith('pyobjc-framework-'):
        name = project[17:]

    else:
        name = project

    return name

def makeBottomMenu(htmlroot, sourceroot, projects):
    allProjects = []

    for project in projects:
        projroot = os.path.join(sourceroot, project, 'Doc')
        if not os.path.exists(projroot):
            continue

        else:
            name = nameForProject(project)
            allProjects.append((name, os.path.join(htmlroot, project, 'index.html')))

    return allProjects

def generateProjectDocumentation(generator, projhtml, projroot, newsfile, name, allProjects):
    doclist = []
    description = ''

    if os.path.exists(newsfile):
        newshtml = os.path.join(projhtml, 'news.html')
        doclist.append(('Current NEWS', newshtml))
        content = open(newsfile, 'r').read()

        parts =  publish_parts(
            source=content,
            source_path=os.path.basename(newsfile),
            writer_name='html',
            settings_overrides=dict(
                input_encoding='utf-8',
                initial_header_level=2,
            ))

        title=parts['title']
        if not title:
            title = os.path.splitext(fn)[0]
        generator.emitHTML(
            newshtml,
            'documentation-doc.html',

            name=name,
            title=Markup(title),
            body=parts['body'],
            bottommenu=allProjects,
        )

    for fn in os.listdir(projroot):
        if fn.endswith('.html') or fn in ('.svn', 'CVS'):
            continue

        elif fn == 'index.txt':
            # XXX: This is not quite right, but the index will always
            # be generated at the moment.
            continue

        if fn.endswith('.txt'):
            content = open(os.path.join(projroot, fn), 'r').read()

            parts =  publish_parts(
                source=content,
                source_path=fn,
                writer_name='html',
                settings_overrides=dict(
                    input_encoding='utf-8',
                    initial_header_level=2,
                ))

            docurl = os.path.splitext(fn)[0] + '.html'
            while docurl[0].isdigit():
                docurl = docurl[1:]
            docurl = os.path.join(projhtml, docurl)
            title=parts['title']
            if not title:
                title = os.path.splitext(fn)[0]
            doclist.append((Markup(title), docurl))

            generator.emitHTML(
                docurl,
                'documentation-doc.html',

                name=name,
                title=Markup(title),
                body=parts['body'],
                bottommenu=allProjects,
            )

        elif os.path.isdir(os.path.join(projroot, fn)):
            if not os.path.exists(os.path.join(projroot, fn, 'index.txt')):
                print "WARNING: ignoring file", fn
                continue

            tutroot = os.path.join(projroot, fn)

            tuthtml = fn
            while tuthtml[0].isdigit():
                tuthtml = tuthtml[1:]
            tuthtml = os.path.join(projhtml, tuthtml)
            for fn in os.listdir(tutroot):
                if fn in ('.svn', 'CVS'):
                    continue

                if os.path.isdir(os.path.join(tutroot, fn)):
                    indir = os.path.join(tutroot, fn)
                    outfn = generator.localPathForSitePath(os.path.join(tuthtml, fn + '.zip'))
                    zf = zipfile.ZipFile(outfn, 'w')
                    for dirpath, dirnames, filenames in os.walk(indir):
                        if '.svn' in dirnames:
                            dirnames.remove('.svn')

                        relpath = dirpath[len(indir):]
                        for fn in filenames:
                            if relpath:
                                zipname = os.path.join(relpath, fn)
                            else:
                                zipname = fn

                            zf.write(os.path.join(dirpath, fn), zipname, zipfile.ZIP_DEFLATED)
                    zf.close()

                elif fn.endswith('.html'):
                    continue

                elif fn.endswith('.txt'):
                    content = open(os.path.join(tutroot, fn), 'r').read()

                    parts =  publish_parts(
                        source=content,
                        source_path=fn,
                        writer_name='html',
                        settings_overrides=dict(
                            input_encoding='utf-8',
                            initial_header_level=2,
                        ))

                    tuturl = os.path.splitext(fn)[0] + '.html'
                    tuturl = os.path.join(tuthtml, tuturl)
                    title=parts['title']
                    if not title:
                        title = os.path.splitext(fn)[0]

                    if fn == 'index.txt':
                        doclist.append((Markup(title), tuturl))

                    generator.emitHTML(
                        tuturl,
                        'documentation-doc.html',

                        name=name,
                        title=Markup(title),
                        body=parts['body'],
                        bottommenu=allProjects,
                    )

                else:
                    fullpath = os.path.join(tutroot, fn)
                    lexer = get_lexer_for_filename(fullpath)
                    formatter = HtmlFormatter(linenos = False, cssclass='source')
                    result = highlight(open(fullpath, 'r').read(), lexer, formatter)
                    style=formatter.get_style_defs()

                    tuturl = fn + '.html'
                    tuturl = os.path.join(tuthtml, tuturl)

                    generator.emitHTML(
                        tuturl,
                        'documentation-source.html',

                        title=fn,
                        body=result,
                        style=style,
                        bottommenu=allProjects,
                    )
                                                                                

        else:
            print "WARNING: ignoring file", fn

    
    generator.emitHTML(
        os.path.join(projhtml, 'index.html'),
        'documentation-project-index.html',

        name=name,
        documents=doclist,
        description=description,

        bottommenu=allProjects,
    )

    return description, doclist

def generateDocs(generator, htmlroot, sourceroot, projects):
    allProjects = makeBottomMenu(htmlroot, sourceroot, projects)
    documentListing = []

    log.info("Generating documentation")

    for project in projects:
        projroot = os.path.join(sourceroot, project, 'Doc')
        newsfile = os.path.join(sourceroot, project, 'NEWS.txt')
        if not os.path.exists(projroot) and not os.path.exists(newsfile):
            continue

        else:
            name = nameForProject(project)
            log.info(" - %s (%s)"%(name, project))

            projhtml = os.path.join(htmlroot, project)

            description, projdocs = generateProjectDocumentation(
                generator, projhtml, projroot, newsfile, name, allProjects)
            documentListing.append((name, description, projdocs))

    generator.emitHTML(
        os.path.join(htmlroot, 'index.html'),
        'documentation-index.html',

        documentation_sections=documentListing,
        bottommenu=allProjects)
