import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='py-to-zip',
    version='0.0.1',
    license='MIT',
    description='libtool is a library for creating a zip with command file from python files.',
    author='matan h',
    author_email='matan.honig2@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/matan-h/czip',
    packages=['py_to_zip'],
    scripts=['py_to_zip\\CZip'],
    package_data={'py_to_zip': ["license.txt"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
