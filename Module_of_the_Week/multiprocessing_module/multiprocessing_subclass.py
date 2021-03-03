# multiprocessing_subclass.py
#
# Although the simplest way to
# start a job in a separate
# process is to use Process
# and  pass a target function,
# it is also possible to use a
# customer subclass.
#

import multiprocessing

# Worker is a subclass of Process class
class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()


##### OUTPUT #####
# In Worker-1
# In Worker-2
# In Worker-3
# In Worker-4
# In Worker-5

# Notes:
#  The derived class should
#  override run() to do its
#  work.
#

