import os
from altgraph.compat import *

class Xcode(object):
    def __init__(self, project, archive, env):
        self.project = project
        self.archive = archive
        self.env = dict(
            BUILT_PRODUCTS_DIR='build',
            TARGET_TEMP_DIR=os.path.join('build', project + '.py2app.build'),
        )
        self.env.update(env)

    def py2app_argv(self, argv):
        action = self.env.get('ACTION', '').strip()
        if not action:
            return argv
        if action == 'build':
            action = 'py2app'
        rval = [argv[0], action]
        return rval

    def findGroup(self, groupName):
        for group in self.archive.root.mainGroup.children:
            if group.name == groupName:
                return group
        raise ValueError("%r group not found" % (groupName,))
    
    def findMainScript(self):
        name = u'Main Script'
        group = self.findGroup(name)
        if len(group.children) != 1:
            raise ValueError("Expecting exactly 1 item in %r group, found %d" % (name, len(group.children),))
        return unicode(group.children[0].path).encode('utf8')

    def iterNIBFiles(self):
        name = u'Resources'
        group = self.findGroup(name)
        for ref in group.children:
            if ref.isa == u'PBXFileReference':
                name, ext = os.path.splitext(ref.path)
            elif ref.isa == u'PBXVariantGroup':
                name, ext = os.path.splitext(ref.name)
            else:
                continue
            if ext == u'.nib':
                yield unicode(os.path.basename(name)).encode('utf8')

    def iterModules(self):
        name = u'Classes'
        group = self.findGroup(name)
        for ref in group.children:
            if ref.isa != u'PBXFileReference':
                raise ValueError('Only file references are allowed in Classes')
            yield os.path.splitext(unicode(ref.path).encode('utf8'))[0]

    def getPlist(self, nibFiles, modules):
        try:
            import plistlib
            plist = plistlib.Plist.fromFile('Info.plist')
        except IOError:
            plist = {}

        plist.update(dict(
            PyObjCXcode=dict(
                NIBFiles=nibFiles,
                Modules=modules,
            ),
        ))

        return plist
    
    def getTarget(self, nibFiles, modules):
        return dict(
            script=self.findMainScript(),
            plist=self.getPlist(nibFiles, modules),
        )

    def iterResources(self):
        name = u'Resources'
        group = self.findGroup(name)
        refs = iter(group.children)
        while True:
            for ref in refs:
                children = getattr(ref, 'children', None)
                if children is not None:
                    refs = chain(ref.children, refs)
                    break
                path = ref.path
                sourceTree = self.env.get(getattr(ref, 'sourceTree', None))
                dirname = unicode(os.path.dirname(path))
                if sourceTree:
                    path = os.path.join(unicode(sourceTree, 'utf-8'), path)
                yield dirname, [unicode(path).encode('utf8')]
            else:
                break

    def py2app_setup_options(self, buildstyle):
        nibFiles = list(self.iterNIBFiles())
        modules = list(self.iterModules())
        py2app = dict(includes=modules)
        resources = list(self.iterResources())
        if self.env.get('BUILD_STYLE') == 'Development':
            py2app['alias'] = True
        py2app['dist_dir'] = self.env['BUILT_PRODUCTS_DIR']
        py2app['bdist_base'] = self.env['TARGET_TEMP_DIR']
        rval = dict(
            data_files=resources,
            options=dict(py2app=py2app),
        )
        rval[buildstyle] = [self.getTarget(nibFiles, modules)]

        return rval
