"""
Code for converting an example in a repository checkout to data on the PyObjC
website

A sample of the website consists of a zipfile with all code for the sample,
and index.html with a description of the example and furthermore HTML files
with colorized source code.
"""

__all__ = ('convertSample',)

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

from docutils.core import publish_parts

from genshi.template import MarkupTemplate, TemplateLoader

from distutils import log


import zipfile
import os
import shutil

gSkipDirectories = ('.svn', 'CVS')
gZipTemplate = "PyObjCExample-%s.zip"

gTemplateDir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'templates')
gTemplateLoader = TemplateLoader(gTemplateDir)

def zipDirectory(outputname, inputdir):
    """
    Create a zipfile containing all files in a directory, but skipping
    version-management turds.
    """

    zf = zipfile.ZipFile(outputname, 'w')
    basename = os.path.basename(outputname)[:-4]

    while inputdir.endswith(os.path.sep):
        inputdir = inputdir[:-1]

    for dirpath, dirnames, filenames in os.walk(inputdir):
        for name in gSkipDirectories:
            if name in dirnames:
                dirnames.remove(name)

        # Relpath is the directory name in the zipfile,
        # prepend the sample name to ensure we don't extract
        # into the current directory.
        relpath = dirpath[len(inputdir)+1:]
        relpath = os.path.join(basename, relpath)

        for fn in filenames:
            zf.write(
                os.path.join(dirpath, fn), 
                os.path.join(relpath, fn),
                zipfile.ZIP_DEFLATED)
    zf.close()

def colorizeSources(inputdir, outputdir):
    """
    Return a list of colorized files:
        [(relativepath, coloredName, html-style, html-body), ...]

    This will *not* write the actual files
    """

    coloredFiles = []

    for dirpath, dirnames, filenames in os.walk(inputdir):
        for name in gSkipDirectories:
            if name in dirnames:
                dirnames.remove(name)
        
        for name in dirnames:
            # Don't bother looking inside nib files.
            if name.endswith('.nib'):
                dirnames.remove(name)

        relpath = dirpath[len(inputdir)+1:]

        for fn in sorted(filenames):
            if relpath:
                path = os.path.join(relpath, fn)
            else:
                path = fn


            ext = os.path.splitext(fn)[-1]
            if ext not in ('.py', '.pyw', '.m', '.h'):
                # Skip all files that aren't clearly source code
                continue

            colorFn = 'source--%s.html' % (path.replace(os.path.sep, '-'),)

            fullpath = os.path.join(dirpath, fn)
            lexer = get_lexer_for_filename(fullpath)
            formatter = HtmlFormatter(linenos = False, cssclass='source')
            result = highlight(open(fullpath, 'r').read(), lexer, formatter)
            style=formatter.get_style_defs()
            coloredFiles.append((path, colorFn, style, result))

    return coloredFiles

def restToHTML(inputFile):
    """
    Read a reStructuredText file and return the HTML representation of it
    """
    input = open(inputFile, 'rU').read()
    output = publish_parts(
            source=input,
            source_path=inputFile,
            writer_name='html', 
            settings_overrides=dict(
                input_encoding='utf-8',
                initial_header_level=2,
            ))
    #print output.keys()

    return output['html_body']



def convertSample(name, inputdir, outputdir):
    """
    Convert an example from the source tree to part of the website

    Returns a small summary of the example.
    """

    if os.path.exists(outputdir):
        shutil.rmtree(outputdir)
    os.makedirs(outputdir)

    zipname = gZipTemplate % name
    zipDirectory(os.path.join(outputdir, zipname), inputdir)

    coloredFiles = colorizeSources(inputdir, outputdir)

    readme = os.path.join(inputdir, "ReadMe.txt")
    summary = os.path.join(inputdir, "Summary.txt")

    if os.path.exists(readme):
        readme = restToHTML(readme)

    elif os.path.exists(summary):
        readme = restToHTML(summary)


    else:
        readme = "A PyObjC Example without documentation"

    tmpl = MarkupTemplate(
            open(os.path.join(gTemplateDir, "sample-index.html"), 'r').read(),
            loader=gTemplateLoader)
    stream = tmpl.generate(
            title=name,
            sources=[item[:2] for item in coloredFiles],
            zipname=zipname,
            readme=readme,
            )
    fp = open(os.path.join(outputdir, "index.html"), 'w')
    fp.write(stream.render('html'))
    fp.close()


    tmpl = MarkupTemplate(
            open(os.path.join(gTemplateDir, "sample-source.html"), 'r').read(),
            loader=gTemplateLoader)
    for realpath, htmlpath, style, body in coloredFiles:
        sources=[item[:2] for item in coloredFiles if item[1] != htmlpath]
        sources.insert(0, (realpath, htmlpath))
        stream = tmpl.generate(
            title='%s -- %s'%(name, realpath),
            sources=sources,
            style=style,
            zipname=zipname,
            body=body)
        fp = open(os.path.join(outputdir, htmlpath), 'w')
        fp.write(stream.render('html'))
        fp.close()

    # XXX: We should extract a small summary from the readme file to use
    # on the sample index package (and not a seperate summary file).
    if os.path.exists(summary):
        return restToHTML(summary)
    return ""

def samplesForProject(title, package, inputdir, outputdir):
    inputdir = os.path.join(inputdir, 'Examples')
    outputdir = os.path.join(outputdir, package)
    if os.path.exists(outputdir):
        shutil.rmtree(outputdir)

    if not os.path.exists(inputdir):
        return None

    samples = []
    for dirpath, dirnames, filenames in os.walk(inputdir):
        for dn in dirnames:
            if os.path.exists(os.path.join(dirpath, dn, 'setup.py')):
                # Found a sample
                relpath = os.path.join(dirpath[len(inputdir)+1:], dn)
                summary = convertSample(dn, os.path.join(dirpath, dn),
                        os.path.join(outputdir, relpath))
                samples.append((relpath, dn, summary))

    if samples:
        tmpl = MarkupTemplate(
            open(os.path.join(gTemplateDir, "sample-framework-index.html"), 'r').read(),
            loader=gTemplateLoader)
        stream = tmpl.generate(
            title="Examples for %s" % (title,),
            samples=samples)
        fp = open(os.path.join(outputdir, "index.html"), 'w')
        fp.write(stream.render('html'))
        fp.close()
    return samples

def generateSamples(basedir, outputdir, frameworkList):
    log.info("Generating HTML for sample code")
    allSamples = []
    if os.path.exists(outputdir):
        shutil.rmtree(outputdir)

    for nm in frameworkList:
        title = 'The %s framework' % ( nm[len('pyobjc-framework-'):], )
        log.info(" - %s" % title)
        listing = samplesForProject(
                title,
                nm,
                os.path.join(basedir, nm),
                outputdir)

        if listing:
            allSamples.append((title, nm, listing))

    if allSamples:
        tmpl = MarkupTemplate(
            open(os.path.join(gTemplateDir, "sample-global-index.html"), 'r').read(),
            loader=gTemplateLoader)
        stream = tmpl.generate(
            samplelist=allSamples)
        fp = open(os.path.join(outputdir, "index.html"), 'w')
        fp.write(stream.render('html'))
        fp.close()



if __name__ == "__main__":
    #convertSample("ClassBrowser", "../../pyobjc-framework-Cocoa/Examples/AppKit/ClassBrowser", "samples/ClassBrowser")
    #convertSample("AutoSample", "../../pyobjc-framework-Automator/Examples/AutoSample", "samples/AutoSample")
    samplesForProject('TTILE', 'pyobjc-framework-Cocoa', '../../pyobjc-framework-Cocoa', 'samples')
