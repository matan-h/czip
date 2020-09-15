from py_to_zip.py_to_zip import by_config

__title__ = 'py_to_zip'
__description__ = 'description of the library.'
__url__ = 'your website url (or github url)'
__version__ = '0.0.1'
__author__ = 'your name'
__author_email__ = 'your email'
__license__ = 'MIT'
if __name__ == "__main__":
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
