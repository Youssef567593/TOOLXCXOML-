# إعدادات مبدئية
settings = {
    "network_scan_range": "192.168.1.0/24",
    "save_data_path": "/home/user/data/settings.txt"
}

def save_settings():
    with open(settings["save_data_path"], "w") as file:
        for key, value in settings.items():
            file.write(f"{key}={value}\n")
    print("[INFO] Settings saved successfully.")

def load_settings():
    try:
        with open(settings["save_data_path"], "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                settings[key] = value
        print("[INFO] Settings loaded successfully.")
    except FileNotFoundError:
        print("[ERROR] Settings file not found.")
