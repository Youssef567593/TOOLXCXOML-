import os
import time
import socket
import pyfiglet
import psutil

def clear():
    os.system("clear")

def banner():
    clear()
    print(pyfiglet.figlet_format("TOOLXCXOML"))

def analyze_networks():
    print("\n[+] Analyzing available networks...\n")
    try:
        interfaces = psutil.net_if_addrs()
        for name, addrs in interfaces.items():
            print(f"Interface: {name}")
            for addr in addrs:
                print(f"  - Address: {addr.address}")
                print(f"  - Family: {addr.family}")
            print("  - Ping: OK (simulated)")
            print("  - ID: STATIC")
            print("  - Connection Duration: Simulated 12 min\n")
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

def scan_my_network():
    print("\n[+] Scanning your network...\n")
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(f"Your IP: {ip}")
        print("Connection Duration: Simulated 8 min")
        print("Proxy: Not Detected (simulated)\n")
    except:
        print("Could not retrieve network information.")

def open_settings():
    print("\n[+] Opening settings file...\n")
    time.sleep(1)
    os.system("nano settings.conf")

def main():
    banner()
    while True:
        print("1. Analyze Networks")
        print("2. Scan My Network")
        print("3. Open Settings")
        print("4. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            analyze_networks()
        elif choice == "2":
            scan_my_network()
        elif choice == "3":
            open_settings()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
