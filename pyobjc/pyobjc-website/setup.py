"""
A simple setup.py file for building and publishing the website. 

Usage:
    python setup.py build

       This will regenerate the website from the current checkout

    python setup.py publish [--skip-build]

       This will upload the website to the server, building it beforehand
       unless the ``--skip-build`` option is used.

Note that this is *NOT* a valid python package, we just use setuptools 
facilities to ensure that all software we need is actually present.
"""
from setuptools import Command, setup

from distutils.errors  import DistutilsError
from distutils import log


import sys, os

# The truly interesting code is in the 'lib' directory, make that available.
sys.path.append('lib')

import sitegen
import samples



#
# Distutils command definitions
#

class buildsite (Command):
    description = "Build the website"
    user_options = []

    def initialize_options(self):
        self.finalized = False

    def finalize_options(self):
        self.finalized = True


    def run(self):
        if not os.path.exists('../pyobjc-core'):
            raise DistutilsError(
                    "Run me in a complete checkout of the pyobjc trunk")

        frameworkList = [dn for dn in os.listdir('..') if dn.startswith('pyobjc-framework') ]
        #frameworkList = ['pyobjc-framework-Cocoa']

        generator = sitegen.SiteGenerator('templates', 'htdocs')

        log.info("Copying static resources")
        for subdir in os.listdir('resources'):
            if subdir.startswith('.'): continue
            log.info(" - %s" % (subdir,))
            generator.copy(os.path.join('resources', subdir), subdir)

        log.info("Copying static HTML")
        for fn in os.listdir('static'):
            if fn.startswith('.'): continue
            log.info(" - %s" % (fn,))
            generator.copyReST(os.path.join('static', fn), os.path.splitext(fn)[0] + '.html')

        samples.generateSamples(generator, '/examples', '..', frameworkList)

class publishsite (Command):
    description = "Publish the website"
    user_options = [
        ('skip-build', None,
            "Skip the build phase")
    ]


    def initialize_options(self):
        self.finalized = False
        self.skip_build = False

    def finalize_options(self):
        self.finalized = True


    def run(self):
        if not self.skip_build:
            self.run_command('build')

        raise DistutilsError("publishsite is not implemented yet")


#
# Run distutils
#

setup(
        name = "pyobjc-website",
        description = "PyObjC's website",
        cmdclass=dict(
            build=buildsite,
            publish=publishsite,
        ),
        setup_requires = [
            'docutils >=0.4',
            'Genshi >=0.4',
            'Pygments',
        ]
)
