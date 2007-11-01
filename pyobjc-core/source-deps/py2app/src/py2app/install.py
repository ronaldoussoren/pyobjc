"""
'import py2app' imports this package, and two magic things happen:

- the 'py2app.build_app' submodule is imported and installed as
  'distutils.command.py2app' command

- the default distutils Distribution class is replaced by the
  special one contained in this module.
"""

import sys
import distutils.dist
import distutils.core
import distutils.command
import py2app.command

class Distribution(distutils.dist.Distribution):

    def __init__(self, attrs):
        self.app = []
        self.plugin = []
        self.zipfile = "site-packages.zip"

        distutils.dist.Distribution.__init__(self, attrs)

distutils.core.Distribution = Distribution

distutils.command.__all__.append('py2app')
sys.modules['distutils.command.py2app'] = py2app.command
setattr(distutils.command, 'py2app', py2app.command)
