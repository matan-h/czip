# py_to_zip


description of the library

py_to_zip runs in Python 3+

## examples

```python
from py_to_zip.py_to_zip import by_config


# you can add ini Directly to function

by_config(
    dict(main_file="py_to_zip.py",  # the main file would be run with the cmd file
         name="py-to-zip",  # the name of project,in default("by file") it will be name of file
         glob_pattern="*.py,data\\**\\*.txt",
         # the glob patterns for search the files to the zip (to use ** you need glob_recursive)
         glob_recursive=True,  # set the recursive for the glob function,this is only to python 3.5+
         cmd_file="czip.bat",  # the name of cmd file,(like run.cmd or play.bat),in default it will be name of file
         python_exe="py")
)
```

### Prerequisites
py_to_zip depends on the python modules:

wheel

### Installing
To install with pip-
type in terminal:
```
(sudo) pip install py_to_zip
```

## Built With
* [wheel](https://github.com/pypa/wheel) - A built-package format for Python

## Author
your name
## License
This project is licensed under the MIT License.

###created by
this library created by [libtool](https://github.com/matan-h/libtool)
