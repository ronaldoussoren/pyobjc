#!/usr/bin/env python

__version__ = '0.1'

import sys
import os
import re
import shutil
import codecs
import tempfile

from optparse import OptionParser, Option, OptionValueError

import logging
from logging import error, info, debug

def deletePath(path):
    info("Removing '%s'...", path)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

## define functions used in script
NASTYFILEEXPR = re.compile(r'|'.join([
    r'(?:%s)' % (_exp,) for _exp in
    [
        r'^\.svn$', r'^CVS$', r'^\.DS_Store$', r'~.*$', r'\.pbxuser$',
        r'^build$', r'\.mode[0-9]$'
    ]
]))

def killNasties(dirName, aName, options):
    if NASTYFILEEXPR.search(aName) is None:
        return

    path = os.path.join(dirName, aName)
    deletePath(path)

## define per-file behaviors
def maybenib(encoding):
    def maybenib(fn):
        if file(fn).read(11) == 'typedstream':
            info("Convert %s to a text nib file if you need substitution", fn)
            return None
        return encoding(fn)
    return maybenib

def maybeutf(encoding=None):
    def maybeutf(fn):
        header = file(fn).read(4)
        if header == '\x00\x00\xFE\xFF':
            return 'ucs4_be'
        elif header == '\xFF\xFE\x00\x00':
            return 'ucs4_le'
        elif header == '\x00\x3C\x00\x3F':
            return 'utf_16_be'
        elif header == '\x3C\x00\x3F\x00':
            return 'utf_16_le'
        elif header == '\x3C\x3F\x78\x6D':
            return 'utf_8'
        elif header.startswith('\xFE\xFF'):
            return 'utf_16_be'
        elif header.startswith('\xFF\xFE'):
            return 'utf_16_le'
        return encoding
    return maybeutf
            
    
def _buildEncodingsDict():
    d = {}
    # XXX - SHOULD CHECK FOR XML ENCODINGS?
    d['.nib'] = maybenib(maybeutf('macroman'))
    for k in ['.pbxproj', '.xib']:
        d[k] = maybeutf('utf_8')
    for k in ['.py', '.m', '.h', '.c', '.pch', '.rtf', '.java', '.applescript', '.dependency', '.plist']:
        d[k] = maybeutf('macroman')
    for k in ['.strings']:
        d[k] = maybeutf('utf16')
    return d
    
ENCODINGS = _buildEncodingsDict()

WORKINGCOPYFILES = ['.pch']
CTYPEFILES = ['.pch']

def doTemplateInfo(aFile, options, translator):
    basename, extension = os.path.splitext(aFile)
    encoding = ENCODINGS.get(extension, lambda fn:None)(aFile)
    doFileSubstitution(aFile, encoding, translator)

SPECIALFILES = {
    "TemplateInfo.plist" : doTemplateInfo,
}

SUBSTITUTIONMESSAGE = u"""
                
// WARNING
// This file is copied from %(name)s.  Keep the two in sync.
// --- file resumes after here ---
"""

def doSubstitutions(dirName, aName, options):
    if options.doReverse:
        translator = REVERSETRANSLATOR
    else:
        translator = FORWARDTRANSLATOR
    
    path = os.path.join(dirName, aName)
    if os.path.isdir(path):
        return

    specialCommand = SPECIALFILES.get(aName)
    if specialCommand is not None:
        specialCommand(path, options, translator)
        return

    basename, extension = os.path.splitext(path)

    encoding = ENCODINGS.get(extension, lambda fn:None)(path)
    if encoding is None:
        error("*WARN* Skipping unknown file with uknown type: %s", path)
    else:
        info('Processing %s....', aName)
        if options.makeWorking and (extension in WORKINGCOPYFILES) and not options.doReverse and aName.split("_", 1)[0] == 'xcPROJECTNAMExc':
            deletePath(path)
        else:
            doFileSubstitution(path, encoding, translator)

    if options.makeWorking and (extension in WORKINGCOPYFILES) and options.doReverse:
            tail = aName.split("_", 1)[1]
            targetFile = os.path.join(dirName, "xcPROJECTNAMExc_%s" % (tail,))

            info('Making working copy of %s to %s...', path, targetFile)

            inFile = codecs.EncodedFile(file(path, "rb"), encoding)
            outFile = codecs.EncodedFile(file(targetFile, 'wb'), encoding)

            if extension in CTYPEFILES:
                outFile.write(SUBSTITUTIONMESSAGE % dict(name = aName))

            for line in inFile:
                outFile.write(line)

            inFile.close()
            outFile.close()

def doFileSubstitution(aFile, encoding, translator):
    _tempFile = tempfile.TemporaryFile()

    # do the translation
    debug('encoding is: %s', encoding)
    inFile = codecs.getreader(encoding)(file(aFile, "rb"))
    outFile = codecs.getwriter(encoding)(_tempFile)
    try:
        for line in inFile:
            tline = translator(line)
            outFile.write(tline)
    except NotImplementedError:
        BUFFER = 16384
        bytes = inFile.read(BUFFER)
        while bytes:
            lines = bytes.splitlines(True)
            bytes = lines.pop()
            for line in lines:
                tline = translator(line)
                outFile.write(tline)
            newbytes = inFile.read(BUFFER)
            bytes += newbytes
            if not newbytes and bytes:
                # "EOF"
                bytes += u'\n'
    inFile.close()

    # do the copy
    _tempFile.seek(0)
    copyFile = file(aFile, "wb")
    shutil.copyfileobj(_tempFile, copyFile)
    copyFile.close()
    _tempFile.close()

## substitution strings
FORWARD = u'xc', u'xc'
REVERSE = u'\N{LEFT-POINTING DOUBLE ANGLE QUOTATION MARK}', u'\N{RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK}'

SUBSTITUTIONSTRINGS = [
    'PROJECTNAME',
    'FULLUSERNAME',
    'DATE',
    'YEAR',
    'PROJECTNAMEASIDENTIFIER',
    'PROJECTNAMEASXML',
    'ORGANIZATIONNAME'
]

BASEREGEX = '(%s)' % ('|'.join(SUBSTITUTIONSTRINGS),)

def getRegSub(forward, reverse, regex=BASEREGEX):
    left, right = forward
    reg = re.compile(left + regex + right)
    sub = r'%s\1%s' % reverse
    def getRegSub(s):
        return reg.sub(sub, s)
    return getRegSub

FORWARDTRANSLATOR = getRegSub(FORWARD, REVERSE)
REVERSETRANSLATOR = getRegSub(REVERSE, FORWARD)

## process options
def build_parser():
    USAGE = """project-tool.py [options] <source> <dest>
        
    Copies tree of templates or projects from <source> to <dest>.  
    Before copying, it cleans up <source> by removing various bits of garbage.
    After copying, it transforms <dest> by replacing strings with their Xcode
    template counterparts.

    The reverse flag can be used to reverse this process; turning an Xcode
    template into a working project."""

    parser = OptionParser(USAGE, version=__version__)

    def store_true(*args, **kwargs):
        kwargs['action'] = 'store_true'
        kwargs['default'] = False
        parser.add_option(*args, **kwargs)
    
    store_true('-v', '--verbose',
        dest='verbose', help='verbose')
    store_true('-k', '--kill-dest',
        dest='killDest', help='erase <dest> (no warning)')
    store_true('-r', '--reverse',
        dest='doReverse', help='reverse transformation (template -> editable project)')
    store_true('-w', '--working',
        dest='makeWorking', help='try to make destination into a working project')
    return parser

def simplePathWalker(walkdir, fn, arg=None):
    def _simplePathWalker(arg, dirname, fnames):
        for name in fnames:
            fn(dirname, name, arg)
    os.path.walk(walkdir, _simplePathWalker, arg)
    
def main():
    parser = build_parser()
    options, args = parser.parse_args()

    if not args:
        parser.print_help()
        return

    if len(args) != 2:
        parser.error("Must specify both a source and destination")
        return

    if options.verbose:
        hdlr = logging.StreamHandler()
        fmt = logging.Formatter('%(message)s')
        hdlr.setFormatter(fmt)
        logger = logging.getLogger()
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)
    else:
        logging.basicConfig()
        
    source, dest = map(os.path.normpath, args)
    if source == dest:
        parser.error("Source and destination may not be the same.")
        return

    if os.path.exists(dest):
        if options.killDest:
            deletePath(dest)
        else:
            parser.error("Destination already exists.  -k to destroy or use different destination.")
            return

    info("Copying from '%s' to '%s'....", source, dest)
    shutil.copytree(source, dest)

    simplePathWalker(dest, killNasties, options)
    simplePathWalker(dest, doSubstitutions, options)

if __name__ == '__main__':
    main()
