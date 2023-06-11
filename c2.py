import argparse
from port_scanner import *
import sys

def main():
    parser = argparse.ArgumentParser(prog='c2.py', description='Custom Command & Control programm')

    # Print help when no argument is given
    parser.add_argument(' ',  default='-h')
    parser.add_argument('--get-all-ip', type=network_address(), help='Find the network ID of the machine where the script is running')

    args = parser.parse_args()

if __name__ == '__main__':
    exit(main())
