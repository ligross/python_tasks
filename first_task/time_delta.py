#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from datetime import timedelta

UNITS = {'d': 'days', 'h': 'hours', 'm': 'minutes', 's': 'seconds'}
PARSE_TEMPLATE = re.compile(r'(?P<value>\d*\.?\d*)?(?P<unit>d|h|m|s)?')
FORMAT_TEMPLATE = re.compile(r'^({0})+$'.format(PARSE_TEMPLATE.pattern))


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

        >>> time_delta_converter('1.5d15s')
        129615

        >>> time_delta_converter('30seconds')
        Traceback (most recent call last):
        ...
        ValueError: Incorrect input string format.
    """
    if not time_str or not FORMAT_TEMPLATE.match(time_str):
        raise ValueError('Incorrect input string format.')

    values_units = {}
    for match in PARSE_TEMPLATE.finditer(time_str):
        if not any(match.groups()):
            break
        value, unit = match.groupdict().values()
        unit = UNITS.get(unit, 'seconds')
        if values_units.has_key(unit):
            raise ValueError('Duplicated unit specifier found.')
        values_units[unit] = float(value or 1)
    return int(round(timedelta(**values_units).total_seconds()))
