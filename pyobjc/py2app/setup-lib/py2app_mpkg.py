import os
import sys
import setuptools
from py2app.util import skipjunk

_bdist_mpkg = setuptools.Distribution().get_command_class('bdist_mpkg')
class bdist_mpkg(_bdist_mpkg):
    def initialize_options(self):
        _bdist_mpkg.initialize_options(self)
        self.scheme_descriptions['tools'] = u'(Optional) py2app tools'
        self.scheme_map['tools'] = '/Developer/Applications/Python Tools/py2app'

        self.scheme_descriptions['examples'] = u'(Optional) py2app example code'
        self.scheme_map['examples'] = '/Developer/Python/py2app/Examples'
        self.scheme_copy['examples'] = 'examples'

        self.scheme_descriptions['doc'] = u'(Optional) py2app documentation'
        self.scheme_map['doc'] = '/Developer/Python/py2app/Documentation'
        self.scheme_copy['doc'] = 'doc'

    def run_extra(self):
        self.py2app_tools()

    def copy_tree(self, *args, **kw):
        if kw.get('condition') is None:
            kw['condition'] = skipjunk
        return _bdist_mpkg.copy_tree(self, *args, **kw)

    def py2app_tools(self):
        scheme = 'tools'
        source = 'tools'
        schemedir = os.path.abspath(self.get_scheme_install_target(scheme))
        builddir = os.path.abspath(os.path.join(self.bdist_base, scheme))
        for root, dirs, files in os.walk(source):
            if '.svn' in dirs:
                dirs.remove('.svn')
            if 'setup.py' not in files:
                continue
            setupfile = os.path.abspath(os.path.join(root, 'setup.py'))
            tool = os.path.basename(os.path.dirname(setupfile))
            args = [
                'py2app', '--strip', '--dist-dir=' + schemedir,
                '--bdist-base=' + os.path.join(builddir, tool)
            ]
            self.sub_setup(setupfile, args)

cmdclass = {'bdist_mpkg': bdist_mpkg}
