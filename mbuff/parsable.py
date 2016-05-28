#!/usr/bin/python3
import re

class parsable:
    def __init__(self, regex, stream):
        if regex is None:
            raise ValueError('regex is null')
        if not isinstance(regex, str):
            raise TypeError('regex is null')
        self.regex = re.compile(regex)
        if stream is None:
            raise ValueError('stream is null')
        if not isinstance(stream, str):
            raise TypeError('stream is not string')
        self.stream = stream
    def parse(self):
        search_res = self.regex.match(self.stream)
        return search_res is not None
