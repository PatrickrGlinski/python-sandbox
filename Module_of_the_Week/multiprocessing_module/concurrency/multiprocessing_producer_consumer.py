# multiprocessing_producer_consumer.py
#
# Manage workers consuming data
# from a JoinableQueue and passing
# results back to the parent process.
#
# - Poison Pill Technique -
# Setup the real tasks, the main program
# adds one 'stop' value per worker to
# the job queue.
# When a worker encounters the special value
# it breaks out of its processing loop.
#
# The main process uses the task queues join()
# method to wait for all of the tasks to finish
# before processing the results
#

import multiprocessing
import time


class Consumer(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison Pill means shutdown
                print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            print('{}: {}'.format(proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


class Task:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        time.sleep(0.1)  # Pretend to take time to do the work
        return '{self.a} * {self.b} = {product}'.format(
            self=self, product=self.a * self.b)

    def __str__(self):
        return '{self.a} * {self.b}'.format(self=self)


if __name__ == '__main__':
    # Establish the communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    # - Start Consumers -
    # Get the number of cpus in the system
    num_consumers = multiprocessing.cpu_count() * 2

    print('Creating {} consumers'.format(num_consumers))  # 24 consumers

    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]
    # Start the child processes of Consumer class
    for w in consumers:
        w.start()

    # Enqueue jobs
    num_jobs = 10
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()

    # Start Printing results
    while num_jobs:
        result = results.get()
        print('Result: ', result)
        num_jobs -= 1


# Notes:
#  Queue Class -
#   Process shared queue implemented using
#   a pipe and a few locks/semaphores.
#   When a process first puts an item on
#   the
#  JoinableQueue Class -
#   A Queue with additional task_done()
#   and join() methods.
#    - task_done() indicate that a formerly enqueued
#      is complete. Used by queue consumers.
#
#
