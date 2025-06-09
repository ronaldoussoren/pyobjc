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
import typing
from sysconfig import get_config_var
from _common_definitions import RED, BOLD, RESET, sort_framework_wrappers

TOPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Module defining a topological sort function, see
# <http://www.bitformation.com/art/python_toposort.html> for more
# information.
#
# Original topological sort code written by Ofer Faigon
# (www.bitformation.com) and used with permission


def topological_sort(
    items: typing.Sequence[str], partial_order: typing.Sequence[tuple[str, str]]
) -> list[str] | None:
    """
    Perform topological sort.
    items is a list of items to be sorted.
    partial_order is a list of pairs. If pair (a,b) is in it, it means
    that item a should appear before item b.
    Returns a list of the items in one of the possible orders, or None
    if partial_order contains a loop.
    """

    class GraphNode:
        numincoming: int
        outgoing: list[str]

        def __init__(self):
            self.numincoming = 0
            self.outgoing = []

    def add_node(graph: dict[str, GraphNode], node: str) -> None:
        """Add a node to the graph if not already exists."""
        if node not in graph:
            graph[node] = GraphNode()  # 0 = number of arcs coming into this node.

    def add_arc(graph: dict[str, GraphNode], fromnode: str, tonode: str) -> None:
        """Add an arc to a graph. Can create multiple arcs.
        The end nodes must already exist."""
        graph[fromnode].outgoing.append(tonode)
        # Update the count of incoming arcs in tonode.
        graph[tonode].numincoming += 1

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
    graph: dict[str, GraphNode] = {}
    for v in items:
        add_node(graph, v)
    for a, b in partial_order:
        add_arc(graph, a, b)

    # Step 2 - find all roots (nodes with zero incoming arcs).
    roots = [node for (node, nodeinfo) in graph.items() if nodeinfo.numincoming == 0]

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
        for child in graph[root].outgoing:
            graph[child].numincoming -= 1
            if graph[child].numincoming == 0:
                roots.append(child)
        del graph[root]
    if len(graph.items()) != 0:
        # There is a loop in the input.
        return None
    return sorted_items


def get_os_level() -> str:
    with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
        pl = plistlib.load(fp)
    v = pl["ProductVersion"]
    return ".".join(v.split(".")[:2])


def get_sdk_level() -> str | None:
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


def build_project(project: str, extra_arg: str | None) -> bool:
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


def version_key(version: str) -> tuple[int, ...]:
    return tuple(int(x) for x in version.split("."))


def main(extra_arg: str | None = None) -> None:
    if sys.platform != "darwin":
        print("{RED}PyObjC requires macOS{RESET}")
        sys.exit(1)

    subprocess.check_call(
        [sys.executable, "-mpip", "install", "-U", "setuptools", "pip", "wheel"]
    )

    all_projects = ["pyobjc-core"] + sort_framework_wrappers()
    for idx, project in enumerate(all_projects):
        print()
        print(
            f"{BOLD}{idx + 1}/{len(all_projects)}: Building project {project!r}{RESET}"
        )
        print()
        if not build_project(project, extra_arg):
            print(f"{RED}Cannot build one of the projects, bailing out{RESET}")
            sys.exit(1)
