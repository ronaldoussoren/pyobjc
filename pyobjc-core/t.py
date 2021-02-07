import subprocess
import plistlib
import pprint

data = subprocess.check_output(
    ["/usr/bin/xcrun", "-sdk", "macosx", "--show-sdk-path"],
    universal_newlines=True,
).strip()

print(data)

value = plistlib.load(open(data + "/SDKSettings.plist", "rb"))
pprint.pprint(value)
