import sys
import os
import shutil
from pyobjc_setup_utils import runtasks
import setuptools
build_ext = setuptools.Distribution().get_command_class('build_ext')

class pyobjc_build_ext (build_ext):
    # Custom build_ext implementation. This differs in two ways from the
    # standard one:
    # 1. We first run the CodeGenerator script
    # 2. We calculate a class-list after building the extensions, and if that
    #    is different from what we had before (e.g. clean install or serious
    #    OS upgrade) we rebuild the extensions.

    def create_empty_class_list(self):
        for fw in ('Fnd', 'App'):
            fd = open('build/codegen/_%s_Classes.inc'%(fw,), 'w')
            fd.write('static const char* gClassNames[] = {\n')
            fd.write('\tNULL\n')
            fd.write('};\n')
            fd.close()

    def create_cached_class_list(self):
        sys.path.insert(0, self.build_lib)
        import objc
        retval = 0

        for pfx, name in (('Fnd', 'Foundation'), ('App', 'AppKit')):
            try:
                m = __import__(name)
            except ImportError:
                continue
            fd = open('build/codegen/_%s_Classes.inc~'%(pfx,), 'w')
            fd.write('static const char* gClassNames[] = {\n')
            for o in m.__dict__.values():
                if not isinstance(o, objc.objc_class):
                    continue
                fd.write('\t"%s",\n'%(o.__name__))
            fd.write('\tNULL\n')
            fd.write('};\n')
            fd.close()

            d1 = open('build/codegen/_%s_Classes.inc~'%(pfx,), 'r').read()
            d2 = open('build/codegen/_%s_Classes.inc'%(pfx,), 'r').read()

            if d1 != d2:
                os.rename(
                        'build/codegen/_%s_Classes.inc~'%(pfx,),
                        'build/codegen/_%s_Classes.inc'%(pfx,)
                    )
                retval = 1


        return retval



    def run(self):
        # Save self.compiler, we need to reset it when we have to rebuild
        # the extensions.
        compiler_saved = self.compiler

        runtasks("Generating wrappers & stubs",
            [sys.executable, "Scripts/CodeGenerators/cocoa_generator.py"])

        if not os.path.exists('build/codegen/_Fnd_Classes.inc'):
            # Create a dummy classname list, to enable bootstrapping. Don't
            # do this if there already is a list, everything is better than
            # an empty list.
            self.create_empty_class_list()

        build_ext.run(self)
        return

        if self.create_cached_class_list():
            # Note: dependencies don't work here, we depend on a file that
            # probably didn't exist when the glob was done...
            print "** Created a fresh class-cache, rebuilding the extensions"
            if os.path.exists(
                        os.path.join(self.build_temp, 'Modules', 'AppKit')):
                shutil.rmtree(
                        os.path.join(self.build_temp, 'Modules', 'AppKit'))
                os.mkdir(
                        os.path.join(self.build_temp, 'Modules', 'AppKit'))

            if os.path.exists(
                        os.path.join(self.build_temp, 'Modules', 'Foundation')):
                shutil.rmtree(
                        os.path.join(self.build_temp, 'Modules', 'Foundation'))
                os.mkdir(
                        os.path.join(self.build_temp, 'Modules', 'Foundation'))

            try:
                os.unlink(os.path.join(self.build_lib, 'AppKit', '_AppKit.so'))
            except os.error:
                pass

            try:
                os.unlink(os.path.join(self.build_lib, 'Foundation', '_Foundation.so'))
            except os.error:
                pass

            self.compiler = compiler_saved

            build_ext.run(self)

    def build_extension(self, ext):
        build_ext.build_extension(self, ext)


cmdclass = dict(build_ext=pyobjc_build_ext)
