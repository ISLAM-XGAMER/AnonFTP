#!/usr/bin/env python3
import ftplib 
import pyfiglet
import colorama
import argparse

parser = argparse.ArgumentParser(description='AnonFTP script',add_help=True)
parser.add_argument('-H', '--host', type=str, help='hostname to check')
parser.add_argument('-f', '--file', type=str, help='Path to the file containing hostnames')
args = parser.parse_args()

if args.file is None and args.host is None:
    parser.error('Please provide either the file argument using -f or --file, or the host argument using -H or --host')




print(pyfiglet.figlet_format("AnonFTP"))
colorama.init()


           
def anonLogin(host):
    try:
        ftp =ftplib.FTP(host , timeout=30)
        ftp.login("anonymous")
        print(f"{colorama.Fore.BLUE + '[+]'}{colorama.Style.RESET_ALL} {colorama.Style.BRIGHT}{str(host)}{colorama.Style.RESET_ALL} FTP Anonymous Login Succeded" , end="\n")
        ftp.quit()
    except Exception:
        print(f"{colorama.Fore.RED + '[+]'} {colorama.Style.RESET_ALL}{colorama.Style.BRIGHT}{str(host)}{colorama.Style.RESET_ALL} FTP Anonymous Login Failed", end="\n")        
                



       


if args.file:
    file_Path = args.file
    with open(file_Path, "r") as file :
        hosts = file.readlines() # everyline in an index in list
        for host in hosts: # Catching every host 
            host = host.rstrip()
            anonLogin(host)
            print(colorama.Style.RESET_ALL)
                


if args.host:
    host = args.host
    anonLogin(host)
    print(colorama.Style.RESET_ALL)



