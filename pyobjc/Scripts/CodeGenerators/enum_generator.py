# This script generates a constant table containing the enum values for
# enumerations in the specified header file.
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os
import sys
from dupfile import dupfile

START_RE=re.compile(r'(typedef[\w]|)enum.*{')
START_RE2=re.compile(r'(typedef[\w]|)enum(?:\s+[A-Za-z_][A-Za-z0-9_]*)?\s*$')
END_RE=re.compile(r'}')
IDENT_RE=re.compile(r'(^|[^A-Za-z_0-9])(?P<identifier>[A-Za-z_][A-Za-z0-9_]*)')
LINE_COMMENT_RE=re.compile(r'//.*')
SINGLE_LINE_RE=re.compile(r'enum.*{([^}]*)}')
BLOCK_1_RE=re.compile(r'/\*([^*]|(\*[^/]))*\*/')
BLOCK_S_RE=re.compile(r'/\*')
BLOCK_E_RE=re.compile(r'\*/')

DEFINE_RE=re.compile(r'^\s*#\s*define\s+([A-Za-z_][A-Za-z0-9]*)\s+(\d+)$')

def entry(fp, val):
    if val.endswith('Mask'):
        unsigned = 1
    else:
        unsigned = 0
    fp.write('\t { "%s", %d, %s },\n'%(val, unsigned, val))

def process_file(outfp, filename):
    fp = open(filename, 'r')

    outfp.write("\n\t/* From: %s */\n"%os.path.basename(filename))

    in_enum = 0
    in_comment = 0

    for ln in fp.xreadlines():
        ln = LINE_COMMENT_RE.sub('', ln)

        m = DEFINE_RE.match(ln)
        if m is not None:
            name, value = m.group(1), m.group(2)
            if name == 'nil':
                # Grr, the compiler on GNUstep complains about this one
                continue
            entry(outfp, name)
            continue

        if not in_enum:
            m = SINGLE_LINE_RE.search(ln)
            if m:
                values = m.group(1)
                values = values.split(',')

                for v in values:
                    m = IDENT_RE.search(v)
                    if not m:
                        continue

                    ident = m.group('identifier')
                    entry(outfp, ident)
            elif START_RE.search(ln):
                in_enum = 1
                need_brace=0
            elif START_RE2.search(ln):
                in_enum = 1
                need_brace=1
        else:
            if in_comment:
                m = BLOCK_E_RE.search(ln)
                if not m:
                    continue
                ln = ln[m.end():]
                in_comment = 0


            if END_RE.match(ln):
                in_enum = 0
                continue

            ln = BLOCK_1_RE.sub('', ln)
            m = BLOCK_S_RE.search(ln)
            if m:
                in_comment = 1
                ln = ln[:m.start()]

            if need_brace:
                if not ln.strip().startswith('{'):
                    in_enum=0
                    continue
                need_brace = 0


            m = IDENT_RE.search(ln)
            if not m:
                continue

            ident = m.group('identifier')
            if not ident in ['if', 'endif', 'else']:
                entry(outfp, ident)


def generate(dirname, fn = None, filter = lambda x: 1, ignore_files=()):
    if not os.path.exists(dirname): return

    if fn:
        fp = dupfile(fn, 'w')
    else:
        fp = sys.stdout

    fnames = [ os.path.join(dirname, fn)
                        for fn in os.listdir(dirname)
                        if fn.endswith('.h') and filter(fn) ]
    fnames.sort()
    for fname in fnames:
        fmwkname = os.path.dirname(os.path.dirname(fname))
        if fmwkname.endswith('.framework'):
            fp.write("#import <%s/%s>\n" % (os.path.splitext(os.path.basename(fmwkname))[0], os.path.basename(fname)))
    fp.write("/*\n")
    fp.write(" * Enumeration constants. This file is generated from files in\n")
    fp.write(" * %s\n"%dirname)
    fp.write(" */\n")
    fp.write("static struct inttable enum_table[] = {\n")
    for f in fnames:
        if os.path.basename(f) in ignore_files:
            continue
        process_file(fp, f)
    fp.write("\t{0, 0, 0} /* Sentinel */\n")
    fp.write("};\n")
    fp.close()

if __name__ == "__main__":
    import sys
    generate(sys.argv[1])
