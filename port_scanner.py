import ipaddress
import netifaces

def network_address():
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
    try:
        with open('data/hosts_in_network.txt', 'w') as f:
            for ip in interface.network.hosts():
                f.write(format(ipaddress.IPv4Address(ip))+"\n")
            print("All IP addresses in the network are written in the file hosts_in_network.txt")
    except FileExistsError:
        print("The file hosts_in_network.txt already exists. End of the programm")
            

