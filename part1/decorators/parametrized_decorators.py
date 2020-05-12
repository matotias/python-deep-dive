"""This file corresponds to lesson 111 of python3: deep dive udemy course"""
from typing import Callable, Any
from time import perf_counter
import logging
from functools import wraps


# Non parametrized example
def timed(fn: Callable) -> Callable:
    @wraps(fn)
    def _inner(*args: Any, **kwargs: Any) -> Any:
        logging.getLogger(__name__)
        start = perf_counter()
        output = fn(*args, **kwargs)
        duration = perf_counter() - start
        logging.info('{0} took {1} seconds to execute with parameters args: \
{2}, kwargs: {3}'.format(fn.__name__, duration, args, kwargs))
        return output
    return _inner


logging.basicConfig(
    format='%(asctime)s [%(levelname)s]: %(message)s',
    level=logging.INFO
)


def calc_fib_recurse(n: int) -> int:
    return 1 if n < 3 else calc_fib_recurse(n - 2) + calc_fib_recurse(n - 1)


@timed
def fib(n: int) -> int:
    return calc_fib_recurse(n)


fib(30)


# Parametrized
def timed_n(repetitions: int) -> Callable:
    def _timed_decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def _inner(*args: Any, **kwargs: Any) -> Any:
            logging.getLogger(__name__)
            start = perf_counter()
            for repetition in range(repetitions):
                output = fn(*args, **kwargs)
            duration = perf_counter() - start
            logging.info(
                '{0} took {1} seconds to execute {2} times with parameters '
                'args: {3}, kwargs: {4}'.
                format(fn.__name__, duration, repetitions, args, kwargs))
            return output
        return _inner
    return _timed_decorator


@timed_n(10)
def fib(n: int) -> int:
    return calc_fib_recurse(n)


fib(30)