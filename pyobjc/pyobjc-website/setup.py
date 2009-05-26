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

import sys, os, shutil, subprocess, stat

# The truly interesting code is in the 'lib' directory, make that available.
sys.path.append('lib')

import sitegen
import samples
import news
import docs



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

        root_menu=[
                ('Home', '/index.html'),
                ('News', '/news.html'),
                ('About', '/about.html'),
                ('History&People', '/people.html'),
                ('Links', '/links.html'),
        ]

        generator = sitegen.SiteGenerator('templates', 'htdocs')

        if os.path.exists('htdocs'):
            shutil.rmtree('htdocs')
        os.mkdir('htdocs')

        log.info("Copying static resources")
        for subdir in os.listdir('resources'):
            if subdir.startswith('.'): continue
            log.info(" - %s" % (subdir,))
            generator.copy(os.path.join('resources', subdir), subdir)



        log.info("Copying static HTML")
        for fn in os.listdir('static'):
            if fn.startswith('.'): continue
            log.info(" - %s" % (fn,))
            generator.copyReST(os.path.join('static', fn), os.path.splitext(fn)[0] + '.html', bottommenu=root_menu)

        log.info("Processing news items")
        newsItems = news.parseNews('news')


        log.info("Emitting news")
        generator.emitHTML("/news.html", "news.html",  news=newsItems, bottommenu=root_menu)
        for item in newsItems:
            # Generate seperate files for the news items, will be used from an RSS feed.
            generator.emitHTML('/news/%s.html'%(item['basename'],), 'news-item.html', newsitem=item, bottommenu=root_menu)

        log.info("Emitting homepage")
        generator.emitHTML("/index.html", "site-index.html",  
                pyobjc_version='2.2b2',
                pyobjc_release_date='May 26th 2009',
                news=news.newsSelection(newsItems),
                bottommenu=root_menu)

        docs.generateDocs(generator, '/documentation', '..', ['pyobjc-core'] + frameworkList)
        samples.generateSamples(generator, '/examples', '..', frameworkList)

class publishsite (Command):
    description = "Publish the website"
    user_options = [
        ('skip-build', None,
            "Skip the build phase"),
        ('username=', None,
            "login to use at SF.net (default to ronaldoussoren)"),
    ]


    def initialize_options(self):
        self.finalized = False
        self.skip_build = False
        self.username = None

    def finalize_options(self):
        if self.username is None:
            self.username = 'ronaldoussoren'

        self.finalized = True


    def run(self):
        if not self.skip_build:
            self.run_command('build')

        # First ensure that files are group-writable, that makes it
        # easier to update the website from several accounts.
        log.info("Makeing files group-writable")
        for dirpath, dirnames, filenames in os.walk('htdocs'):
            for fn in dirnames +filenames:
                st = os.stat(os.path.join(dirpath, fn))
                mode = stat.S_IMODE(st.st_mode) | stat.S_IWGRP
                os.chmod(os.path.join(dirpath, fn), mode)

        # Use rsync to push the new version of the website to SF.net
        log.info("Running rsync")
        p = subprocess.Popen(['rsync', 
            '-C', '-e', 'ssh', '--delete', '--delete-after', '-v', '-rltgoDz', 
            '--exclude', 'cvs-snapshots',
            'htdocs/', self.username + '@shell.sourceforge.net:/home/groups/p/py/pyobjc/htdocs/'])
        status = p.wait()
        if status != 0:
            log.error("Rsync failed with exit code %s", status)
            raise DistutilsError("rsync failed")
    
        log.info("Update is ready, don't forget to check the website!")
#
# Run distutils
#

setup(
        name = "pyobjc-website",
        description = "PyObjC's website",
        cmdclass=dict(
            build=buildsite,
            publish=publishsite,
            install=publishsite,
        ),
        setup_requires = [
            'docutils >=0.4',
            'Genshi >=0.4',
            'Pygments',
        ]
)
