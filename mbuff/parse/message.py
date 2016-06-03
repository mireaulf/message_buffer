#!/usr/bin/python3
import re
import hashlib
from parse.parsable import parsable
from parse.type import type

class message(parsable):
    regex_start = 'message ([a-zA-Z0-9_]+)\s+{\s+'
    regex_end = re.compile('};\s*')

    def __init__(self, stream):
        super().__init__(self.regex_start, stream)
        self.id = ''
        self.types = list()
        self.hash = ''
 
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
        res = (False, None)
        if res_parse[0]:
            self.id = res_parse[1].group(1)
            digest = hashlib.sha256()
            digest.update(self.id.encode())
            self.hash = digest.hexdigest()
            stream = self.regex.sub('', self.stream.strip(), 1)
            res_parse_types = self.parse_types(stream)
            match = self.regex_end.match(res_parse_types)
            if match is None:
                res = (False, None)
            else:
                res_stream = self.regex_end.sub('', res_parse_types, 1)
                res = (True, res_stream)
        return res