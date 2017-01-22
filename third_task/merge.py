#!/usr/bin/python
# -*- coding: utf-8 -*-
import heapq


# Seems to be a cheat method to solve this task because of it`s just a one-line function,
# but the point is that heapq.merge has a true iterative nature and means that it never reads any of the supplied
# sequences all at once and already returns a fair generator.
# Similar sorted(itertools.chain(*iterables)) pull the data into memory all at once because of sorted returns us
# a simple list, so it seems useless to wrap it as generator because of potential problems with really long iterables
# as an input sequence.
def merge(*iterables):
    """ Merge arbitrary number of sorted iterables. Uses heapq.

    Args:
        *iterables (tuple of iterables): an arbitrary number of iterables each of sorted numbers,
        Empty iterables and no args allowed.

    Yields:
        int: the next value of merged input iterables in  the sorted order

    Examples:
        >>> list(merge((1, 2, 3), (0, 1), (5, 7)))
        [0, 1, 1, 2, 3, 5, 7]

        >>> list(merge())
        []

        >>> list(merge([1, 3], (0,)))
        [0, 1, 3]
    """
    return heapq.merge(*iterables)


# Custom function doing the same but without heapq and itertools
def custom_merge(*iterables):
    """ Merge arbitrary number of sorted iterables. Uses k-way merging algorithm.

    Args:
        *iterables (tuple of iterables): an arbitrary number of iterables each of sorted numbers,
        Empty iterables and no args allowed.

    Yields:
        int: the next value of merged input iterables in the sorted order

    Examples:
        >>> list(custom_merge((1, 2, 3), (0, 1), (5, 7)))
        [0, 1, 1, 2, 3, 5, 7]

        >>> list(custom_merge())
        []

        >>> list(custom_merge([1, 3], (0,)))
        [0, 1, 3]
    """
    iterables = map(list, iterables)
    while any(iterable for iterable in iterables):
        ind, min_value = min(((ind, iterable[0]) for ind, iterable in enumerate(iterables) if iterable),
                             key=lambda i: i[1])
        iterables[ind].remove(min_value)
        yield min_value
