import os
import platform 
import time

def check_os() -> None:
    current_os = platform.system()
    
    if current_os == 'Linux':
        linux_persistence()
    if current_os == 'Windows':
        windows_persistence()

def windows_persistence() -> None:

    
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
