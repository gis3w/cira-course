import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

logging.basicConfig( level=logging.DEBUG, filename='logs/debug.log')
logging.basicConfig( level=logging.ERROR, filename='logs/error.log')

logging.Formatter("%(asctime)s - %(message)s")
