import os
import glob

def xcodeFromEnvironment(project, env):
    from PyObjCTools.XcodeSupport import ArchiveGraph
    from PyObjCTools.XcodeSupport import Xcode
    path = os.path.join(project, 'project.pbxproj')
    if not os.path.exists(path):
        path = glob.glob('*.xcode/project.pbxproj')[0]
    return Xcode.Xcode(project, ArchiveGraph.ArchiveGraph.fromPath(path), env)
