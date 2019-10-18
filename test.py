import os, platform

def main():
    print("OS Name: {} \nPlatform System: {} \nPlatform Release: {}".format(os.name, platform.system(), platform.release()))

if __name__ == "__main__":
    main()