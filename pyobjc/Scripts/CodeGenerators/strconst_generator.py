# This script generates a constant table containing the enum values for
# enumerations in the specified header file.
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os
import sys
from dupfile import *

ON_OSX= (sys.platform == "darwin")

MATCH_RE=re.compile(r'NSString\s*\*\s*(const\s+)?([A-Za-z_][A-Za-z0-9_]*(\s*,\s*\*\s*[A-Za-z_][A-Za-z0-9_]*)*)(\s+AVAILABLE_\w+)?;')

def entry(fp, val, ignore):
    vals = val.split(',')
    if len(vals) == 1:
        if val in ignore: return
        if ON_OSX:
            fp.write('\t { @"%s", @encode(NSString*) },\n'%(val, ))
        else:
            fp.write('\t { @"%s", @encode(NSString*), &(%s) },\n'%(val, val))
    else:
        for  v in vals:
            v = v.strip()
            if v[0] == '*':
                v = v[1:].strip()
            if v in ignore: continue
            if ON_OSX:
                fp.write('\t { @"%s", @encode(NSString*) },\n'%(v, ))
            else:
                fp.write('\t { @"%s", @encode(NSString*), &(%s) },\n'%(v, v))

def process_file(outfp, filename, ignore):
    fp = open(filename, 'r')

    outfp.write("\n\t/* From: %s */\n"%os.path.basename(filename))

    in_class = 0
    struct_level = 0
    maybe_struct_level = 0

    for ln in fp.xreadlines():
        if maybe_struct_level:
            if ln.strip().startswith('{'):
                struct_level += 1
                continue
        maybe_struct_level = 0

        # Skip declarations in objective-C class definitions
        if not in_class:
            if ln.startswith("@interface"):
                in_class = 1
                continue
        else:
            if ln.startswith("@end"):
                in_class = 0
            continue

        # Also skip struct definitions
        # XXX: This is very minimal, but good enough..
        if struct_level:
            if ln.strip().startswith('}'):
                struct_level -= 1

        if ln.strip().startswith('struct ') and ln.strip().endswith('{'):
            struct_level += 1
        elif ln.strip().startswith('struct '):
            maybe_struct_level = 1

        if struct_level:
            continue
            

        m = MATCH_RE.search(ln)
        if m: 
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
    fnames.sort()
    for f in fnames:
        process_file(fp, f, ignore)
    fp.write("\t{0, 0} /* Sentinel */\n")
    fp.write("};\n")

if __name__ == "__main__":
    import sys
    generate(sys.argv[1])
