
## Message format
### Definition
<pre>
<code>
message_file :=
  package
  messages
package := package id;
id := [a-zA-Z0-9_]
messages := message+
message :=
  message id {
    (type id;)+
  };
type := [ bool | int8 | int32 | string ]
</code>
</pre>
