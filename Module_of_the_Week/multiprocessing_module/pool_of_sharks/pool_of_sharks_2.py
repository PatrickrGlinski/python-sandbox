#
# 1. In the Parent process, log msgs get routed
#    to the queue, and a thread reads from the queue
#    and writes those messages to a log file.
#
# 2. Another thread writes a continuous stream of log
#    messages.
#
# 3. Finally, we start a process pool, and log a message
#    in one of the child subprocesses.
#

import logging
from threading import Thread
from queue import Queue
from logging.handlers import QueueListener, QueueHandler
from multiprocessing import Pool


def setup_logging():
    """
    Logs get written to a queue. The thread reads
    from that queue and writes messages to a file
    """
    _log_queue = Queue()
    QueueListener(
        _log_queue, logging.FileHandler('out_2.log')).start(), \
    logging.getLogger().addHandler(QueueHandler(_log_queue))

    # Our parent process is running a thread that
    # logs messages
    def write_logs():
        while True:
            logging.error('Hello, I just did something')
    Thread(target=write_logs()).start()


def runs_in_subprocess():
    print("About to log...")
    logging.error("Hello, I did something")
    print("....logged")


if __name__ == '__main__':
    setup_logging()

    # Meanwhile, start a process pool that writes
    # logs. We do this in a loop to make race condition
    # more likely to be triggered.
    while True:
        with Pool() as pool:
            pool.apply(runs_in_subprocess())

