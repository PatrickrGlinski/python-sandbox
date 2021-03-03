# multiprocessing_import_main.py
#
# - Importable Target Functions -
# Extra protection for __main__.
# Due to the way new processes are started,
# child process needs to be able to import
# the script containing the target function.
#

import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import_worker.worker
        )
        jobs.append(p)
        p.start()

# OUTPUT #
# Worker
# Worker
# Worker
# Worker
# Worker
