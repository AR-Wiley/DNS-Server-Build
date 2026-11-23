import os
import sys

var_log = "/var/log"
log_dir = "/var/log/SysAdmin-Logs"
log_files = [
    "users.log",
    "groups.log",
    "sudo.log",
    "authentication.log",
    "permissions.log",
    "software.log",
    "updates.log",
    "services.log",
    "network.log",
    "config.log",
    "security.log",
    "errors.log"
]

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root", file=sys.stderr)
        sys.exit(1)

def validate_var_log(path):
    if not os.path.exists(path):
        print(f"{path} does not exist. Cannot proceed.")
        sys.exit(1)

def main():

    check_root()
    validate_var_log(var_log)

    if not os.path.exists(log_dir):
        print("Path does not exist")
        print("Creating path")
        try:
            os.makedirs(log_dir)
            print("Path has been created")
            print(log_dir)
        except Exception as e:
            print(f"An error has occured: {e}")

    for i in log_files:
        file_path = os.path.join(log_dir, i)
        if not os.path.isfile(file_path):
            print(f"Log file {i} does not exist")
            print(f"Creating file {i}")
            try:
                with open(file_path, "x") as f:
                    f.write(f"{i} ceated")
                print(f"Created: {i}")
            except FileExistsError:
                print(f"{i} already exits.")
            except Exception as e:
                print(f"An error has occured: {e}")

if __name__ == "__main__":
    main()
