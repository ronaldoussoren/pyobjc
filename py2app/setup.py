#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

import sys, os
from setuptools import setup, find_packages
from pkg_resources import require, DistributionNotFound

cmdclass = {}
if 0:
    try:
        require("bdist_mpkg>=0.4")
    except DistributionNotFound:
        pass
    else:
        sys.path.insert(1, 'setup-lib')
        import py2app_mpkg
        cmdclass.update(py2app_mpkg.cmdclass)

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
    name='py2app',
    version='0.4.1',
    description='Create standalone Mac OS X applications with Python',
    author='Bob Ippolito',
    author_email='bob@redivi.com',
    url='http://undefined.org/python/#py2app',
    download_url='http://undefined.org/python/#py2app',
    license='MIT or PSF License',
    platforms=['MacOS X'],
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    #setup_requires=[
    #    "bdist_mpkg>=0.4.2",
    #],
    install_requires=[
        "altgraph>=0.6.7",
        "modulegraph>=0.7",
        "macholib>=1.1",
        "bdist_mpkg>=0.4",
    ],

    # sources
    cmdclass=cmdclass,
    packages=find_packages(exclude=["ez_setup"]),
    package_data={
        'py2app.apptemplate': [
            'prebuilt/main',
            'lib/__error__.sh',
            'lib/site.py',
            'src/main.c',
        ],
        'py2app.bundletemplate': [
            'prebuilt/main',
            'lib/__error__.sh',
            'lib/site.py',
            'src/main.m',
        ],
    },
    entry_points={
        'distutils.commands': [
            "py2app = py2app.build_app:py2app",
        ],
        'distutils.setup_keywords': [
            "app = py2app.build_app:validate_target",
            "plugin = py2app.build_app:validate_target",
        ],
        'console_scripts': [
            "py2applet = py2app.script_py2applet:main",
        ],
    },
    zip_safe=False,
    # workaround for setuptools 0.6b4 bug
    dependency_links=[],
)
