#
# Run tasks in a pool of processes to
# improve the parallelism of your program.
#

from multiprocessing import Pool
from os import getpid


def double(i):
    print("Luke, I am your process! ", getpid())
    return i * 2


if __name__ == '__main__':
    with Pool() as pool:
        result = pool.map(double, [1, 2, 3, 4, 5])
        print(result)

## OUTPUT ##
# Luke, I am your process!  30393
# Luke, I am your process!  30395
# Luke, I am your process!  30392
# Luke, I am your process!  30393
# Luke, I am your process!  30391
# [2, 4, 6, 8, 10]
