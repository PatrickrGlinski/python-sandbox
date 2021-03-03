# multiprocessing_simpleargs.py
#
# Spawn a process w/ args to tell it what work to do.
#
# In order to pass args to a multiprocessing Process
# the arguments must be able to be serialized using
# pickle.


import multiprocessing

def worker(num):
    """thread worker function"""
    print('Worker: ', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()


## OUTPUT ##
# Worker:  3
# Worker:  0
# Worker:  4
# Worker:  1
# Worker:  2

