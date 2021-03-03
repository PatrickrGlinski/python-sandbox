# multiprocessing_terminat.py
#
# - Terminating Processes -
# If a process is hung or deadlocked
# it can be useful to be able to kill
# the process forcibly.
# Calling terminate() on a process object
# kills the child process.

import multiprocessing
import time


def slow_worker():
    print('Starting Worker')
    time.sleep(0.1)
    print('Finished Worker')


if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker())
    print('BEFORE: ', p, p.is_alive())

    p.start()
    print('DURING:', p, p.is_alive())

    p.terminate()
    print('TERMINATED:', p, p.is_alive())

    p.join()
    print('JOINED:', p, p.is_alive())

## OUTPUT ##
# BEFORE: <Process(Process-1, initial)> False
# DURING: <Process(Process-1, started)> True
# TERMINATED: <Process(Process-1, started)> True
# JOINED: <Process(Process-1, stopped[SIGTERM])> False

# Notes:
#  It is important to join() the process after
#  terminating it in order to give the process
#  management code time to update the status of
#  the object to reflect termination

