"""
parse a dhcpd leases file
"""

import itertools
def leases(lines):
    lines = itertools.imap(lambda s:s.strip(), lines)
    for line in lines:
        if line == '{':
            d = {}
            for line in lines:
                if line == '}':
                    yield d
                    break
                if not line:
                    continue
                k,v = line.split('=', 1)
                d[k] = v

EXAMPLE = """
{
        name=EXAMPLEDATA
        ip_address=192.168.2.2
        hw_address=1,0:40:63:d6:61:2b
        identifier=1,0:40:63:d6:61:2b
        lease=0x416213ae
}
"""

if __name__ == '__main__':
    import pprint
    for lease in leases(EXAMPLE.splitlines()):
        pprint.pprint(lease)
