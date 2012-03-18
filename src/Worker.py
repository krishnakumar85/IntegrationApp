from threading import Thread
from Queue import Queue


class Worker(Thread):
    """
        A daemon thread to execute Sequencer inherited objects.
        Use function assign_work to assign work to this thread.
    """
    def __init__(self):
        Thread.__init__(self)
        self.queue = Queue()
        self.setDaemon(True)

    def assign_work(self, sequencer):
        self.queue.put(sequencer, True)

    def run(self):
        while True:
            work = self.queue.get(True)
            work.execute()
