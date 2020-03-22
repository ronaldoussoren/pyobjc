from __future__ import print_function

import errno
import os
import stat
import sys

import Cocoa
import FSEvents


def T_or_F(x):
    if x:
        return "TRUE"
    else:
        return "FALSE"


class Settings(object):
    __slots__ = (
        "sinceWhen",
        "latency",
        "flags",
        "array_of_paths",
        "print_settings",
        "verbose",
        "flush_seconds",
    )

    def __init__(self):
        self.sinceWhen = FSEvents.kFSEventStreamEventIdSinceNow
        self.latency = 60
        self.flags = 0
        self.array_of_paths = []
        self.print_settings = False
        self.verbose = False
        self.flush_seconds = -1

    def mesg(self, fmt, *args, **kwds):
        if args:
            fmt = fmt % args

        elif kwds:
            fmt = fmt % kwds

        if self.verbose:
            print(fmt, file=sys.stderr)
        else:
            print(fmt, file=sys.stdout)

    def debug(self, fmt, *args, **kwds):
        if not self.verbose:
            return

        if args:
            fmt = fmt % args

        elif kwds:
            fmt = fmt % kwds

        print(fmt, file=sys.stderr)

    def error(self, fmt, *args, **kwds):
        if args:
            fmt = fmt % args

        elif kwds:
            fmt = fmt % kwds

        print(fmt, file=sys.stderr)

    def dump(self):
        self.mesg("settings->sinceWhen = %d", self.sinceWhen)
        self.mesg("settings->latency = %f", self.latency)
        self.mesg("settings->flags = %#x", self.flags)
        self.mesg("settings->num_paths = %d", len(self.array_of_paths))
        for idx, path in enumerate(self.array_of_paths):
            self.mesg("settings->array_of_paths[%d] = '%s'", idx, path)
        self.mesg("settings->verbose = %s", T_or_F(self.verbose))
        self.mesg("settings->print_settings = %s", T_or_F(self.print_settings))
        self.mesg("settings->flush_seconds = %d", self.flush_seconds)

    def parse_argv(self, argv):
        self.latency = 1.0
        self.sinceWhen = -1  # FSEvents.kFSEventStreamEventIdSinceNow
        self.flush_seconds = -1

        idx = 1
        while idx < len(argv):
            if argv[idx] == "-usage":
                usage(argv[0])

            elif argv[idx] == "-print_settings":
                self.print_settings = True

            elif argv[idx] == "-sinceWhen":
                self.sinceWhen = int(argv[idx + 1])
                idx += 1

            elif argv[idx] == "-latency":
                self.latency = float(argv[idx + 1])
                idx += 1

            elif argv[idx] == "-flags":
                self.flags = int(argv[idx + 1])
                idx += 1

            elif argv[idx] == "-flush":
                self.flush_seconds = float(argv[idx + 1])
                idx += 1

            elif argv[idx] == "-verbose":
                self.verbose = True

            else:
                break

            idx += 1

        self.array_of_paths = argv[idx:]


settings = Settings()


def usage(progname):
    settings.mesg("")
    settings.mesg("Usage: %s <flags> <path>", progname)
    settings.mesg("Flags:")
    settings.mesg(
        "       -sinceWhen <when>          "
        "Specify a time from whence to search for applicable events"
    )
    settings.mesg("       -latency <seconds>         Specify latency")
    settings.mesg("       -flags <flags>             Specify flags as a number")
    settings.mesg(
        "       -flush <seconds>           "
        "Invoke FSEventStreamFlushAsync() after the specified number of seconds."
    )
    settings.mesg("")
    sys.exit(1)


def timer_callback(timer, streamRef):
    settings.debug(
        "CFAbsoluteTimeGetCurrent() => %.3f", Cocoa.CFAbsoluteTimeGetCurrent()
    )
    settings.debug("FSEventStreamFlushAsync(streamRef = %s)", streamRef)
    FSEvents.FSEventStreamFlushAsync(streamRef)


def fsevents_callback(
    streamRef, clientInfo, numEvents, eventPaths, eventMasks, eventIDs
):
    settings.debug(
        "fsevents_callback(streamRef = %s, clientInfo = %s, numEvents = %s)",
        streamRef,
        clientInfo,
        numEvents,
    )
    settings.debug(
        "fsevents_callback: FSEventStreamGetLatestEventId(streamRef) => %s",
        FSEvents.FSEventStreamGetLatestEventId(streamRef),
    )
    full_path = clientInfo

    for i in range(numEvents):
        path = eventPaths[i]
        if path[-1] == "/":
            path = path[:-1]

        if eventMasks[i] & FSEvents.kFSEventStreamEventFlagMustScanSubDirs:
            recursive = True

        elif eventMasks[i] & FSEvents.kFSEventStreamEventFlagUserDropped:
            settings.mesg("BAD NEWS! We dropped events.")
            settings.mesg("Forcing a full rescan.")
            recursive = 1
            path = full_path

        elif eventMasks[i] & FSEvents.kFSEventStreamEventFlagKernelDropped:
            settings.mesg("REALLY BAD NEWS! The kernel dropped events.")
            settings.mesg("Forcing a full rescan.")
            recursive = 1
            path = full_path

        else:
            recursive = False

        new_size = get_directory_size(path, recursive)
        if new_size < 0:
            print("Could not update size on %s" % (path,))

        else:
            print(
                "New total size: %d (change made to %s) for path: %s"
                % (get_total_size(), path, full_path)
            )


def my_FSEventStreamCreate(path):
    if settings.verbose:
        print([path])

    streamRef = FSEvents.FSEventStreamCreate(
        Cocoa.kCFAllocatorDefault,
        fsevents_callback,
        path,
        [path],
        settings.sinceWhen,
        settings.latency,
        settings.flags,
    )
    if streamRef is None:
        settings.error("ERROR: FSEVentStreamCreate() => NULL")
        return None

    if settings.verbose:
        FSEvents.FSEventStreamShow(streamRef)

    return streamRef


def main(argv=None):
    if argv is None:
        argv = sys.argv

    settings.parse_argv(argv)

    if settings.verbose or settings.print_settings:
        settings.dump()

    if settings.print_settings:
        return 0

    if len(settings.array_of_paths) != 1:
        usage(argv[0])

    full_path = os.path.abspath(settings.array_of_paths[0])

    streamRef = my_FSEventStreamCreate(full_path)

    FSEvents.FSEventStreamScheduleWithRunLoop(
        streamRef, Cocoa.CFRunLoopGetCurrent(), Cocoa.kCFRunLoopDefaultMode
    )

    startedOK = FSEvents.FSEventStreamStart(streamRef)
    if not startedOK:
        settings.error("failed to start the FSEventStream")
        return

    # NOTE: we get the initial size *after* we start the
    #       FSEventStream so that there is no window
    #       during which we would miss events.
    #
    # dir_sz = get_directory_size(full_path, 1)
    print("Initial total size is: %d for path: %s" % (get_total_size(), full_path))

    if settings.flush_seconds >= 0:
        settings.debug(
            "CFAbsoluteTimeGetCurrent() => %.3f", Cocoa.CFAbsoluteTimeGetCurrent()
        )

        timer = Cocoa.CFRunLoopTimerCreate(
            FSEvents.FSEventStreamGetSinceWhen(streamRef),
            Cocoa.CFAbsoluteTimeGetCurrent() + settings.flush_seconds,
            settings.flush_seconds,
            0,
            0,
            timer_callback,
            streamRef,
        )
        Cocoa.CFRunLoopAddTimer(
            Cocoa.CFRunLoopGetCurrent(), timer, Cocoa.kCFRunLoopDefaultMode
        )

    # Run
    Cocoa.CFRunLoopRun()

    # Stop / Invalidate / Release
    FSEvents.FSEventStreamStop(streamRef)
    FSEvents.FSEventStreamInvalidate(streamRef)
    # FSEventStreamRelease(streamRef)
    return


#
# --------------------------------------------------------------------------------
# Routines to keep track of the size of the directory hierarchy
# we are watching.
#
# This code is not exemplary in any way.  It should definitely
# not be used in production code as it is inefficient.
#


class dir_item(object):
    __slots__ = ("dirname", "size")


dir_items = {}


def get_total_size():
    return sum(dir_items.values())


def iterate_subdirs(dirname, recursive):
    dir_items[dirname] = 0

    try:
        names = os.listdir(dirname)
    except os.error as msg:
        if msg.errno in (errno.ENOENT, errno.EPERM, errno.EACCES):
            del dir_items[dirname]
            return 0

        raise

    size = 0
    for nm in names:
        full_path = os.path.join(dirname, nm)
        st = os.lstat(full_path)
        size += st.st_size

        if stat.S_ISDIR(st.st_mode) and (recursive or (full_path not in dir_items)):
            size += get_directory_size(full_path, 1)

    dir_items[dirname] = size
    return size


def check_for_deleted_dirs():
    for path in dir_items.keys():
        try:
            os.stat(path)
        except os.error:
            del dir_items[path]


def get_directory_size(dirname, recursive):
    check_for_deleted_dirs()
    return iterate_subdirs(dirname, recursive)


if __name__ == "__main__":
    main()
