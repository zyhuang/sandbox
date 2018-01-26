
### Strings and Collections

* Raw string: `'\n'` gives the newline. `r'\n'` gives `'\n'` literally.
* Unicode string representations: unicode `'\uxxxx'` (`'\u'` + 4-characters), hexidesimal `'\xaa'` (`'\x'` + 2-characters),  octal `'\nnn'` (`'\'` + 3-digits). 
* Byte string `b'data'` is converted to and from Unicode string using `bS.decode()` and `uS.encode()` methods (see [Codecs](https://docs.python.org/3/library/codecs.html)). For example

```
>>> normal_str = '如是我闻'
>>> byte_str = normal_str.encode('utf-8')  # 3 hex per char
b'\xe5\xa6\x82\xe6\x98\xaf\xe6\x88\x91\xe9\x97\xbb'
>>> byte_str.decode('utf-8')
'如是我闻'
```




