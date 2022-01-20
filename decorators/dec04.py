from functools import wraps
import logging

def log(logger, level='info'):
    def log_decorator(fn):
        @wraps(fn)
        def wrapper(*a, **kwa):
            getattr(logger, level)(fn.__name__)
            return fn(*a, **kwa)
        return wrapper
    return log_decorator

@log(logging.getLogger('main'), level='warning')
def tenx(foo):
    for _ in range(10):
        yield(foo)

p = tenx('plurff')
print(next(p))
print(next(p))
