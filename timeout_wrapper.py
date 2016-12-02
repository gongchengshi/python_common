from multiprocessing import TimeoutError
import signal


class Timeout:
    def __init__(self, seconds=1, error=TimeoutError('Timeout')):
        self._seconds = seconds
        self._error = error

    def handle_timeout(self, signum, frame):
        raise self._error

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self._seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)


