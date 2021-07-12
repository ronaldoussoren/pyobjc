import os
import zipfile

destination_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_dir = os.path.dirname(destination_dir)
verbose = True


def split_groups(info):
    result = []
    current = (None, [])

    for path, summary in info:
        if path is None:
            if current[1]:
                result.append(current)
            current = (summary, [])
        else:
            current[1].append(path)

    if current[1]:
        result.append(current)
    return result


def zip_directory(input_dir, output_file, verbose):
    if verbose:
        print(f"Zip {input_dir} -> {output_file}")

    zf = zipfile.ZipFile(output_file, "w")
    basename = os.path.basename(output_file)[:-4]

    while input_dir.endswith(os.path.sep):
        input_dir = input_dir[: -len(os.path.sep)]

    for dirpath, _dirnames, filenames in os.walk(input_dir):
        relpath = os.path.join(basename, dirpath[len(input_dir) + 1 :])

        for fn in filenames:
            if os.path.islink(os.path.join(dirpath, fn)):
                # Skip symbolic links
                continue

            zf.write(
                os.path.join(dirpath, fn),
                os.path.join(relpath, fn),
                zipfile.ZIP_DEFLATED,
            )
    zf.close()


def convert_script_example(name, input_file, output_dir, verbose):
    if verbose:
        print(f"Fetching example {name} from {input_file}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file) as fp_in:
        with open(
            os.path.join(output_dir, os.path.basename(input_file)), "w"
        ) as fp_out:
            fp_out.write(fp_in.read())

    readme = "..."

    with open(os.path.join(output_dir, "index.rst"), "w") as fp:
        print(name, file=fp)
        print("=" * len(name), file=fp)
        print("", file=fp)
        print(
            f"* :download:`Download example <{os.path.basename(input_file)}>`",
            file=fp,
        )
        print("", file=fp)
        print(readme, file=fp)
        print("", file=fp)

        lang = "python"
        with open(input_file) as src_fp:
            source = src_fp.read()

        print("", file=fp)
        path = os.path.basename(input_file)
        print(path, file=fp)
        print("." * len(path), file=fp)
        print("", file=fp)

        print(f".. sourcecode:: {lang}", file=fp)
        print("", file=fp)
        for ln in source.splitlines():
            print(f"    {ln.rstrip()}", file=fp)
        print("", file=fp)


def convert_example(name, input_dir, output_dir, verbose):
    if verbose:
        print(f"Fetching example {name} from {input_dir}")

    zipname = f"PyObjCExample-{name}.zip"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    zip_directory(input_dir, os.path.join(output_dir, zipname), verbose)

    readme_file = os.path.join(input_dir, "ReadMe.txt")
    summary_file = os.path.join(input_dir, "Summary.txt")
    if os.path.exists(readme_file):
        with open(readme_file) as fp:
            readme = fp.read()

    elif os.path.exists(summary_file):
        with open(summary_file) as fp:
            readme = fp.read()

    else:
        print(f"WARNING: Example at {input_dir} does not contain a readme")
        readme = "A PyObjC Example without documentation"

    with open(os.path.join(output_dir, "index.rst"), "w") as fp:
        print(name, file=fp)
        print("=" * len(name), file=fp)
        print("", file=fp)
        print(f"* :download:`Download example <{zipname}>`", file=fp)
        print("", file=fp)
        print(readme, file=fp)
        print("", file=fp)

        print(".. rst-class:: tabber", file=fp)
        print("", file=fp)
        print("Sources", file=fp)
        print("-------", file=fp)
        print("", file=fp)

        for dirpath, dirnames, filenames in os.walk(input_dir):
            for name in list(dirnames):
                if name.endswith(".nib"):
                    dirnames.remove(name)

            relpath = dirpath[len(input_dir) + 1 :]

            for fn in sorted(filenames):
                if relpath:
                    path = os.path.join(relpath, fn)
                else:
                    path = fn

                ext = os.path.splitext(fn)[-1]
                if ext in {".py", ".pyw"}:
                    lang = "python"
                elif ext in {".m", ".c", ".h"}:
                    lang = "objective-c"
                else:
                    continue

                with open(os.path.join(dirpath, fn)) as src_fp:
                    source = src_fp.read()

                print(".. rst-class:: tabbertab", file=fp)
                print("", file=fp)
                print(path, file=fp)
                print("." * len(path), file=fp)
                print("", file=fp)

                print(f".. sourcecode:: {lang}", file=fp)
                print("", file=fp)
                for ln in source.splitlines():
                    print(f"    {ln.rstrip()}", file=fp)
                print("", file=fp)

        # TODO: Store other links with examples and add them to this list


def examples_for_project(input_dir, output_dir, verbose):
    result = []
    input_dir = os.path.join(input_dir, "Examples")
    if not os.path.exists(input_dir):
        return

    for dirpath, dirnames, _filenames in os.walk(input_dir):
        to_remove = set()

        added_dir = False

        for dn in dirnames:
            if dn in ("NonFunctional",):
                # Skip broken examples
                continue

            elif os.path.exists(os.path.join(dirpath, dn, "setup.py")):
                # Found an example
                relpath = os.path.join(dirpath[len(input_dir) + 1 :], dn)
                summary = convert_example(
                    dn,
                    os.path.join(dirpath, dn),
                    os.path.join(output_dir, relpath),
                    verbose,
                )
                to_remove.add(dn)
                if not added_dir and dirpath[len(input_dir) + 1 :]:
                    added_dir = True
                    result.append((None, dirpath[len(input_dir) + 1 :]))
                result.append((os.path.join(relpath, "index"), summary))

            elif dn == "Scripts":
                to_remove.add(dn)
                relpath = os.path.join(output_dir, dirpath[len(input_dir) + 1 :])
                if not os.path.exists(relpath):
                    os.makedirs(relpath)
                zf = zipfile.ZipFile(os.path.join(relpath, "scripts.zip"), "w")

                for fn in os.listdir(os.path.join(dirpath, dn)):
                    if not fn.endswith(".py"):
                        continue

                    zf.write(os.path.join(dirpath, dn, fn), fn)

                    relpath = os.path.join(dirpath[len(input_dir) + 1 :], dn, fn[:-3])
                    if relpath.startswith("/"):
                        relpath = relpath[1:]
                    summary = convert_script_example(
                        os.path.join(dn, fn[:-3]),
                        os.path.join(dirpath, dn, fn),
                        os.path.join(output_dir, relpath),
                        verbose,
                    )
                    if not added_dir and dirpath[len(input_dir) + 1 :]:
                        added_dir = True
                        result.append((None, dirpath[len(input_dir) + 1 :]))
                    result.append((os.path.join(relpath, "index"), summary))
                zf.close()

        for dn in to_remove:
            # Don't peek inside examples
            dirnames.remove(dn)

    return result


def copy_zip_contents(zfout, zfin, relpath):
    for nm in zfin.namelist():
        data = zfin.read(nm)
        zfout.writestr(os.path.join(relpath, nm), data)


def merge_example_zips(output_fn, input_directory, verbose):
    if verbose:
        print(f"Merging example zips in {input_directory} into {output_fn}")

    if os.path.exists(output_fn):
        os.unlink(output_fn)

    zf = zipfile.ZipFile(output_fn, "w", compression=zipfile.ZIP_DEFLATED)

    for dn, _dirs, files in os.walk(input_directory):
        for fn in files:
            if fn.endswith(".zip"):
                zfpath = os.path.join(dn, fn)
                if os.path.abspath(zfpath) == os.path.abspath(output_fn):
                    continue

                zfin = zipfile.ZipFile(zfpath, "r")
                copy_zip_contents(
                    zf, zfin, os.path.join(dn[len(input_directory) + 1 :], fn[:-4])
                )


def build_examples(app):
    print("hello", app)

    all_examples = []
    for dn in sorted(os.listdir(source_dir)):
        if not dn.startswith("pyobjc-framework-") and not dn.startswith("pyobjc-core"):
            continue

        input_dir = os.path.join(source_dir, dn)
        if dn == "pyobjc-core":
            output_dir = os.path.join(destination_dir, "examples", "core")
        else:
            output_dir = os.path.join(destination_dir, "examples", dn[17:])

        info = examples_for_project(input_dir, output_dir, verbose)
        if info:
            all_examples.append((dn, info))

    merge_example_zips(
        os.path.join(destination_dir, "examples", "all-examples.zip"),
        os.path.join(destination_dir, "examples"),
        verbose,
    )

    for dn in os.listdir(os.path.join(destination_dir, "examples")):
        path = os.path.join(destination_dir, "examples", dn)
        if not os.path.isdir(path):
            continue

    if verbose:
        print("Generating examples/index.rst")

    with open(os.path.join(destination_dir, "examples", "index.rst"), "w") as fp:
        print("Examples overview", file=fp)
        print("=================", file=fp)
        print("", file=fp)
        if not all_examples:
            print("There are no examples on the website", file=fp)

        else:
            print("* :download:`Download all examples <all-examples.zip>`", file=fp)
            print("", file=fp)
            for project, info in all_examples:
                print(project, file=fp)
                print("-" * len(project), file=fp)
                print("", file=fp)

                for grp, items in split_groups(info):
                    if grp:
                        print(grp, file=fp)
                        print("." * len(grp), file=fp)
                        print("", file=fp)

                    print(".. toctree::", file=fp)
                    print("   :maxdepth: 1", file=fp)
                    print("", file=fp)
                    for path in items:
                        if project == "pyobjc-core":
                            print(f"   core/{path}", file=fp)
                        else:
                            print(f"   {project[17:]}/{path}", file=fp)
                    print("", file=fp)


def setup(app):
    app.connect("builder-inited", build_examples)
