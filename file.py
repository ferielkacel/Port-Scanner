#portscanner
import socket

def portScanner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return "open" if result == 0 else "closed"


def scan_range(ip_range, port_range):
    for ip in ip_range:
        for port in port_range:
            status = portScanner(ip, port)
            print(f"IP: {ip}, Port: {port}, Status: {status}")

def main():
    host = input("Please enter the base IP address you want to scan: ")
    start_port = int(input("Please enter the starting port: "))
    end_port = int(input("Please enter the ending port: "))
    ip_range = [f"{host[:-1]}{i}" for i in range(1, 255)]
    port_range = range(start_port, end_port + 1)
    scan_range(ip_range, port_range)

main()
