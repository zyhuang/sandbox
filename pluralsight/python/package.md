### the difference between packages and modules

* a python **package** is represented by a *directory* and a python **module** is represented by a *file*.
* a **package** generally has a `__path__` member (a list of paths in python 3.3+), as well as a `__file__` member (a string of path to `package_path/__init__.py`)
* a **module** has only `__file__` member (the absolute path of the module)
* After `import`, `type(package)` and `type(module)` both give `<class 'module'>`.


### include a package in python 

To manually include a package in `sys.path`,
```python
import sys
sys.path.append('path_to_package')
import package
```
or, append `path_to_package` to system environment variable `PYTHONPATH`, *e.g.* using `expoert PYTHONPATH=$PYTHONPATH:path_to_package`. 


### create a package of modules

First create `__init__.py` in the package directory by `touch __init__.py`, then add modules (python scripts) or packages (directories) to that directory. 

*TIP:* We can add in `__init__.py`,  
```python
from package1.module1 import method1
```
so that method `method1` defined in `module1.py` can be directly called 
```python
import package1
package1.method1()
```
rather than `package1.module1.method1()`.


