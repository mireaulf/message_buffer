#!/usr/bin/python3
import re
import hashlib
from parse.parsable import parsable
from parse.message import message

class package(parsable):
    def __init__(self, stream):
        super().__init__('package ([a-zA-Z0-9_]+);', stream)
        self.name = ''
        self.messages = list()
        self.hash = ''

    def __cmp__(self, other):
        return self.name == other.name and self.messages == other.messages

    def __eq__(self, other):
        return self.__cmp__(other)

    def __parse_messages(self, stream):
        while True:
            msg = message(stream)
            res = msg.parse()
            if res[0] == False:
                break
            for m in self.messages:
                if m.id == msg.id:
                    raise ValueError('duplicate message')
            self.messages.append(msg)
            stream = res[1].strip()
        return stream

    def parse(self):
        res_parse = parsable.parse(self);
        res = (False, None)
        if res_parse[0]:
            self.name = res_parse[1].group(1)
            digest = hashlib.sha256()
            digest.update(self.name.encode())
            self.hash = digest.hexdigest()
            stream = self.regex.sub('', self.stream, 1)
            res_parse_message = self.__parse_messages(stream.strip())
            res = (len(self.messages) > 0 and len(res_parse_message) == 0, res_parse_message)            
        return res
