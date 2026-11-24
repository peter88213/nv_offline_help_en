"""Provide a service class for the offline help function.

Copyright (c) 2024-2026 Peter Triesberger
For further information see https://github.com/peter88213/nv_offline_help_en
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import webbrowser


class OfflineHelp:

    def __init__(self, helpSite):
        self.helpSite = helpSite

    def open_help_page(self, page, site=None):
        """Show the online help page specified by page."""
        if not site:
            site = self.helpSite
            if '#' in page:
                page = page.split('#')[0]
            elif not page.endswith('.html'):
                if page and not page.endswith('/'):
                    page = f'{page}/'
                page = f'{page}index.html'
        webbrowser.open(f'{site}/{page}')

