import os
import sys

home_dir = "/home"
dns_admin_dir = "dnsadmin"
dns_admin_path = os.path.join(home_dir,dns_admin_dir)
dns_admin_sub_dir = ["backups", "config-mgmt", "dns", "docs", "scripts", "security", "staging", "tmp"]

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root", file=sys.stderr)
        sys.exit(1)

def home_dir_validation(path):
    if not os.path.exists(path):
        print(f"{path} does not exist. Unable to proceed")
        sys.exit(1)

def main():

    check_root()
    home_dir_validation(home_dir)    

    if not os.path.exists(dns_admin_path):
        print(f"{dns_admin_path} does not exist")
        print(f"Creating {dns_admin_path}")
        try:
            os.makedirs(dns_admin_path)
            print(f"{dns_admin_path} has been created")
            print(dns_admin_path)
        except Exception as e:
            print(f"An error has occured in creating {dns_admin_path}: {e}")

    for i in dns_admin_sub_dir:
        if not os.path.exists(os.path.join(dns_admin_path, i)):
            print(f"{i} does not exist...")
            print(f"Creating {i}...")
            try:
                os.makedirs(os.path.join(dns_admin_path, i))
                print(f"{i} successfully created")
            except Exception as e:
                print(f"An error has occurred: {e}")
        else:
            print(f"{i} already exists")


if __name__ == "__main__":
    main()
