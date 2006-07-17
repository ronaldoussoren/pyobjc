import os
HDIUTIL = '/usr/bin/hdiutil'
if not os.path.exists(HDIUTIL):
    raise ImportError("hdiutil not present")

import sys
import shutil
from distutils.dep_util import newer
from setuptools import Command
from pyobjc_setup_utils import runtasks
from macosx_version import sw_vers

OSX_VERSION = sw_vers()

DMG_FILES = filter(None,
"""
HISTORIC.txt
Install.html
Install.txt
License.txt
NEWS.txt
NEWS.html
ReadMe.html
ReadMe.txt
""".splitlines())

class bdist_dmg(Command):
    description = "Create a Mac OS X disk image with the binary installer"
    user_options = [
        ('release-dir=', None,
         'Release directory [default: release]'),
    ]

    def initialize_options(self):
        self.release_dir = 'release'
        self.finalized = False

    def finalize_options(self):
        self.finalized = True

    def run(self):
        print "Creating a simple disk image"
        dist = self.distribution
        ident = '%s-python%s-macosx%s' % (
            dist.get_fullname(),
            sys.version[:3],
            '.'.join(map(str, OSX_VERSION.version[:2])),
        )
        release_temp = os.path.join(self.release_dir, ident)
        release_file = release_temp + '.dmg'

        mpkg = self.reinitialize_command('bdist_mpkg', reinit_subcommands=1)
        mpkg.dist_dir = release_temp
        mpkg.keep_temp = True
        mpkg.ensure_finalized()
        mpkg.run()
        for fn in DMG_FILES:
            self.copy_file(fn, os.path.join(release_temp, fn))
        runtasks("Creating " + release_file, [
            HDIUTIL, 'create',
            '-ov',
            '-imagekey', 'zlib-level=9',
            '-srcfolder', release_temp,
            release_file,
        ])

cmdclass = dict(bdist_dmg=bdist_dmg)
