import ipaddress
import netifaces
import socket
import subprocess
import sys
import time


def get_network_address() -> ipaddress.IPv4Network:
    # Get all network interfaces except localhost
    for iface in netifaces.interfaces():
        if iface == 'lo' or iface.startswith('vbox'):
            continue
        # Get details for the rest of the ipv4 interfaces 
        iface_details = netifaces.ifaddresses(iface)
        if iface_details[netifaces.AF_INET]:
            ipv4 = iface_details[netifaces.AF_INET][0]['addr']
            netmask = iface_details[netifaces.AF_INET][0]['netmask']
            # Build network addr + netmask
            interface = ipaddress.IPv4Interface(ipv4 + '/' + netmask)
            print(f"The programm found the network {interface.network}.")
    return interface.network

def network_address() -> None:
    # Get all network interfaces except localhost
    for iface in netifaces.interfaces():
        if iface == 'lo' or iface.startswith('vbox'):
            continue
        # Get details for the rest of the ipv4 interfaces 
        iface_details = netifaces.ifaddresses(iface)
        if iface_details[netifaces.AF_INET]:
            ipv4 = iface_details[netifaces.AF_INET][0]['addr']
            netmask = iface_details[netifaces.AF_INET][0]['netmask']
            # Build network addr + netmask
            interface = ipaddress.IPv4Interface(ipv4 + '/' + netmask)
            print(f"type interface: {type(interface.network)}")
            print(f"The programm found the network {interface.network}.")
    try:
        with open('data/hosts_in_network.txt', 'w') as f:
            for ip in interface.network.hosts():
                f.write(format(ipaddress.IPv4Address(ip))+"\n")
            print("All IP addresses in the network are written in the file hosts_in_network.txt")
    except FileExistsError:
        print("The file hosts_in_network.txt already exists. End of the programm")


def check_ping() -> None:
    try:
        with open('data/hosts_in_network.txt', 'r') as f:
            for ip in f.readlines():
                # Process to ping
                res = subprocess.call(['ping', '-c', '3', ip.rstrip()])
                time.sleep(1)
                if res == 0:
                    try:
                        # Write hosts that are up in the file
                        with open('data/hosts_up.txt', 'a') as file:
                            file.write(ip)
                    except FileExistsError as e:
                        print(e)
                elif res == 2:
                    print("No response from", ip)
    except FileNotFoundError as e:
        print(f"Error: {e}")

def port_scan(starting_port:int, ending_port:int) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # Scan the range of ports set by the user
    try:
        for port in range(starting_port , ending_port + 1):
            try:
                with open('data/hosts_up.txt', 'r') as f:
                    for host in f.readlines():
                        if sock.connect_ex((host.rstrip(), port)) == 0:
                            banner = sock.recv(1024).decode()
                            with open('data/ports_open.txt', 'w') as file:
                                print(f"New entry in the ports_open.txt file: port {port} on host {host.rstrip()} is open with banner {banner}")
                                file.write(f"{port} on host {host.rstrip()} is open")
            except FileNotFoundError as e:
                print(f"Error: {e}")
        sock.close()

    except socket.gaierror:
        print("\n Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit() 
