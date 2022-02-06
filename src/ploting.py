"""
ploting.py
====================================
Moduł odpowiedzialny za tworzenie wykresów, zapis do pliku i ich wyświetlanie.
"""

from typing import List
import matplotlib.pyplot as plt
import math


def make_plot(xs: List[float], ys: List[float] ) -> None:
    """Funkcja generująca wykres.

    Parameters
    ----------
    xs : List[float]
        Wartości na osi X.
    ys : List[float]
        Wartości na osi Y.

    Returns
    -------
    None

    """
    plt.clf()
    plt.plot(xs, ys)


def save_plot(loc: str, trans: bool) -> None:
    """Funkcja zapisująca wykres jako plik png.

    Parameters
    ----------
    loc : str
        Lokalizacja, w której ma być zapisany wynik.
    trans : bool
        Czy wykres ma być przeźroczysty.

    Returns
    -------
    None

    """
    if trans:
        plt.axis("off")
    else:
        plt.axis("on")
    plt.savefig(loc, transparent=trans)


def show_plot() -> None:
    """Funkcja wyświetlająca wykres.

    Returns
    -------
    None

    """
    plt.show()
