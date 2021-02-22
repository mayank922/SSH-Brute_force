# SSH-Brute_force

A simple pyton script to brute force the ssh cridentials using following modules :

Pxssh-  Module of pexpect library use to handle the ssh login session

Argparse- For taking the command line input

usage: ssh_brute.py [-h] -H HOST -U USER [-p PASSWORD] [-C CMD] [-P PORT] [-f PASSWDFILE]

A SSH interaction script

optional arguments:
  
    -h, --help     show this help message and exit
  
    -H HOST        Enter the target host to connect
  
    -U USER        Enter the username
  
    -p PASSWORD    Enter the password
  
    -C CMD         Enter any command to want to add
  
    -P PORT        Enter the port if required
  
    -f PASSWDFILE  specify password file
