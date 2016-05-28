#!/usr/bin/python3
import re
from parsable import parsable

class message(parsable):
    def __init__(self, stream):
        regex = re.compile('message ([a-zA-Z0-9_]+) \{ \};')
        super().__init__(regex, stream)
