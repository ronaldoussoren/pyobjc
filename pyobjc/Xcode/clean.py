#!/usr/bin/env python

import sys
import os
import re
import shutil

import getopt

## usage
def usage(msg=None, exitCode=1):
    if msg:
        print "Error:", msg
    print """
clean.py [-hvkrw] <source> <dest>
    
Copies tree of templates or projects from <source> to <dest>.  Before copying,
cleans up <source> by removing various bits of garbage.   After copying,
transforms <dest> by replacing strings with their Xcode template counterparts.

The -r flag can be used to reverse the project;  turning an Xcode template into
a working project.

Options:
    -h/--help              show usage
    -v/--verbose           verbose
    -k/--kill-destination  erase <dest> (no warning)
    -r/--reverse           reverse transformation (template -> editable project)
    -w/--working           try to make destination into a working project
    """
    sys.exit(exitCode)

## settings
verbose = False
killDest = False
doReverse = False
makeWorking = False

## process options
try:
    opts, args = getopt.getopt(sys.argv[1:], "hvkrw", ["help", "verbose", "kill-destination", "reverse", "working"])
except getopt.GetoptError, details:
    usage(details, 2)

if len(args) != 2:
    usage(None, 2)

for opt, value in opts:
    if opt in ['-h', '--help']:
        usage(None, 1)
    if opt in ['-v', '--verbose']:
        verbose = True
        continue
    if opt in ['-k', '--kill-destination']:
        killDest = True
        continue
    if opt in ['-r', '--reverse']:
        doReverse = True
        continue
    if opt in ['-w', '--working']:
        makeWorking = True
        continue

## define functions used in script
def killNasties(irrelevant, dirName, names):
    for aName in names:
        if len(filter(lambda expr, aName=aName: expr.match(aName), nastyFileExprs)):
            path = os.path.join(dirName, aName)
            if verbose:
                print "Removing '%s'..." % path
            if os.path.isdir(path):
		shutil.rmtree(path)
            else:
                os.remove(path)

def doSubstitutions(irrelevant, dirName, names):
    for aName in names:
        didPch = False
        path = os.path.join(dirName, aName)
        if os.path.isdir(path): continue
        if aName in specialFiles:
            specialFiles[aName](path)
            continue
        extension = os.path.splitext(path)[1]
        if extension in utf16Extensions:
            doFileSubstitution(path, utf16Substitutions)
        elif extension in utf8Extensions:
            doFileSubstitution(path, utf8Substitutions)
        elif extension in asciiExtensions:
            doFileSubstitution(path, asciiSubstitutions)
        else:
            sys.stderr.write("*WARN* Skipping unknown file with uknown type: %s\n" % path)
        if makeWorking and (extension in [".pch"]):
            if verbose:
                print 'Making working copy of %s...' % path
            tail = aName.split("_", 1)[1]
            targetFile = os.path.join(dirName, "xcPROJECTNAMExc_%s" % tail)
            inFile = file(path, "r")
            data = inFile.read()
            inFile.close()
            if extension in [".pch"]: # C type file
                message = "\n\n// WARNING\n// This file is copied from %s.  Keep the two in sync.\n// --- file resumes after here ---\n" % aName
            outFile = file(targetFile, "w")
            outFile.write(message)
            outFile.write(data)
            outFile.flush()
            outFile.close()

def doFileSubstitution(aFile, subs):
    if verbose:
        print 'Processing %s....' % aFile
    inFile = file(aFile, "r")
    data = inFile.read()
    inFile.close()
    for originalString, targetString in subs:
        data = data.replace(originalString, targetString)
    outFile = file(aFile, "w")
    outFile.write(data)
    outFile.flush()
    outFile.close()

def doTemplateInfo(aFile):
    if not doReverse:
        doFileSubstitution(aFile, utf8Substitutions)

## define per-file behaviors
specialFiles = {
    "TemplateInfo.plist" : doTemplateInfo
    }

utf8Extensions = ['.plist', '.pbxproj', '.nib', '.xib']
asciiExtensions = ['.m', '.h', '.c', '.pch', '.rtf', '.java', '.applescript', '.dependency']
utf16Extensions = ['.strings']

## define character mappings
asciiSimpleSurrounds = [('xc', 'xc')]
asciiSurrounds = [('\xc7', '\xc8')]

utf8SimpleSurrounds = asciiSimpleSurrounds
utf8Surrounds = [('\xc2\xab', '\xc2\xbb')]

utf16SimpleSurrounds = [('\x00x\x00c', '\x00x\x00c')]
utf16Surrounds = [('\x00\xab', '\x00\xbb')]

## substitution strings
substitutionStrings = [
    'PROJECTNAME',
    'FULLUSERNAME',
    'DATE',
    'YEAR',
    'PROJECTNAMEASIDENTIFIER',
    'PROJECTNAMEASXML',
    'ORGANIZATIONNAME'
    ]

utf16SubstitutionStrings = ["".join(['\x00%s' % c for c in aString]) for aString in substitutionStrings]

utf16Substitutions = None
utf8Substitutions = None
asciiSubstitutions = None

## build substitution tables based on options
if doReverse:
    asciiSubstitutions = [("%s%s%s" % (surround[0], aString, surround[1]),
                            "%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]))
                         for aString in substitutionStrings
                         for surround in asciiSurrounds
                         for simpleSurround in asciiSimpleSurrounds]
    utf8Substitutions = [("%s%s%s" % (surround[0], aString, surround[1]),
                          "%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]))
                         for aString in substitutionStrings
                         for surround in utf8Surrounds
                         for simpleSurround in utf8SimpleSurrounds]
    utf16Substitutions = [("%s%s%s" % (surround[0], aString, surround[1]),
                          "%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]))
                         for aString in utf16SubstitutionStrings
                         for surround in utf16Surrounds
                         for simpleSurround in utf16SimpleSurrounds]
else:
    asciiSubstitutions = [("%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]),
                            "%s%s%s" % (surround[0], aString, surround[1]))
                         for aString in substitutionStrings
                         for surround in asciiSurrounds
                         for simpleSurround in asciiSimpleSurrounds]
    utf8Substitutions = [("%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]),
                          "%s%s%s" % (surround[0], aString, surround[1]))
                         for aString in substitutionStrings
                         for surround in utf8Surrounds
                         for simpleSurround in utf8SimpleSurrounds]
    utf16Substitutions = [("%s%s%s" % (simpleSurround[0], aString, simpleSurround[1]),
                          "%s%s%s" % (surround[0], aString, surround[1]))
                         for aString in utf16SubstitutionStrings
                         for surround in utf16Surrounds
                         for simpleSurround in utf16SimpleSurrounds]

## processing starts here
source = os.path.normpath(args[0])
dest = os.path.normpath(args[1])

if os.path.exists(dest):
    if killDest:
        if verbose:
            print "Removing '%s'..." % dest
        shutil.rmtree(dest)
    else:
        usage("Destination already exists.  -k to destroy or use different destination.")

if verbose:
    print "Creating destination '%s'...." % dest
try:
    head, tail = os.path.split(dest)
    if not os.path.isdir(head):
        os.makedirs(dest)
except OSError, errno:
    usage(errno)

nastyFileExprs = [re.compile(expr) for expr in ['^.DS_Store$', '.*~.*$', '.*.pbxuser$']]

os.path.walk(source, killNasties, None)

if verbose:
    print "Copying from '%s' to '%s'...." % (source, dest)
shutil.copytree(source, dest)

os.path.walk(dest, doSubstitutions, None)
