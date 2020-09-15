# py-to-zip


libtool is a Python library for creating a zip from python files,
so you can send the zip to another computer.
it also create a command file so you can acsess with one command

py-to-zip runs in Python 3+ and only in Windows.

## Instructions
You need to make a settings.ini like this:


```ini
[settings]
main_file=main.py
#the main file would be run with the cmd file
name=name of project
#in default("by file") it will be name of file

glob_pattern=*.py,data/*.png,data/**/*.txt
# the glob patterns for search the files to the zip
glob_recursive=1
# set the recursive for the glob function,this is only to python 3.5+

cmd_file=czip.bat
#the name of cmd file,(like run.cmd or play.bat),in default it will be name of file
python_exe=py
#the python name who can access from the command-line.(py,python,python3,...)

```
the main file have to be find by glob.

To create zip from ini:
```
czip {your ini file}
or
CZip.bat {your ini file}
```
And the py-to-zip creates the zip and command file automatically.

### Access from python
To access the py-to-zip from a python file:
```python
from py_to_zip.py_to_zip import by_config


# its add ini Directly to function

by_config(
    dict(main_file="py_to_zip.py",  # the main file would be run with the cmd file
         name="py-to-zip",  # the name of project,in default("by file") it will be name of file
         glob_pattern="*.py,data\\**\\*.txt",
         # the glob patterns for search the files to the zip (to use ** you need glob_recursive)
         glob_recursive=True,  # set the recursive for the glob function,this is only to python 3.5+
         cmd_file="czip.bat",  # the name of cmd file,(like run.cmd or play.bat),in default it will be name of file
         python_exe="py",
         )
)
```
And the py-to-zip creates the zip and command file automatically.


### Installing

To install with pip-
type in terminal:
```
(sudo) pip install py_to_zip
```
## Additional options
if you want to use one function without another function
```python
from py_to_zip.py_to_zip import Zip
z= Zip(
         main_file="py_to_zip.py",  # the main file would be run with the cmd file
         name="py-to-zip",  # the name of project,in default("by file") it will be name of file
         glob_pattern="*.py,data\\**\\*.txt",
         # the glob patterns for search the files to the zip (to use ** you need glob_recursive)
         glob_recursive=True,  # set the recursive for the glob function,this is only to python 3.5+
         cmd_file="czip.bat",  # the name of cmd file,(like run.cmd or play.bat),in default it will be name of file
         python_exe="py"
         with_print=True or False 
        # if set to False,the program not print anything.this can exists also in INI
)
#the automatically is:
z.create_zip()
#but you can acsess
z._find_names() #to find names of file with glob
z._create_cmd()#to create the cmd script
from py_to_zip.py_to_zip import _parse_cmd_argev 
_parse_cmd_argev(["file"])#this is for the cmd script....
```

## Author

matan h

## License

This project is licensed under the MIT License.

##created by

this library was created and updated by [libtool](https://github.com/matan-h/libtool)
