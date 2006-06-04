import os
if not os.path.exists('/usr/bin/sw_vers'):
    # detect Mac OS X
    raise ImportError('Not Mac OS X')

import sys
from distutils.version import LooseVersion
from distutils import log
from bdist_mpkg.command import bdist_mpkg as _bdist_mpkg
from py2app.util import skipfunc, skipjunk

from altgraph.compat import *
from bdist_mpkg import tools

# XXX - not used
SCHEME_REMOVE = dict(
    # This should take care of any previous version of PyObjC
    platlib = [
        'PyObjC',
        'PyObjC.pth',
    ],
    # Remove old examples and documentation
    examples = ['.'],
    documentation = ['.'],
    # Remove old nibclassbuilder
    scripts = ['nibclassbuilder'],
    # Remove old Xcode templates
    xcode = [
        'File Templates/Cocoa/Python NIB class.pbfiletemplate',
        'File Templates/Cocoa/Python class.pbfiletemplate',
        'Pure Python',
        'Project Templates/Application/Cocoa-Python Application',
        'Project Templates/Application/Cocoa-Python Document-based Application',
    ],
)

CUSTOM_SCHEMES = dict(
    xcode=(
        u'(Optional) Xcode File and Project templates for PyObjC',
        '/Library/Application Support/Apple/Developer Tools',
        'Xcode',
    ),
    docs=(
        u'(Optional) PyObjC Documentation',
        '/Developer/Python/PyObjC/Documentation',
        'Doc',
    ),
    examples=(
        u'(Optional) PyObjC Example Code',
        '/Developer/Python/PyObjC/Examples',
        'Examples',
    ),
)

SUBPROJECT_SCHEMES = dict(
    py2app='source-deps/py2app-source/setup.py',
)


class pyobjc_bdist_mpkg(_bdist_mpkg):
    def initialize_options(self):
        _bdist_mpkg.initialize_options(self)
        self.readme = 'Installer Package/%s/Resources/ReadMe.txt' % (
            '.'.join(map(str, self.macosx_version.version[:2])),
        )
        schemes = CUSTOM_SCHEMES.copy()
        if self.macosx_version < LooseVersion('10.3'):
            del schemes['xcode']
        for scheme, (description, prefix, source) in schemes.iteritems():
            self.scheme_descriptions[scheme] = description
            self.scheme_map[scheme] = prefix
            self.scheme_copy[scheme] = source
        self.scheme_command['doc'] = 'build_html'
        self.scheme_subprojects.update(SUBPROJECT_SCHEMES)

    def copy_tree(self, *args, **kw):
        if kw.get('condition') is None:
            kw['condition'] = skipjunk
        return _bdist_mpkg.copy_tree(self, *args, **kw)

cmdclass = {'bdist_mpkg': pyobjc_bdist_mpkg}
