#!/usr/bin/env python

# Script for generating files in the PyObjC website from reStructuredText
# files, making use of hthtml, by  Ollie Rutherfurd, from the docutils sandbox
#
# Usage: Call this script in the root of the pyobjc-web tree (e.g. the one
# containing 'docroot'). Optinally provide the path to the source-tree.

import sys
import os
import shutil
import re
import docutils.core


PHP_HEADER='''\
<?
    $title = "%(title)s";
    $cvs_author = '$Author: ronaldoussoren $';
    $cvs_date = '$Date: 2003/07/05 14:59:47 $';

    include "header.inc";
?>'''

PHP_FOOTER='''\
<?
    include "footer.inc";
?>'''


def copy_tutorial_file(fn, tutdir, dstname):
    src = os.path.join(tutdir, fn)
    if os.path.isdir(src):
        dstname = dstname + '.zip'
        if os.path.exists(dstname):
            os.unlink(dstname)
        cwd = os.getcwd()
        dstname = os.path.abspath(dstname)
        srcdir, srcfile = os.path.split(src)
        os.chdir(os.path.abspath(srcdir))
        try:
            args = ['/usr/bin/zip', '-rq9', dstname, srcfile, '-x', '*/.svn/*']
            os.spawnv(os.P_WAIT, args[0], args)
        finally:
            os.chdir(cwd)
    else:
        if os.path.exists(dstname):
            os.unlink(dstname)
        shutil.copy(src, dstname)
    return (os.path.basename(src), os.path.basename(dstname))


def replace_tutorial_zips(fn, replacements):
    text = open(fn, 'r').read()
    for orig, new in replacements:
        if orig != new:
            text = text.replace('"%s"' % (orig,), '"%s"' % (new,))
    open(fn, 'w').write(text)


if len(sys.argv) == 2:
    srctree = sys.argv[1]
else:
    srctree = '../pyobjc'

def copy_project_docs(srctree):
    """
    Copy the documentation in '$srctree/Doc' to 'docroot/doc'
    """
    docdir = os.path.join(srctree, 'Doc')

    # This block shouldn't be here, but I do not yet know how to
    # embed this in ReST files.
    extra_info = {}
    if os.path.exists(os.path.join(docdir, 'website.lst')):
        fd = open(os.path.join(docdir, 'website.lst'))
        for ln in fd.readlines():
            if ln.startswith('#'): continue
            fields = ln.split(',')
            extra_info[fields[0].strip()] = {
                'section': fields[1].strip(),
                'priority': int(fields[2].strip()),
            }

    docs =  [ os.path.join(docdir, fn) 
                    for fn in os.listdir(docdir) if fn.endswith('.txt') ]
    docs.append(os.path.join(srctree, 'Install.txt'))
    docs.append(os.path.join(srctree, 'NEWS.txt'))
    docs.append(os.path.join(docdir, 'tutorial', 'tutorial.txt'))
    docs.append(os.path.join(docdir, 'tutorial_embed', 'extending_objc_with_python.txt'))

    alldocs = {}

    for fname in docs:
        print "-", fname
        docinfo = {}

        bn = os.path.split(fname)[-1]
        if bn in ('index.txt', 'announcement.txt'):
            continue
        if extra_info.has_key(bn):
            docinfo.update(extra_info[bn])

        if bn.endswith('.txt'):
            bn = bn[:-3].lower() + "php"
        else:
            bn = bn.lower() + '.php'
        fd = open(fname)
        input = fd.read()
        fd.close()
        output = docutils.core.publish_string(
            source = input,
            source_path = fname,
            destination_path = bn,
            writer_name = 'hthtml')
        
        output_lines = output.split('\n')
        for i in range(len(output_lines)):
            if output_lines[i] == '':
                break
            idx = output_lines[i].find(':')
            if idx == -1:
                break

            key = output_lines[i][:idx].strip()
            value = output_lines[i][idx+1:].strip()
            docinfo[key] = value

        output = '\n'.join(output_lines[i:])
        if not docinfo.has_key('title'):
            docinfo['title'] = bn
        alldocs[bn] = docinfo
         
        fd = open(os.path.join('docroot', 'doc', bn), 'w')
        fd.write(PHP_HEADER%docinfo)

        fd.write(output);

        fd.write(PHP_FOOTER)

    # Calculate indices for user and developer documentation
    docs = alldocs.keys()
    developer_docs = []
    user_docs = []

    for doc in alldocs:
        if not alldocs[doc].has_key('section'):
            print "Skipping", doc
            continue

        if alldocs[doc]['section'] == 'user':
            user_docs.append([alldocs[doc]['title'], doc])
        elif alldocs[doc]['section'] == 'developer':
            developer_docs.append([alldocs[doc]['title'], doc])

    def doccmp(a, b):
        r = cmp(alldocs[a[1]]['priority'], alldocs[b[1]]['priority'])
        if r != 0: return r

        return cmp(a[1], b[1])
    user_docs.sort(doccmp)
    developer_docs.sort(doccmp)
  
    # Rewrite the indices (substitute the current document lists)
    for fname in ('index.php', 'usage.php', 'developer.php'):
        fd = open(os.path.join('docroot', 'doc', fname), 'r')
        index_php = fd.readlines()
        fd.close()

        fd = open(os.path.join('docroot', 'doc', fname), 'w')
        skip = 0
        for ln in index_php:
            if not skip:
                fd.write(ln)
            if ln.find('/USERDOC') != -1:
                skip = 0
                fd.write(ln)
            elif ln.find('USERDOC') != -1:
                skip = 1
                for title, link in user_docs:
                    fd.write('<LI><A HREF="%s">%s</A>\n'%(link, title))
            if ln.find('/DEVDOC') != -1:
                skip = 0
                fd.write(ln)
            elif ln.find('DEVDOC') != -1:
                skip = 1
                for title, link in developer_docs:
                    fd.write('<LI><A HREF="%s">%s</A>\n'%(link, title))

    # Copy tutorial files
    TUTORIAL_ENDINGS = ['.nib', '.py', '-src', '.h', '.m']
    tutdir = os.path.join(docdir, 'tutorial')
    files = os.listdir(tutdir)
    replacements = []
    for fn in files:
        for ext in TUTORIAL_ENDINGS:
            if fn.endswith(ext):
                dstname = os.path.join('docroot', 'doc', fn)
                replacements.append(copy_tutorial_file(fn, tutdir, dstname))
                break
    replace_tutorial_zips(os.path.join('docroot', 'doc', 'tutorial.php'), replacements)
 
    tutdir = os.path.join(docdir, 'tutorial_embed', 'src')
    files = os.listdir(tutdir)
    if not os.path.exists(os.path.join('docroot', 'doc', 'src')):
        os.mkdir(os.path.join('docroot', 'doc', 'src'))
    for fn in files:
        for ext in TUTORIAL_ENDINGS:
            if fn.endswith(ext):
                dstname = os.path.join('docroot', 'doc', 'src', fn)
                replacements.append(copy_tutorial_file(fn, tutdir, dstname))
                break
    replace_tutorial_zips(os.path.join('docroot', 'doc', 'tutorial.php'), replacements)

    #print "Don't forget to update docroot/doc/tutorial.php: it's references to"
    #print "'step3-MainMenu.nib' and 'step12-src' should be changed to ZIP files"

if __name__ == "__main__":
    copy_project_docs(srctree)
