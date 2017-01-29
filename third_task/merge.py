#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import imap


def merge(*iterables):
    """ Merge arbitrary number of sorted iterables. Uses k-way merging algorithm.

    Args:
        *iterables (tuple of iterables): an arbitrary number of iterables each of sorted numbers,
        Empty iterables and no args allowed.

    Yields:
        int: the next value of merged input iterables in the sorted order

    Examples:
        >>> list(merge((1, 2, 3), (0, 1), (5, 7)))
        [0, 1, 1, 2, 3, 5, 7]

        >>> list(merge())
        []

        >>> list(merge([1, 3], (0,)))
        [0, 1, 3]
    """
    iterators = []
    for iterator in imap(iter, iterables):
        try:
            iterators.append([iterator.next(), iterator.next])
        except StopIteration:
            pass

    while iterators:
        iterators.sort(key=lambda x: x[0])
        min_value, next_value = iterators[0]
        yield min_value
        try:
            iterators[0][0] = next_value()
        except StopIteration:
            iterators.pop(0)