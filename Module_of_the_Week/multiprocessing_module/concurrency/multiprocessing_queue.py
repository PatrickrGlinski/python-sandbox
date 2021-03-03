# multiprocessing_queue.py
#
# - Passing Messages to Processes -
# A common use of multiple processes
# is to divide a job up among several
# workers to run in parallel.
# Multiple processes usually need to
# communicate between eachother.
# The Queue class provides a simple
# way to communicate between processes.
#
# Any object that can be serialized with
# pickle can pass through a Queue.

import multiprocessing


class MySimpleClass:

    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print('Doing something in {} for {}!'.format(
            proc_name, self.name
        ))


def worker(q):
    obj = q.get()
    obj.do_something()


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue,))
    p.start()

    queue.put(MySimpleClass('Simple Pat'))

    # Wait for the worker to finish
    queue.close()
    queue.join_thread()
    p.join()

# OUTPUT #
# Doing something in Process-1 for Simple Pat!
#

# Notes:
#  We pass a single message
#  to a single worker, then
#  the main process waits for
#  the worker to finish.
#



