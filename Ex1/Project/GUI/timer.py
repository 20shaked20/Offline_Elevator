import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self, dt: int = 10):
        """
        :param dt: A scale of one second in our count
        """
        self._start_time = None
        self.dt = dt

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def get_time(self):
        """
        :return: The amount of time that has elapsed since the function .start() was called.
        """
        if self._start_time == None:
            raise TimerError("Timer is not running. Use .start() to start it")

        return (time.perf_counter() - self._start_time) * self.dt

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        elapsed_time = (time.perf_counter() - self._start_time) * self.dt
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
