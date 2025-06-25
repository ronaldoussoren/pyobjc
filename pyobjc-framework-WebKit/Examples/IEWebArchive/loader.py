import email

from Cocoa import NSURL, NSData, NSString
from WebKit import WebArchive, WebResource


# def loadMHT(filename):
#     """
#     Load a .HMT HTML archive and return the WebArchive representation.
#     """
#     return HMTLoad(filename).asWebArchive()


class MHTLoader:
    """
    A loader for .mht files, and archive format used by MS Internet Explorer
    on Windows.
    """

    def __init__(self, filename):
        self.filename = filename

        # root of the archive (index into self.parts)
        self.root = None

        # filename -> (content-type, data)
        self.parts = {}

        self.loadFile(filename)

    def loadFile(self, filename):
        with open(filename) as fp:
            msg = email.message_from_file(fp)

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue

            filename = part.get("Content-Location")
            contentType = part.get_content_type()
            data = part.get_payload(decode=True)

            self.parts[filename] = (contentType, data)
            if self.root is None:
                self.root = filename

    def fixupURL(self, url):
        # IE creates MHT files with file: URLS containing backslashes,
        # NSURL insists that those are invalid, replace backslashes by
        # forward slashes.
        if url.startswith("file:"):
            return url.replace("\\", "/")
        else:
            return url

    def asWebArchive(self):
        """
        Convert the MHT archive to a webarchive.
        """
        rootType, rootText = self.parts[self.root]
        pageResource = (
            WebResource.alloc().initWithData_URL_MIMEType_textEncodingName_frameName_(  # noqa: B950
                NSData.dataWithBytes_length_(
                    rootText.replace(b"\\", b"/"), len(rootText)
                ),
                NSURL.URLWithString_(self.fixupURL(self.root)),
                NSString.stringWithString_(rootType),
                None,
                None,
            )
        )

        resources = []
        for url in self.parts:
            if url == self.root:
                continue

            tp, data = self.parts[url]
            resources.append(
                WebResource.alloc().initWithData_URL_MIMEType_textEncodingName_frameName_(
                    NSData.dataWithBytes_length_(data, len(data)),
                    NSURL.URLWithString_(self.fixupURL(url)),
                    NSString.stringWithString_(tp),
                    None,
                    None,
                )
            )

        return WebArchive.alloc().initWithMainResource_subresources_subframeArchives_(
            pageResource, resources, None
        )


def main():
    # Testing...
    p = MHTLoader("python-home.mht")
    a = p.asWebArchive()
    with open("python-home.webarchive", "wb") as fp:
        fp.write(a.data().bytes())


if __name__ == "__main__":
    main()
