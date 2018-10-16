'''
Wrappers for the "CoreAudio" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

#
# Distutils doesn't undestand '.mm' as an extension
#
import distutils.unixccompiler
distutils.unixccompiler.UnixCCompiler.src_extensions.append('.mm')

setup(
    name='pyobjc-framework-CoreAudio',
    description = "Wrappers for the framework CoreAudio on macOS",
    packages = [ "CoreAudio" ],
    ext_modules = [
         Extension('CoreAudio._inlines',
            [ 'Modules/_CoreAudio_inlines.mm' ],
            extra_link_args=['-framework', 'CoreAudio']),
        Extension("CoreAudio._CoreAudio",
            [ "Modules/_CoreAudio.m" ],
            extra_link_args=["-framework", "CoreAudio"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreAudio')
            ]
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
