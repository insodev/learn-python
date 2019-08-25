"""
декоратор который замеряет время
"""
import time
import random
from functools import wraps


def timeit(func):
    # @wraps
    def wrapper(*args, **kwargs):
        start_time = time.time()

        r = func(*args, **kwargs)

        end_time = time.time()

        print(func, 'run for', end_time - start_time, args, kwargs)

        return r

    return wrapper


def increase_heavy(heavy_time=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                enough_heavy = func(*args, **kwargs)

                if enough_heavy:
                    break
                else:
                    args = (args[0] + (heavy_time or 1),) + args[1:]

            return enough_heavy

        return wrapper
    return decorator


@increase_heavy(heavy_time=2)
@timeit
def heavy_func(heavy: int, heavy_time=None):
    if heavy_time is None:
        heavy_time = 0.1
    work_time = heavy * random.random() * heavy_time * 2

    time.sleep(work_time)
    return work_time > 5


if __name__ == '__main__':
    print(heavy_func(5))
