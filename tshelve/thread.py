import threading
from collections import deque


class HiThread(threading.Thread):
    inputter = deque(maxlen=20)
    outputter = deque(maxlen=20)
    event = threading.Event()

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            try:
                function, args, kwargs = self.inputter.pop()
            except IndexError:
                continue
            self.outputter.append(function(*args, **kwargs))
            self.event.set()


def get_in_thread(tup):
    HiThread.inputter.append(tup)
    HiThread.event.clear()
    HiThread.event.wait()
    return HiThread.outputter.pop()


HiThread().start()
