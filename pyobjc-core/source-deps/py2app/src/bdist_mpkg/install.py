import sys
import distutils.command

import bdist_mpkg.command
distutils.command.__all__.append('bdist_mpkg')
sys.modules['distutils.command.bdist_mpkg'] = bdist_mpkg.command
setattr(distutils.command, 'bdist_mpkg', bdist_mpkg.command)
