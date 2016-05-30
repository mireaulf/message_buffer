#!/usr/bin/python3
import re
from parsable import parsable
from type import type

class message(parsable):
    regex_start = 'message ([a-zA-Z0-9_]+)\s+{\s+'
    regex_end = re.compile('};\s*')
    def __init__(self, stream):
        super().__init__(self.regex_start, stream)
        self.id = ''
        self.types = list()
 
    def parse_types(self, stream):
        while True:
            t = type(stream)
            res = t.parse()
            if res[0] == False:
                break
            self.types.append(t)
            stream = res[1].strip()
        return stream
        
    def parse(self):
        res_parse = parsable.parse(self)
        res = res_parse
        if res[0]:
            self.id = res[1].group(1)
            res = (res[0], self.regex.sub('', self.stream.strip()))
            rest_stream = self.parse_types(res[1])
            if self.regex_end.match(rest_stream) is None:
                res = (False, None)
            else:
                res = (True, self.regex_end.sub('', rest_stream, 1))
            print(res)
        return res