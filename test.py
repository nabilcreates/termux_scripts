import os, platform, subprocess

def main():
    print("OS Name: {} \nPlatform System: {} \nPlatform Release: {}".format(os.name, platform.system(), platform.release()))
    subprocess.call("pkg i nmap")

if __name__ == "__main__":
    main()