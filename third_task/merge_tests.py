#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import unittest

from merge import merge


class MergeTests(unittest.TestCase):
    """Tests for `merge.py`."""
    message = '`merge` should be returned {} as output value, but {} returned'

    def test_arbitrary_iterators(self):
        """Are arbitrary number of iterators with random length processed as expected?"""
        iterators = [sorted(random.sample(range(10), random.randint(1, 7))) for _ in range(1, random.randint(5, 10))]
        expected_result = sorted(reduce(lambda x, y: x + y, iterators))
        result = list(merge(*iterators))
        self.assertListEqual(result, expected_result, msg=self.message.format(expected_result, result))

    def test_empty_iterator(self):
        """Is passed empty iterator as one of the arguments processed correctly?"""
        tuple1, tuple2, tuple3 = (7, 10, 11, 11), (), (1, 1, 2, 3, 5)
        expected_result = sorted(tuple1 + tuple2 + tuple3)
        result = list(merge(tuple1, tuple2, tuple3))
        self.assertListEqual(result, expected_result, msg=self.message.format(expected_result, result))

    def test_no_args(self):
        """Did we get an empty sequence in case when no arguments were passed?"""
        result = list(merge())
        self.assertListEqual(result, [], self.message.format([], result))


if __name__ == '__main__':
    unittest.main()
