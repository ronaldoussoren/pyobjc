#!/usr/bin/env python
"""
Script for updating the HTML documentation. This uses docutils and DocArticle.
The latter can be found in the docutils sandbox.

Usage:
        python Scripts/update_html.py 

"""

import sys
import getopt
import os
import errno
import shutil

PYTHON=sys.executable

def rest2HTML(irrelevant, dirName, names):
    for aName in names:
        if aName.endswith('.txt') or aName == 'NEWS':
            anInputPath = os.path.join(dirName, aName)
            if irrelevant is not None and anInputPath in irrelevant:
                continue
            anOutputPath = os.path.splitext(anInputPath)[0] + '.html'
            print '- %s'%(anInputPath)
            os.system("docarticle.py '%s' > '%s' || rm '%s'"%(
                escquotes(anInputPath), escquotes(anOutputPath), 
                escquotes(anOutputPath)))

def escquotes(val):
	return val.replace("'", "'\"'\"'")

print "Generateing HTML documentation"
os.path.walk('Doc', rest2HTML, ['Doc/announcement.txt'])
rest2HTML(None, '.', ['NEWS', 'Install.txt', 'ReadMe.txt', 'Examples/00ReadMe.txt', 'Installer Package/ReadMe.txt', 'ProjectBuilder Extras/Project Templates/00README.txt'], )
os.rename('ProjectBuilder Extras/Project Templates/00README.html', 'Doc/ProjectBuilder-Templates.html')
