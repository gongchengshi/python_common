import threading
import thread
import signal
import sys


# noinspection PyClassHasNoInit
class GlobalInterruptableThreadHandler:
    threads = []
    initialized = False

    @staticmethod
    def initialize():
        signal.signal(signal.SIGTERM, GlobalInterruptableThreadHandler.sig_handler)
        signal.signal(signal.SIGINT, GlobalInterruptableThreadHandler.sig_handler)
        GlobalInterruptableThreadHandler.initialized = True

    @staticmethod
    def add_thread(t):
        # Ensures that initialize() only gets called once and only by the main thread.
        # if threading.current_thread().name != 'MainThread':
        #     raise InvalidOperationException("InterruptableThread objects may only be started from the Main thread.")

        if not GlobalInterruptableThreadHandler.initialized:
            GlobalInterruptableThreadHandler.initialize()

        GlobalInterruptableThreadHandler.threads.append(t)

    @staticmethod
    def sig_handler(signum, frame):
        for t in GlobalInterruptableThreadHandler.threads:
            t.stop()

        GlobalInterruptableThreadHandler.threads = []


class InterruptableThread:
    def __init__(self, target=None):
        self._stop_requested = threading.Event()
        self._t = threading.Thread(target=target, args=[self]) if target else threading.Thread(target=self._run_i)
        self._return_value = None
        self._exception = None
        self._exception_info = None

    def _run_i(self):
        try:
            self._return_value = self.run()
        except Exception, ex:
            self._exception = ex
            self._exception_info = sys.exc_info()

    def run(self):
        pass

    def start(self):
        GlobalInterruptableThreadHandler.add_thread(self)
        self._t.start()

    def stop(self):
        self._stop_requested.set()

    def is_stop_requested(self):
        return self._stop_requested.is_set()

    def join(self):
        try:
            while self._t.is_alive():
                self._t.join(timeout=1)
        except (KeyboardInterrupt, SystemExit):
            self._stop_requested.set()
            self._t.join(timeout=5)
            if self._t.is_alive():
                thread.exit()  # Todo: This isn't working yet

    def is_alive(self):
        return self._t.is_alive()

    @property
    def return_value(self):
        return self._return_value

    @property
    def threw_exception(self):
        return self._exception is not None

    @property
    def exception(self):
        return self._exception

    @property
    def exc_info(self):
        return self._exception_info
