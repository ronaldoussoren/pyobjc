import DocArticle
import os
import subprocess
from distutils.dep_util import newer

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
    yield os.path.dirname(os.path.dirname(DocArticle.__file__))
    for path in os.environ.get('PATH', '/usr/bin:/usr/local/bin').split(':'):
        yield path

for path in _iter_paths():
    TOOL = os.path.join(path, 'docarticle.py')
    if os.path.exists(TOOL):
        break
else:
    TOOL = None

def build_html():
    if TOOL is None:
        print "*** Can't generate HTML, docarticle.py is missing"
        return
    os.path.walk('Doc', rest2HTML, ['Doc/announcement.txt'])
    rest2HTML(None, '.', ['Install.txt', 'ReadMe.txt', 'Examples/00ReadMe.txt', 'Installer Package/10.2/ReadMe.txt', 'Installer Package/10.3/ReadMe.txt', 'ProjectBuilder Extras/Project Templates/00README.txt', 'NEWS'])
    if os.path.exists('ProjectBuilder Extras/Project Templates/00README.html'):
            os.rename('ProjectBuilder Extras/Project Templates/00README.html', 'Doc/ProjectBuilder-Templates.html')
