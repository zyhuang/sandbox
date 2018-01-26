
### Strings and Collections

* Raw string: `'\n'` gives the newline. `r'\n'` gives `'\n'` literally.
* Unicode string representations: unicode `'\uxxxx'` (`'\u'` + 4-characters), hexidecimal `'\xaa'` (`'\x'` + 2-characters),  octal `'\nnn'` (`'\'` + 3-digits). 
* Byte string is commonly used in files, network resources and HTTP requests. It can be converted to and from Unicode string using `uS = bS.decode('utf-8')` and `bS = uS.encode('utf-8')` methods (see [Codecs](https://docs.python.org/3/library/codecs.html)). For example, 


```python
>>> normal_str = '如是我闻'
>>> byte_str = normal_str.encode('utf-8')  # 3 hex per char
b'\xe5\xa6\x82\xe6\x98\xaf\xe6\x88\x91\xe9\x97\xbb'
>>> byte_str.decode('utf-8')
'如是我闻'
```

### Style

[PEP8](https://www.python.org/dev/peps/pep-0008/)

* two lines between functions
* beginning shebang (to allow for loading of correct python interpreter): `#!/usr/bin/env python3`


### Docstring

[PEP257](https://www.python.org/dev/peps/pep-0257/)
[Google Style Guide](https://google.github.io/styleguide/pyguide.html) 

Other documentation tools: reStructuredText, Sphinx

* add docstring after every function definition
* docstring of module can be retrieved under REPL with `help(module)`.

```python
"""What this module does.

Usage:

    python3 module.py 
"""

def say_hello(message):
    """Return a formatted message. 
    
    Args:
    	message: the message to print
    	
    Returns:
    	A formatted string containing the input message.
    """
    return "your message is {}".format(message)
```


### Modularity

* If a program is imported, `__name__ == module_name`. If it is executed, `__name__ == '__main__'`. 

### Object

* `a is b` tests if they are the same object `id(a) == id(b)`.
* Value equality is not identity. Two different objects may have the same value (i.e. `a == b` but `a is b == False`). 
* The id of a variable may change when the referred object changes (e.g. be reassigned a value). List expension does not change the object id and hence its reference.
* `id(var)` deals with the underlying object, variable names are just named references.
* Function arguments are passing by object referenc, or the value of reference (not the value of object), so the function will modify the object rather than modifying a copy of the object. 
* NOTE: Reassigning the input argument to other values will reassign the variable to a local object. So the global object that the variable originally refers to may not be changed.
 








