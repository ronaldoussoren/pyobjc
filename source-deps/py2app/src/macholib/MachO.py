"""
Utilities for reading and writing Mach-O headers
"""

import sys
from macholib.mach_o import *
from macholib.dyld import dyld_find, framework_info
from altgraph.compat import *

__all__ = ['MachO']

RELOCATABLE = set((
    # relocatable commands that should be used for dependency walking
    LC_LOAD_DYLIB,
    LC_LOAD_WEAK_DYLIB,
    LC_PREBOUND_DYLIB,
))

RELOCATABLE_NAMES = {
    LC_LOAD_DYLIB: 'load_dylib',
    LC_LOAD_WEAK_DYLIB: 'load_weak_dylib',
    LC_PREBOUND_DYLIB: 'prebound_dylib',
}

def shouldRelocateCommand(cmd):
    """Should this command id be investigated for relocation?"""
    return cmd in RELOCATABLE

class MachO(object):
    """Provides reading/writing the Mach-O header of a specific existing file"""
    #   filename   - the original filename of this mach-o
    #   sizediff   - the current deviation from the initial mach-o size
    #   header     - the mach-o header
    #   commands   - a list of (load_command, somecommand, data)
    #                data is either a str, or a list of segment structures
    #   total_size - the current mach-o header size (including header)
    #   low_offset - essentially, the maximum mach-o header size
    #   id_cmd     - the index of my id command, or None

    def __init__(self, filename):

        # supports the ObjectGraph protocol
        self.graphident = filename
        self.filename = filename

        # These are all initialized by self.load()
        self.header = None
        self.commands = None
        self.id_cmd = None
        self.sizediff = None
        self.total_size = None
        self.low_offset = None
        self.filetype = None

        self.load(file(filename, 'rb'))

    def __repr__(self):
        return "<MachO filename=%r>" % (self.filename,)

    def load(self, fh):
        self.sizediff = 0
        header = self.header = mach_header.from_fileobj(fh)
        cmd = self.commands = []

        self.filetype = MH_FILETYPE_SHORTNAMES[header.filetype]

        read_bytes = 0
        low_offset = sys.maxint
        for i in range(header.ncmds):
            # read the load command
            cmd_load = load_command.from_fileobj(fh)

            # read the specific command
            klass = LC_REGISTRY.get(cmd_load.cmd, None)
            if klass is None:
                raise ValueError, "Unknown load command: %d" % (cmd_load.cmd,)
            cmd_cmd = klass.from_fileobj(fh)

            if cmd_load.cmd == LC_ID_DYLIB:
                # remember where this command was
                if self.id_cmd is not None:
                    raise ValueError, "This dylib already has an id"""
                self.id_cmd = i

            if cmd_load.cmd == LC_SEGMENT:
                # for segment commands, read the list of segments
                segs = []
                # assert that the size makes sense
                expected_size = (
                    sizeof(klass) + sizeof(load_command) +
                    (sizeof(section) * cmd_cmd.nsects)
                )
                if cmd_load.cmdsize != expected_size:
                    raise ValueError, "Segment size mismatch"
                # this is a zero block or something
                # so the beginning is wherever the fileoff of this command is
                if cmd_cmd.nsects == 0:
                   if cmd_cmd.filesize != 0:
                        low_offset = min(low_offset, cmd_cmd.fileoff)
                else:
                    # this one has multiple segments
                    for j in range(cmd_cmd.nsects):
                        # read the segment
                        seg = section.from_fileobj(fh)
                        # if the segment has a size and is not zero filled
                        # then its beginning is the offset of this segment
                        if seg.size > 0 and ((seg.flags & S_ZEROFILL) != S_ZEROFILL):
                            low_offset = min(low_offset, seg.offset)
                        segs.append(seg)
                # data is a list of segments
                cmd_data = segs
            else:
                # data is a raw str
                data_size = (
                    cmd_load.cmdsize - sizeof(klass) - sizeof(load_command)
                )
                cmd_data = fh.read(data_size)
            cmd.append((cmd_load, cmd_cmd, cmd_data))
            read_bytes += cmd_load.cmdsize
                
        # make sure the header made sense
        if read_bytes != header.sizeofcmds:
            raise ValueError, "Read %d bytes, header reports %d bytes" % (read_bytes, header.sizeofcmds)
        self.total_size = sizeof(mach_header) + read_bytes
        self.low_offset = low_offset

        # this header overwrites a segment, what the heck?
        if self.total_size > low_offset:
            raise ValueError("total_size > low_offset")


    def walkRelocatables(self, shouldRelocateCommand=shouldRelocateCommand):
        """
        for all relocatable commands
        yield (command_index, command_name, filename)
        """
        for (idx, (lc, cmd, data)) in enumerate(self.commands):
            if shouldRelocateCommand(lc.cmd):
                name = RELOCATABLE_NAMES[lc.cmd]
                ofs = cmd.name - sizeof(lc.__class__) - sizeof(cmd.__class__)
                yield idx, name, data[ofs:data.find('\x00', ofs)]
    
    def rewriteInstallNameCommand(self, loadcmd):
        """Rewrite the load command of this dylib"""
        if self.id_cmd is not None:
            self.rewriteDataForCommand(self.id_cmd, loadcmd)
            return True
        return False

    def changedHeaderSizeBy(self, bytes):
        self.sizediff += bytes
        if (self.total_size + self.sizediff) > self.low_offset:
            print "WARNING: Mach-O header may be too large to relocate"
        
    def rewriteLoadCommands(self, changefunc):
        """
        Rewrite the load commands based upon a change dictionary
        """
        data = changefunc(self.filename)
        changed = False
        if data is not None:
            if self.rewriteInstallNameCommand(data):
                changed = True
        for idx, name, filename in self.walkRelocatables():
            data = changefunc(filename)
            if data is not None:
                if self.rewriteDataForCommand(idx, data):
                    changed = True
        return True
    
    def rewriteDataForCommand(self, idx, data):
        lc, cmd, old_data = self.commands[idx]
        hdrsize = sizeof(lc.__class__) + sizeof(cmd.__class__)
        data = data + ('\x00' * (4 - (len(data) % 4)))
        newsize = hdrsize + len(data)
        self.commands[idx] = (lc, cmd, data)
        self.changedHeaderSizeBy(newsize - lc.cmdsize)
        lc.cmdsize, cmd.name = newsize, hdrsize
        return True

    def synchronize_size(self):
        if (self.total_size + self.sizediff) > self.low_offset:
            raise ValueError, "New Mach-O header is too large to relocate"
        self.header.sizeofcmds += self.sizediff
        self.total_size = sizeof(mach_header) + self.header.sizeofcmds
        self.sizediff = 0

    def write(self, fileobj):
        # serialize all the mach-o commands
        self.synchronize_size()
        # this should nearly always be 0, but we keep track anyway
        begin = fileobj.tell()
        self.header.to_fileobj(fileobj)
        for (lc, cmd, data) in self.commands:
            lc.to_fileobj(fileobj)
            cmd.to_fileobj(fileobj)
            if isinstance(data, str):
                fileobj.write(data)
            else:
                # segments..
                for obj in data:
                    obj.to_fileobj(fileobj)

        # zero out the unused space, doubt this is strictly necessary
        # and is generally probably already the case
        fileobj.write('\x00' * (self.low_offset - (fileobj.tell() - begin)))
    
    def getSymbolTableCommand(self):
        for (lc, cmd, data) in self.commands:
            if lc.cmd == LC_SYMTAB:
                return cmd
        return None

    def getDynamicSymbolTableCommand(self):
        for (lc, cmd, data) in self.commands:
            if lc.cmd == LC_DYSYMTAB:
                return cmd
        return None

def main(fn):
    m = MachO(fn)
    seen = set()
    for idx, name, other in m.walkRelocatables():
        if other not in seen:
            seen.add(other)
            print '\t'+other

if __name__ == '__main__':
    import sys
    files = sys.argv[1:] or ['/bin/ls']
    for fn in files:
        print fn
        main(fn)
