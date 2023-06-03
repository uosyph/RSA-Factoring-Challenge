#!/usr/bin/python3
import sys
import ctypes
from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function):
    """Return `real`, `sys` and `user` elapsed time."""

    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return f"\nreal: {end_time - start_time}\n\
    user: {end_resources.ru_utime - start_resources.ru_utime}\n\
    sys: {end_resources.ru_stime - start_resources.ru_stime}"


def print_factors():
    func = ctypes.CDLL("./lib_factors_functions.so")
    func.trial_division.argtypes = [ctypes.c_long]

    with open(sys.argv[1], 'r') as f:
        line = f.readline()
        while line != '':
            num = int(line)
            func.trial_division(num)
            line = f.readline()
