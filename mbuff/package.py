#!/usr/bin/python3
import re
from parsable import parsable

class package(parsable):
    def __init__(self, stream):
        super().__init__('package ([a-zA-Z0-9_]+);', stream)
        self.name = ''
    def parse(self):
        res_parse = parsable.parse(self);
        res = (res_parse[0], res_parse[1])
        if res[0]:
            self.name = res[1].group(1)
            res = (res[0], self.regex.sub('', self.stream))
        return res
