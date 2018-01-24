### Principles

* Exceptions can not be ignored.
* Exceptions are part of the API. Callers needs to know when to expect what exceptions, so that they can handle the errors properly.
* Use exceptions that users will anticipate (e.g. standard exceptions)



### Types of exceptions and when to raise

* runtime error: `ValueError`, `TypeError`
* programmer development error (do not catch these): `IndentationError`, `SyntaxError`, `NameError`

* raise `ValueError(err_msg_str)` when a function is supplied with an illegal value (e.g. `log(-1)`). This is usually placed at beginning of a function as a security check. 


### Exception example

Typical syntax for `try`/`except` clause:

```python
try:
    statements
except (ValueError, TypeError) as e:
    statements to handle exceptions
    raise ErrorConstructor('Define Your Custom Error Message Here')
```

where `e` is an exception object, and its string version `str(e)` contains the description of exception details, e.g. `invalid literal for int() with base 10: `. 

During the exception handling, the exception should be re-raised using `raise`, so that other functions calling this function can catch the error. This also makes it easier to traceback the origin of errors, when function calls are nested. 





