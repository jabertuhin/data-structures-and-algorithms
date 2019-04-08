from unittest import TestCase

from data_structures import right_shift


class TestRightShift(TestCase):
    def test_right_shift(self):
        a = [i for i in range(1, 11)]
        b = right_shift(a[:])

        self.assertListEqual([a[-1]] + a[0:-1], b)

    def test_in_place_shifting(self):
        a = [1, 2, 3, 4, 5]
        right_shift(a)
        shiftedA = [5, 1, 2, 3, 4]

        self.assertListEqual(shiftedA, a)

    def test_empty_array(self):
        a = right_shift([])

        self.assertListEqual([], a)

    def test_array_with_one_element(self):
        a = [5]
        b = right_shift(a[:])

        self.assertListEqual([a[-1]] + a[0:-1], b)

    def test_array_with_multiple_type(self):
        a = [-1, 0, 3.1416, "hello world", object(), b'bytes']
        b = right_shift(a[:])

        self.assertListEqual([a[-1]] + a[0:-1], b)
