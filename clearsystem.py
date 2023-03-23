#!/bin/python3
import subprocess

def clear():
    print("Clear system")
    subprocess.call(["apt-get", "clean", "-y"])
    subprocess.call(["apt-get", "autoremove", "-y"])
    print("System clear!")


if __name__ == '__main__':
    clear()
