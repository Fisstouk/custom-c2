import argparse
from port_scanner import *
import sys

def main():
    try:
        parser = argparse.ArgumentParser(prog='c2.py', description='Custom Command & Control program')

        parser.add_argument('-g', '--get_ip', action='store_true', help='Print all the ip addresses of the host in a text file')
        parser.add_argument('-p', '--ping', dest='ping', action='store_true', help='Ping each ip in a text file and keep systems up in another text file')
        parser.add_argument('-s', '--port_scan', action='store', nargs=2, help='Scan ports from 1 to 1024 by default for each hosts in the file hosts_up.txt, can enter custom ports')
        parser.add_argument('-e', '--persistence', action='store_true', help='Add a persistence program to the target, Windows or Linux')

        args = parser.parse_args()

        # dict_arg = vars(args)

        if args.get_ip:
            network_address()
        if args.ping:
            check_ping()
        if args.port_scan:
            dict_arg = vars(args)
            start_port = dict_arg['port_scan'][0]
            end_port = dict_arg['port_scan'][1]
            port_scan(int(start_port), int(end_port))
        if args.persistence:
            win32serviceutil.HandleCommandLine(windows_persistence)

        """        
        dict_choice = {
            "get_ip": network_address,
            "ping": check_ping,
            "port_scan": port_scan
        }

        for (key1, value1), (key2, value2) in zip(dict_arg.items(), dict_choice.items()):
            print(key1, value1, key2, value2)
            if key1 == key2:
                value2()
        """

    except KeyboardInterrupt:
        print('\nUser has exited the program')

if __name__ == '__main__':
    exit(main())
