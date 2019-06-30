import os
import sys
import yaml
import uvicorn
import app

config_name = "config.yml"

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

config_path = os.path.join(application_path, config_name)

with open(config_path, 'r') as stream:
    config = yaml.safe_load(stream)

uvicorn.run(app, 
    host=config['server']['host'], 
    port=config['server']['port'], 
    log_level=config['server']['loglevel'], 
    reload=False)