import os

def scan_directory(path):
    try:
        files = os.listdir(path)
        for f in files:
            print(f)
    except PermissionError:
        print("permission denied")
    except FileNotFoundError:
        print("path not found")

if __name__ == "__main__":
    target = input("enter path: ")
    scan_directory(target)
