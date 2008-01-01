"""
Some distutils commands that make it easier to work with the metadata in a
project:

* update_metadata 

  This command runs the metadata generator and refreshes the 
  PyObjC.bridgesupport file.

* update_exceptions

  This command runs the metadata generator and refreshes the metadata
  exceptions file.

* build_html

  Convert documentation in the 'Doc' directory from text to HTML using
  docutils. Requires docutils to be installed.

* bdist_mpkg

  A subclass of the generic bdist_mpkg command that will automaticly include
  documentation and examples as well (when these are present).

  (This one is not actually defined here, we just change the configuration
  of the standard bdist_mpkg command).

* update_static_inlines

  Update wrapper module for static inline functions

"""
__all__ = [ 'extra_cmdclass', 'extra_options' ]

from setuptools import Command
from distutils.dep_util import newer
from distutils.command.build import build as base_build
import subprocess
import os, sys
from PyObjCMetaData.et import *

# Additional schemes for bdist_mpkg
CUSTOM_SCHEMES=dict(
    docs=dict(
        description=u"(Optional) Documentation for the %(framework)s wrapper",
        prefix=u'/Developer/Documentation/Python/PyObjC/%(framework)s',
        source='Doc',
    ),
    examples=dict(
        description=u"(Optional) Examples for the %(framework)s wrapper",
        prefix=u'/Developer/Examples/Python/PyObjC/%(framework)s',
        source='Examples',
    )
)


#
# Implementation for update_metadata and update_exceptions
#


def _path_to_script(scriptname):
    """
    Return the full path of a python script. 

    Scripts are usually installed in ${sys.prefix}/bin, but Apple has tweaked
    the system python on Leopard to install in /usr/local/bin instead.
    """
    if sys.prefix.startswith('/System') and os.uname()[2] >= '9.':
        return os.path.join('/usr/local/bin', scriptname)
    return os.path.join(sys.prefix, 'bin', scriptname)


class BaseCommand (Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


    def get_files(self):
        files = [ fn for fn in os.listdir('Exceptions') if fn.endswith('.bridgesupport') ]
        if not files:
            raise RuntimeError, "Cannot find exception file"

        for fn in files:
            exceptionsfile = os.path.join('Exceptions', fn)
            framework = os.path.splitext(fn)[0]
            metadatafile = os.path.join('Lib', framework, 
                    'PyObjC.bridgesupport')
            if not os.path.exists(metadatafile):
                for subdir in os.listdir('Lib'):
                    metadatafile = os.path.join('Lib', subdir, framework,
                            'PyObjC.bridgesupport')
                    if os.path.exists(metadatafile):
                        break
                else:
                    metadatafile = os.path.join('Lib', framework, 
                        'PyObjC.bridgesupport')

            yield framework, exceptionsfile, metadatafile

class update_exceptions (BaseCommand):
    description = "Update the metadata exceptions file"

    def run(self):
        for framework, exceptionsfile, metadatafile in self.get_files():
            result = subprocess.call([
                _path_to_script('pyobjc-metadata-gen'), 
                '-v',
                '-f', framework,
                '-F', 'both',
                '-e', exceptionsfile,
                '-o', metadatafile,
                '-O', exceptionsfile,
                ])
            if result != 0:
                raise RuntimeError, "Updating metadata failed"

class update_metadata (BaseCommand):
    description = "Update the metadata file"

    def run(self):
        for framework, exceptionsfile, metadatafile in self.get_files():
            result = subprocess.call([
                _path_to_script('pyobjc-metadata-gen'), 
                '-v',
                '-f', framework,
                '-F', 'final-md',
                '-e', exceptionsfile,
                '-o', metadatafile])
            if result != 0:
                raise RuntimeError, "Updating metadata failed"

#
# Implementation for the build_html command
# 

def rest2HTML(irrelevant, dirName, names):
    while '.svn' in names:
        names.remove('.svn')
    for aName in names:
        if aName.endswith('.txt'):
            anInputPath = os.path.join(dirName, aName)
            if irrelevant is not None and anInputPath in irrelevant:
                continue
            anOutputPath = anInputPath[:-4] + '.html'
            if not newer(anInputPath, anOutputPath):
                print '- %s (skipped: up to date)' % (anInputPath,)
                continue
            print '- %s'%(anInputPath)
            outfile = file(anOutputPath, 'w')
            ret = subprocess.call([TOOL, anInputPath], stdout=outfile)
            outfile.close()
            if ret:
                os.remove(anOutputPath)

def _iter_paths():
    try:
        import DocArticle
    except ImportError:
        return
    yield os.path.dirname(os.path.dirname(DocArticle.__file__))
    for path in os.environ.get('PATH', '/usr/bin:/usr/local/bin').split(':'):
        yield path

for path in _iter_paths():
    TOOL = os.path.join(path, 'docarticle.py')
    if os.path.exists(TOOL):
        break
else:
    TOOL = None

class build_html(Command):
    description = "Generate HTML from ReST documentation"
    user_options = []

    def initialize_options(self):
        self.finalized = False

    def finalize_options(self):
        self.finalized = True

    def run(self):
        if TOOL is None:
            print "*** Can't generate HTML, docutils is not installed"
            return

        os.path.walk('Doc', rest2HTML, [])


INLINES_HEADER="""\
#include "Python.h"
#import <%(framework)s/%(framework)s.h>

typedef void (*FUNCTION)(void);

struct function_map {
    const char* name;
    FUNCTION    function;
} function_map[] = {
"""

INLINES_FOOTER="""\
    { 0, 0 }
};

static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};

void init_inlines(void)
{
    PyObject* m = Py_InitModule4("_inlines", mod_methods, NULL, NULL, PYTHON_API_VERSION);

    PyModule_AddObject(m, "_inline_list_", 
        PyCObject_FromVoidPtr(function_map, NULL));
}
"""

class update_static_inlines (BaseCommand):
    def run(self):
        for  framework, exceptionsfile, metadatafile in self.get_files():
            meta = ET.parse(metadatafile).getroot()
            inlines = [ e.get('name') for e in meta.findall('function') if e.get('inline', 'false') == 'true' ]
            fn = os.path.join('Modules', '_%s_inlines.m'%(framework,))
            if not inlines:
                if os.path.exists(fn):
                    print " *** %s exists, but no inlines left"%(fn,)

                else:
                    # No inlines.m present and no inlines: just go to the
                    # next metadata file.
                    continue

            else:
                if not os.path.exists(fn):
                    print " *** added %s, please add a new extension to setup.py"%(fn,)

            fp = open(fn, 'w')
            fp.write(INLINES_HEADER % locals())
            for nm in inlines:
                fp.write('\t{"%s", (FUNCTION)&%s },\n'%(nm, nm))
            fp.write(INLINES_FOOTER)


#
# Setup our public interface
#

def _mpkg_options(framework):
    """
    Generate additional options for bdist_mpkg.
    """

    custom_schemes = CUSTOM_SCHEMES.copy()
    if not os.path.exists('Doc'):
        del custom_schemes['docs']
    if not os.path.exists('Examples'):
        del custom_schemes['examples']

    for scheme in custom_schemes.values():
        for k in scheme.keys():
            scheme[k] = scheme[k] % locals()

    opts = dict(
        custom_schemes=custom_schemes,
        readme='README.txt',
        license='LICENSE.txt',
    )

    if 'docs' in custom_schemes:
        opts['scheme_command'] = dict(docs='build_html')

    if not os.path.exists('README.txt'):
        del opts['readme']

    if not os.path.exists('LICENSE.txt'):
        del opts['license']

    return opts


extra_cmdclass = {
    'update_static_inlines': update_static_inlines,
    'update_metadata': update_metadata, 
    'update_exceptions': update_exceptions,
}

if os.path.exists('Doc'):
    extra_cmdclass['build_html'] = build_html

def extra_options(framework):
    """
    Return a dictionary with additional distutils options.

    Usage:

    setup=(
        ...
        options=extra_options('AppKit'),
    )
    """
    return {
        'bdist_mpkg': _mpkg_options(framework),
    }
