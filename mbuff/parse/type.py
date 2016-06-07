#!/usr/bin/python3
import re
import hashlib
from parse.parsable import parsable

class type(parsable):
    types = ('bool', 'int8', 'int32', 'string')

    def __init__(self, stream):
        l = str()
        for t in self.types:
            l += '{0}|'.format(t)
        l = '({0}) ([a-zA-Z0-9_]+);'.format(l[:-1])
        super().__init__(l, stream)
        self.type = ''
        self.name = ''
        self.hash = ''

    def __cmp__(self, other):
        return self.type == other.type and self.name == other.name

    def __eq__(self, other):
        return self.__cmp__(other)

    def parse(self):
        res_parse = parsable.parse(self)
        res = res_parse
        if res[0]:
            self.type = res[1].group(1)
            self.name = res[1].group(2)
            res = (res[0], self.regex.sub('', self.stream, 1))
        return res
