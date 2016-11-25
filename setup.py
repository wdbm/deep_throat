#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pypandoc
import setuptools

def main():

    setuptools.setup(
        name             = "deep_throat",
        version          = "2016.11.25.0050",
        description      = "speech",
        long_description = pypandoc.convert("README.md", "rst"),
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
                           "numpy",
                           "propyte",
                           "pyaudio",
                           "pyprel",
                           "scipy",
                           "shijian"
                           ],
        scripts          = [
                           "deep_throat.py"
                           ],
        entry_points     = """
            [console_scripts]
            deep_throat = deep_throat:deep_throat
        """
    )

def read(*paths):
    with open(os.path.join(*paths), "r") as filename:
        return filename.read()

if __name__ == "__main__":
    main()
