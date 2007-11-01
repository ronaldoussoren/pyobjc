from Foundation import *
from AppKit import *

class FileSettings(NSObject):
    fsdefault_py = None
    fsdefault_pyw = None
    fsdefault_pyc = None
    default_py = None
    default_pyw = None
    default_pyc = None
    factorySettings = None
    prefskey = None
    settings = None

    def getFactorySettingsForFileType_(cls, filetype):
        if filetype == u'Python Script':
            curdefault = cls.fsdefault_py
        elif filetype == u'Python GUI Script':
            curdefault = cls.fsdefault_pyw
        elif filetype == u'Python Bytecode Document':
            curdefault = cls.fsdefault_pyc
        else:
            NSLog(u'Funny File Type: %s\n' % (filetype,))
            curdefault = cls.fsdefault_py
            filetype = u'Python Script'
        if curdefault is None:
            curdefault = FileSettings.alloc().initForFSDefaultFileType_(filetype)
        return curdefault
    getFactorySettingsForFileType_ = classmethod(getFactorySettingsForFileType_)

    def getDefaultsForFileType_(cls, filetype):
        if filetype == u'Python Script':
            curdefault = cls.default_py
        elif filetype == u'Python GUI Script':
            curdefault = cls.default_pyw
        elif filetype == u'Python Bytecode Document':
            curdefault = cls.default_pyc
        else:
            NSLog(u'Funny File Type: %s\n' % (filetype,))
            curdefault = cls.default_py
            filetype = u'Python Script'
        if curdefault is None:
            curdefault = FileSettings.alloc().initForDefaultFileType_(filetype)
        return curdefault
    getDefaultsForFileType_ = classmethod(getDefaultsForFileType_)

    def newSettingsForFileType_(cls, filetype):
        return FileSettings.alloc().initForFileType_(filetype)
    newSettingsForFileType_ = classmethod(newSettingsForFileType_)

    def initWithFileSettings_(self, source):
        self = super(FileSettings, self).init()
        self.settings = source.fileSettingsAsDict().copy()
        self.origsource = None
        return self

    def initForFileType_(self, filetype):
        defaults = FileSettings.getDefaultsForFileType_(filetype)
        self = self.initWithFileSettings_(defaults)
        self.origsource = defaults
        return self

    def initForFSDefaultFileType_(self, filetype):
        self = super(FileSettings, self).init()
        if type(self).factorySettings is None:
            bndl = NSBundle.mainBundle()
            path = bndl.pathForResource_ofType_(u'factorySettings', u'plist')
            type(self).factorySettings = NSDictionary.dictionaryWithContentsOfFile_(path)
            if type(self).factorySettings is None:
                NSLog(u'Missing %s' % (path,))
                return None
        dct = type(self).factorySettings.get(filetype)
        if dct is None:
            NSLog(u'factorySettings.plist misses file type "%s"' % (filetype,))
            return None

        self.applyValuesFromDict_(dct)
        interpreters = dct[u'interpreter_list']
        mgr = NSFileManager.defaultManager()
        self.settings['interpreter'] = u'no default found'
        for filename in interpreters:
            filename = filename.nsstring().stringByExpandingTildeInPath()
            if mgr.fileExistsAtPath_(filename):
                self.settings['interpreter'] = filename
                break
        self.origsource = None
        return self

    def applyUserDefaults_(self, filetype):
        dct = NSUserDefaults.standardUserDefaults().dictionaryForKey_(filetype)
        if dct:
            self.applyValuesFromDict_(dct)

    def initForDefaultFileType_(self, filetype):
        fsdefaults = FileSettings.getFactorySettingsForFileType_(filetype)
        self = self.initWithFileSettings_(fsdefaults)
        if self is None:
            return self
        self.settings['interpreter_list'] = fsdefaults.settings['interpreter_list']
        self.settings['scriptargs'] = u''
        self.applyUserDefaults_(filetype)
        self.prefskey = filetype
        return self

    def reset(self):
        if self.origsource:
            self.updateFromSource_(self.origsource)
        else:
            fsdefaults = FileSettings.getFactorySettingsForFileType_(self.prefskey)
            self.updateFromSource_(fsdefaults)

    def updateFromSource_(self, source):
        self.settings.update(source.fileSettingsAsDict())
        if self.origsource is None:
            NSUserDefaults.standardUserDefaults().setObject_forKey_(self.fileSettingsAsDict(), self.prefskey)

    def applyValuesFromDict_(self, dct):
        if self.settings is None:
            self.settings = {}
        self.settings.update(dct)

    def commandLineForScript_(self, script):
        cur_interp = None
        if self.settings['honourhashbang']:
            try:
                line = file(script, 'rU').next().rstrip()
            except:
                pass
            else:
                if line.startswith('#!'):
                    cur_interp = line[2:]
        if cur_interp is None:
            cur_interp = self.settings['interpreter']
        cmd = []
        cmd.append('"'+cur_interp.replace('"', '\\"')+'"')
        if self.settings['debug']:
            cmd.append('-d')
        if self.settings['verbose']:
            cmd.append('-v')
        if self.settings['inspect']:
            cmd.append('-i')
        if self.settings['optimize']:
            cmd.append('-O')
        if self.settings['nosite']:
            cmd.append('-S')
        if self.settings['tabs']:
            cmd.append('-t')
        others = self.settings['others']
        if others:
            cmd.append(others)
        cmd.append('"'+script.replace('"', '\\"')+'"')
        cmd.append(self.settings['scriptargs'])
        if self.settings['with_terminal']:
            cmd.append("""&& echo "Exit status: $?" && python -c 'import sys;sys.stdin.readline()' && exit 1""")
        else:
            cmd.append('&')
        return ' '.join(cmd)

    def fileSettingsAsDict(self):
        return self.settings
