"""
saving.py
====================================
Moduł odpowiedzialny za zapis danych do pliku.
"""

from typing import List
import csv


def save_points(loc: str, data: List[List[float]]) -> None:
    """Funkcja zapisująca wykres do pliku.

    Parameters
    ----------
    loc : str
        Nazwa pliku.
    data : List[List[float]]
        Dane wykresu.

    Returns
    -------
    None

    """
    dt = [[data[0][i], data[1][i]] for i in range(len(data[0]))]
    csv.writer(open(loc, "w", newline="")).writerows(dt)


def save_moments(loc: str, M: List[float]) -> None:
    """Funkcja zapisująca momenty NIFS3 do pliku.

    Parameters
    ----------
    loc : str
        Nazwa pliku.
    M : List[float]
        Wartości momentów NIFS3.

    Returns
    -------
    None

    """
    csv.writer(open(loc,"w")).writerow(M)


def save_projects(pr: List[str]) -> None:
    """Funkcja zapisująca dane o projektach.

    Parameters
    ----------
    pr: List[str]
        Lista nazw projektów.

    Returns
    -------
    None

    """
    csv.writer(open("../projects/projects.csv", "w", newline="")).writerow(pr)
