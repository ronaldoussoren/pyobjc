#!/usr/bin/env python

import sys, os
# allow py2app to use itself :)
sys.path[1:1] = map(os.path.abspath, ['src', 'setup-lib'])
import bdist_mpkg

from setuptools import setup, find_packages
from di_sdist import cmd_sdist
import py2app_mpkg

cmdclass = {'sdist': cmd_sdist}
cmdclass.update(py2app_mpkg.cmdclass)

packages = find_packages('src')

LONG_DESCRIPTION = file('README.txt').read()

CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X :: Cocoa',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Objective C',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Build Tools',
]

setup(
    # metadata
    name = 'py2app',
    version = '0.1.6',
    description = 'distutils commands for creating MacOS X applications and installer packages',
    author = 'Bob Ippolito',
    author_email = 'bob@redivi.com',
    url = 'http://undefined.org/python/#py2app',
    download_url = 'http://undefined.org/python/#py2app',
    license = 'MIT or PSF License',
    platforms = ['MacOS X'],
    long_description = LONG_DESCRIPTION,
    classifiers = CLASSIFIERS,

    # sources
    extra_path = 'py2app',
    scripts = ['scripts/bdist_mpkg', 'scripts/py2applet'],
    package_dir = {'':'src'},
    packages = packages,
    cmdclass = cmdclass,
    package_data = {
        'py2app.apptemplate': [
            'prebuilt/main',
            'lib/__error__.sh',
            'lib/site.py',
            'src/main.m',
        ],
        'py2app.bundletemplate': [
            'prebuilt/main',
            'lib/__error__.sh',
            'lib/site.py',
            'src/main.m',
        ],
        'bdist_mpkg': [
            'lib/prepanther/InstallationCheck',
            'lib/prepanther/English.lproj/InstallationCheck.strings',
            'lib/postjaguar/InstallationCheck',
            'lib/postjaguar/English.lproj/InstallationCheck.strings',
        ],
    },
)
