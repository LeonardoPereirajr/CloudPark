import json

def read_configuration():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
            if not data:
                print("The file contains no information.")
            else:
                print("Contents of the config.json file:")
                print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("The config.json file does not exist.")

def write_configuration():
    server_name = input("Enter the server name: ")
    server_ip = input("Enter the server IP: ")
    server_password = input("Enter the server password: ")

    data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Information successfully saved in the config.json file.")
    print("Contents of the config.json file:")
    print(json.dumps(data, indent=4))

def main():
    while True:
        print("\nChoose an option:")
        print("1 - Read configuration")
        print("2 - Write configuration")
        print("3 - Exit")
        
        choice = input("Enter the number of the desired option: ")
        
        if choice == "1":
            read_configuration()
        elif choice == "2":
            write_configuration()
        elif choice == "3":
            print("Program closed.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()