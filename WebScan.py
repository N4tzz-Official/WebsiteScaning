#!/usr/bin/env python3

import os
import requests

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    banner = """
███╗   ██╗██╗  ██╗████████╗███████╗███████╗███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗     ██╗    ██╗███████╗██████╗ ███████╗██╗████████╗███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗  ██║██║  ██║╚══██╔══╝╚══███╔╝╚══███╔╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗    ██║    ██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔██╗ ██║███████║   ██║     ███╔╝   ███╔╝ ███████╗██║   ██║██║   ██║███████║██║  ██║    ██║ █╗ ██║█████╗  ██████╔╝███████╗██║   ██║   █████╗      ███████╗██║     ███████║██╔██╗ ██║
██║╚██╗██║╚════██║   ██║    ███╔╝   ███╔╝  ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║    ██║███╗██║██╔══╝  ██╔══██╗╚════██║██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚████║     ██║   ██║   ███████╗███████╗███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝    ╚███╔███╔╝███████╗██████╔╝███████║██║   ██║   ███████╗    ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═══╝     ╚═╝   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                                                                                                    Coded By N4tzzSquad
                                                                                                                                                  DONT COPYRIGHT ALL !!!!!
    """
    print(banner)

def scan_website(url):
    try:
        response = requests.get(url)
        print(f"\nScanning {url}...")
        print(f"Status Code: {response.status_code}")
        print(f"Response Time: {response.elapsed.total_seconds()} seconds")
        
        if response.status_code == 200:
            print("Scan results: Website is accessible.")
            if "Server" in response.headers:
                print(f"Server: {response.headers['Server']}")
            if "X-Powered-By" in response.headers:
                print(f"X-Powered-By: {response.headers['X-Powered-By']}")
        else:
            print(f"Scan results: Received status code {response.status_code}.")

    except requests.exceptions.RequestException as e:
        print(f"Error scanning {url}: {e}")

def help_text():
    print("\nHelp: This tool allows you to scan websites for vulnerabilities.")
    print("You can enter a URL (e.g., http://example.com) to check its status and response time.")
    print("Make sure to include http:// or https:// in the URL.")
    
def main():
    while True:
        clear_screen()
        display_banner()
        print("1) Scan Website")
        print("2) Help")
        print("00) Exit")

        choice = input("Select an option: ")

        if choice == '1':
            url = input("Enter URL to scan (including http:// or https://): ")
            scan_website(url)
            input("\nPress Enter to continue...")
        elif choice == '2':
            help_text()
            input("\nPress Enter to return to the menu...")
        elif choice == '00':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
