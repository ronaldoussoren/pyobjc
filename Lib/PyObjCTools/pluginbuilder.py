"""
pluginbuilder.py -- Tools to assemble MacOS X python-based plugin bundles 

This module defines one class to build python based plugin bundles for MacOS X.
Examples of plugin bundles include PreferencePanes and InterfaceBuilder 
palletes.

The PluginBuilder class is instantated with a number of keyword arguments and
have a build() method that will do all the work. See the class docstrings for
a description of the constructor arguments.

The module contains a main program that can be used in two ways:
  % python pluginbuilder.py [options] build
  % python buildplugin.py [options] build

Where "buildplugin.py" is a user-supplied setup.py-like script following this
model:

  from PyObjCTools.pluginbuilder import buildplugin

  buildplugin(<lots-of-keyword-args>)

"""

__all__ = ( "BundleBuilderError", "buildplugin", "PluginBuilder" )

import bundlebuilder
import os
import getopt
import sys
from bundlebuilder import BundleBuilderError


CODE="""\
/*
 * !!!! THIS IS GENERATED CODE, DO NOT EDIT !!!!
 */
#import <Foundation/Foundation.h>

#include <Python/Python.h>

@interface PyObjC_Bundle_%(BUNDLE)s
{
}

+(void)load;

@end

@implementation PyObjC_Bundle_%(BUNDLE)s

+(void)load
{
	NSBundle* bundle;
	NSString* mainPath;
	FILE*     fp;

        NSLog(@"Loading prefpane %(MAINFILE)s %(BUNDLE)s");

	bundle = [NSBundle bundleForClass:self];
	[bundle load];

        mainPath = [bundle pathForResource:@"%(MAINFILE)s" ofType:@"py"];

	if (mainPath == NULL) {
		mainPath = [bundle pathForResource:@"%(MAINFILE)s" ofType:@"pyc"];
		[NSException raise:NSInternalInconsistencyException 
			format:@"Bundle %%@ does not contain a %(MAINFILE)s file",
			bundle];
	}

	if (!Py_IsInitialized()) {
		Py_Initialize();
	}

	fp = fopen([mainPath cString], "r");
	if (fp == NULL) {
		abort();
	}

	PyRun_SimpleFile(fp, [mainPath cString]);
}

@end
"""


class PluginBuilder(bundlebuilder.BundleBuilder):

    # Override type of the bundle
    type = "BNDL"

    # platform, name of the subfolder of Contents that contains the 
    # executable
    platform = "MacOS"

    # A python mainmodule
    mainmodule = None

    # The name of the main nib. *Must* be specified
    nibname = None

    # The name of the principal class
    principalClass = None

    # The name of the icon file to be copied to Resources and used for the
    # Finder icon
    iconfile = None

    # Bundle suffix
    bundlesuffix = ".bnld"

    # Is this a standalone bundle?
    standalone = 0

    # Should binaries be stripped?
    strip = 0

    # Found Python modules: [(name, codeobject, ispkg), ...]
    pymodules = []

    # Modules that modulefinder couldn't find:        
    missingModules = []
    maybeMissingModules = []

    # List of all binaries (executables or shared libs), for stripping purposes
    binaries = []

    def setup(self):
        if self.mainmodule is None:
            raise bundlebuilder.BundleBuilderError, ("must specify 'mainmodule'"
                " when building a plugin bundle")
        else:
            self.files.append((self.mainmodule, os.path.join(
                'Contents', 'Resources', self.mainmodule)))


        if self.standalone:
            raise bundlebuilder.BundleBuilderError, ("can't specify "
                "'standalone' at the moment, sorry")

        if self.strip:
            raise bundlebuilder.BundleBuilderError, ("can't specify "
                "'strip' at the moment, sorry")

        if self.nibname is None:
            raise bundlebuilder.BundleBuilderError, ("must specify 'nibname'"
                " when building a plugin bundle")

        self.execdir = os.path.join("Contents", self.platform)

        if self.name is None:
            self.name = os.path.splitext(self.mainmodule)[0]

        if not self.name.endswith(self.bundlesuffix):
            self.name += self.bundlesuffix

        if self.nibname:
            self.plist.NSMainNibFile = self.nibname
            if not hasattr(self.plist, "NSPrincipalClass"):
                if self.principalClass is None:
                    raise bundlebuilder.BundleBuilderError, (
                        "must specify 'principalClass' when building a "
                        "plugin bundle")
                self.plist.NSPrincipalClass = self.principalClass

        bundlebuilder.BundleBuilder.setup(self)

        self.plist.CFBundleExecutable = self.name


        if self.standalone:
            self.findDependencies()

    def preProcess(self):

        if self.iconfile is not None:
            iconbase = os.path.basename(self.iconfile)
            self.plist.CFBunelIconFile = iconbase
            self.files.append((self.iconfile, os.path.join(resdir, iconbase)))

    def postProcess(self):
        destdir = os.path.join(self.bundlepath, self.execdir)
        if not os.path.exists(destdir):
            os.mkdir(destdir)
        compileBundle(os.path.join(destdir, self.name), 
            self.name, self.mainmodule)
        self.binaries.append(os.path.join(self.execdir, self.name))

        if self.standalone:
            self.addPythonModules()

        if self.strip:
            self.stripBinaries()

        if self.missingModules or self.maybeMissingModules:
            self.reportMissing()

def compileBundle(outputName, bundle, mainModule):
    tmpFile = outputName + '.m'
    mainModule = os.path.splitext(mainModule)[0]
    fd = open(tmpFile, 'w')
    try:
        fd.write(CODE%{'BUNDLE':bundle, 'MAINFILE':mainModule})
        fd.close()

        quoteArg = lambda arg: arg.replace("'", "'\"'\"'")

        fd = os.popen(
                "cc -bundle -Wno-long-double -o '%s' '%s' -framework Foundation -framework Python 2>&1"%(
                    quoteArg(outputName), quoteArg(tmpFile)                    
                ),  'r')
        for ln in fd:
            sys.stdout.write(ln)

        xit = fd.close()
        if xit is not None:
            raise ValueError, "Compilation failed"

    finally:
        os.unlink(tmpFile)


cmdline_doc = """\
Usage:
  python pluginbuilder.py [options] command
  python mybuildscript.py [options] command

Commands:
  build      build the application
  report     print a report

Options:
  -b, --builddir=DIR     the build directory; defaults to "build"
  -n, --name=NAME        plugin name
  -r, --resource=FILE    extra file or folder to be copied to Resources
  -f, --file=SRC:DST     extra file or folder to be copied into the bundle;
                         DST must be a path relative to the bundle root
  -m, --mainmodule=FILE the Python main program
  -p, --plist=FILE       .plist file (default: generate one)
      --nib=NAME         main nib name
      --principalClass=NAME principal class name
      --iconfile=FILE    filename of the icon (an .icns file) to be used
                         as the Finder icon
      --standalone       build a standalone application, which is fully
                         independent of a Python installation
      --lib=FILE         shared library or framework to be copied into
                         the bundle
  -x, --exclude=MODULE   exclude module (with --standalone)
  -i, --include=MODULE   include module (with --standalone)
      --package=PACKAGE  include a whole package (with --standalone)
      --strip            strip binaries (remove debug info)
  -v, --verbose          increase verbosity level
  -q, --quiet            decrease verbosity level
  -h, --help             print this message
"""

def usage(msg=None):
	if msg:
		print msg
	print cmdline_doc
	sys.exit(1)

def main(builder=None):
	if builder is None:
		builder = PluginBuilder(verbosity=1)

	shortopts = "b:n:r:f:m:p:x:i:hvq"
	longopts = ("builddir=", "name=", "resource=", "file=", 
		"mainmodule=", "creator=", "nib=", "principalClas=",
                "plist=", "help", "verbose", "quiet", "standalone",
		"exclude=", "include=", "package=", "strip", "iconfile=",
		"lib=")

	try:
		options, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
	except getopt.error:
		usage()

	for opt, arg in options:
		if opt in ('-b', '--builddir'):
			builder.builddir = arg
		elif opt in ('-n', '--name'):
			builder.name = arg
		elif opt in ('-r', '--resource'):
			builder.resources.append(arg)
		elif opt in ('-f', '--file'):
			srcdst = arg.split(':')
			if len(srcdst) != 2:
				usage("-f or --file argument must be two paths, "
				      "separated by a colon")
			builder.files.append(srcdst)
		elif opt == '--iconfile':
			builder.iconfile = arg
		elif opt == "--lib":
			builder.libs.append(arg)
		elif opt == "--nib":
			builder.nibname = arg
		elif opt in ('-p', '--plist'):
			builder.plist = Plist.fromFile(arg)
		elif opt in ('-h', '--help'):
			usage()
		elif opt in ('-v', '--verbose'):
			builder.verbosity += 1
		elif opt in ('-q', '--quiet'):
			builder.verbosity -= 1
		elif opt == '--standalone':
			builder.standalone = 1
		elif opt in ('-x', '--exclude'):
			builder.excludeModules.append(arg)
		elif opt in ('-i', '--include'):
			builder.includeModules.append(arg)
		elif opt == '--package':
			builder.includePackages.append(arg)
		elif opt == '--strip':
			builder.strip = 1
		elif opt == '--principalClass':
			builder.principalClass = arg

	if len(args) != 1:
		usage("Must specify one command ('build', 'report' or 'help')")
	command = args[0]

	if command == "build":
		builder.setup()
		builder.build()
	elif command == "report":
		builder.setup()
		builder.report()
	elif command == "help":
		usage()
	else:
		usage("Unknown command '%s'" % command)


def buildplugin(**kwargs):
	builder = PluginBuilder(**kwargs)
	main(builder)

if __name__ == "__main__":
	main()
