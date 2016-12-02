#! /usr/bin/python2
import time
import sys
import traceback
from python_common.interruptable_thread import InterruptableThread


def test1():
    class Foo(InterruptableThread):
        def __init__(self):
            InterruptableThread.__init__(self)

        def run(self):
            sys.stdout.write("run started\n")
            sys.stdout.flush()
            while not self.is_stop_requested():
                time.sleep(2)

            sys.stdout.write("run exited\n")
            sys.stdout.flush()

    foo = Foo()
    foo2 = Foo()
    foo.start()
    foo2.start()
    foo.join()
    foo2.join()

    sys.stdout.write("all exited\n")
    sys.stdout.flush()


def test2():
    def run(t):
        sys.stdout.write("run started\n")
        sys.stdout.flush()
        while not t.is_stop_requested():
            time.sleep(2)

        sys.stdout.write("run exited\n")
        sys.stdout.flush()

    t1 = InterruptableThread(run)
    t2 = InterruptableThread(run)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    sys.stdout.write("all exited\n")
    sys.stdout.flush()


def test3():
    class Foo(InterruptableThread):
        def __init__(self):
            InterruptableThread.__init__(self)

        def run(self):
            sys.stdout.write("run started\n")
            sys.stdout.flush()
            while not self.is_stop_requested():
                time.sleep(2)

            sys.stdout.write("run exited\n")
            sys.stdout.flush()

    import os
    os.fork()

    foo = Foo()
    foo.start()
    foo.join()

    sys.stdout.write("all exited\n")
    sys.stdout.flush()


def test_exception():
    class Foo(InterruptableThread):
        def __init__(self):
            InterruptableThread.__init__(self)

        def run(self):
            raise Exception("exceptional situation")

    foo = Foo()
    foo.start()
    foo.join()

    if foo.threw_exception:
        print str(foo.exception)
        print ''.join(traceback.format_tb(foo.exc_info[2]))

test_exception()
