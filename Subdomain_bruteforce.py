import shodan
import requests
from threading import Thread
import socket
import sys
import argparse
import os

SHODAN_API_KEY = "API_KEY"
api = shodan.Shodan(SHODAN_API_KEY)

#argument
my_parser = argparse.ArgumentParser()

my_parser.add_argument("-file", help="Enter the subdomain file name", required=True)
my_parser.add_argument("-target", help="Specify the targeted domain", required=True)

args = my_parser.parse_args()

#variable
ip=[]

def making_wordlist():
    with open(args.file) as fp:
        lines = fp.read().splitlines()
    with open("domain.txt", "w") as fp:
        for line in lines:
            print(line + "." + args.target, file=fp)

def shodan():
    with open("domain.txt") as domain_wordlist:
        for target in domain_wordlist:
            target = target.rstrip("\n")
            dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY
            print(dnsResolve)
            try:
                # First we need to resolve our targets domain to an IP
                resolved = requests.get(dnsResolve)
                hostIP = resolved.json()[target]

                # Then we need to do a Shodan search on that IP
                host = api.host(hostIP)
                ip.append(host['ip_str'])

            except:
                'An error occured'


def port_scanning():
    for ip_add in ip:
        remoteServer = ip_add
        remoteServerIP = socket.gethostbyname(remoteServer)

        # Print a nice banner with information on which host we are about to scan
        print("-" * 30)
        print(remoteServer)
        try:
          for port in (80, 443, 8080, 22):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

    # Printing the information to screen
    print("Scanning Completed")

if __name__ == '__main__':
    #calling thread
    Thread(target=making_wordlist()).start()
    Thread(target=shodan()).start()
    print(ip)
    Thread(target=port_scanning()).start()

os.remove("domain.txt")




