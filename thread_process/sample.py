# threading test
# Alex Boschmans
# www.boschmans.net
# January 2010

#
# IMPORT SECTION
#
import threading, Queue

#
# Variables setup
#
THREAD_LIMIT = 3  # This is how many threads we want
jobs = Queue.Queue(5)  # This sets up the queue object to use 5 slots
singlelock = threading.Lock()  # This is a lock so threads don't print trough each other (and other reasons)

# Our list of work todo
inputlist = [(5, 5), (10, 4), (78, 5), (87, 2), (65, 4), (10, 10), (65, 2), (88, 95), (44, 55), (33, 3)]


#
# This is called from the main function
# It spawns the threads, fills up the queue with work items that the threads will use
# And then waits for the threads to finish
# This could use some more try:except code...
#


#
# Main thread class - based on threading.Thread
# This class is cloned/used as a thread template to spawn those threads.
# The class has a run function that gets a job out of the jobs queue
# And lets the queue object know when it has finished.
#
class workerbee(threading.Thread):
    def run(self):
        # run forever
        while 1:
            # Try and get a job out of the queue
            try:
                job = jobs.get(True, 1)
                singlelock.acquire()  # Acquire the lock
                print "Multiplication of {0} with {1} gives {2}".format(job[0], job[1], (job[0] * job[1]))
                singlelock.release()  # Release the lock
                # Let the queue know the job is finished.
                jobs.task_done()
            except:
                break  # No more jobs in the queue


#
# Executes if the program is started normally, not if imported
#
if __name__ == '__main__':
    # Call the mainfunction that sets up threading.
    print("------main start-------")

    print "Inputlist received..."
    print inputlist

    # Spawn the threads
    print "Spawning the {0} threads.".format(THREAD_LIMIT)
    for x in xrange(THREAD_LIMIT):
        print "Thread {0} started.".format(x)
        # This is the thread class that we instantiate.
        workerbee().start()

    # Put stuff in queue
    print "Putting stuff in queue"
    for i in inputlist:
        # Block if queue is full, and wait 5 seconds. After 5s raise Queue Full error.
        try:
            jobs.put(i, block=True, timeout=5)
        except:
            singlelock.acquire()
            print "The queue is full !"
            singlelock.release()

    # Wait for the threads to finish
    singlelock.acquire()  # Acquire the lock so we can print
    print "Waiting for threads to finish."
    singlelock.release()  # Release the lock
    jobs.join()  # This command waits for all threads to finish.

    print("------main end-------")
