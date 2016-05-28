#!/usr/bin/python3
import re

class from_stream:
    def __init__(self, regex, stream):
        if regex is None:
            raise ValueError('regex is null')
        self.regex = regex;
        if stream is None:
            raise ValueError('stream is null')
        if not isinstance(stream, str):
            raise TypeError('stream is not string')
        self.stream = stream
