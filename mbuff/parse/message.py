#!/usr/bin/python3
import re
import hashlib
from parse.parsable import parsable
from parse.type import type

class message(parsable):
    regex_start = 'message ([a-zA-Z0-9_]+)\s+{\s+'
    regex_end = re.compile('};\s*')

    def __init__(self, stream:str):
        super().__init__(self.regex_start, stream)
        self.id = ''
        self.types = list()
        self.hash = ''
 
    def __cmp__(self, other):
        return self.id == other.id and self.types == other.types

    def __eq__(self, other):
        return self.__cmp__(other)        

    def __parse_types(self, stream:str):
        while True:
            t = type(stream)
            res = t.parse()
            if res[0] == False:
                break
            if t in self.types:
                raise ValueError('duplicate type')
            self.types.append(t)
            stream = res[1].strip()
        return stream

    def parse(self):
        res_parse = parsable.parse(self)
        res = (False, None)
        if res_parse[0]:
            self.id = res_parse[1].group(1)
            stream = self.regex.sub('', self.stream.strip(), 1)
            res_parse_types = self.__parse_types(stream)
            match = self.regex_end.match(res_parse_types)
            if match is None:
                res = (False, None)
            else:
                res_stream = self.regex_end.sub('', res_parse_types, 1)
                res = (True, res_stream)
        return res