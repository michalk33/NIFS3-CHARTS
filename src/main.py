"""
main.py
====================================
Główny moduł.
"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from typing import List
import interface as intfc


def start_running() -> None:
    """Funkcja główna aplikacji.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
    win = intfc.MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


#wykona się tylko przy bezpośrednim uruchomieniu main.py
if __name__ == "__main__":
    start_running()
