# init db
from iotpotential.database import init_db
init_db()


# constants
DEVICE_ID = '1C8779C000000156'


# setup logger
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
current_dir = os.path.dirname(__file__)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)
