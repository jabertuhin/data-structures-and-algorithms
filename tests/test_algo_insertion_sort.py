import math
from unittest import TestCase

from algorithms import insertion_sort


class TestInsertionSort(TestCase):
    def test_insertion_sort(self):
        a = [i for i in range(10, 0, -1)]
        b = insertion_sort(a[:])

        self.assertListEqual(sorted(a), b)

    def test_in_place_sorting(self):
        a = [4, 2, 1, 3, 5]
        insertion_sort(a)

        self.assertListEqual([1, 2, 3, 4, 5], a)

    def test_empty_array(self):
        a = []
        b = insertion_sort(a[:])

        self.assertListEqual(b, a)

    def test_one_element_array(self):
        a = [5]
        b = insertion_sort(a[:])

        self.assertListEqual(a, b)

    def test_float_type(self):
        a = [10.45, 3.1416, -0.1, -0.5, 1.0, 1.2, 1.200000000000000001, math.pi, -905.34534897349857,
             9.5555555555555556, 9.56]
        b = insertion_sort(a[:])

        self.assertListEqual(sorted(a), b)

    def test_multiple_type(self):
        a = [math.pi, 3.1416, 10, 56, 99, 09.56, -0.9999999999999999, 1]
        b = insertion_sort(a[:])

        self.assertListEqual(sorted(a), b)

    def test_large_array(self):
        a = [i for i in range(10000, 1, -2)]
        b = insertion_sort(a[:])

        self.assertListEqual(sorted(a), b)
