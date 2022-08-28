#!/usr/bin/env python3
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

from os.path import exists

def git_keys():
    path_to_file = input()    
    file_exists = exists(path_to_file)
    if(file_exists):
        print ("Charizard_exists")
        keyFile = open("../ssh/clientpubKey", "br")
        pubKeyPEM= keyFile.read()
        keyFile.close()
        keyFile = open("../ssh/clientprivKey", "br")
        privKeyPEM= keyFile.read()
        keyFile.close()
        print (privKeyPEM)
    else:
        print ("Charizard is not real")
        keyPair = RSA.generate(3072)
 
        pubKey = keyPair.publickey() 
        pubKeyPEM = pubKey.exportKey()
        privKeyPEM = keyPair.exportKey()
        pubKeyfile = open("../ssh/clientpubKey" , "bw+")
        pubKeyfile.write(pubKeyPEM)
        pubKeyfile.close()
        privKeyfile = open("../ssh/clientprivKey" , "bw+")
        privKeyfile.write(privKeyPEM)
        privKeyfile.close()                                                                                                                                                                                                                    
git_keys()
exit()

     
encryptor = PKCS1_OAEP.new(pubKey)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    inp = input()
    s.sendall(bytes(inp,'utf-8'))
   #: s.sendall(b"Hello, world")
    data = s.recv(1024)
    print("Encrypted:", binascii.hexlify(encryptor.encrypt (bytes(inp, 'utf-8'))))
print(f"Received {data!r}")

