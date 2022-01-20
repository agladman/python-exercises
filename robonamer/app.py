import logging
from pathlib import Path

from src.robonamer import Robot

# set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(funcName)s - %(message)s')

# logging to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

# logging to file
fh = logging.FileHandler(f'{Path(__file__).stem}.log')
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
logger.addHandler(fh)

def main():
    r = Robot()
    logger.debug(f"{r=}")
    r.boot()
    logger.debug(f"{r=}")
    r.reset()
    logger.debug(f"{r=}")
    logger.info(f"used names: {len(r.load_used_names())}")

if __name__ == '__main__':
    main()
