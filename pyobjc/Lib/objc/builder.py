"""
Utility module that helps with building a module.

Usage:
    import objc.builder

    objc.builder.build_applet('myapp', 'main.py', ['mod1.py' ... ],
        [ 'English.lproj', ...])

TODO: 
* the same module should contain function for replacing/enhancing the 
  Info.plist in the generated application.
* Add compiled version of the extra sources, instead of the sources themselves
* Add interface to use the python-starter trick as used by the Interface Builder
  project.
"""

import buildtools
import shutil
import os

try:
    getattr(__builtins__, 'True')
except AttributeError:
    True=1
    False=0

def build_applet(app_name,
        main_py, 
        extra_src = [], 
        extra_files = [], 
        raw=False, 
        resource_file=None,
        info_plist=None):
    """
    Build an applet. 
    """

    def dirname(path):
        r = os.path.split(path)[0]
        if not r:
            return '.'
        else:
            return r

    # Basic argument checks
    assert isinstance(app_name, str)
    assert os.path.exists(dirname(app_name))
    assert isinstance(main_py, str)
    assert os.path.exists(main_py)
    assert isinstance(extra_src, (list, tuple))
    assert reduce(lambda x, y: x and y, 
        [ os.path.exists(x) for x in extra_src ], True)
    assert isinstance(extra_files, list) or isinstance(extra_files, tuple)
    assert reduce(lambda x, y: x and y, 
        [ os.path.exists(x) for x in extra_files ], True)
    assert isinstance(raw, int)
    assert (resource_file is None) or (
        isinstance(resource_file, str) and 
        os.path.exists(resource_file))
    
    assert (info_plist is None) or isinstance(info_plist, str)

    template  = buildtools.findtemplate()
    
    others = extra_src[:]
    others.extend(extra_files)

    # remove the output if it already exists
    if os.path.exists(app_name + '.app'):
        shutil.rmtree(app_name + '.app')

    buildtools.process(template, main_py, app_name, 1,
        rsrcname = resource_file, others = others,
        raw = raw, progress = None)

    if info_plist:
        shutil.copyfile(info_plist,
            os.path.join(app_name + '.app', 
                'Contents', 'Info.plist'))
