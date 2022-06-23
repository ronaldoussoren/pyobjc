import re

LOGGING_FORMAT = r'''^(?P<client>\S+)●\S+●(?P<userid>\S+)●\[(?P<datetime>[^\]]+)\]↵
●"(?P<method>[A-Z]+)●(?P<request>[^●"]+)?●HTTP/[0-9.]+"↵
●(?P<status>[0-9]{3})●(?P<size>[0-9]+|-)●"(?P<referrer>[^"]*)"↵
●"(?P<useragent>[^"]*)"'''
RE_TABLE = str.maketrans("●", " ", "↵\n")
RE_LOGGING_FORMAT = LOGGING_FORMAT.translate(RE_TABLE)
print(repr(RE_LOGGING_FORMAT))
print(RE_LOGGING_FORMAT)
print(re.compile(RE_LOGGING_FORMAT))
