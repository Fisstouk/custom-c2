import argparse
from port_scanner import *
import sys

def main():
    try:
        parser = argparse.ArgumentParser(prog='c2.py', description='Custom Command & Control program')

        # Print help when no argument is given
        parser.add_argument(' ',  default='-h')
        parser.add_argument('--get-all-ip', type=network_address(), help='Print all the ip addresses of the host in a text file')
        parser.add_argument('--check-ping', type=check_ping(), help='Ping each ip in a text file and keep systems up in another text file')
        parser.add_argument('--port_scan', nargs='*', type=int, help='Scan ports from 1 to 1024 by default for each hosts in the file hosts_up.txt, can enter custom ports')

        args = parser.parse_args()
        port_scan(port_scan)

    except KeyboardInterrupt:
        print('User has exited the program')

if __name__ == '__main__':
    exit(main())
