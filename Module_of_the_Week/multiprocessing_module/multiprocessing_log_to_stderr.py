# multiprocessing_log_to_stderr.py

# - Logging -
# When debugging concurrency issues,
# it can be useful to have access
# to the internals of the objects
# provided by multiprocessing.
#
# log_to_stderr() is a module level
# function to enable logging.
# It sets up a logger object using
# logging and adds a handler so that
# log messages are sent to the std err
# channel.
#

import multiprocessing
import logging
import sys


def worker():
    print('Doing some work')
    sys.stdout.flush()


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()


### OUTPUT ###
# [INFO/Process-1] child process calling self.run()
# Doing some work
# [INFO/Process-1] process shutting down
# [DEBUG/Process-1] running all "atexit" finalizers with priority >= 0
# [DEBUG/Process-1] running the remaining "atexit" finalizers
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# [DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
# [DEBUG/MainProcess] running the remaining "atexit" finalizers

# Notes:
#  To manipulate the logger directly
#  (change its level setting or add
#  handlers), use get_logger()
#

def manipulate_logger():
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()


