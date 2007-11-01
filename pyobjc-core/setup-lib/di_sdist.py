"""
Custom 'sdist' action for setup.py
"""

# distutils doesn't know about subversion and I'm to lazy to reverse engineer
# distutils in the hope of detecting how to specify that all svn directories
# should be removed.
import setuptools
sdist_base = setuptools.Distribution().get_command_class('sdist')

class sdist (sdist_base):

    def run(self):
        self.run_command('build_html')
        sdist_base.run(self)

    def prune_file_list(self):
        sdist_base.prune_file_list(self)
        self.filelist.exclude_pattern(r'/\.svn/.*$', is_regex=1)
        self.filelist.exclude_pattern(r'/build/.*$', is_regex=1)
        self.filelist.exclude_pattern(r'/.*~\.nib/.*$', is_regex=1)

cmdclass = dict(sdist=sdist)
