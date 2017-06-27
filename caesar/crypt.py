# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 23:18:18 2017

@author: Эмиль
"""
def checkchr(c):
    if (ord(c) < ord('a') or ord(c) > ord('z')):
        return 1
    else:
        return 0
def encrypt(file, shift):
    string=''
    text = file.read()
    for i in range(len(text)):
        if(checkchr(text[i])):
            string = string + text[i]
            g.write(text[i])
        else:
            c = ord(text[i]) + shift
            if (c > ord('z')):
                string = string + chr(c - ord('z') + ord('a') - 1)
                g.write(chr(c - ord('z') + ord('a') - 1))
            else:
                if(c < ord('a')):
                    string = string + chr(ord('z') - ord('a') - c + 1)
                    g.write(chr(ord('z') - ord('a') - c + 1))
                else:
                    string = string + chr(c)
                    g.write(chr(c))
    return string
def decrypt(text,shift):
    string=''
    for i in range(len(text)):
        if(checkchr(text[i])):
            string = string + text[i]
        else:
            c = ord(text[i]) - shift
            if (c > ord('z')):
                string = string + chr(c - ord('z') + ord('a') - 1)
            else:
                if(c < ord('a')):
                    string = string + chr(ord('z') - (ord('a') - c) + 1)
                else:
                    string = string + chr(c)
    return string


def main():
    global  g
    f = open('10.txt')
    g = open('text2.txt','w')
    shift = 10
    
    ec = encrypt(f, shift)
    decrypt(ec,shift)
    f.close()
    g.close()
    
if __name__=="__main__":
    main()