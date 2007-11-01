import os
import glob

def xcodeFromEnvironment(project, env):
    from PyObjCTools.XcodeSupport import ArchiveGraph
    from PyObjCTools.XcodeSupport import Xcode
    from PyObjCTools.XcodeSupport import XcodeProj
    path = os.path.join(project, 'project.pbxproj')
    if not os.path.exists(path):
        path = ArchiveGraph.xcodeFiles('.')[0]
    projType = os.path.splitext(os.path.dirname(path))[1]
    if projType == '.xcodeproj':
        mod = XcodeProj
    elif projType == '.xcode':
        mod = Xcode
    return mod.Xcode(project, ArchiveGraph.ArchiveGraph.fromPath(path), env)

def main():
    import sys
    return xcodeFromEnvironment(sys.argv[1], dict(os.environ))

if __name__ == '__main__':
    main()
