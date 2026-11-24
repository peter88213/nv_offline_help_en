"""English offline help pages for novelibre.

Requires Python 3.7+
Copyright (c) 2024-2026 Peter Triesberger
For further information see https://github.com/peter88213/nv_offline_help_en
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from nvlib.controller.plugin.plugin_base import PluginBase
from nvofflinehelp.offline_help import OfflineHelp
from pathlib import Path
from shutil import rmtree
import os


class Plugin(PluginBase):
    """plugin class."""
    VERSION = '@release'
    API_VERSION = '5.63'
    DESCRIPTION = 'English offline help pages'
    URL = 'https://github.com/peter88213/nv_offline_help_en'

    def install(self, model, view, controller):
        """Install the plugin at runtime.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        homeDir = str(Path.home()).replace('\\', '/')
        self.helpSite = f'{homeDir}/.novx/help'
        if not os.path.isdir(self.helpSite):
            raise FileNotFoundError('Offline help pages not installed')

        super().install(model, view, controller)
        self.originalHelpService = self._ctrl.helpService
        self._ctrl.helpService = OfflineHelp(self.helpSite)

    def uninstall(self):
        rmtree(self.helpSite, ignore_errors=True)
        self._ctrl.helpService = self.originalHelpService
        self.isActive = False

