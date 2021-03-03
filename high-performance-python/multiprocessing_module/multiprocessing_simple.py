# multiprocessing_simple.py

import multiprocessing


def worker():
    """Worker Function"""
    print('Worker')


if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()


# Each process is competing for access
# to the output stream.

# OUTPUT #
# Worker
# Worker
# Worker
# Worker
# Worker


