#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from time_delta import time_delta_converter


class TimeDeltaConverterTests(unittest.TestCase):
    """Tests for `time_delta_converter.py`."""
    message = 'time_delta_converter("{}") should be returned {} as output value, but {} returned'

    def test_default_units(self):
        """Are the numbers without time units calculated in seconds by default?"""
        for seconds in xrange(0, 100, 20):
            result = time_delta_converter(str(seconds))
            self.assertEquals(result, seconds, msg=self.message.format(seconds, seconds, result))

    def test_default_value(self):
        """Is one considered as default value if only the time unit passed?"""
        time_units_defaults = {'d': 60 * 60 * 24, 'h': 60 * 60, 'm': 60, 's': 1}
        for time_unit, default_value in time_units_defaults.items():
            result = time_delta_converter(time_unit)
            self.assertEquals(result, default_value, msg=self.message.format(time_unit, default_value, result))

    def test_time_unit(self):
        """Is  the time delta with units returned correctly?"""
        test_data = {'0s': 0, '10s': 10, '70.5s': 71, '100.4s': 100,
                     '0m': 0, '4m': 240, '5.5m': 330, '10.7m': 642,
                     '0h': 0, '2h': 7200, '4.4h': 15840, '101h': 363600,
                     '0d': 0, '1d': 86400, '4.6d': 397440, '75.2d': 6497280,
                     '15m1.2s': 901, '2d3m4s': 172984, '4h3': 14403, 'm3s': 63}
        for test_input in test_data:
            result = time_delta_converter(test_input)
            self.assertEquals(result, test_data[test_input], self.message.format(test_input, test_data[test_input], result))

    def test_exceptions(self):
        """Are incorrect input values processed correctly?"""
        test_data = ('10seconds', '1y', 'year', '', '1d2d', '1.5d3.3h2s3s')
        for test_input in test_data:
            with self.assertRaises(ValueError, msg='ValueError is not raised with {} as input value'.format(test_input)):
                time_delta_converter(test_input)

if __name__ == '__main__':
    unittest.main()
