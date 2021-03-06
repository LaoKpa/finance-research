#!/usr/bin/env pypy
###############################################################################
#
# A module containing some common and helpful utility functions for processing
# and converting TAQ data.
#
# Copyright (C) 2013, Jonathan Gillett
# All rights reserved.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
import time
import datetime


def convert_mil(ms):
    """Converts a time in milliseconds from midnight format into a
    compatible time format of HH:MM:SS, currently the time provided
    in milliseconds is floored to avoid having times in the future.
    """
    # Floor the results to avoid rounding errors for seconds entries
    try:
        ms = int(float(ms))
        hour = (ms / 3600000) % 24
        min = (ms / 60000) % 60
        sec = (ms / 1000) % 60

        return datetime.time(hour, min, sec)
    except ValueError:
        return None


def convert_sec(sec):
    """Converts a time in seconds from midnight format into compatible
    time format of HH:MM:SS
    """

    # Ensure the value is an integer
    try:
        sec = int(float(sec))
        hour = (sec / 3600) % 24
        min = (sec / 60) % 60
        sec = sec % 60

        return datetime.time(hour, min, sec)
    except ValueError:
        return None


def convert_str(time):
    """Convers a time that is a string of the format HH:MM:SS into a compatible
    time format object of HH:MM:SS
    """
    try:
        return datetime.datetime.strptime(time, '%H:%M:%S').time()
    except ValueError:
        return None


def float_to_int(value):
    """Converts a string representation of a float value to an int
    FLOORING the value (e.g. 2.99 becomes 2)
    """
    try:
        return int(float(value))
    except ValueError:
        return None


def market_hours(time):
    """Determines if the time provide is within the market operating hours,
    which are usually between 9:30 and 16:00.

    :param time: A datetime.time object of the time to check
    """
    open = datetime.time(9, 30, 00)
    close = datetime.time(16, 00, 00)

    try:
        if time < open or time > close:
            return False

        return True
    except:
        return False


def time_delta(before, after):
    """Determines the number of seconds difference between two times.

    :param before: A datetime.time object of the time before
    :param after: A datetime.time object of the time after
    """
    # Create a placeholder date
    date = datetime.datetime(1984, 1, 1)

    # Get the time delta between the two times
    before_time = date.combine(date, before)
    after_time = date.combine(date, after)
    return (after_time - before_time).seconds


def add_seconds(time, seconds):
    """Adds the specified number of seconds to the time provided and returns a
    datetime.time object

    :param time: A datetime.time object of the time to add seconds to.
    :param seconds: An integer, the number of seconds to add
    """
    # Create a placeholder date
    date = datetime.datetime(1984, 1, 1)

    # Get the new time
    orig_time = date.combine(date, time)
    return (orig_time + datetime.timedelta(0, seconds)).time()
