#!/usr/bin/python3
from mbuff.parse.type import type as type_type
from mbuff.parse.message import message as message_type
from mbuff.parse.package import package as package_type 
import hashlib

class to_cpp:
    @staticmethod
    def type(o:type_type, hint:str):
        if o is None or hint is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        h.update(o.name.encode())
        h.update(o.type.encode())
        h.update(hint.encode())
        o.hash = h.hexdigest()
        return """
private:
hash_type_member m_{1}_hash = {0};
bool m_{1}_is_set = false;
{2} m_{1};
public:
void set_{1}({2} value) {{
    m_{1} = value;
}}
{2} get_{1}() const {{
    return m_{1};
}}
""".format(o.hash, o.name, o.type)

    @staticmethod
    def message(o:message_type, hint:str):
        if o is None or hint is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        types = str()
        for t in o.types:
            types += to_cpp.type(t, o.id)
            h.update(t.hash.encode())
        h.update(hint.encode())
        o.hash = h.hexdigest()
        return """
struct {1} {{
hash_type_message m_{1}_hash = {0};
{2}
}};
""".format(o.hash, o.id, types)

    @staticmethod
    def package(o:package_type):
        if o is None:
            raise ValueError('invalid arguments')
        h = hashlib.sha256()
        messages = str()
        for m in o.messages:
            messages += to_cpp.message(m, o.name)
            h.update(m.hash.encode())
        o.hash = h.hexdigest()
        return """
namespace {0} {{
{1}
}}
""".format(o.name, messages)
