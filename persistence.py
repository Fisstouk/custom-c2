import os
import platform 
import servicemanager
import socket
import sys
import time
import win32serviceutil
import win32service
import win32event

def check_os() -> None:
    current_os = platform.system()
    
    if current_os == 'Linux':
        linux_persistence()
    if current_os == 'Windows':
        windows_persistence()

class windows_persistence(win32serviceutil.ServiceFramework):
    _svc_name_: str = 'PythonScriptService'
    _svc_display_name_: str = 'Python Script Service'

    def __init__(self, args: list[str]) -> None:
        super().__init__(args)
        self.is_running: bool = False

    def SvcStop(self) -> None:
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False

    def SvcDoRun(self) -> None:
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.is_running = True

        try:
            # Initialization code for your service
            while self.is_running:
                # Insert your main service logic here
                # This can include data processing, periodic tasks, or any other functionality

                # Example: Print a message every 5 seconds
                print("Service is running...")
                time.sleep(5)  # Delay for 5 seconds before the next iteration

        except Exception as e:
            # Handle any exceptions or errors that occur during service execution
            servicemanager.LogErrorMsg(str(e))

        # Cleanup or service stop code
        servicemanager.LogInfoMsg("Service stopped")
    
def linux_persistence() -> None:
    service_path = "/etc/systemd/system/my_script.service"
    if not os.path.exists(service_path):
        open(service_path, "w").writelines('''
        [Unit]
        Description=Persitence
        
        [Service]
        ExecStart=/usr/bin/python3 /home/lyronn/Documents/securite_python/persistence.py

        [Install]
        WantedBy=multi-user.target''')
        os.system("systemctl enable --now persistence.service")

    while True:
        print("Script is running...")
        time.sleep(60)
