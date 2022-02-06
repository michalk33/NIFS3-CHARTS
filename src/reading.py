"""
reading.py
====================================
Moduł odpowiedzialny za odczyt danych z pliku.
"""

from typing import List
import csv


def read_file(loc: str) -> List[List[float]]:
    """Funkcja wczytująca dane liczbowe z pliku.

    Parameters
    ----------
    loc : str
        Nazwa pliku.

    Returns
    -------
    List[List[float]]
        Wynikowe dane z pliku.

    """
    return [list(map(float, i)) for i in list(csv.reader(open(loc)))]


def read_points(loc: str) -> List[List[float]]:
    """Funkcja wczytująca dane wykresu.

    Parameters
    ----------
    loc : str
        Nazwa pliku.

    Returns
    -------
    List[List[float]]
        Tablica punktów wykresu.

    """
    ret = read_file(loc)
    xs = [i[0] for i in ret]
    ys = [i[1] for i in ret]
    return [xs, ys]


def read_moments(loc: str) -> List[float]:
    """Funkcja wczytująca momenty NIFS3.

    Parameters
    ----------
    loc : str
        Nazwa pliku.

    Returns
    -------
    List[float]
        Tablica momentów NIFS3.

    """
    return list(map(float, list(csv.reader(open(loc)))[0]))


def read_projects() -> List[List[str]]:
    """Funkcja wczytująca dane o istniejących projektach.

    Returns
    -------
    List[str]
        Lista nazw projektów.

    """
    return list(csv.reader(open("../projects/projects.csv")))
