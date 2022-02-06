"""
events.py
====================================
Moduł odpowiedzialny za obsługę zdarzeń.
"""

from typing import List
import saving as sa
import reading as rd
import nifs as ns
import ploting as pt


def check_new_project(loc: str, name: str) -> int:
    """Funkcja sprawdzająca, czy jest możliwe utworzenie nowego projektu.

    Parameters
    ----------
    loc : str
        Nazwa pliku z danymi.
    name : str
        Nazwa nowego projektu.

    Returns
    -------
    int
        0, jeśli nie można utworzyć projektu.
        1, jeśli wymagane jest potwierdzenie chęci nadpisania projektu.
        2, jeśli można utworzyć projekt.

    """
    if loc == "No file chosen" or name == "":
        return 0
    prnames = rd.read_projects()
    if prnames != [] and (name in prnames[0]):
        return 1
    return 2


def add_new_project(loc: str, name: str) -> bool:
    """Funkcja tworząca nowy projekt.

    Parameters
    ----------
    loc : str
        Nazwa pliku z danymi.
    name : str
        Nazwa nowego projektu.

    Returns
    -------
    bool
        True, jeśli utworzono pomyślnie projekt.
        False, w przeciwnym wypadku.

    """
    try: 
        points = rd.read_points(loc)
        ll = len(points[0])
        xn = [float(i) for i in range(ll)]
        mx = ns.nifs3_m(xn, points[0])
        my = ns.nifs3_m(xn, points[1])
        sa.save_moments("../data/"+name+".mx", mx)
        sa.save_moments("../data/"+name+".my", my)
        sa.save_points("../data/"+name+".pt", points)
        prnames = rd.read_projects()
        if prnames != [] and (not (name in prnames[0])):
            prnames[0].append(name)
            sa.save_projects(prnames[0])
        if prnames == []:
            prnames = [[name]]
            sa.save_projects(prnames[0])
    except Exception as exc:
        return False
    return True


def check_new_chart(name: str, nn: str) -> bool:
    """Funkcja sprawdzająca, czy jest możliwe utworzenie nowego wykresu.

    Parameters
    ----------
    name : str
        Nazwa projektu.
    nn : str
        Liczba punktów nowego wykresu.

    Returns
    -------
    bool
        False, jeśli nie można utworzyć wykresu.
        True, jeśli można utworzyć wykres.

    """
    try:
        mm = int(nn)
    except Exception as exc:
        return False
    prnames = rd.read_projects()
    if mm < 5 or prnames == []:
        return False
    if name in prnames[0]:
        return True
    return False


def save_new_chart(file: str, name: str, nn: str) -> bool:
    """Funkcja tworząca nowy wykres.

    Parameters
    ----------
    file : str
        Nazwa pliku docelowego.
    name : str
        Nazwa projektu.
    nn : str
        Liczba punktów nowego wykresu.

    Returns
    -------
    bool
        False, jeśli nie udało się utworzyć wykresu.
        True, jeśli udało się utworzyć wykres.

    """
    try:
        mm = int(nn)
        points = rd.read_points("../data/"+name+".pt")
        points2 = ns.nifs3_2d(points[0], points[1], rd.read_moments("../data/"+name+".mx"), rd.read_moments("../data/"+name+".my"), mm-1)
        pt.make_plot(points2[0], points2[1])
        pt.save_plot(file, True)
    except Exception as exc:
        return False
    return True


def save_new_chart_d(file: str, name: str, nn: str) -> bool:
    """Funkcja tworząca plik danych nowego wykresu.

    Parameters
    ----------
    file : str
        Nazwa pliku docelowego.
    name : str
        Nazwa projektu.
    nn : str
        Liczba punktów nowego wykresu.

    Returns
    -------
    bool
        False, jeśli nie udało się utworzyć pliku danych wykresu.
        True, jeśli udało się utworzyć plik danych wykresu.

    """
    try:
        mm = int(nn)
        points = rd.read_points("../data/"+name+".pt")
        points2 = ns.nifs3_2d(points[0], points[1], rd.read_moments("../data/"+name+".mx"), rd.read_moments("../data/"+name+".my"), mm-1)
        sa.save_points(file, points2)
    except Exception as exc:
        return False
    return True
