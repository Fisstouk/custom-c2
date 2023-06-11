import argparse
from port_scanner import *
import sys

def main():
    parser = argparse.ArgumentParser(prog='c2.py', description='Custom Command & Control programm')

    # Print help when no argument is given
    parser.add_argument(' ',  default='-h')
    parser.add_argument('--get-all-ip', type=network_address(), help='Print all the ip addresses of the host in a text file')
    parser.add_argument('--check-ping', type=check_ping(), help='Ping each ip in a text file and keep systems up in another text file')

    args = parser.parse_args()

if __name__ == '__main__':
    exit(main())
