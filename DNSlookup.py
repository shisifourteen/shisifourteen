from scapy.all import *
from art import *
import time
art = tprint("DNS lookups")
time.sleep(0.2)
kwai = tprint("KWAI:gnehs123456")
print("kuaishou:gnehs123456\n")
time.sleep(0.2)
while True:

    name = str(input("enter the domain name that you will be querying:\n"))
    dnsser = input("enter the DNS server address(default=8.8.8.8):\n")
    if dnsser == '':
        dnsser = "8.8.8.8"
    print("wait for the server to respond...\n")
    pkt=IP(dst=dnsser)/UDP(dport=53)/DNS(qr=0,opcode=0,rd=1,qd=DNSQR(qname=name))
    timeout = 8
    try:
        dnsre = sr1(pkt,verbose=0,timeout=timeout)
        if dnsre is not None:
            loop = 0
            loop1 = 1
            while True:
                try:
                    if dnsre.getlayer(DNS).fields['an'][loop].fields['type'] == 1 or dnsre.getlayer(DNS).fields['an'][loop].fields['type'] ==5:
                        dnsip = dnsre.getlayer(DNS).fields['an'][loop].fields['rdata']
                        print("the IP address of domain name %s is\n%d:"%(name,loop1),dnsip)
                        print("\n")
                        loop+=1
                        loop1+=1
                    else:
                        break

                except TypeError:
                    print("WARING:no such name!")
                    break
        else:
            print("the DNS server is not responding to the outgoing IP address, check the domain name and the DNS server and try again\n")
    except IndexError:
        loop1-=1
        print("%d results received"%loop1)
    time.sleep(0.2)
    conti = input("\ndo you want to quit?(default=no)\n")
    if conti == 'q' or conti == 'Q' or conti == 'y' or conti == 'Y' or conti == "quit" or conti == "Quit" or conti == "yes":
        tprint("\nhave  a  happy  day  !\n")
        break
