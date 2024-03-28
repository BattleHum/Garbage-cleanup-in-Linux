#!/bin/python3
import subprocess

def upgrade():
    print("Upgrade system...")
    subprocess.call(["apt-get", "update", "-y"])
    subprocess.call(["apt-get", "upgrade", "-y"])
    subprocess.call(["apt-get", "dist-upgrade", "-y"])
    print("You kali upgrade!")

def clean():
    print("Clear system")
    subprocess.call(["apt-get", "clean", "-y"])
    subprocess.call(["apt-get", "autoremove", "-y"])
    print("System clear!")
    
if __name__ == '__main__':
    upgrade()
    clean()
