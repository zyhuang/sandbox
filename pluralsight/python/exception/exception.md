### Principles

**Errors should never pass silently, unless explicitly silenced.** Errors are like bells. They are of no use when silenced. 

* An exception object contains where and why the exception event occured, and should be raised to exception handler to interrogate and take action. 
* Exceptions are part of the **API**. Callers needs to know when to expect what exceptions, so that they can handle the errors properly.
* Methods with similar functions should raise exceptions following the same **protocols** (e.g. list index, dictionary key, value range error, input type error).
* **Exceptions can not be ignored** (unhandled exceptinos terminate the program). Exceptions require explicit handling. Error codes are silent by default.
* Try to use standard exceptions that users will anticipate and understand (e.g. `ValueError`, `TypeError`, `IndexError`, `KeyError`).
* **It is easier to ask for forgiveness than permission (EAFP)**: Blindly hope for the best and prepare for the consequences if not. 
* **Look Before You Leap (LBYL)**: check all pre-conditions for a failure-prone operation in advance of attempting the operation. 
* Exceptions allow centralized non-local handling. Error checking codes require interspersed, local handling.





### Types of exceptions and when to raise

* runtime error (need to catch and raise): `ValueError`, `TypeError`, `IndexError`, `KeyError`
* programmer error (do not catch these): `IndentationError`, `SyntaxError`, `NameError`
* raise `ValueError(err_msg_str)` when a function is supplied with an illegal value (e.g. `log(-1)`). This is usually placed at beginning of a function as a security check. 
* Avoid limiting your function with *specific* type checks (e.g. using `isinstance()`) (This is LBYL, and negates the dynamic typing in Python). Instead just let them fail and try to catch `TypeError`.

### Exception example

Typical syntax for `try`/`except` clause:

```python
try:
    # statements that may raise exceptions
except (ValueError, TypeError) as e:
    # statements to handle expected exceptions
    raise ErrorConstructor('Define Your Custom Error Message Here')
finally:
    # cleanup statements to run even when try-block fails
```

where `e` is an exception object, and its string version `str(e)` contains the description of exception details, e.g. `invalid literal for int() with base 10: `. 

During the exception handling, the exception should be re-raised using `raise`, so that other functions calling this function can catch the error. This also makes it easier to backtrace the origin of errors, especially when function calls are nested. 





