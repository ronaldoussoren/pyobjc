#!/usr/bin/env python3

import pathlib


def readinfo(path):
    result = {}
    bench = result["bench"] = {}

    for line in path.open():
        if line.startswith("@"):
            item = line.strip()[1:].split(None, 1)
            result[item[0]] = item[1]
        else:
            if not line.strip():
                continue
            item = line.split(":", 1)
            bench[item[0].strip()] = float(item[1].strip())
    return result


def main():
    curdir = pathlib.Path(__file__).parent
    results = []
    for p in (curdir / "results").glob("pyobjcbench*.txt"):
        results.append(readinfo(p))

    results.sort(key=lambda item: (item["python"], item["objc"]))
    keys = list(results[0]["bench"].keys())

    headers = ("test name",) + tuple(r["objc"] for r in results)
    fmt = " | ".join(["{:40s}"] + ["{:16s}"] * len(results))
    print(fmt.format(*headers))
    print("+".join(["-" * 41] + ["-" * 18] * len(results)))
    for key in keys:
        base = results[0]["bench"][key]
        row = [key]
        for r in results:
            try:
                cur = r["bench"][key]
            except KeyError as exc:
                print(f"{key}: {exc!r}")
                continue
            if cur == base:
                row.append(f"{cur:.3f}")
            else:
                row.append(f"{cur:.3f} ({((cur-base)/base)*100:+.1f}%)")
        print(fmt.format(*row))


if __name__ == "__main__":
    main()
