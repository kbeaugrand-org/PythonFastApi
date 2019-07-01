import os
import sys
import yaml

import logging
from logging.handlers import RotatingFileHandler

import uvicorn

from app import main

config_name = "config.yml"

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, config_name)

with open(config_path, 'r') as stream:
    config = yaml.safe_load(stream)

logging.basicConfig(filename=config['server']['log']['file']['path'], 
                    format=config['server']['log']['format'],
                    level=config['server']['log']['level'].upper())

logger = logging.getLogger('main_logger')
handler = RotatingFileHandler(config['server']['log']['file']['path'], 
                               maxBytes=config['server']['log']['file']['maxBytes'], 
                               backupCount=config['server']['log']['file']['keep'])
logger.addHandler(handler)

uvicorn.run(main.api, 
    host=config['server']['host'], 
    port=config['server']['port'], 
    log_level=config['server']['log']['level'],
    access_log=config['server']['log']['access_log'],
    logger=logger,
    reload=False)