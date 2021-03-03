# multiprocessing_daemon_join.py
#
# - Waiting for Processes -
# To wait until a process has completed
# its work and exited, use the join()
# method.
#

import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('Starting: ', name)
    time.sleep(2)
    print('Exiting:', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('Starting: ', name)
    print('Exiting: ', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join(1)
    print('d.is_alive()', d.is_alive())
    n.join()


## OUTPUT ##
# Starting:  daemon
# Starting:  non-daemon
# Exiting:  non-daemon
# d.is_alive() True

# Notes:
#  Since the main process waits
#  for the daemon to exit using
#  join(), the 'Exiting' message
#  is printed this time.
#
#  Join blocks indefinitely by
#  default. We can also pass a
#  timeout argument to specify the
#  number of seconds to wait for the
#  process to become inactive.
#  If the process does not complete within
#  the timeout period, join() returns anyways

