# This script generates a constant table containing the enum values for
# enumerations in the specified header file.
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os
from dupfile import *

MATCH_RE=re.compile('NSString \*([ ]*const[ ]+)?([A-Za-z_][A-Za-z0-9_]*([ ]*,[ ]*\*[ ]*[A-Za-z_][A-Za-z0-9_]*)*);')

def entry(fp, val, ignore):
    vals = val.split(',')
    if len(vals) == 1:
        if val in ignore: return
        fp.write('\t { @"%s", @encode(NSString*) },\n'%(val, ))
    else:
        for  v in vals:
            v = v.strip()
            if v[0] == '*':
                v = v[1:].strip()
            if v in ignore: continue
            fp.write('\t { @"%s", @encode(NSString*) },\n'%(v, ))

def process_file(outfp, filename, ignore):
    fp = open(filename, 'r')

    outfp.write("\n\t/* From: %s */\n"%os.path.basename(filename))

    in_class = 0

    for ln in fp.xreadlines():

        # Skip declarations in objective-C class definitions
        if not in_class:
            if ln.startswith("@interface"):
                in_class = 1
                continue
        else:
            if ln.startswith("@end"):
                in_class = 0
            continue

        m = MATCH_RE.search(ln)
        if not m: continue

        ident = m.group(2)
        entry(outfp, ident, ignore)

def generate(dirname, fn = None, ignore=(), filter = lambda x: 1):
    if not os.path.exists(dirname): return

    if fn:
        fp = dupfile(fn, 'w')
    else:
        import sys
        fp = sys.stdout
        del sys

    fp.write("/*\n")
    fp.write(" * String constants. This file is generated from files in\n")
    fp.write(" * %s\n"%dirname)
    fp.write(" */\n")
    fp.write("static struct vartable string_table[] = {\n")
    fnames = [ os.path.join(dirname, fn)
                        for fn in os.listdir(dirname)
                        if fn.endswith('.h') and filter(fn) ]
    for f in fnames:
        process_file(fp, f, ignore)
    fp.write("\t{0, 0} /* Sentinel */\n")
    fp.write("};\n")

if __name__ == "__main__":
    import sys
    generate(sys.argv[1])
