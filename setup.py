#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():

    setuptools.setup(
        name             = "deep_throat",
        version          = "2017.02.05.0145",
        description      = "speech",
        long_description = long_description(),
        url              = "https://github.com/wdbm/deep_throat",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        py_modules       = [
                           "deep_throat"
                           ],
        install_requires = [
                           "datavision",
                           "docopt",
                           "matplotlib",
                           "nltk",
                           "numpy",
                           "propyte",
                           "pyaudio",
                           "pyprel",
                           "scipy",
                           "shijian",
                           ],
        scripts          = [
                           "deep_throat.py"
                           ],
        entry_points     = """
            [console_scripts]
            deep_throat = deep_throat:deep_throat
        """
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
