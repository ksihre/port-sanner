import socket

def scan_port(ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")
        sock.close()

if __name__ == "__main__":
    ip = input("Enter IP address to scan: ")
    ports = [22, 80, 443, 8080]  # Customize the ports you want to scan
    scan_port(ip, ports)
