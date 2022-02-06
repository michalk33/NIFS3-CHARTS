"""
test1.py
====================================
Testy.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath("../src/"))

import nifs
import saving
import reading
import events


class tests(unittest.TestCase):

    def test_nifs3m(self):
        """Sprawdza typ wynikowy funkcji wyznaczającej momenty NIFS3."""
        tmpx = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        tmpy = [1.1, 3.3, 2.8, -6.7, 2.3, 10.0]
        tmpm = nifs.nifs3_m(tmpx, tmpy)
        for i in tmpm:
            assert type(i) == float
        assert len(tmpm) == len(tmpx)

    def test_nifs3v(self):
        """Sprawdza typ wynikowy funkcji wyznaczającej wartości NIFS3."""
        tmpx = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        tmpy = [1.1, 3.3, 2.8, -6.7, 2.3, 10.0]
        tmpm = nifs.nifs3_m(tmpx, tmpy)
        ret = nifs.nifs3_v(tmpx, tmpy, tmpm, 0.0, 5.0, 1000)
        assert len(ret) == 2
        assert len(ret[0]) == 1001
        assert len(ret[1]) == 1001
        for i in ret[0]:
            assert type(i) == float
        for i in ret[1]:
            assert type(i) == float

    def test_nifs32d(self):
        """Sprawdza typ wynikowy funkcji wyznaczającej nową krzywą."""
        tmpx = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        tmpy = [1.1, 3.3, 2.8, -6.7, 2.3, 10.0]
        tmpmx = nifs.nifs3_m(tmpx, tmpx)
        tmpmy = nifs.nifs3_m(tmpx, tmpy)
        ret = nifs.nifs3_2d(tmpx, tmpy, tmpmx, tmpmy, 10000)
        assert len(ret) == 2
        assert len(ret[0]) == 10001
        assert len(ret[1]) == 10001
        for i in ret[0]:
            assert type(i) == float
        for i in ret[1]:
            assert type(i) == float

    def test_svpoints(self):
        """Sprawdza zapis i odczyt punktów wykresu."""
        tmpx = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        tmpy = [1.1, 3.3, 2.8, -6.7, 2.3, 10.0]
        tmpp = [tmpx, tmpy]
        saving.save_points("tmp.csv", tmpp)
        ret = reading.read_points("tmp.csv")
        assert len(ret) == 2
        assert len(ret[0]) == 6
        assert len(ret[1]) == 6
        for i in ret[0]:
            assert type(i) == float
        for i in ret[1]:
            assert type(i) == float

    def test_svmoments(self):
        """Sprawdza zapis i odczyt momentów NIFS3."""
        tmpm = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
        saving.save_moments("tmp2.csv", tmpm)
        ret = reading.read_moments("tmp2.csv")
        assert len(ret) == 6
        for i in ret:
            assert type(i) == float

    def test_checknp(self):
        """Sprawdza funkcję kontrolującą tworzenie nowego projektu."""
        assert events.check_new_project("No file chosen", "") == 0
        assert events.check_new_project("No file chosen", "Project1") == 0
        assert events.check_new_project("points.csv", "") == 0

    def test_checknc(self):
        """Sprawdza funkcję kontrolującą tworzenie nowego wykresu."""
        assert not events.check_new_chart("Project1", "A5")
        assert not events.check_new_chart("Project1", "3")


unittest.main()
