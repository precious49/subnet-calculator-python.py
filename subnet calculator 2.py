import ipaddress

def get_ip_class(ip):
    first_octet = int(str(ip).split(".")[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Unknown"

def subnet_calculator(ip_with_subnet):
    try:
        # Create an IPv4 network object
        network = ipaddress.IPv4Network(ip_with_subnet, strict=False)

        # Network details
        network_address = network.network_address
        broadcast_address = network.broadcast_address
        num_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
        netmask = network.netmask
        wildcard_mask = ipaddress.IPv4Address(int(network.hostmask))
        cidr = network.prefixlen
        ip_class = get_ip_class(network.network_address)

        # Display results
        print("\n--- Subnet Calculation Results ---")
        print(f"IP with Subnet:     {ip_with_subnet}")
        print(f"IP Class:           {ip_class}")
        print(f"Network Address:    {network_address}")
        print(f"Broadcast Address:  {broadcast_address}")
        print(f"Number of Hosts:    {num_hosts}")
        print(f"Subnet Mask:        {netmask}")
        print(f"Wildcard Mask:      {wildcard_mask}")
        print(f"Mask bits (CIDR):   /{cidr}")
        print("---------------------------------")

    except ValueError:
        print("⚠️ Invalid IP address or subnet mask. Please try again.")

if __name__ == "__main__":
    print("📌 Subnet Calculator Project")
    print("============================")

    # Ask user for input
    ip_with_subnet = input("Enter an IP address with subnet (e.g. 192.168.1.0/24): ")
    subnet_calculator(ip_with_subnet)
