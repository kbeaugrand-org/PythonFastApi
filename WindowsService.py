import os
import servicemanager
import inspect  
import socket
import sys
import win32event
import win32service
import win32serviceutil
import uvicorn
import yaml
import app.main

class PredictService(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonWindowsService"
    _svc_display_name_ = "Python Windows Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogInfoMsg("{serviceName} - is alive and well".format(serviceName=self._svc_name_)) 
        config_name = "config.yml"

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        config_path = os.path.join(application_path, config_name)
        servicemanager.LogInfoMsg("Config file path is {config_path}".format(config_path=config_path)) 
        
        with open(config_path, 'r') as stream:
            config = yaml.safe_load(stream)
        
        uvicorn.run(app.main, 
                    host=config['server']['host'], 
                    port=config['server']['port'], 
                    log_level=config['server']['loglevel'], 
                    reload=False)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(PredictService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(PredictService)
