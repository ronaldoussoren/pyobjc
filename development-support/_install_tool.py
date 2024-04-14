"""
The implementation for the install.py and develop.py
scripts in the root of the repository.
"""

import os
import plistlib
import shlex
import shutil
import subprocess
import sys
from sysconfig import get_config_var

TOPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if os.isatty(sys.stdout.fileno()):
    RED = "\033[31m"
    BOLD = "\033[1m"
    RESET = "\033[39m\033[m"
else:
    RED = ""
    BOLD = ""
    RESET = ""


# Module defining a topological sort function, see
# <http://www.bitformation.com/art/python_toposort.html> for more
# information.
#
# Original topological sort code written by Ofer Faigon
# (www.bitformation.com) and used with permission


def topological_sort(items, partial_order):
    """
    Perform topological sort.
    items is a list of items to be sorted.
    partial_order is a list of pairs. If pair (a,b) is in it, it means
    that item a should appear before item b.
    Returns a list of the items in one of the possible orders, or None
    if partial_order contains a loop.
    """

    def add_node(graph, node):
        """Add a node to the graph if not already exists."""
        if node not in graph:
            graph[node] = [0]  # 0 = number of arcs coming into this node.

    def add_arc(graph, fromnode, tonode):
        """Add an arc to a graph. Can create multiple arcs.
        The end nodes must already exist."""
        graph[fromnode].append(tonode)
        # Update the count of incoming arcs in tonode.
        graph[tonode][0] += 1

    # step 1 - create a directed graph with an arc a->b for each input
    # pair (a,b).
    # The graph is represented by a dictionary. The dictionary contains
    # a pair item:list for each node in the graph. /item/ is the value
    # of the node. /list/'s 1st item is the count of incoming arcs, and
    # the rest are the destinations of the outgoing arcs. For example:
    #           {'a':[0,'b','c'], 'b':[1], 'c':[1]}
    # represents the graph:   c <-- a --> b
    # The graph may contain loops and multiple arcs.
    # Note that our representation does not contain reference loops to
    # cause GC problems even when the represented graph contains loops,
    # because we keep the node names rather than references to the nodes.
    graph = {}
    for v in items:
        add_node(graph, v)
    for a, b in partial_order:
        add_arc(graph, a, b)

    # Step 2 - find all roots (nodes with zero incoming arcs).
    roots = [node for (node, nodeinfo) in graph.items() if nodeinfo[0] == 0]

    # step 3 - repeatedly emit a root and remove it from the graph. Removing
    # a node may convert some of the node's direct children into roots.
    # Whenever that happens, we append the new roots to the list of
    # current roots.
    sorted_items = []
    while len(roots) != 0:
        # If len(roots) is always 1 when we get here, it means that
        # the input describes a complete ordering and there is only
        # one possible output.
        # When len(roots) > 1, we can choose any root to send to the
        # output; this freedom represents the multiple complete orderings
        # that satisfy the input restrictions. We arbitrarily take one of
        # the roots using pop(). Note that for the algorithm to be efficient,
        # this operation must be done in O(1) time.
        root = roots.pop()
        sorted_items.append(root)
        for child in graph[root][1:]:
            graph[child][0] = graph[child][0] - 1
            if graph[child][0] == 0:
                roots.append(child)
        del graph[root]
    if len(graph.items()) != 0:
        # There is a loop in the input.
        return None
    return sorted_items


def get_os_level():
    with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
        pl = plistlib.load(fp)
    v = pl["ProductVersion"]
    return ".".join(v.split(".")[:2])


def get_sdk_level():
    cflags = get_config_var("CFLAGS")
    cflags = shlex.split(cflags)
    for i, val in enumerate(cflags):
        if val == "-isysroot":
            sdk = cflags[i + 1]
            break
    else:
        return None

    if sdk == "/":
        return get_os_level()

    sdkname = os.path.basename(sdk)
    assert sdkname.startswith("MacOSX")
    assert sdkname.endswith(".sdk")

    settings_path = os.path.join(sdk, "SDKSettings.plist")
    if os.path.exists(settings_path):
        try:
            with open(os.path.join(sdk, "SDKSettings.plist"), "rb") as fp:
                pl = plistlib.load(fp)
            return pl["Version"]
        except Exception:
            raise
            raise SystemExit("Cannot determine SDK version")
    else:
        version_part = sdkname[6:-4]
        assert version_part != ""
        return version_part


def sorted_framework_wrappers():
    frameworks = []
    partial_order = []
    cur_platform = get_sdk_level() or get_os_level()
    for subdir in os.listdir(TOPDIR):
        if not subdir.startswith("pyobjc-framework-"):
            continue

        setup = os.path.join(TOPDIR, subdir, "setup.py")
        in_requires = False
        requires = []
        min_platform = "10.0"
        max_platform = "99.9"

        with open(setup) as fp:
            for ln in fp:
                if not in_requires:
                    if ln.strip().startswith("install_requires"):
                        in_requires = True

                        if "]" in ln:
                            # Dependencies on a single line
                            start = ln.find("[")
                            deps = ln[start + 1 :].strip().split(",")
                            for d in deps:
                                d = d.strip()[1:]
                                if d.startswith("pyobjc-framework-"):
                                    d = d.split(">")[0]
                                    requires.append(d)
                else:
                    if ln.strip().startswith("]"):
                        in_requires = False
                        continue

                    dep = ln.strip()[1:-1]
                    if dep.startswith("pyobjc-framework"):
                        dep = dep.split(">")[0]
                        requires.append(dep)

                if ln.strip().startswith("min_os_level"):
                    min_platform = ln.strip().split("=")[-1]
                    if min_platform.endswith(","):
                        min_platform = min_platform[:-1]
                    min_platform = min_platform[1:-1]

                if ln.strip().startswith("max_os_level"):
                    max_platform = ln.strip().split("=")[-1]
                    if max_platform.endswith(","):
                        max_platform = max_platform[:-1]
                    max_platform = max_platform[1:-1]

        if not (
            version_key(min_platform)
            <= version_key(cur_platform)
            <= version_key(max_platform)
        ):
            print(
                "Skipping {!r} because it is not supported on the current platform".format(
                    subdir
                )
            )
            continue
        frameworks.append(subdir)
        for dep in requires:
            partial_order.append((dep, subdir))

    frameworks = topological_sort(frameworks, partial_order)
    return frameworks


def build_project(project, extra_arg):
    proj_dir = os.path.join(TOPDIR, project)

    # First ask distutils to clean up
    print(f"Cleaning {project!r} using {sys.executable!r}")
    status = subprocess.call([sys.executable, "setup.py", "clean"], cwd=proj_dir)
    if status != 0:
        print(f"{RED}Cleaning of {project!r} failed, status {status}{RESET}")
        return False

    # Explicitly remove the 'build' directory, just in case...
    if os.path.exists(os.path.join(proj_dir, "build")):
        shutil.rmtree(os.path.join(proj_dir, "build"))

    print(f"Installing {project!r} using {sys.executable!r}, {extra_arg}")
    status = subprocess.call(
        [
            sys.executable,
            "-mpip",
            "install",
            "--no-cache-dir",
        ]
        + ([extra_arg, "."] if extra_arg is not None else ["."]),
        cwd=proj_dir,
    )

    if status != 0:
        print(f"{RED}Installing {project!r} failed (status {status}){RESET}")
        return False

    return True


def version_key(version):
    return tuple(int(x) for x in version.split("."))


def main(extra_arg=None):
    if sys.platform != "darwin":
        print("{RED}PyObjC requires macOS{RESET}")
        sys.exit(1)

    subprocess.check_call(
        [sys.executable, "-mpip", "install", "-U", "setuptools", "pip", "wheel"]
    )

    all_projects = ["pyobjc-core"] + sorted_framework_wrappers()
    for idx, project in enumerate(all_projects):
        print()
        print(f"{BOLD}{idx+1}/{len(all_projects)}: Building project {project!r}{RESET}")
        print()
        if not build_project(project, extra_arg):
            print("{RED}Cannot build one of the projects, bailing out{RESET}")
            sys.exit(1)
