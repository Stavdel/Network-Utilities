import socket
import os

def ping_host(host):
    """
    Pings a host to check for connectivity.
    """
    response = os.system(f"ping -c 1 {host}")
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down!")

def dns_lookup(host):
    """
    Performs a DNS lookup for a given host.
    """
    try:
        ip_address = socket.gethostbyname(host)
        print(f"The IP address of {host} is: {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve host: {host}")

if __name__ == "__main__":
    ping_host("8.8.8.8")
    dns_lookup("google.com")
