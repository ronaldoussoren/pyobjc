from altgraph.compat import *
from macholib.MachOGraph import MachOGraph, MissingMachO
from macholib.util import iter_platform_files, in_system_path, mergecopy, mergetree, writablefile, has_filename_filter, thin_to_archs
from macholib.dyld import framework_info
import os

class ExcludedMachO(MissingMachO):
    pass

class FilteredMachOGraph(MachOGraph):
    def __init__(self, delegate, *args, **kwargs):
        super(FilteredMachOGraph, self).__init__(*args, **kwargs)
        self.delegate = delegate

    def createNode(self, cls, name):
        cls = self.delegate.getClass(name, cls)
        res = super(FilteredMachOGraph, self).createNode(cls, name)
        return res

    def locate(self, filename):
        newname = super(FilteredMachOGraph, self).locate(filename)
        if newname is None:
            return None
        return self.delegate.locate(newname)

class MachOStandalone(object):
    def __init__(self, base, archs, dest=None, graph=None, env=None, executable_path=None):
        self.base = os.path.join(os.path.abspath(base), '')
        if dest is None:
            dest = os.path.join(self.base, 'Contents', 'Frameworks')
        self.dest = dest
        self.mms = dict([[arch, FilteredMachOGraph(self, arch, graph=graph, env=env, executable_path=executable_path)] for arch in archs])
        self.changemap = {}
        self.excludes = []
        self.pending = deque()
        self.archs = archs

    def getClass(self, name, cls):
        if in_system_path(name):
            return ExcludedMachO
        for base in self.excludes:
            if name.startswith(base):
                return ExcludedMachO
        return cls

    def locate(self, filename):
        if in_system_path(filename):
            return filename
        if filename.startswith(self.base):
            return filename
        for base in self.excludes:
            if filename.startswith(base):
                return filename
        info = framework_info(filename)
        if info is None:
            res = self.copy_dylib(filename)
            self.changemap[filename] = res
            return res
        else:
            res = self.copy_framework(info)
            self.changemap[filename] = res
            return res

    def copy_dylib(self, filename):
        dest = os.path.join(self.dest, os.path.basename(filename))
        if not os.path.exists(dest):
            self.mergecopy(filename, dest)
        return dest

    def mergecopy(self, src, dest):
        return mergecopy(src, dest)

    def mergetree(self, src, dest):
        return mergetree(src, dest)

    def copy_framework(self, info):
        dest = os.path.join(self.dest, info['shortname'] + '.framework')
        destfn = os.path.join(self.dest, info['name'])
        src = os.path.join(info['location'], info['shortname'] + '.framework')
        if not os.path.exists(dest):
            self.mergetree(src, dest)
            self.pending.append((destfn, iter_platform_files(dest)))
        return destfn

    def run_file(self, fn):
        for mm in self.mms.itervalues():
            mm.run_file(fn)

    def run(self, platfiles=None, contents=None):
        if contents is None:
            contents = '@executable_path/..'

        for arch in self.archs:
            pf = platfiles
            if pf is None:
                pf = iter_platform_files(self.base)

            mm = self.mms[arch]

            for fn in pf:
                mm.run_file(fn)

            while self.pending:
                fmwk, files = self.pending.popleft()
                ref = mm.findNode(fmwk)
                for fn in files:
                    mm.run_file(fn, caller=ref)

        changemap = {}
        skipcontents = os.path.join(os.path.dirname(self.dest), '')
        # filename -> MachO object
        machfiles = {}
        # filename -> list of archs
        archs = {}

        for arch in self.archs:
            mm = self.mms[arch]
            for node in mm.flatten(has_filename_filter):
                machfiles[node.filename] = node
                archs.setdefault(node.filename, [])
                archs[node.filename].append(arch)
                dest = os.path.join(contents, node.filename[len(skipcontents):])
                changemap[node.filename] = dest

        for node in machfiles.itervalues():
            filename = node.filename
            nodearchs = archs[node.filename]
            changed = False
            for arch in nodearchs:
                mm = self.mms[arch]
                def changefunc(path):
                    res = mm.locate(path)
                    return changemap.get(res)

                fn = mm.locate(node.filename)
                if fn is not None:
                    changed = node.getArch(arch).rewriteLoadCommands(changefunc) or changed

            if True or changed:
                f = writablefile(filename, 'rb+')
                node.write(f)
                f.seek(0, 2)
                f.flush()
                f.close()
        
            if node.fat:
                thin_to_archs(filename, nodearchs)

        return set(filter(None, [mm.locate(node.filename) for node in machfiles.itervalues()]))

