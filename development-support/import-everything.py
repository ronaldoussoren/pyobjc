from _common_definitions import (
    TOP_DIR,
    sort_framework_wrappers,
)
import importlib
import os
import ast
import functools
import platform
import traceback
import sys

# Reconfigure stdout/stderr to be line buffered,
# that # makes it easier to redirect output to a
# file, # including stderr.
try:
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
except AttributeError:
    pass


@functools.total_ordering
class MacVersion:
    def __init__(self, version_string):
        self.version_string = version_string
        self.version_tuple = tuple(int(x) for x in version_string.split("."))

    def __eq__(self, other):
        if not isinstance(other, MacVersion):
            return False

        return self.version_tuple == other.version_tuple

    def __lt__(self, other):
        if not isinstance(other, MacVersion):
            raise TypeError

        return self.version_tuple < other.version_tuple

    def __str__(self):
        return f"<MacVersion {self.version_tuple}>"


sys_version = MacVersion(platform.mac_ver()[0])


def flatten_list(list_value, setup_ast):
    if isinstance(list_value, ast.List):
        return [node.value for node in list_value.elts]

    elif isinstance(list_value, ast.BinOp):
        assert isinstance(list_value.left, ast.List)
        assert isinstance(list_value.right, ast.Name)
        assert list_value.right.id == "subpackages"

        # In pyobjc the right is always "subpackages" and
        # "from main import *" will also import all symbols
        # in the subpackage.
        return [node.value for node in list_value.left.elts]

    else:
        raise RuntimeError("Don't know how to handle {ast.dump(list_value)}")


def get_info(project):
    setup_py = os.path.join(TOP_DIR, project, "setup.py")

    with open(setup_py) as stream:
        contents = stream.read()

    setup_ast = compile(contents, setup_py, "exec", ast.PyCF_ONLY_AST)
    for node in ast.iter_child_nodes(setup_ast):  # noqa: B007
        pass

    assert isinstance(node, ast.Expr)
    assert isinstance(node.value, ast.Call)
    assert node.value.func.id == "setup"

    min_os_level = None
    max_os_level = None
    packages = []
    modules = []

    for keyword in node.value.keywords:
        if keyword.arg == "min_os_level":
            min_os_level = keyword.value.value
        elif keyword.arg == "max_os_level":
            max_os_level = keyword.value.value
        elif keyword.arg == "packages":
            packages = flatten_list(keyword.value, setup_ast)

        elif keyword.arg == "modules":
            modules = flatten_list(keyword.value, setup_ast)

    return min_os_level, max_os_level, packages + modules


def main():
    for project in sort_framework_wrappers():
        print(f"Checking '{project}'")
        min_os_level, max_os_level, to_import = get_info(project)

        if min_os_level is not None:
            if MacVersion(min_os_level) > sys_version:
                print(f"  skipped {min_os_level} is too new")
                continue

        if max_os_level is not None:
            if MacVersion(max_os_level) < sys_version:
                print(f"  skipped {max_os_level} is too old")
                continue

        for name in to_import:
            if name == "PyObjCTools":
                # Namespace package, requires special code
                continue

            print(f"  scan {name}")
            # First import the module
            try:
                mod = importlib.import_module(name)
            except Exception:
                traceback.print_exc()
                continue

            # Then resolve all symbols, because
            # framework bindings use a lazy importer
            try:
                mod.__all__
            except Exception:
                traceback.print_exc()

        print()

    import PyObjCTools

    print("Checking namespace package PyObjCTools")
    for dname in PyObjCTools.__path__:
        for nm in os.listdir(dname):
            if nm.endswith(".py"):
                modname = f"PyObjCTools.{nm[:-3]}"
                print(f"  scan {modname}")
                try:
                    mod = importlib.import_module(modname)
                except Exception:
                    traceback.print_exc()
                    continue


if __name__ == "__main__":
    main()
