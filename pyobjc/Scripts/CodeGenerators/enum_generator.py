# This script generates a constant table containing the enum values for
# enumerations in the specified header file.
#
# This is script is rather fragile, and tuned to the MacOS 10.1 header-files.
#
# We should probably use bgen, but how does one use that tool?

import re
import os

START_RE=re.compile('(typedef[\w]|)enum.*{')
END_RE=re.compile('}')
IDENT_RE=re.compile('[A-Za-z_][A-Za-z_0-9]*')
LINE_COMMENT_RE=re.compile('//.*')
SINGLE_LINE_RE=re.compile('enum.*{([^}]*)}')
BLOCK_1_RE=re.compile('/\*([^*]|(\*[^/]))*\*/')
BLOCK_S_RE=re.compile('/\*')
BLOCK_E_RE=re.compile('\*/')

def entry(fp, val):
	fp.write('\t { "%s", %s },\n'%(val, val))

def process_file(outfp, filename):
	fp = open(filename, 'r')

	outfp.write("\n\t/* From: %s */\n"%os.path.basename(filename))

	in_enum = 0
	in_comment = 0

	for ln in fp.xreadlines():
		if not in_enum:
			m = SINGLE_LINE_RE.search(ln)
			if m:
				values = m.group(1)
				values = values.split(',')

				for v in values:
					m = IDENT_RE.search(v)
					if not m:
						continue

					ident = v[m.start():m.end()]
					entry(outfp, ident)
			elif START_RE.search(ln):
				in_enum = 1
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

			ln = LINE_COMMENT_RE.sub('', ln)	
			ln = BLOCK_1_RE.sub('', ln)
			m = BLOCK_S_RE.search(ln)
			if m:
				in_comment = 1
				ln = ln[:m.start()]

			m = IDENT_RE.search(ln)
			if not m:
				continue

			ident = ln[m.start():m.end()]
			if not ident in ['if', 'endif', 'else']:
				entry(outfp, ident)


def generate(dirname, fn = None, filter = lambda x: 1):
	if not os.path.exists(dirname): return

	if fn:
		fp = open(fn, 'w')
	else:
		import sys
		fp = sys.stdout
		del sys

	fp.write("/*\n")
	fp.write(" * Enumeration constants. This file is generated from files in\n")
	fp.write(" * %s\n"%dirname)
	fp.write(" */\n")
	fp.write("static struct inttable enum_table[] = {\n")
	fnames = [ os.path.join(dirname, fn)
				for fn in os.listdir(dirname)
				if fn.endswith('.h') and filter(fn) ]
	for f in fnames:
		process_file(fp, f)
	fp.write("\t{0, 0} /* Sentinel */\n")
	fp.write("};\n")

if __name__ == "__main__":
	import sys
	generate(sys.argv[1])
