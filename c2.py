import argparse
from port_scanner import *
import sys

def main():
    try:
        parser = argparse.ArgumentParser(prog='c2.py', description='Custom Command & Control program')

        parser.add_argument('-g', '--get_ip', action='store_true', help='Print all the ip addresses of the host in a text file')
        parser.add_argument('-p', '--ping', dest='ping', action='store_true', help='Ping each ip in a text file and keep systems up in another text file')
        parser.add_argument('-s', '--port_scan', action='store', help='Scan ports from 1 to 1024 by default for each hosts in the file hosts_up.txt, can enter custom ports')

        args = parser.parse_args()

        # dict_arg = vars(args)

        if args.get_ip:
            network_address()
        if args.ping:
            check_ping()
        if args.port_scan:
            dict_arg = vars(args)
            end_port = dict_arg['port_scan'][0]
            port_scan(int(end_port))

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
        print('User has exited the program')

if __name__ == '__main__':
    exit(main())
