from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

from sphinx.domains import changeset


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_css_file("available.css")
    # Change labels for macOS:
    app.add_directive("macosadded", changeset.VersionChange)
    app.add_directive("macosdeprecated", changeset.VersionChange)
    app.add_directive("macoschanged", changeset.VersionChange)
    app.add_directive("macosremoved", changeset.VersionChange)

    changeset.versionlabels["macosadded"] = "New in macOS %s"
    changeset.versionlabels["macosdeprecated"] = "Deprecated in macOS %s"
    changeset.versionlabels["macoschanged"] = "Changed in macOS %s"
    changeset.versionlabels["macosremoved"] = "Removed in macOS %s"

    changeset.versionlabel_classes["macosadded"] = "added"
    changeset.versionlabel_classes["macosdeprecated"] = "deprecated"
    changeset.versionlabel_classes["macoschanged"] = "changed"
    changeset.versionlabel_classes["macosremoved"] = "removed"

    # And for Python:
    app.add_directive("pythonadded", changeset.VersionChange)
    app.add_directive("pythondeprecated", changeset.VersionChange)
    app.add_directive("pythonchanged", changeset.VersionChange)
    app.add_directive("pythonremoved", changeset.VersionChange)

    changeset.versionlabels["pythonadded"] = "New in Python %s"
    changeset.versionlabels["pythondeprecated"] = "Deprecated in Python %s"
    changeset.versionlabels["pythonchanged"] = "Changed in Python %s"
    changeset.versionlabels["pythonremoved"] = "Removed in Python %s"

    changeset.versionlabel_classes["pythonadded"] = "added"
    changeset.versionlabel_classes["pythondeprecated"] = "deprecated"
    changeset.versionlabel_classes["pythonchanged"] = "changed"
    changeset.versionlabel_classes["pythonremoved"] = "removed"

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
