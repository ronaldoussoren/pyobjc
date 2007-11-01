import os
import subprocess
from distutils.dep_util import newer
from setuptools import Command

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
        os.path.walk('Doc', rest2HTML, ['Doc/announcement.txt'])
        rest2HTML(None, '.', [
            'NEWS.txt', 'Install.txt', 'ReadMe.txt', 'Examples/00ReadMe.txt',
            'Installer Package/10.2/ReadMe.txt',
            'Installer Package/10.3/ReadMe.txt',
            'Installer Package/10.4/ReadMe.txt',
            'Xcode/Project Templates/00README.txt',
        ])
        if os.path.exists('Xcode/Project Templates/00README.html'):
                os.rename('Xcode/Project Templates/00README.html', 'Doc/Xcode-Templates.html')

cmdclass = dict(build_html=build_html)
