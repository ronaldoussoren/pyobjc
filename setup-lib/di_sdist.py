"""
Custom 'sdist' action for setup.py
"""

# distutils doesn't know about subversion and I'm to lazy to reverse engineer
# distutils in the hope of detecting how to specify that all svn directories
# should be removed.
from distutils.command.sdist import sdist as sdist_base

class cmd_sdist (sdist_base):

    def prune_file_list(self):
        sdist_base.prune_file_list(self)
        self.filelist.exclude_pattern(r'/\.svn/.*$', is_regex=1)
        self.filelist.exclude_pattern(r'/build/.*$', is_regex=1)
        self.filelist.exclude_pattern(r'/.*~\.nib/.*$', is_regex=1)
