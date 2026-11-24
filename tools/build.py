"""Build the nv_offline_help_en novelibre plugin package.
        
Note: VERSION must be updated manually before starting this script.

Copyright (c) 2024-2026 Peter Triesberger
For further information see https://github.com/peter88213/nv_offline_help_en
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys

sys.path.insert(0, f'{os.getcwd()}/../../novelibre/tools')
from package_builder import PackageBuilder

VERSION = '5.68.0'


class PluginBuilder(PackageBuilder):

    PRJ_NAME = 'nv_offline_help_en'
    LOCAL_LIB = 'nvofflinehelp'
    GERMAN_TRANSLATION = False

    def add_extras(self):
        self.sampleSource = '../../nvhelp-en/docs'
        self.sampleTarget = f'{self.buildDir}/help'
        self.add_sample()


def main():
    pb = PluginBuilder(VERSION)
    pb.run()


if __name__ == '__main__':
    main()
