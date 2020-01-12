#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: ossdev

import unittest
from ossdev import Vector


class VectorTest(unittest.TestCase):
    """Simple vector tests"""

    def __init__(self, *args, **kwargs):
        super(VectorTest, self).__init__(*args, **kwargs)

    def test_from_arr(self):
        u = Vector.from_arr([0, 1, 2, 3])
        self.assertEqual(u.get(), [0, 1, 2, 3])

    def test_from_size(self):
        u = Vector.from_size(3)
        self.assertEqual(u.get(), [0, 0, 0])

        v = Vector.from_size(0)
        self.assertEqual(v.get(), [])

    def test_set(self):
        u = Vector([1, 2, 3])
        self.assertEqual(u.get(), [1, 2, 3])

        u.set([4, 5, 6])
        self.assertEqual(u.get(), [4, 5, 6])

    def test_len(self):
        u = Vector.from_size(0)
        v = Vector.from_size(100)

        self.assertEqual(len(u), 0)
        self.assertEqual(len(v), 100)

    def test_repr(self):
        u = Vector.from_size(0)
        self.assertEqual(repr(u), "Vector([])")

        u = Vector([1, 4])
        self.assertEqual(repr(u), "Vector([1, 4])")

    def test_cmp(self):
        u, v = Vector([1, 2, 3]), Vector([1, 2, 3])

        self.assertEqual(u.__cmp__(v), 0)
        self.assertEqual(v.__cmp__(u), 0)

        u, v = Vector([]), Vector([1])
        self.assertEqual(u.__cmp__(v), -1)
        self.assertEqual(v.__cmp__(u), 1)

        u, v = Vector([1, 2, 3]), Vector([1, 2, 5])
        self.assertEqual(u.__cmp__(v), -1)
        self.assertEqual(v.__cmp__(u), 1)

    def test_neg(self):
        u = Vector([1, 2, 3])
        self.assertEquals((-u).get(), [-1, -2, -3])

    def test_reversed(self):
        u = Vector([1, 2, 3])
        self.assertEqual(reversed(u).get(), [3, 2, 1])

    def test_add(self):
        a = Vector([0, 1, 2, 3])
        b = Vector([3, 2, 1, 0])

        self.assertEqual((a + b).get(), [3, 3, 3, 3])

    def test_sub(self):
        a = Vector([1, 2, 3, 4])
        b = Vector([0, 1, 1, 1])

        self.assertEqual((a - b).get(), [1, 1, 2, 3])

    def test_mul(self):
        a = Vector([1, 2, 3, 4])

        self.assertEqual((a * 5).get(), [5, 10, 15, 20])

    def test_xor(self):
        a = Vector([1, 3, 7])

        self.assertEqual((a ^ 3).get(), [2, 0, 4])

    def test_length(self):
        test_cases = [
            (Vector([1, 1]), 2 ** 0.5),
            (Vector([15]), 15),
            (Vector([1, 2, 3]), 14 ** 0.5),
        ]

        for vector, length in test_cases:
            self.assertEqual(vector.length(), length)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
