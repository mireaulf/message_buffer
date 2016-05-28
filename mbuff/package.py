#!/usr/bin/python3
import re
from from_stream import from_stream

class package(from_stream):
    regex = re.compile('package ([a-zA-Z0-9_]+);')
    def __init__(self, stream):
        super().__init__(package.regex, stream)
        self.name = ''
    def parse(self):
        search_res = self.regex.match(self.stream)
        parse_res = (False, None)
        if search_res is not None:
            self.name = search_res.group(1)
            parse_res = (True, self.regex.sub('', self.stream))
        return parse_res

if __name__ == "__main__":
    pack = package('foo bar package asd;'.strip())
    res = pack.parse()
    print(res)

    pack = package(' package asd; foo bar'.strip())
    res = pack.parse()
    print(res)