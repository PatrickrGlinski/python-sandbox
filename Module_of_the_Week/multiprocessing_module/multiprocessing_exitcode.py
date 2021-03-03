# multiprocessing_exitcode.py
#
# - Process Exit Status -
# The status code produced when
# the process exits can be accessed
# by using the exitcode attribute.

# Multiprocessing Exit Codes
#  _________________________________________
# | Code |    Meaning                       |
# | == 0 | No Error was produced.           |
# | > 0  | process has an error, w/ code    |
# | < 0  | process kill w/ signal -1 * code |
# |_________________________________________|

import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)


def exit_ok():
    return


def return_value():
    return 1


def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)


if __name__ == '__main__':
    jobs = []

    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated
    ]

    for f in funcs:
        print('Starting process for', f.__name__)
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print('{:>15}.exitcode = {}'.format(j.name, j.exitcode))



##### CONSOLE OUTPUT #####
#
# Starting process for exit_error
#     Starting process for exit_ok
#     Starting process for return_value
#     Starting process for raises
#     Starting process for terminated
#     exit_error.exitcode = 1
#     exit_ok.exitcode = 0
# Process raises:
# Traceback (most recent call last):
# File "/usr/local/Cellar/python@...
# self.run()
# File "/usr/local/Cellar/python@...
# self._target(*self._args, **self._kwargs)
# File "/Users/glinsp/hub......
# raise RuntimeError('There was an error!')
# RuntimeError: There was an error!
# return_value.exitcode = 0
# raises.exitcode = 1
#
# terminated.exitcode = -15


# Notes:
#  Processes that raise an exception
#  automatically get an exitcode of 1.
#

