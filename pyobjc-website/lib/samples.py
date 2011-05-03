"""
Code for converting an example in a repository checkout to data on the PyObjC
website

A sample of the website consists of a zipfile with all code for the sample,
and index.html with a description of the example and furthermore HTML files
with colorized source code.
"""


from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter

from docutils.core import publish_parts


from distutils import log


import zipfile
import os
import shutil

gSkipDirectories = ('.svn', 'CVS')
gZipTemplate = "PyObjCExample-%s.zip"

def zipDirectory(outputname, inputdir):
    """
    Create a zipfile containing all files in a directory, but skipping
    version-management turds.
    """
    outdn = os.path.dirname(outputname)
    if not os.path.exists(outdn):
        os.makedirs(outdn)

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
            formatter = HtmlFormatter(cssclass='source', linenos='inline')
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



def convertSample(generator, outputdir, name, inputdir, allProjects):
    """
    Convert an example from the source tree to part of the website

    Returns a small summary of the example.
    """

    zipname = gZipTemplate % name
    
    zipDirectory(
            generator.localPathForSitePath(os.path.join(outputdir, zipname)), 
            inputdir)

    coloredFiles = colorizeSources(inputdir, outputdir)

    readme = os.path.join(inputdir, "ReadMe.txt")
    summary = os.path.join(inputdir, "Summary.txt")

    if os.path.exists(readme):
        readme = restToHTML(readme)

    elif os.path.exists(summary):
        readme = restToHTML(summary)


    else:
        readme = "A PyObjC Example without documentation"

    generator.emitHTML(
            os.path.join(outputdir, 'index.html'),
            'sample-index.html',

            title=name,
            sources=[item[:2] for item in coloredFiles],
            zipname=zipname,
            readme=readme,
            bottommenu=allProjects,
            )

    for realpath, htmlpath, style, body in coloredFiles:
        sources=[(item[0], item[1], '') for item in coloredFiles if item[1] != htmlpath]
        sources.insert(0, (realpath, htmlpath, 'selected'))


        generator.emitHTML(
                os.path.join(outputdir, htmlpath),
                'sample-source.html',

                title='%s -- %s'%(name, realpath),
                sources=sources,
                style=style,
                zipname=zipname,
                body=body,
                bottommenu=allProjects)

    # XXX: We should extract a small summary from the readme file to use
    # on the sample index package (and not a seperate summary file).
    if os.path.exists(summary):
        return restToHTML(summary)
    return ""

def haveSamplesForProject(inputdir):
    for dirpath, dirnames, filenames in os.walk(inputdir):
        for dn in dirnames:
            if os.path.exists(os.path.join(dirpath, dn, 'setup.py')):
                return True
    return False

def samplesForProject(generator, outputdir, framework, package, inputdir, allProjects=[]):
    inputdir = os.path.join(inputdir, 'Examples')
    outputdir = os.path.join(outputdir, package)
    if not os.path.exists(inputdir):
        return None

    samples = []
    bottommenu=[]
    if allProjects:
        for title, subdir in allProjects:
            if title == framework:
                bottommenu.append((title, ''))
            else:
                bottommenu.append((title, subdir))

    for dirpath, dirnames, filenames in os.walk(inputdir):
        if '.svn' in dirnames:
            dirnames.remove('.svn')

        toremove=[]

        l = len(samples)
        for dn in dirnames:
            if os.path.exists(os.path.join(dirpath, dn, 'setup.py')):
                # Found a sample
                relpath = os.path.join(dirpath[len(inputdir)+1:], dn)
                summary = convertSample(generator, 
                        os.path.join(outputdir, relpath),
                        dn, os.path.join(dirpath, dn), allProjects)
                samples.append((relpath, dn, summary))
                toremove.append(dn)

        for dn in toremove:
            # Don't peek inside examples for subexamples.
            dirnames.remove(dn)


        if len(samples) != l and dirpath != inputdir:
            # We added some samples from a subdirectory, add subheader.
            relpath = dirpath[len(inputdir)+1:]
            samples.append((relpath, relpath, -1))


    samples.sort()

    if samples:

        generator.emitHTML(
                os.path.join(outputdir, 'index.html'),
                'sample-framework-index.html',
                title="Examples for %s" % (framework,),
                samples=samples,
                bottommenu=bottommenu,
                )
    return samples

def generateSamples(generator, outputdir, basedir, frameworkList):
    log.info("Generating HTML for sample code")
    allSamples = []

    allProjects = []
    for nm in frameworkList:
        framework = '%s' % ( nm[len('pyobjc-framework-'):], )
        if haveSamplesForProject(os.path.join(basedir, nm)):
            allProjects.append((framework, os.path.join(outputdir, nm, 'index.html')))

    for nm in frameworkList:
        framework = '%s' % ( nm[len('pyobjc-framework-'):], )
        log.info(" - %s" % framework)
        listing = samplesForProject(
                generator, 
                outputdir,
                framework,
                nm,
                os.path.join(basedir, nm),
                allProjects)

        if listing:
            allSamples.append((framework, nm, listing))

    if allSamples:
        bottommenu = []
        for framework, nm, listing in allSamples:
            bottommenu.append((framework, os.path.join(nm, 'index.html')))
        generator.emitHTML(
                os.path.join(outputdir, 'index.html'),
                'sample-global-index.html',
                samplelist=allSamples,
                bottommenu=bottommenu)
