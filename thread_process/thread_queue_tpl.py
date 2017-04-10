from __future__ import print_function

import threading

try:
    import queue
except ImportError:
    import Queue as queue

table = queue.Queue()


class Eater(threading.Thread):
    def __init__(self, name):
        super(Eater, self).__init__()
        self.name = name

    def run(self):
        while True:
            print("[{:^10}]: Try to get bread".format(self.name))
            try:
                bread = table.get(block=True, timeout=3)
                print("[{:^10}]: Eats: {}".format(self.name, bread))
                table.task_done()

            except queue.Empty:
                # Actually thread still running until 'break'
                break

if __name__ == "__main__":
    print("[{:^10}]: Started".format("Main"))

    for i in range(5):
        t = Eater("Eater-{}".format(i))
        t.start()

    for i in range(100):
        table.put("bread-{}".format(i))

    table.join()  # Block until all items processed
    print("[{:^10}]: Exited".format("Main"))
