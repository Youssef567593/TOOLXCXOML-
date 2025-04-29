import os
import pyfiglet  # لاستعمال ASCII Art لتحويل النص إلى شكل كبير

# Function to analyze the network
def analyze_network():
    print("[INFO] Starting network analysis...")
    # Add your code for network analysis here
    os.system("ifconfig")  # Or any command that suits your needs for network analysis

# Function to scan the network
def scan_network():
    print("[INFO] Starting network scan...")
    # Add your code for network scanning here
    os.system("nmap -sP 192.168.1.0/24")  # Or any other command for network scanning

# Function for settings and saving data
def settings_menu():
    print("[INFO] Welcome to the settings menu. You can configure your tool here.")
    print("[INFO] 1. Save data settings")
    print("[INFO] 2. Modify analysis preferences")
    user_choice = input("[INFO] Select an option: ")
    if user_choice == "1":
        print("[INFO] Saving data...")
        # Add your code for saving settings here
    elif user_choice == "2":
        print("[INFO] Modifying preferences...")
        # Add your code for modifying preferences
    else:
        print("[INFO] Invalid choice. Returning to main menu.")
        return

# Function to exit the tool
def exit_tool():
    print("[INFO] Exiting tool...")
    exit()

# Function to display the main menu
def show_tool_interface():
    # Display the tool name in ASCII Art
    ascii_art = pyfiglet.figlet_format("TOOLXCXOML")
    print(ascii_art)  # Display "TOOLXCXOML" in large ASCII letters
    print("1. Analyze Networks")
    print("2. Scan Networks")
    print("3. Exit Tool")
    print("4. Settings Menu")
    
    user_choice = input("[INFO] Select an option: ")

    if user_choice == "1":
        analyze_network()
    elif user_choice == "2":
        scan_network()
    elif user_choice == "3":
        exit_tool()
    elif user_choice == "4":
        settings_menu()
    else:
        print("[INFO] Invalid choice. Try again.")

# Start the tool
if __name__ == "__main__":
    show_tool_interface()
