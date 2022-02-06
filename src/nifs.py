"""
nifs.py
====================================
Moduł odpowiedzialny za wyznaczanie naturalnej interpolacyjnej funkcji sklejanej trzeciego stopnia.
"""

from typing import List

def nifs3_m(x: List[float], y: List[float] ) -> List[float]:
    """Funkcja generująca wartości momentów NIFS3.

    Parameters
    ----------
    x : List[float]
        Wartości na osi X.
    y : List[float]
        Wartości na osi Y.

    Returns
    -------
    List[float]
        Momenty NIFS3.

    """
    tmp = lambda x1, x2, y1, y2: (y2-y1) / (x2-x1)
    tmp2 = lambda x1, x2, x3, y1, y2, y3: (tmp(x2, x3, y2, y3)-tmp(x1, x2, y1, y2)) / (x3-x1)
    n = len(x)-1
    h = [0.0] + [x[i]-x[i-1] for i in range(1, n+1)]
    lam = [0.0] + [h[i] / (h[i]+h[i+1]) for i in range(1, n)]
    d = [0.0] + [6.0*tmp2(x[i], x[i+1], x[i+2], y[i], y[i+1], y[i+2]) for i in range(0, n-1)]

    q = [0.0]
    p = [0.0]
    u = [0.0]
    for i in range(1, n):
        p.append(lam[i]*q[i-1] + 2)
        q.append((lam[i]-1) / p[i])
        u.append((d[i] - lam[i]*u[i-1]) / p[i])
    
    M = [0.0 for i in range(n+1)]
    M[n-1] = u[n-1]
    for k in range(2, n-1):
        i = n-k
        M[i] = u[i] + q[i]*M[i+1]
    
    return M


def nifs3_v(x: List[float], y: List[float], M: List[float], x0: float, x1: float, nn: int ) -> List[List[float]]:
    """Funkcja generująca wykres NIFS3.

    Parameters
    ----------
    x : List[float]
        Wartości na osi X.
    y : List[float]
        Wartości na osi Y.
    M : List[float]
        Wartości momentów NIFS3.
    x0 : float
        Początek przedziału.
    x1 : float
        Koniec przedziału.
    nn : int
        Liczba obliczonych wartości NIFS3.

    Returns
    -------
    List[List[float]]
        Punkty NIFS3 w formacie [[x0,x1,x2,...][y0,y1,y2,...]].

    """
    h = [0.0] + [x[i]-x[i-1] for i in range(1, len(x))]
    f1 = lambda xx, ii: (M[ii-1]*((x[ii]-xx)**3)/6 + M[ii]*((xx-x[ii-1])**3)/6) / h[ii]
    f2 = lambda xx, ii: ((y[ii-1]-M[ii-1]*(h[ii]**2)/6)*(x[ii]-xx) + (y[ii]-M[ii]*(h[ii]**2)/6)*(xx-x[ii-1])) / h[ii]
    f3 = lambda xx, ii: f1(xx, ii) + f2(xx, ii)

    rety = []
    retx = []
    it = 1
    for i in range(0, nn+1):
        ax = x0 + (x1-x0)*(i/nn)
        if i == nn:
            ax = x1
        while ax > x[it]:
            it += 1
        retx.append(ax)
        rety.append(f3(ax, it))
    return [retx, rety]


def nifs3_2d(x: List[float], y: List[float], mx: List[float], my: List[float], nn: int ) -> List[List[float]]:
    """Funkcja generująca NIFS3 dla zadanej krzywej z dokładnością do nn+1 punktów.

    Parameters
    ----------
    x : List[float]
        Wartości na osi X.
    y : List[float]
        Wartości na osi Y.
    mx : List[float]
        Wartości momentów NIFS3 dla osi X.
    my : List[float]
        Wartości momentów NIFS3 dla osi Y.
    nn : int
        Liczba punktów nowej krzywej (pomniejszona o 1).

    Returns
    -------
    List[List[float]]
        Krzywa interpolująca krzywą wejściową.

    """
    ll = len(x)
    xn = [float(i) for i in range(ll)]
    return [nifs3_v(xn, x, mx, 0, ll-1, nn)[1], nifs3_v(xn, y, my, 0, ll-1, nn)[1]]
