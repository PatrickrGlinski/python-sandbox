# multiprocessing_daemon.py
#
# - Daemon Processes -
# By default, main program will not exit
# until all of the children have exited.
# Sometimes we want to start a background
# process that runs w/o blocking the main
# program.
# ex: heartbeat monitoring tool service

import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    # force 'flush' the standard out buffer
    sys.stdout.flush()
    time.sleep(2)
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ', p.name, p.pid)
    sys.stdout.flush()
    print('Exiting: ', p.name, p.pid)
    sys.stdout.flush()


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
    n.daemon = False  # Default is False

    d.start()
    time.sleep(1)
    n.start()


#   OUTPUT   #
# Starting: daemon 36250
# Starting: non-daemon 36256
# Exiting : non-daemon 36256

# Notes:
#  output doesnt include 'Exiting' daemon process
#  since all of the non-daemon processes exit
#  before the daemon process wakes up from its
#  two second sleep.

#  The daemon process is termed automatically
#  before the main program exits. This avoids
#  leaving orphaned processes running.
#
#  Use ps (process status) command to search for
#  the 'Starting: daemon' pid.
