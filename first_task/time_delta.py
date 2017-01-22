#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from datetime import timedelta


def time_delta_converter(time_str):
    """Convert  the time delta string to integer seconds.

    Supported time units: s – seconds, m – minute, h – hour, d – day,
    with seconds being default unit and one being default value.

    Args:
        time_str (str): time delta specifier

    Returns:
        int: time interval in seconds

    Raises:
        ValueError: If time_str format is unsupported

    Examples:
        >>> time_delta_converter('30s')
        30

        >>> time_delta_converter('h')
        3600

        >>> time_delta_converter('15')
        15

        >>> time_delta_converter('30seconds')
        Traceback (most recent call last):
        ...
        ValueError: Incorrect input string format.
    """
    result = time_delta_converter.template.match(time_str)
    if not result or not any(result.groups()):
        raise ValueError('Incorrect input string format.')
    unit = next((k for k, v in result.groupdict().iteritems() if v and k != 'value'), 'seconds')
    value = float(result.groupdict()['value'] or 1)
    return int(round(timedelta(**{unit: value}).total_seconds()))


time_delta_converter.template = re.compile(
    r'^(?P<value>\d*\.?\d*)?((?P<days>d)|(?P<hours>h)|(?P<minutes>m)|(?P<seconds>s))?$')

if __name__ == '__main__':
    print time_delta_converter('1s')
