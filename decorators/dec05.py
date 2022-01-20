from functools import wraps
import json
import logging.config
from pathlib import Path

default_path=Path("/Users/anthonygladman/Documents/Code/python-exercises/decorators/logging.json")
default_level=logging.DEBUG

if default_path.exists():
    with open(default_path, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
else:
    logging.basicConfig(level=default_level)

logger = logging.getLogger(__name__)

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"Exception raised in {func.__name__}: {type(e).__name__}", exc_info=False)
            raise e
    return wrapper

@log
def powerup(a, b, c=0):
    return a**b % c

@log
def fukkitup(foo):
    raise NotImplementedError

def main():
    print(powerup(2,25,c=2.6))
    fukkitup(9)

if __name__ == '__main__':
    # logger.info("Starting")
    main()
