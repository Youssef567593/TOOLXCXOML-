def display_menu():
    print("TOOLXCXOML - Network Analysis Tool")
    print("1. Analyze Networks")
    print("2. Scan Networks")
    print("3. Exit")
    print("4. Settings")

def analyze_networks():
    print("Analyzing networks...")

def scan_networks():
    print("Scanning networks...")

def settings():
    print("Opening settings...")
    # Here you can add functionality for settings

def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            analyze_networks()
        elif choice == '2':
            scan_networks()
        elif choice == '3':
            print("Exiting...")
            break
        elif choice == '4':
            settings()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
