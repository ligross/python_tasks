#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def generate_from_files(*files):
    """ Eternal generator which outputs passed files in a
    multiplexed file-by-file, line-by-line order.

    Args:
        files (tuple): tuple with file names as strings
        Empty files are allowed

    Yields:
        str: the next line from one of the files
    """
    files_iterators = tuple(open(f) for f in files if os.stat(f).st_size)
    while True:
        for file_iterator in files_iterators:
            try:
                yield next(file_iterator)
            except StopIteration:
                file_iterator.seek(0)
                yield next(file_iterator)

# a simple test code
if __name__ == '__main__':
    root_path = './test_files'
    for line in generate_from_files(*('/'.join((root_path, f)) for f in os.listdir(root_path))):
        print line

