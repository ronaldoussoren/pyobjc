#!/usr/bin/env python
"""Create a "virtual" Python installation
"""

import sys
import os
import optparse
import shutil
import logging
import distutils.sysconfig
import zlib
import base64
import subprocess
    
join = os.path.join
py_version = 'python%s.%s' % (sys.version_info[0], sys.version_info[1])
is_jython = sys.platform.startswith('java')
expected_exe = is_jython and 'jython' or 'python3'

REQUIRED_MODULES = ['os', 'posix', 'posixpath', 'ntpath', 'genericpath',
                    'fnmatch', 'locale', 'encodings', 'codecs',
                    'stat', 'UserDict', 'readline', 'copy_reg', 'types',
                    're', 'sre', 'sre_parse', 'sre_constants', 'sre_compile',
                    'lib-dynload', 'config', 'zlib', 'warnings', 'linecache',
                    '_abcoll', 'abc', 'io', '_weakrefset', 'copyreg',
                    'tempfile', 'random', '__future__', 'collections',
                    'keyword', 'tarfile', 'shutil', 'struct', 'copy']

class Logger(object):

    """
    Logging object for use in command-line script.  Allows ranges of
    levels, to avoid some redundancy of displayed information.
    """

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    NOTIFY = (logging.INFO+logging.WARN)/2
    WARN = WARNING = logging.WARN
    ERROR = logging.ERROR
    FATAL = logging.FATAL

    LEVELS = [DEBUG, INFO, NOTIFY, WARN, ERROR, FATAL]

    def __init__(self, consumers):
        self.consumers = consumers
        self.indent = 0
        self.in_progress = None
        self.in_progress_hanging = False

    def debug(self, msg, *args, **kw):
        self.log(self.DEBUG, msg, *args, **kw)
    def info(self, msg, *args, **kw):
        self.log(self.INFO, msg, *args, **kw)
    def notify(self, msg, *args, **kw):
        self.log(self.NOTIFY, msg, *args, **kw)
    def warn(self, msg, *args, **kw):
        self.log(self.WARN, msg, *args, **kw)
    def error(self, msg, *args, **kw):
        self.log(self.WARN, msg, *args, **kw)
    def fatal(self, msg, *args, **kw):
        self.log(self.FATAL, msg, *args, **kw)
    def log(self, level, msg, *args, **kw):
        if args:
            if kw:
                raise TypeError(
                    "You may give positional or keyword arguments, not both")
        args = args or kw
        rendered = None
        for consumer_level, consumer in self.consumers:
            if self.level_matches(level, consumer_level):
                if (self.in_progress_hanging
                    and consumer in (sys.stdout, sys.stderr)):
                    self.in_progress_hanging = False
                    sys.stdout.write('\n')
                    sys.stdout.flush()
                if rendered is None:
                    if args:
                        rendered = msg % args
                    else:
                        rendered = msg
                    rendered = ' '*self.indent + rendered
                if hasattr(consumer, 'write'):
                    consumer.write(rendered+'\n')
                else:
                    consumer(rendered)

    def start_progress(self, msg):
        assert not self.in_progress, (
            "Tried to start_progress(%r) while in_progress %r"
            % (msg, self.in_progress))
        if self.level_matches(self.NOTIFY, self._stdout_level()):
            sys.stdout.write(msg)
            sys.stdout.flush()
            self.in_progress_hanging = True
        else:
            self.in_progress_hanging = False
        self.in_progress = msg

    def end_progress(self, msg='done.'):
        assert self.in_progress, (
            "Tried to end_progress without start_progress")
        if self.stdout_level_matches(self.NOTIFY):
            if not self.in_progress_hanging:
                # Some message has been printed out since start_progress
                sys.stdout.write('...' + self.in_progress + msg + '\n')
                sys.stdout.flush()
            else:
                sys.stdout.write(msg + '\n')
                sys.stdout.flush()
        self.in_progress = None
        self.in_progress_hanging = False

    def show_progress(self):
        """If we are in a progress scope, and no log messages have been
        shown, write out another '.'"""
        if self.in_progress_hanging:
            sys.stdout.write('.')
            sys.stdout.flush()

    def stdout_level_matches(self, level):
        """Returns true if a message at this level will go to stdout"""
        return self.level_matches(level, self._stdout_level())

    def _stdout_level(self):
        """Returns the level that stdout runs at"""
        for level, consumer in self.consumers:
            if consumer is sys.stdout:
                return level
        return self.FATAL

    def level_matches(self, level, consumer_level):
        """
        >>> l = Logger()
        >>> l.level_matches(3, 4)
        False
        >>> l.level_matches(3, 2)
        True
        >>> l.level_matches(slice(None, 3), 3)
        False
        >>> l.level_matches(slice(None, 3), 2)
        True
        >>> l.level_matches(slice(1, 3), 1)
        True
        >>> l.level_matches(slice(2, 3), 1)
        False
        """
        if isinstance(level, slice):
            start, stop = level.start, level.stop
            if start is not None and start > consumer_level:
                return False
            if stop is not None or stop <= consumer_level:
                return False
            return True
        else:
            return level >= consumer_level

    #@classmethod
    def level_for_integer(cls, level):
        levels = cls.LEVELS
        if level < 0:
            return levels[0]
        if level >= len(levels):
            return levels[-1]
        return levels[level]

    level_for_integer = classmethod(level_for_integer)

def mkdir(path):
    if not os.path.exists(path):
        logger.info('Creating %s', path)
        os.makedirs(path)
    else:
        logger.info('Directory %s already exists', path)

def copyfile(src, dest, symlink=True):
    if not os.path.exists(src):
        # Some bad symlink in the src
        logger.warn('Cannot find file %s (bad symlink)', src)
        return
    if os.path.exists(dest):
        logger.debug('File %s already exists', dest)
        return
    if not os.path.exists(os.path.dirname(dest)):
        logger.info('Creating parent directories for %s' % os.path.dirname(dest))
        os.makedirs(os.path.dirname(dest))
    if symlink and hasattr(os, 'symlink'):
        logger.info('Symlinking %s', dest)
        os.symlink(os.path.abspath(src), dest)
    else:
        logger.info('Copying to %s', dest)
        if os.path.isdir(src):
            shutil.copytree(src, dest, True)
        else:
            shutil.copy2(src, dest)

def writefile(dest, content, overwrite=True):
    if not os.path.exists(dest):
        logger.info('Writing %s', dest)
        f = open(dest, 'wb')
        f.write(content)
        f.close()
        return
    else:
        f = open(dest, 'rb')
        c = f.read()
        f.close()
        if c != content:
            if not overwrite:
                logger.notify('File %s exists with different content; not overwriting', dest)
                return
            logger.notify('Overwriting %s with new content', dest)
            f = open(dest, 'wb')
            f.write(content)
            f.close()
        else:
            logger.info('Content %s already in place', dest)

def rmtree(dir):
    if os.path.exists(dir):
        logger.notify('Deleting tree %s', dir)
        shutil.rmtree(dir)
    else:
        logger.info('Do not need to delete %s; already gone', dir)

def make_exe(fn):
    if hasattr(os, 'chmod'):
        oldmode = os.stat(fn).st_mode & 0o7777
        newmode = (oldmode | 0o555) & 0o7777
        os.chmod(fn, newmode)
        logger.info('Changed mode of %s to %s', fn, oct(newmode))

def install_setuptools(py_executable, unzip=False):
    #setup_fn = 'setuptools-0.6c9-py%s.egg' % sys.version[:3]
    search_dirs = ['.', os.path.dirname(__file__), join(os.path.dirname(__file__), 'support-files')]
    if os.path.splitext(os.path.dirname(__file__))[0] != 'virtualenv3':
        # Probably some boot script; just in case virtualenv is installed...
        try:
            import virtualenv3
        except ImportError:
            pass
        else:
            search_dirs.append(os.path.join(os.path.dirname(virtualenv3.__file__), 'support-files'))

    setup_fn = None
    for dir in search_dirs:
        for fn in os.listdir(dir):
            if fn.startswith('distribute') and fn.endswith('-py%s.egg'%(sys.version[:3],)):
                setup_fn = join(dir, fn)
                break


    path = os.environ['PATH']
    path = os.path.dirname(py_executable) + ":" + path
    env = { "PATH": path }
    cmd = [ "/bin/sh", setup_fn ]

    call_subprocess(cmd, show_stdout=False,
        filter_stdout=filter_ez_setup,
        extra_env=env,
        )

def filter_ez_setup(line):
    if not line.strip():
        return Logger.DEBUG
    for prefix in ['Reading ', 'Best match', 'Processing setuptools',
                   'Copying setuptools', 'Adding setuptools',
                   'Installing ', 'Installed ']:
        if line.startswith(prefix):
            return Logger.DEBUG
    return Logger.INFO

def main():
    parser = optparse.OptionParser(
        version="1.3.4dev",
        usage="%prog [OPTIONS] DEST_DIR")

    parser.add_option(
        '-v', '--verbose',
        action='count',
        dest='verbose',
        default=0,
        help="Increase verbosity")

    parser.add_option(
        '-q', '--quiet',
        action='count',
        dest='quiet',
        default=0,
        help='Decrease verbosity')

    parser.add_option(
        '-p', '--python',
        dest='python',
        metavar='PYTHON_EXE',
        help='The Python interpreter to use, e.g., --python=python2.5 will use the python2.5 '
        'interpreter to create the new environment.  The default is the interpreter that '
        'virtualenv was installed with (%s)' % sys.executable)

    parser.add_option(
        '--clear',
        dest='clear',
        action='store_true',
        help="Clear out the non-root install and start from scratch")

    parser.add_option(
        '--no-site-packages',
        dest='no_site_packages',
        action='store_true',
        help="Don't give access to the global site-packages dir to the "
             "virtual environment")

    parser.add_option(
        '--unzip-setuptools',
        dest='unzip_setuptools',
        action='store_true',
        help="Unzip Setuptools when installing it")

    parser.add_option(
        '--relocatable',
        dest='relocatable',
        action='store_true',
        help='Make an EXISTING virtualenv environment relocatable.  '
        'This fixes up scripts and makes all .pth files relative')

    if 'extend_parser' in globals():
        extend_parser(parser)

    options, args = parser.parse_args()

    global logger

    if 'adjust_options' in globals():
        adjust_options(options, args)

    verbosity = options.verbose - options.quiet
    logger = Logger([(Logger.level_for_integer(2-verbosity), sys.stdout)])

    if options.python and not os.environ.get('VIRTUALENV_INTERPRETER_RUNNING'):
        env = os.environ.copy()
        interpreter = resolve_interpreter(options.python)
        if interpreter == sys.executable:
            logger.warn('Already using interpreter %s' % interpreter)
        else:
            logger.notify('Running virtualenv with interpreter %s' % interpreter)
            env['VIRTUALENV_INTERPRETER_RUNNING'] = 'true'
            file = __file__
            if file.endswith('.pyc'):
                file = file[:-1]
            os.execvpe(interpreter, [interpreter, file] + sys.argv[1:], env)

    if not args:
        print('You must provide a DEST_DIR')
        parser.print_help()
        sys.exit(2)
    if len(args) > 1:
        print('There must be only one argument: DEST_DIR (you gave %s)' % (
            ' '.join(args)))
        parser.print_help()
        sys.exit(2)

    home_dir = args[0]

    if os.environ.get('WORKING_ENV'):
        logger.fatal('ERROR: you cannot run virtualenv while in a workingenv')
        logger.fatal('Please deactivate your workingenv, then re-run this script')
        sys.exit(3)

    if os.environ.get('PYTHONHOME'):
        if sys.platform == 'win32':
            name = '%PYTHONHOME%'
        else:
            name = '$PYTHONHOME'
        logger.warn('%s is set; this can cause problems creating environments' % name)

    if options.relocatable:
        make_environment_relocatable(home_dir)
        return

    create_environment(home_dir, site_packages=not options.no_site_packages, clear=options.clear,
                       unzip_setuptools=options.unzip_setuptools)
    if 'after_install' in globals():
        after_install(options, home_dir)

def call_subprocess(cmd, show_stdout=True,
                    filter_stdout=None, cwd=None,
                    raise_on_returncode=True, extra_env=None):
    cmd_parts = []
    for part in cmd:
        if isinstance(part, bytes):
            part = part.decode('utf-8')
        if len(part) > 40:
            part = part[:30]+"..."+part[-5:]
        if ' ' in part or '\n' in part or '"' in part or "'" in part:
            part = '"%s"' % part.replace('"', '\\"')
        cmd_parts.append(part)
    cmd_desc = ' '.join(cmd_parts)
    if show_stdout:
        stdout = None
    else:
        stdout = subprocess.PIPE
    logger.debug("Running command %s" % cmd_desc)
    if extra_env:
        env = os.environ.copy()
        env.update(extra_env)
    else:
        env = None
    try:
        proc = subprocess.Popen(
            cmd, stderr=subprocess.STDOUT, stdin=None, stdout=stdout,
            cwd=cwd, env=env)
    except Exception as e:
        logger.fatal(
            "Error %s while executing command %s" % (e, cmd_desc))
        raise
    all_output = []
    if stdout is not None:
        stdout = proc.stdout
        while 1:
            line = stdout.readline().decode('ascii')
            if not line:
                break
            line = line.rstrip()
            all_output.append(line)
            if filter_stdout:
                level = filter_stdout(line)
                if isinstance(level, tuple):
                    level, line = level
                logger.log(level, line)
                if not logger.stdout_level_matches(level):
                    logger.show_progress()
            else:
                logger.info(line)
    else:
        proc.communicate()
    proc.wait()
    if proc.returncode:
        if raise_on_returncode:
            if all_output:
                logger.notify('Complete output from command %s:' % cmd_desc)
                logger.notify('\n'.join(all_output) + '\n----------------------------------------')
            raise OSError(
                "Command %s failed with error code %s"
                % (cmd_desc, proc.returncode))
        else:
            logger.warn(
                "Command %s had error code %s"
                % (cmd_desc, proc.returncode))


def create_environment(home_dir, site_packages=True, clear=False,
                       unzip_setuptools=False):
    """
    Creates a new environment in ``home_dir``.

    If ``site_packages`` is true (the default) then the global
    ``site-packages/`` directory will be on the path.

    If ``clear`` is true (default False) then the environment will
    first be cleared.
    """
    home_dir, lib_dir, inc_dir, bin_dir = path_locations(home_dir)

    py_executable = install_python(
        home_dir, lib_dir, inc_dir, bin_dir, 
        site_packages=site_packages, clear=clear)

    install_distutils(lib_dir, home_dir)

    install_setuptools(py_executable, unzip=unzip_setuptools)

    install_activate(home_dir, bin_dir)

def path_locations(home_dir):
    """Return the path locations for the environment (where libraries are,
    where scripts go, etc)"""
    # XXX: We'd use distutils.sysconfig.get_python_inc/lib but its
    # prefix arg is broken: http://bugs.python.org/issue3386
    if sys.platform == 'win32':
        # Windows has lots of problems with executables with spaces in
        # the name; this function will remove them (using the ~1
        # format):
        mkdir(home_dir)
        if ' ' in home_dir:
            try:
                import win32api
            except ImportError:
                print('Error: the path "%s" has a space in it' % home_dir)
                print('To handle these kinds of paths, the win32api module must be installed:')
                print('  http://sourceforge.net/projects/pywin32/')
                sys.exit(3)
            home_dir = win32api.GetShortPathName(home_dir)
        lib_dir = join(home_dir, 'Lib')
        inc_dir = join(home_dir, 'Include')
        bin_dir = join(home_dir, 'Scripts')
    elif is_jython:
        lib_dir = join(home_dir, 'Lib')
        inc_dir = join(home_dir, 'Include')
        bin_dir = join(home_dir, 'bin')
    else:
        lib_dir = join(home_dir, 'lib', py_version)
        inc_dir = join(home_dir, 'include', py_version)
        bin_dir = join(home_dir, 'bin')
    return home_dir, lib_dir, inc_dir, bin_dir

def install_python(home_dir, lib_dir, inc_dir, bin_dir, site_packages, clear):
    """Install just the base environment, no distutils patches etc"""
    if sys.executable.startswith(bin_dir):
        print('Please use the *system* python to run this script')
        return
        
    if clear:
        rmtree(lib_dir)
        ## FIXME: why not delete it?
        ## Maybe it should delete everything with #!/path/to/venv/python in it
        logger.notify('Not deleting %s', bin_dir)

    if hasattr(sys, 'real_prefix'):
        logger.notify('Using real prefix %r' % sys.real_prefix)
        prefix = sys.real_prefix
    else:
        prefix = sys.prefix
    mkdir(lib_dir)
    fix_lib64(lib_dir)
    stdlib_dirs = [os.path.dirname(os.__file__)]
    if sys.platform == 'win32':
        stdlib_dirs.append(join(os.path.dirname(stdlib_dirs[0]), 'DLLs'))
    elif sys.platform == 'darwin':
        stdlib_dirs.append(join(stdlib_dirs[0], 'site-packages'))
        macosx_framework_name = distutils.sysconfig.get_config_var('PYTHONFRAMEWORK')
        macosx_framework = '/' + macosx_framework_name + '.framework/'

    for stdlib_dir in stdlib_dirs:
        if not os.path.isdir(stdlib_dir):
            continue
        if hasattr(os, 'symlink'):
            logger.info('Symlinking Python bootstrap modules')
        else:
            logger.info('Copying Python bootstrap modules')
        logger.indent += 2
        try:
            for fn in os.listdir(stdlib_dir):
                if fn != 'site-packages' and os.path.splitext(fn)[0] in REQUIRED_MODULES:
                    copyfile(join(stdlib_dir, fn), join(lib_dir, fn))
        finally:
            logger.indent -= 2
    mkdir(join(lib_dir, 'site-packages'))
    writefile(join(lib_dir, 'site.py'), SITE_PY)
    writefile(join(lib_dir, 'orig-prefix.txt'), prefix.encode('utf-8'))
    site_packages_filename = join(lib_dir, 'no-global-site-packages.txt')
    if not site_packages:
        writefile(site_packages_filename, b'')
    else:
        if os.path.exists(site_packages_filename):
            logger.info('Deleting %s' % site_packages_filename)
            os.unlink(site_packages_filename)

    stdinc_dir = join(prefix, 'include', py_version)
    if os.path.exists(stdinc_dir):
        copyfile(stdinc_dir, inc_dir)
    else:
        logger.debug('No include dir %s' % stdinc_dir)

    if sys.exec_prefix != prefix:
        if sys.platform == 'win32':
            exec_dir = join(sys.exec_prefix, 'lib')
        elif is_jython:
            exec_dir = join(sys.exec_prefix, 'Lib')
        else:
            exec_dir = join(sys.exec_prefix, 'lib', py_version)
        for fn in os.listdir(exec_dir):
            copyfile(join(exec_dir, fn), join(lib_dir, fn))
    
    if is_jython:
        # Jython has either jython-dev.jar and javalib/ dir, or just
        # jython.jar
        for name in 'jython-dev.jar', 'javalib', 'jython.jar':
            src = join(prefix, name)
            if os.path.exists(src):
                copyfile(src, join(home_dir, name))
        # XXX: registry should always exist after Jython 2.5rc1
        src = join(prefix, 'registry')
        if os.path.exists(src):
            copyfile(src, join(home_dir, 'registry'), symlink=False)
        copyfile(join(prefix, 'cachedir'), join(home_dir, 'cachedir'),
                 symlink=False)

    mkdir(bin_dir)
    py_executable = join(bin_dir, os.path.basename(sys.executable))
    if sys.platform == 'darwin' and macosx_framework in prefix:
        # The name of the python executable is not quite what
        # we want, rename it.
        py_executable = os.path.join(
                os.path.dirname(py_executable), 'python3')

    logger.notify('New %s executable in %s', expected_exe, py_executable)
    if sys.executable != py_executable:
        ## FIXME: could I just hard link?
        executable = sys.executable
        if sys.platform == 'cygwin' and os.path.exists(executable + '.exe'):
            # Cygwin misreports sys.executable sometimes
            executable += '.exe'
            py_executable += '.exe'
            logger.info('Executable actually exists in %s' % executable)
        shutil.copyfile(executable, py_executable)
        make_exe(py_executable)
        if sys.platform == 'win32' or sys.platform == 'cygwin':
            pythonw = os.path.join(os.path.dirname(sys.executable), 'pythonw.exe')
            if os.path.exists(pythonw):
                logger.info('Also created pythonw.exe')
                shutil.copyfile(pythonw, os.path.join(os.path.dirname(py_executable), 'pythonw.exe'))
                
    if os.path.splitext(os.path.basename(py_executable))[0] != expected_exe:
        secondary_exe = os.path.join(os.path.dirname(py_executable),
                                     expected_exe)
        py_executable_ext = os.path.splitext(py_executable)[1]
        if py_executable_ext == '.exe':
            # python2.4 gives an extension of '.4' :P
            secondary_exe += py_executable_ext
        if os.path.exists(secondary_exe):
            logger.warn('Not overwriting existing %s script %s (you must use %s)'
                        % (expected_exe, secondary_exe, py_executable))
        else:
            logger.notify('Also creating executable in %s' % secondary_exe)
            shutil.copyfile(sys.executable, secondary_exe)
            make_exe(secondary_exe)
    
    if sys.platform == 'darwin' and macosx_framework in prefix:
        logger.debug('MacOSX Python framework detected')
        
        # Make sure we use the the embedded interpreter inside
        # the framework, even if sys.executable points to
        # the stub executable in ${sys.prefix}/bin
        # See http://groups.google.com/group/python-virtualenv/
        #                              browse_thread/thread/17cab2f85da75951
        embedded = os.path.join(prefix, 'Resources/Python.app/Contents/MacOS/Python')
        if not os.path.exists(embedded):
            embedded = os.path.join(prefix, 'Resources/Python.app/Contents/MacOS', macosx_framework_name)
        shutil.copy(
                embedded,
                py_executable)

        # Copy the framework's dylib into the virtual 
        # environment
        virtual_lib = os.path.join(home_dir, '.Python')

        if os.path.exists(virtual_lib):
            os.unlink(virtual_lib)
        copyfile(
            os.path.join(prefix, macosx_framework_name),
            virtual_lib)

        if (sys.version_info[0] == 2 and sys.version_info[1] >= 7) or \
            (sys.version_info[0] == 3 and sys.version_info[1] >= 2):
            # Python 2.7 (and later) and Python 3.2 (and later) include
            # a version of pythonw with hooks for virtualenv, use those hooks.
            embedded = os.path.join(home_dir, '.Resources/Python.app/Contents/MacOS', macosx_framework_name)
            if not os.path.exists(os.path.dirname(embedded)):
                os.makedirs(os.path.dirname(embedded))

            os.rename(py_executable, embedded)
            try:
                call_subprocess(
                    ["install_name_tool", "-change",
                     os.path.join(prefix, macosx_framework_name),
                     '@executable_path/../../../../.Python',
                     embedded])
            except:
                logger.fatal(
                    "Could not call install_name_tool -- you must have Apple's development tools installed")
                raise

            shutil.copy(os.path.join(prefix, 'bin/python3'), py_executable)


        # And then change the install_name of the copied python executable
        try:
            call_subprocess(
                ["install_name_tool", "-change",
                 os.path.join(prefix, macosx_framework_name),
                 '@executable_path/../.Python',
                 py_executable])
        except:
            logger.fatal(
                "Could not call install_name_tool -- you must have Apple's development tools installed")
            raise

        # Some tools depend on pythonX.Y being present
        py_executable_version = '.%s' % (
            sys.version_info[1],)
        if not py_executable.endswith(py_executable_version):
            # symlinking pythonX.Y > python
            pth = py_executable + '.%s' % (
                    sys.version_info[1],)
            if os.path.exists(pth):
                os.unlink(pth)
            os.symlink('python3', pth)
        else:
            # reverse symlinking python -> pythonX.Y (with --python)
            pth = join(bin_dir, 'python3')
            if os.path.exists(pth):
                os.unlink(pth)
            os.symlink(os.path.basename(py_executable), pth)

    if sys.platform == 'win32' and ' ' in py_executable:
        # There's a bug with subprocess on Windows when using a first
        # argument that has a space in it.  Instead we have to quote
        # the value:
        py_executable = '"%s"' % py_executable
    cmd = [py_executable, '-c',
           'import sys; sys.stdout.write(sys.prefix)']
    logger.info('Testing executable with %s %s "%s"' % tuple(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    proc_stdout, proc_stderr = proc.communicate()
    proc_stdout = proc_stdout.decode('utf-8').strip()
    proc_stdout = os.path.normcase(os.path.abspath(proc_stdout))
    if proc_stdout != os.path.normcase(os.path.abspath(home_dir)):
        logger.fatal(
            'ERROR: The executable %s is not functioning' % py_executable)
        logger.fatal(
            'ERROR: It thinks sys.prefix is %r (should be %r)'
            % (proc_stdout, os.path.normcase(os.path.abspath(home_dir))))
        logger.fatal(
            'ERROR: virtualenv is not compatible with this system or executable')
        sys.exit(100)
    else:
        logger.info('Got sys.prefix result: %r' % proc_stdout)

    pydistutils = os.path.expanduser('~/.pydistutils.cfg')
    if os.path.exists(pydistutils):
        logger.notify('Please make sure you remove any previous custom paths from '
                      'your %s file.' % pydistutils)
    ## FIXME: really this should be calculated earlier
    return py_executable

def install_activate(home_dir, bin_dir):
    if sys.platform == 'win32' or is_jython and os._name == 'nt':
        files = {'activate.bat': ACTIVATE_BAT,
                 'deactivate.bat': DEACTIVATE_BAT}
        if os.environ.get('OS') == 'Windows_NT' and os.environ.get('OSTYPE') == 'cygwin':
            files['activate'] = ACTIVATE_SH
    else:
        files = {'activate': ACTIVATE_SH}
    files['activate_this.py'] = ACTIVATE_THIS
    for name, content in list(files.items()):
        content = content.replace(b'__VIRTUAL_ENV__',
                                  os.path.abspath(home_dir).encode('utf-8'))
        content = content.replace(b'__VIRTUAL_NAME__',
                                  os.path.basename(os.path.abspath(home_dir))
                                  .encode('utf-8'))
        content = content.replace(b'__BIN_NAME__',
                                  os.path.basename(bin_dir).encode('utf-8'))

        writefile(os.path.join(bin_dir, name), content)

def install_distutils(lib_dir, home_dir):
    distutils_path = os.path.join(lib_dir, 'distutils')
    mkdir(distutils_path)
    ## FIXME: maybe this prefix setting should only be put in place if
    ## there's a local distutils.cfg with a prefix setting?
    home_dir = os.path.abspath(home_dir)
    ## FIXME: this is breaking things, removing for now:
    #distutils_cfg = DISTUTILS_CFG + "\n[install]\nprefix=%s\n" % home_dir
    writefile(os.path.join(distutils_path, '__init__.py'), DISTUTILS_INIT)
    writefile(os.path.join(distutils_path, 'distutils.cfg'), DISTUTILS_CFG, overwrite=False)

def fix_lib64(lib_dir):
    """
    Some platforms (particularly Gentoo on x64) put things in lib64/pythonX.Y
    instead of lib/pythonX.Y.  If this is such a platform we'll just create a
    symlink so lib64 points to lib
    """
    if [p for p in list(distutils.sysconfig.get_config_vars().values()) 
        if isinstance(p, str) and 'lib64' in p]:
        logger.debug('This system uses lib64; symlinking lib64 to lib')
        assert os.path.basename(lib_dir) == 'python%s' % sys.version[:3], (
            "Unexpected python lib dir: %r" % lib_dir)
        lib_parent = os.path.dirname(lib_dir)
        assert os.path.basename(lib_parent) == 'lib', (
            "Unexpected parent dir: %r" % lib_parent)
        copyfile(lib_parent, os.path.join(os.path.dirname(lib_parent), 'lib64'))

def resolve_interpreter(exe):
    """
    If the executable given isn't an absolute path, search $PATH for the interpreter
    """
    if os.path.abspath(exe) != exe:
        paths = os.environ.get('PATH', '').split(os.pathsep)
        for path in paths:
            if os.path.exists(os.path.join(path, exe)):
                exe = os.path.join(path, exe)
                break
    if not os.path.exists(exe):
        logger.fatal('The executable %s (from --python=%s) does not exist' % (exe, exe))
        sys.exit(3)
    return exe

############################################################
## Relocating the environment:

def make_environment_relocatable(home_dir):
    """
    Makes the already-existing environment use relative paths, and takes out 
    the #!-based environment selection in scripts.
    """
    activate_this = os.path.join(home_dir, 'bin', 'activate_this.py')
    if not os.path.exists(activate_this):
        logger.fatal(
            'The environment doesn\'t have a file %s -- please re-run virtualenv '
            'on this environment to update it' % activate_this)
    fixup_scripts(home_dir)
    fixup_pth_and_egg_link(home_dir)
    ## FIXME: need to fix up distutils.cfg

OK_ABS_SCRIPTS = ['python', 'python%s' % sys.version[:3],
                  'activate', 'activate.bat', 'activate_this.py']

def fixup_scripts(home_dir):
    # This is what we expect at the top of scripts:
    shebang = '#!%s/bin/python' % os.path.normcase(os.path.abspath(home_dir))
    # This is what we'll put:
    new_shebang = '#!/usr/bin/env python%s' % sys.version[:3]
    activate = "import os; activate_this=os.path.join(os.path.dirname(__file__), 'activate_this.py'); execfile(activate_this, dict(__file__=activate_this)); del os, activate_this"
    bin_dir = os.path.join(home_dir, 'bin')
    for filename in os.listdir(bin_dir):
        filename = os.path.join(bin_dir, filename)
        f = open(filename, 'rb')
        lines = f.readlines()
        f.close()
        if not lines:
            logger.warn('Script %s is an empty file' % filename)
            continue
        if not lines[0].strip().startswith(shebang):
            if os.path.basename(filename) in OK_ABS_SCRIPTS:
                logger.debug('Cannot make script %s relative' % filename)
            elif lines[0].strip() == new_shebang:
                logger.info('Script %s has already been made relative' % filename)
            else:
                logger.warn('Script %s cannot be made relative (it\'s not a normal script that starts with %s)'
                            % (filename, shebang))
            continue
        logger.notify('Making script %s relative' % filename)
        lines = [new_shebang+'\n', activate+'\n'] + lines[1:]
        f = open(filename, 'wb')
        f.writelines(lines)
        f.close()

def fixup_pth_and_egg_link(home_dir):
    """Makes .pth and .egg-link files use relative paths"""
    home_dir = os.path.normcase(os.path.abspath(home_dir))
    for path in sys.path:
        if not path:
            path = '.'
        if not os.path.isdir(path):
            continue
        path = os.path.normcase(os.path.abspath(path))
        if not path.startswith(home_dir):
            logger.debug('Skipping system (non-environment) directory %s' % path)
            continue
        for filename in os.listdir(path):
            filename = os.path.join(path, filename)
            if filename.endswith('.pth'):
                if not os.access(filename, os.W_OK):
                    logger.warn('Cannot write .pth file %s, skipping' % filename)
                else:
                    fixup_pth_file(filename)
            if filename.endswith('.egg-link'):
                if not os.access(filename, os.W_OK):
                    logger.warn('Cannot write .egg-link file %s, skipping' % filename)
                else:
                    fixup_egg_link(filename)

def fixup_pth_file(filename):
    lines = []
    prev_lines = []
    f = open(filename)
    prev_lines = f.readlines()
    f.close()
    for line in prev_lines:
        line = line.strip()
        if (not line or line.startswith('#') or line.startswith('import ')
            or os.path.abspath(line) != line):
            lines.append(line)
        else:
            new_value = make_relative_path(filename, line)
            if line != new_value:
                logger.debug('Rewriting path %s as %s (in %s)' % (line, new_value, filename))
            lines.append(new_value)
    if lines == prev_lines:
        logger.info('No changes to .pth file %s' % filename)
        return
    logger.notify('Making paths in .pth file %s relative' % filename)
    f = open(filename, 'w')
    f.write('\n'.join(lines) + '\n')
    f.close()

def fixup_egg_link(filename):
    f = open(filename)
    link = f.read().strip()
    f.close()
    if os.path.abspath(link) != link:
        logger.debug('Link in %s already relative' % filename)
        return
    new_link = make_relative_path(filename, link)
    logger.notify('Rewriting link %s in %s as %s' % (link, filename, new_link))
    f = open(filename, 'w')
    f.write(new_link)
    f.close()

def make_relative_path(source, dest, dest_is_directory=True):
    """
    Make a filename relative, where the filename is dest, and it is
    being referred to from the filename source.

        >>> make_relative_path('/usr/share/something/a-file.pth',
        ...                    '/usr/share/another-place/src/Directory')
        '../another-place/src/Directory'
        >>> make_relative_path('/usr/share/something/a-file.pth',
        ...                    '/home/user/src/Directory')
        '../../../home/user/src/Directory'
        >>> make_relative_path('/usr/share/a-file.pth', '/usr/share/')
        './'
    """
    source = os.path.dirname(source)
    if not dest_is_directory:
        dest_filename = os.path.basename(dest)
        dest = os.path.dirname(dest)
    dest = os.path.normpath(os.path.abspath(dest))
    source = os.path.normpath(os.path.abspath(source))
    dest_parts = dest.strip(os.path.sep).split(os.path.sep)
    source_parts = source.strip(os.path.sep).split(os.path.sep)
    while dest_parts and source_parts and dest_parts[0] == source_parts[0]:
        dest_parts.pop(0)
        source_parts.pop(0)
    full_parts = ['..']*len(source_parts) + dest_parts
    if not dest_is_directory:
        full_parts.append(dest_filename)
    if not full_parts:
        # Special case for the current directory (otherwise it'd be '')
        return './'
    return os.path.sep.join(full_parts)
                


############################################################
## Bootstrap script creation:

def create_bootstrap_script(extra_text, python_version=''):
    """
    Creates a bootstrap script, which is like this script but with
    extend_parser, adjust_options, and after_install hooks.

    This returns a string that (written to disk of course) can be used
    as a bootstrap script with your own customizations.  The script
    will be the standard virtualenv.py script, with your extra text
    added (your extra text should be Python code).

    If you include these functions, they will be called:

    ``extend_parser(optparse_parser)``:
        You can add or remove options from the parser here.

    ``adjust_options(options, args)``:
        You can change options here, or change the args (if you accept
        different kinds of arguments, be sure you modify ``args`` so it is
        only ``[DEST_DIR]``).

    ``after_install(options, home_dir)``:

        After everything is installed, this function is called.  This
        is probably the function you are most likely to use.  An
        example would be::

            def after_install(options, home_dir):
                subprocess.call([join(home_dir, 'bin', 'easy_install'),
                                 'MyPackage'])
                subprocess.call([join(home_dir, 'bin', 'my-package-script'),
                                 'setup', home_dir])

        This example immediately installs a package, and runs a setup
        script from that package.

    If you provide something like ``python_version='2.4'`` then the
    script will start with ``#!/usr/bin/env python2.4`` instead of
    ``#!/usr/bin/env python``.  You can use this when the script must
    be run with a particular Python version.
    """
    filename = __file__
    if filename.endswith('.pyc'):
        filename = filename[:-1]
    f = open(filename, 'rb')
    content = f.read()
    f.close()
    py_exe = 'python%s' % python_version
    content = (('#!/usr/bin/env %s\n' % py_exe)
               + '## WARNING: This file is generated\n'
               + content)
    return content.replace('##EXT' 'END##', extra_text)

##EXTEND##

##file site.py
SITE_PY = zlib.decompress(base64.b64decode(b"""
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
0b2P0K0N+QJdHZ2F1u43OXpzbdKtlp/8L6y4BuM=
"""))

##file ez_setup.py
EZ_SETUP_PY = zlib.decompress(base64.b64decode(b"""
eJztG2tv28jxu37FVkZA6iLRTu7aokZ1QO7iXI2mSWA7dx8Sg16RK4lnvo5LWtb9+s7MPrh8SEma
tkCBOkBMcmdn57Xz2vXJH8p9vS3yyXQ6/aEoallXvGRxAr+TVVMLluSy5mnK6wSAJpdrti8atuN5
zeqCNVIwKeqmrIsilQCLoxUreXTPN8KTajAo93P2ayNrAIjSJhas3iZysk5SRA8vgIRnAlatRFQX
1Z7tknrLknrOeB4zHsc0ARdE2LooWbFWKxn85+eTCYOfdVVkDvUhjbMkK4uqRmrDllqC737yZwMO
K/FbA2QxzmQpomSdROxBVBKEgTS0U+f4DFBxscvTgseTLKmqopqzoiIp8ZzxtBZVzkGmBqjleE6L
RgAVF0wWbLVnsinLdJ/kmwkyzcuyKsoqwelFicogedzd9Tm4uwsmkxsUF8k3ooURo2BVA88SWYmq
pCT2tHaJynJT8djVZ4BGMdHCK6R5knv7WCeZMM/rPON1tLVDIiuRAvvOK3q1GmrqBE1GjabFZjKp
q/15q0WZoPWp4ffXF1fh9eXNxUQ8RgJIv6TvFyhiNcVCsCV7U+TCwWbIblYgwkhIqUwlFmsWKuMP
oyz2v+HVRs7UFPzBV0DmA7uBeBRRU/NVKuYz9pSGLFwF8qpyB30QgUR9wsaWS3Y2OUj0CRg6CB9U
A1qM2Rq0oAhiz4Nv/61EnrDfmqIGY8LPTSbyGkS/huVzsMUWDD4hphK2OxCTIfkewHz73GuXNGQh
QoFszrpjGo8H/2Bzw/hw2BGbN30ipx57goADOA3TH9JMf2gpINHBg15R3va1U8hAlhx2nQ9P78Jf
XlzezFlPaOwbV2cvL169eP/6Jvz54ur68u0bWG96Fvwp+G5qR95fvcav27ouz09Py32ZBEpTQVFt
TrUPlKcS/FQkTuPT1i2dTifXFzfv3928ffv6Onz395/Cyzev3iKy6fTj5B+i5jGv+eJn5WjO2bPg
bPIGPOS5szkndhTIiv4yuW6yjIPJs0f4mfytyMSihPXpffKiAboq93khMp6k6svrJBK51KAvhfIO
hBo/oA+YTMgQtbfwYS+v4PfMWLF4hKgRkXmRg1bDNFhnJTg5YM34gyC7j/EZfC2Ow8YPdrzKfe+i
RQJafCK9uZ6sAIs0DncxIAIFbkQd7WKNwe5zgoLdt4U5vjuVoDgRoZxQUJQit1xYmFDzoVnsTA6i
tJACA0S7pTaFJhaZtq7cAoBHUKwDUSWvt8GvAK8Jm+PHFAzCofXD2e1syIjC0g60AntT7NiuqO5d
iRloh0qtNAwkQxyXdpC9tObptatxKQX4TtcFeSbmwnKeRq5nrJMcXsbUobQ3M4a0ahL4IDYbowTQ
dREi5f83qf8BkyL1UTDJGShxBNEPFsKxK4RtFaH03UrqkIktfsP/V+g90WLo0wLf4L/KQeTQp5y+
sZ1KyCat7TCGCpN6uhJz7c/8QBzTaU2gf/s4FUhonfniifwmQMIgiPWCxkhkbOORoz9aek5UOXxU
PIHE8fItJQy+92PRpDHLi1qJn1iDZYMv3XsxrKbzT1+nsnObkYYrLoWRqfM5Finfa3a0kYMV2mEn
AT2AcjQH6P4cWJRmouUsj/kNgqLcBcUKbgncln82x4mzThbYzf+dZHdlqh8T5kJKQ5dk4Up2vVxb
s7rsab3H+tLJF0bFoDhYor6aakQCy2d/tG4x47Q3ZQMlyY7SRrIDvpJFijsMuZ+0SB1PASD423fl
teMyVHIR6Aa98n4Twm6hhEVS+oYSzYq4SYXEGuGjpd9r5dAHHLrQzoujjM56/Y2Hlr7lktd15XcA
YfeFsROshptsze97ZV0fQu+tNiG3EIdydTtTbeCv2UaH5dLhM9C1pz9tuf1+OX2qV5uNkNXnootP
Z4w/Fvk6TaIaa0Ex8HeuTQwlCxVoXvv+4Pv0hhwt0Ru7FbLTSfC/Xz6B9BoqU1Qtf4D8k/Luj/l0
iA8Lf6hdvRqrI70hAfNui56bugG6iIUnqGvR2QfsXSpA7qP4TKHLWVZUSCqkvLUldJ1Usp7DdgI0
o9M9QLw3joEt3jt8ecEI/Mf8Y+7/2FQVrJLuFWL2pJpNZxAlWnsRAZYcGKWV91/iNoJ4JKpqaLOq
XElq/3l3TKRSDDUFpsZ628bZox96e/0Wp2DgpLZEcX8obn2J2X+Gy2cHt8aoAdtUAlZ9U9SviiaP
v3p3fpLMMRIH0TaMKsFrEfZcT4gMJPm6sH6XAsmRwPm10YR+RkJKN5JAUfeybULZLUoRz7a6YL+l
RUSdP2rEaeEmteot5VCRqmzlTtN+x+SWspQVNsweeJp0sJvdljfZSlSwizltX+sJCBc2qCirpETN
dspA0zRFsLuOPO4YluE++IVoa1YXeazCG3YROfNOvVnA7pRM7nDFTnINPkVUwqRTtiNjVhFxoHgk
CdrpmgfqAUZFHlM3ruQYkFdijS4GG29R3fC07QkSfzWWKnVg1PAfCeym4VlBabeiOCLIv6l3oTqT
+q3klVSirze/h6hUbER08tsAq5XN71PwXVqHqnladZJAVAd7arGo/Io/CBBMv2DRcdGA6uytihCd
rE0LjzhRiYCZDv5P1tJXaGfnKLkXD0WCtlni/ostOW0+MYiytkyxe4C8s5ySTLrOVRHVFWQAr1Tu
DaBP2JXg8emuwt4lRgqsMXIwCdhH93Ns7O7QsjCsKX8B5hkVVQU+gLZUDxkwT6ZqNkGCLfZaELyx
S+uleM2BUqAXyORxL+dRUiWilezmbLpbTQdAAZHuI7J2bODstGJgrWHcQQJMYduDB/wjcQoWdeF7
BRLwkpJ5a5WbKqbEYixEmfk4PAcxgmTyuvVvv9BG5tF9U5IU1ypzEDmjueDGzO4jowITCDUOIylE
PHOlCTwMYZdm6Za3E9A9TturpUQ8UiG/6EIETtNFi+AVT/XGbGe9Q2jMdQIzAcIjbqGQhEQUqwDl
MgEZ884baW2stbqN7MZD23pMPzdVI4wu8PDGyGNUG0anfaE6wjO4BtwoDLnYGdeEX8HNeMHb1y+D
JxLLbjyGCPC/QQfoCtGp3Y1bp1C9B0WjwTkmGDqAaGtDCeFvVTwav/rSxI5r9d3OIxYekkIdlw26
9fhTctm6pj6ioJ2M5a590WZ6uDIhrKqphXUDsuWPcak1YT62Us+KB0heYLXQPfDzy5RHYlukEHw1
Hz2HnEhsMQzBump4n9+DD+ucJUIg1Mpw5h7eAmvM9UAm7pfRPs44KYcbOa2WqYuzwGStX1Oaxcno
3YEV2PG9K5Z1NyVtJdB2byilco/Z3HV7ApgMzBn0hOYsUqEOcYqmxiQEHdyO71u3YPLOfuh1xGMa
Tpr8nkb1/JlrY+Sp0DCV9wWyww6sMtNOOTKYpFy2njFnI+cgugWmJaoRjMkU9jTve9E561Izakwn
gHnHUlF7kqHh2/jQl6c1NC1vtDXfbX3Me00T3bPEs0t8dKRnMBzTh4aZuWbby3wMSNdAO25zgGVY
II7ZJfh91VQEsRpitSS88ULDu26P/mOnNPN6nIyEDL6GNMaeJ+FkzZETIBHEHlDb7pw18FZwmDUC
BuzhQxjKMvClYbH61W9PJwLT0ishv4ZMTkXOT5VsHc+k6P6SKR1/6ZIL9jSS037Kh45oygjHVGlD
/0GS2j+QjGC/6HhJx8U6kye6P5zdqvZA5+MzfXjgMEoOd+l6zQUdPy7KPWC3fgzWoFU/3xX11hh4
JSOkoVsa9QcK/Ig36Bnbj6hXlScMJrWplPVax9OpUZ9GAMdTq7LeGgEfFpQj+gAmeP2Mp8eJRtnn
RH/+FCcdMpxuQl9bn2Svk7XbuNHmdyfaG4MTj+5R7wm+jWXRB61J5bkXP/20QIGjFwbhq+cvsKZk
kM8eDVWH3OrnhibHPbbh6UBKD8Rn91Zu3U9HRTH7RErwScn913bASKRQ3RQbKgZh4gfVbTkYJ4Zn
ARoxdZTCshLr5NE3HrR12jZ4kMvVJxyQzz+0tLvU4ru+l2IAP5gHiD6xeHTC0dNn57c2taDBubm9
IvImExVX91rc2gFB1cUvlYQsFhWwqk5DFRP9rBWYABwBrFnVEnthaJZL9M0Kz8jBSV2UurtEM8s0
qX0P11l6sw+LZ7eDCVoERnzuYhpXv1etqMLKT1ExenkoBVtTl3G+V/IZv0PUIVd+IMinI1T+y5Rq
geM1qMWikaLyqBHaXjbThxnYrjp41ju2pMVwyO4HZtu3++uI06mHczhirhyN7cyDJ27HqsoTthMe
bK4ISBiJt076B8bpnPPHhVBykUJk2Bh1z3CGnQ563eHW6ebS+iYCiqGfh2C+B/A7GWAy1D0fDK7U
ORQmoKq72UnZZzYa9PGBMruKdC9GuPdc3WRXlXzjPJ2wWNRCX0DBmIanazYwoIrjPmO24b7skxeY
ob4huPdvnfpaLQ1mYQrtkVV0qUWdRuVQUJPkUJJHIrasoOCMRayu4iZrDe9e+pVOWRvruyvZvO10
mnabmw53ve8YZeNa0NhAoPM+wYBINUjHbjQNXYK6nQi0bCE5PpxAd7ITMGelR+nefNEsjTARiDzW
npduiBxgKl+oizGt8jp04MY43KEZ1ard9Yo0wDF2TDZSrjt3pw6TdCiRGCHleF6hSfQPpWVoc906
9wtSs4O52ZHOa0823XnD3qtrG7afj9uaTpIqgYk7neo4jjIXfdV2k+Kv1WePXjoRyYXTLU55k0fb
Ng9qv/RDzJUe6fCMMYFtOTZN8Ha8gqBq1NyuRihzRbd7xfaWPbXZkXJ85kh79Pa0JdG5RCdFulYN
3OU0mM5ZJvAcTi7Rcbe9f33xj45gNITq6dKZWgUsKfrxNVKn9Obem5Frez6Ijg8v9xe7HAuwrIjx
zwCUk8WmMwGUosoSKelefpH3kSSgaWp5gGBjGbA7ZMCz56x4Jx+QrgURMrj2B4RqCcAjTNYceeju
VIbCUyIiw7+xoLNXkCeRTP0bgwdbpNpUwCxWe7YRtcblz7oHkjpdiIpy775DEQC5qb4towSqrj8a
AC349kqNKwGwh1vb2zNqGQRdM4ABMF1PbJ4MK5HTAbetQTpVmx7W7cve5j8xhHXo0efDkq8FalX0
DtRayICXUP3Evl6j6y8MXUuSVoD/HQXEKxhY4p8Vfz47swDIa6C1bKYrO7cx+kpgd0YwiYJ2qbP5
TK+Bw/7K/Odz9p0jDNxOOF9UPmB4Nkc8z2djzoRFWUkwAdaiCjBoDxL6EkKkvsI8DlAp6v2xJvEA
0b3YL42tBXgDDCwVafaQAG82ZxrbEjNmKyDIhOg0FXDZzWo3KFopSR5To77wevbljHeIpKOn0erZ
6LYroMHJM2k52gJxrY413tkQsKEjrc8AjLbA2RFAneO7m3P88peyQhxPQcApVF/PRsoavDvXq5XG
biARsjBebXyws6l2FOd4zg4lqDDOPeMJ1XoPc3bgBkzr1i+P/bUSafmCy72GMq7s+HVVHRb7f9kA
xGEniA7JwpAKwDBEUsNQ/ykM0W1LfSjoZ5N/ApFpCZ4=
"""))

##file activate.sh
ACTIVATE_SH = zlib.decompress(base64.b64decode(b"""
eJytU11P2zAUffevuKQ8AFqJ+srUh6IhgcTKRFgnjSLXTW4aS6ld2U6zgvbfd50PSD+GNI08JLHv
8fW5557bg4dMWkhljrAsrIM5QmExgVK6DAKrCxMjzKUKRezkWjgM4Cw1eglzYbMz1oONLiAWSmkH
plAgHSTSYOzyDWMJtqfg5BReGNAjU3iEvoLgmN/dfuGTm/uH76Nb/m30cB3AE3wGl6GqkP7x28ND
0FcE/lpp4yrg616hLDrYO1TFU8mqb6+u3Ga6yBNI0BHnqigQKoFnm32CMpNxBplYIwj6UCjWy6UP
u0y4Sq8mFakWizwn3ZyGBd1NMtBfqo1frAQJ2xy15wA/SFtduCbspFo0abaAXgg49rwhzoRaoIWS
miQS/9qAF5yuNWhXxByTHXEvRxHp2df16md0zSdX99HN3fiAyFVpfbMlz9/aFA0OdSka7DWJgHs9
igbvtqgJtxRqSBu9Gk/eiB0RLyIyhEBplaB1pvBGwx1uPYgwT6EFHO3c3veh1qHt1b8ZmbqOS2Mw
p+4rB2thpJjnaLue3r6bsQ7VYcB5Z8l5wBoRuvWwPYuSjLW9m0UHHXJ+eTPm49HXK84vGljX/WxX
TZ/Mt6GSLJiRuVGJJcJ0K+80mFVKEsdd9by1pMjJ2xa9W2FEO4rst5BxM+baSBKlgSNC5tzqIgzL
sjx/RkdmXZ+ToUOrU1cKg6HwGUL26prHDq0ZpTxIcDqbPUFdC+YW306fvFPUaX2AWtqxH/ugsf+A
kf/Pcf/3UW/HnBT5Axjqy2Y=
"""))

##file activate.bat
ACTIVATE_BAT = zlib.decompress(base64.b64decode(b"""
eJx9kMsOgjAQRfdN+g+zoAn8goZEDESJPBpEViSzkFbZ0IX8f+RRaVW0u5mee3PanbjeFSgpKXmI
Hqq4KC9BglFW+YjWhEgJJa2ETvXQCNl2ogFe5CkvwaUEhjPm543vcOdAiacjLxzzJFw6f2bZCsZ0
2YitXPtswawi1zwgC9II0QPD/RELyuOb1jB/Sg0rNhM31Ss4n2I+7ibLb8epQGco2Rja1Fs/zeoa
cR9nWnprJaMspOQJdBR1/g==
"""))

##file deactivate.bat
DEACTIVATE_BAT = zlib.decompress(base64.b64decode(b"""
eJxzSE3OyFfIT0vj4spMU0hJTcvMS01RiPf3cYkP8wwKCXX0iQ8I8vcNCFHQ4FIAguLUEgWIgK0q
FlWqXJpcICVYpGzx2OAY4oFsPpCLbjpQCLvZILVcXFaufi5cACHzOrI=
"""))

##file distutils-init.py
DISTUTILS_INIT = zlib.decompress(base64.b64decode(b"""
eJytVk2L5DYQvetXFN0E28msCcltoVkIe1lYcgiBHIbBaGy5Wxm3ZCT1dHd+faokty35Y5PDGmZw
q0pVr56qnizPvTYOtGUyvNn7+HrlRkl1tPBYqLVq5bHnxgoD+/SntKC0Aw7v0rgL74R6h7NuLp14
AqvhKqDmCi5WgHTgNLRSNeBOAqxrOvnKWCON4mcBBwRT9tydymGFTNZdnOxsReuRx99aqnzmnsew
yqpqZSeqqniCbAyTFUy2YxClzZle8jRNAYcFlHyxZ4xffGSAz4Ozkl5yv0TP7k+sNGJmTAU9r9/4
UQB38IMF3vcCgRNBr8iUCgwRLZ2uuZNaAbdh8W6dOE+BPu0KJjorAozKl1BVpVTIgst/foJZdd5N
3ESd615MJHpGU1dkrqqkkg7D9fesKEojeJMXBWOt0REEGNqEFjZMiDocD2Nsv8fiXX2C14vsmkrc
HEyZodHCqszBm9JXOOEfUnIUzteO/YIO0ojaaXMfAp0AybliV+mrhQ/UZSdumlo3IhBGLkiw0Zeh
8Xxy0RCmsjeilTesCPvC/+64a/GMqQcyDPrrL1kgNi2rrPX5zFVTTiUMhU4LeF4aX8cFH6buuLWT
U554DK1ETyNamhTeyX9EpXtqAAu5FV0bOdFDuHG1RGoMN/cK2bE0k79rJVJPepauB3h+SdzYN/2j
vko6h7jD7uiqQOgT7L7iWe2KIgmXVFvO6wvlLcGsU79K+PijChIUAsxXo1M7TEbfmFMaehtaxX5k
jKCTdFWhjf30E3vkVn7Gf0a+XqiMcuHFhsNMV+PDbH1vHmA1SURLmP1qGpaZIi7mN2KtPWYhyD6S
QHFDB5vP4w6w9iO26NgXvuOB7eGvE/caX/OuC6MmzIcL3RKhIKCC2NC2iCHoPk5ar628ZVO/0h5f
/XAz7FCAklp2QcZG3VvdtLpn7rVo40cHJ45FhNq7S0umPHWasKCGoBKhTqOUdwgi9zQuZ5d8SqEa
e5V4qWQzxFmxHOFwHkac9bvIaXvBUhNdJarJV+Ab4S5GBTf2PxoX2Vk2czolo67PRgUVu+rv7qQV
3iA1Bhody9Tkh2M0zvblJMeV7UUtW1kfsPvC4RxI3QZukMSwuFS9Yd0nj9UpJmMJNk36SFmwLZD4
qdHouqqG+V03sq36Y2pmexdMohBvMUlfUptMonHJpHUoonhRknWT2dgJSHS/I9ULVCmm/yAePbaJ
j4zrxM+YnO2diB/M79zflGmoyLZCfWTNf+Tm+NBUz80QbyXL4Dvy/61PEnoQLd3LazqWXsedv47H
fSQ9FkUdCa9FPoKir8XaFf6os69ffvv85Y/Mf96jjI1OqSaNy8+PDS+I5oFrj7fyG35rkR7ipTDu
FN0mApLLGQLMTrRsJMZ00/tP8DzkfkmSU9S4GccdbPPcVvprxco2u2LRYXHH/Avon569
"""))

##file distutils.cfg
DISTUTILS_CFG = zlib.decompress(base64.b64decode(b"""
eJxNj00KwkAMhfc9xYNuxe4Ft57AjYiUtDO1wXSmNJnK3N5pdSEEAu8nH6lxHVlRhtDHMPATA4uH
xJ4EFmGbvfJiicSHFRzUSISMY6hq3GLCRLnIvSTnEefN0FIjw5tF0Hkk9Q5dRunBsVoyFi24aaLg
9FDOlL0FPGluf4QjcInLlxd6f6rqkgPu/5nHLg0cXCscXoozRrP51DRT3j9QNl99AP53T2Q=
"""))

##file activate_this.py
ACTIVATE_THIS = zlib.decompress(base64.b64decode(b"""
eJx1UsGOnDAMvecrIlYriDRlKvU20h5aaY+teuilGo1QALO4CwlKAjP8fe1QGGalRoLEefbzs+Mk
Sb7NcvRo3iTcoGqwgyy06As+HWSNVciKaBTFywYoJWc7yit2ndBVwEkHkIzKCV0YdQdmkvShs6YH
E3IhfjFaaSNLoHxQy2sLJrL0ow98JQmEG/rAYn7OobVGogngBgf0P0hjgwgt7HOUaI5DdBVJkggR
3HwSktaqWcCtgiHIH7qHV+esW2CnkRJ+9R5cQGsikkWEV/J7leVGs9TV4TvcO5QOOrTHYI+xeCjY
JR/m9GPDHv2oSZunUokS2A/WBelnvx6tF6LUJO2FjjlH5zU6Q+Kz/9m69LxvSZVSwiOlGnT1rt/A
77j+WDQZ8x9k2mFJetOle88+lc8sJJ/AeerI+fTlQigTfVqJUiXoKaaC3AqmI+KOnivjMLbvBVFU
1JDruuadNGcPmkgiBTnQXUGUDd6IK9JEQ9yPdM96xZP8bieeMRqTuqbxIbbey2DjVUNzRs1rosFS
TsLAdS/0fBGNdTGKhuqD7mUmsFlgGjN2eSj1tM3GnjfXwwCmzjhMbR4rLZXXk+Z/6Hp7Pn2+kJ49
jfgLHgI4Jg==
"""))

if __name__ == '__main__':
    main()

## TODO:
## Copy python.exe.manifest
## Monkeypatch distutils.sysconfig
