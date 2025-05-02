#by Andi Akbar official 
import re
import os
import hashlib


def pass_write(text,password):
    print("hashed password :", password)
    f = open("pass.txt", "a")
    f.write(text+"\t"+password+"\n")
    f.close()

def md5_hash(password):
    h = hashlib.md5(password.encode())
    pass_write (password,h.hexdigest())


def sha256_hash(password):
    h = hashlib.sha256(password.encode())
    pass_write(password,h.hexdigest())


def sha224_hash(password):
    h = hashlib.sha224(password.encode())
    pass_write(password,h.hexdigest())


def sha1_hash(password):
    h = hashlib.sha1(password.encode())
    pass_write(password,h.hexdigest())


def sha384_hash(password):
    h = hashlib.sha384(password.encode())
    pass_write(password,h.hexdigest())


def sha512_hash(password):
    h = hashlib.sha512(password.encode())
    pass_write(password,h.hexdigest())


def hash_cracker(pass_file,hash_str):
    file1 = open(pass_file, "r")
    string = file1.read()
    list1 = string.split('\n')
    list2 = []
    for i in range(len(list1)):
        lst = list1[i].split('\t')
        list2.append(lst)
        if lst[1] == hash_str:
            print("Password found :", lst[0])
            break

def main():
    func_list = ['','md5_hash(password)','sha256_hash(password)','sha224_hash(password)','sha1_hash(password)','sha384_hash(password)','sha512_hash(password)']
    HoC = input("would you like to hash or crack the hash ? (hash-live/crack) : ")
    if HoC == 'hash-live':
        password = input("enter text to hash : ")
        method = input("""  choose your method :
                                                                        
1) md5
2) sha1
3) sha224
4) sha256
5) sha384
6) sha512
""")
        eval(func_list[int(method)])
    elif HoC == 'crack':
        pass_file = input("enter the password file name ")
        hash_str = input("enter the string to be hashed ")
        hash_cracker(pass_file,hash_str)
                                                                                                      

main()
