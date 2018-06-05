from __future__ import print_function

import threading
try:
    import queue
except ImportError:
    import Queue as queue

table = queue.Queue(5)
single_lock = threading.Lock()


class Baker(threading.Thread):
    def __init__(self, name, total):
        super(Baker, self).__init__()
        self.name = name
        self.total = total

    def run(self):
        global table

        # while True:
        for x in range(self.total):
            bread = "bread-{}".format(x)
            try:
                table.put(bread, block=True, timeout=3)
                single_lock.acquire()
                print("[{:^10}]: {} baked".format(self.name, bread))
                single_lock.release()
            except queue.Full:
                single_lock.acquire()
                print("[{:^10}]: Table is full".format(self.name))
                single_lock.release()

        print("[{:^10}]: Exited".format(self.name))


class Eater(threading.Thread):
    def __init__(self, name):
        super(Eater, self).__init__()
        self.name = name

    def run(self):
        global table

        while True:
            single_lock.acquire()
            print("[{:^10}]: Try to get bread".format(self.name))
            single_lock.release()

            try:
                bread = table.get(block=True, timeout=3)
                single_lock.acquire()
                print("[{:^10}]: Eats: {}".format(self.name, bread))
                single_lock.release()

                table.task_done()
            except queue.Empty:
                # Actually thread still running until 'break'
                break


if __name__ == "__main__":
    print("[{:^10}]: Started".format("Main"))

    for i in range(5):
        t = Eater("Eater-{}".format(i))
        t.start()

    baker = Baker("Baker", 100)
    baker.start()
    # Main process will not block
    # if comment out the line below
    baker.join()

    # Will block until all item
    # in the queue processed
    table.join()
    print("[{:^10}]: Exited".format("Main"))

