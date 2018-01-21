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

or, append `path_to_package` to system environment variable `PYTHONPATH`, 

```bash
export PYTHONPATH=$PYTHONPATH:path_to_package
```


### create a package of modules

First create `__init__.py` in the package directory by `touch __init__.py`, then add modules (python scripts) or sub-packages (sub-directories) to that package. 

We can add in `__init__.py`,  

```python
from package1.module1 import method1
```

so that the method `method1` defined in `module1.py` can be directly called 

```python
import package1
package1.method1()
```

rather than `package1.module1.method1()`.

### relative import 

***NOTE: absolute import is more recommended.***

If we have following package directory

	 package
    ├── __init__.py
    ├── a.py
    ├── b.py
    └── subpackage
        ├── __init__.py
        └── c.py
        └── d.py

in `d.py` we can use relative import (with `from xxx import yyy`):

```python
from . import c    
from .. import a   
from .c import C
from ..a import A
```

But, do not try to run module with relative import, e.g. `python3 package/subpackage/d.py`, since in this case, `__name__` is `__main__`, and you will get the following error:

	SystemError: Parent module '' not loaded, cannot perform relative import

Instead, import methods in `d.py` using absolute import

```python
import package.subpackage.d
from package.subpackage import d
```

### import with `__all__` 

***NOTE: `from xxx import *` is not recommended.***

To control what will be imported using `from package import *`, we can define in `__init__.py`, 

```python
from module1 import object1
from module2 import object2

__all__ == ['object1', 'object2']	
```

In REPL, the imported variable mapping can be verified using `locals()`.

### namespace packages

***REF: [PEP-420](https://www.python.org/dev/peps/pep-0420/)***

If packages in several independent directories (no need to have `__init__.py`) have the same name, they are **namespace packages** (stored in different directories).

	.
	├── path1
	│   └── nspackage
	│       └── module1
	│           ├── __init__.py
	│           └── a.py
	└── path2
	    └── nspackage
	        └── module2
	            ├── __init__.py
	            └── b.py

```python
import sys
sys.path.extend(['path1', 'path2'])
import nspackage
import nspackage.module1
import nspackage.module2
```

Then, in the REPL

	>>> nspakcage.__path__
	_NamespacePath(['path1/nspackage','path2/nspackage'])
	>>> nspakcage.module1.__path__
	['path1/nspackage/module1']
	>>> nspakcage.module2.__path__
	['path2/nspackage/module2']


### executable directories

Create a `__main__.py` in the package directory `package/__main__.py`, then the directory is **executable** `python3 package` -- a way to provide user interface to the package. 

In `__main__.py`, we can import the modules in the package and add some code. Note, there is no need to add `if __name__ == '__main__':` clause (`__name__ === '__main__'` in `__main__.py`). The parent directory is automatically added to `sys.path`. 

The executable directory can be zipped. (**NOTE:** `__main__.py` must be at the top level of zip file, not `package/__main__.py`)

```bash
cd package
zip -r ../package.zip *
cd ..
```

Then the zipped package is executable as well `python3 package.zip`.


### A recommended project/package layout

The top level `project` contains supporting scripts `setup.py`, `__main__.py` and package directory. The package level directory `package` contains subpackages, modules and a test subpackage `test`. 


	project
	├── __main__.py
	├── package
	│   ├── __init__.py
	│   ├── module.py
	│   ├── subpackage
	│   │   └── __init__.py
	│   └── test
	│       ├── __init__.py
	│       └── test.py
	└── setup.py






