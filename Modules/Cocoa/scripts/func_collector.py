# Non-string variables
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os

IDENT='[A-Za-z_][A-Za-z0-9_]*'

def process_file(outfp, filename, match_prefix='', ignore_list=()):

	MATCH_RE=re.compile('%(match_prefix)s(.*\(.*\);)'%{'match_prefix':match_prefix, 'IDENT':IDENT})

	fp = open(filename, 'r')

	outfp.write("\n# From: %s\n"%os.path.basename(filename))

	in_class = False

	for ln in fp.xreadlines():

		# Skip declarations in objective-C class definitions
		if not in_class:
			if ln.startswith("@interface"):
				in_class = True
				continue
		else:
			if ln.startswith("@end"):
				in_class = False
			continue

		m = MATCH_RE.match(ln)
		if not m: continue

		outfp.write('%s\n'%m.group(1).strip())

def generate(dirname, fn = None, match_prefix='', ignore_list=()):
	if fn:
		fp = open(fn, 'w')
	else:
		import sys
		fp = sys.stdout
		del sys

	fp.write("#\n")
	fp.write("# List of functions. Generated from files in \n")
	fp.write("# %s\n"%dirname)
	fp.write("# \n")
	fp.write("# Used to check for new functions\n")
	fp.write("# \n")

	fnames = [ os.path.join(dirname, fn)
				for fn in os.listdir(dirname)
				if fn.endswith('.h') ]
	for f in fnames:
		process_file(fp, f, match_prefix, ignore_list)

if __name__ == "__main__":
	import sys
	generate(sys.argv[1], match_prefix=sys.argv[2])
