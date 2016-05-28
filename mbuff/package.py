#!/usr/bin/python3
import re

class package:
    regex = re.compile('package [a-zA-Z0-9_]+;')
    def __init__(self, stream):
        if stream is None:
            raise ValueError('stream is null')
        if not isinstance(stream, str):
            raise TypeError('stream is not string')
        self.stream = stream;
    def parse(self):
        search_res = self.regex.match(self.stream)
        parse_res = tuple(False, ())
        if search_res is not None:
            parse_res = tuple(True, self.regex.sub('', self.stream))
        return parse_res

if __name__ == "__main__":
    pack = package('foo bar package asd;'.strip())
    res = pack.parse()
    print(res)

    pack = package(' package asd; foo bar'.strip())
    res = pack.parse()
    print(res)