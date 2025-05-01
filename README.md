# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*:  Kanchan Vilas Jadhav

*INTERN ID*: CT04DA375

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# DESCRIPTION OF TASK: Overview:
This Python-based toolkit performs two main penetration testing tasks:

1.Port Scanning – Identifies which ports are open on a target IP address.

2.SSH Brute-Forcing – Attempts to gain access to the target system using common SSH login credentials (only if SSH is running on port 22).


# Editor used: VS Studio


# File: main.py
-Purpose
This is the main script that runs the entire toolkit. It handles user interaction and ties together all other modules.

-Breakdown: 
import sys, os
# Standard libraries for file and path operations.

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
# Ensures Python can find the local module penetration_toolkit.

from penetration_toolkit import port_scanner, brute_forcer
# Imports the two key functionalities: port scanning and brute-forcing.

print("--- Welcome to the Penetration Testing Toolkit ---")
target_ip = input("Enter the IP address of the target: ")
# Greets the user and asks for the target IP to scan.

ports_to_scan = list(range(1, 1025))
open_ports = port_scanner.run_port_scanner(target_ip, ports_to_scan)
# Scans ports 1 to 1024 to find which are open.

if 22 in open_ports:
    ...
    found_password = brute_forcer.ssh_brute_force(...)
# If SSH (port 22) is open, it asks for a username and runs a brute-force attack using a small password list.

print("--- Penetration Test Completed ---")
# Ends the scan and prints a message.

# File: penetration_toolkit/port_scanner.py
-Purpose:
Scans a list of TCP ports on a given IP address to check which are open.

-Breakdown:

import socket
from concurrent.futures import ThreadPoolExecutor
# Uses Python’s socket for networking and ThreadPoolExecutor for fast, parallel scanning.

-Function: scan_port(ip, port)

with socket.socket(...) as s:
    s.settimeout(1)
    s.connect((ip, port))
    
~ Tries to connect to a specific port.
~ If successful, it means the port is open.

-Function: run_port_scanner(ip, ports, threads=100)

with ThreadPoolExecutor(max_workers=threads) as executor:
    results = executor.map(lambda p: scan_port(ip, p), ports)

~ Scans all specified ports using 100 threads for faster performance.
~ Collects and returns a list of all open ports.

# File: penetration_toolkit/brute_forcer.py
-Purpose:
Attempts to guess the SSH login password by trying a list of known or guessed passwords.

-Breakdown:

import paramiko
# Uses the paramiko library to interact with SSH.

Function: ssh_brute_force(ip, username, password_list)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Initializes a secure SSH client that accepts new host keys automatically.


client.connect(ip, username=username, password=password, timeout=2)
# Tries each password from the list until it finds one that works (or gives up).


return password
# Returns the correct password if found, otherwise returns None.

# Requirements: pip install paramiko

## Legal Warning ##
This toolkit is intended for authorized penetration testing only. Do not scan or attack systems you don’t have explicit permission to test. Always follow ethical hacking guidelines and laws.

## SUMMARY
1.The user runs main.py and enters an IP address.

2.The port scanner runs and returns a list of open ports.

3.If port 22 is open, the brute-forcer runs using a test list of passwords.

4.The toolkit prints out whether it was able to log in via SSH.

# Output: (Due to unavailability of another device and ofcourse due to legal reasons, couldn't perform brute force attack on other device except for mine in which port 22 is closed)


