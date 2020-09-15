

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='py_to_zip',
    version='0.0.1',
    license='MIT',
    description='description of the library',
    author='your name',
    author_email='your email',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'your website url (or github url)',
    packages=['py_to_zip'],
    
    install_requires = ['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)