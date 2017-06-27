# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:13:27 2017

@author: Эмиль
"""
def calc_shift(d,  dict_lit):
    r = []
    for i in range(len(d)):
        for j in range(len(dict_lit)):
            if (d[chr(ord('a') + i)] + 0.2 >= dict_lit[chr(ord('a') + j)] and 
                d[chr(ord('a') + i)] - 0.2 <= dict_lit[chr(ord('a') + j)]):
                    r.append(abs(ord(chr(ord('a') + i)) - ord(chr(ord('a') + j))))
    r.sort()
    count = maxcount = number = 0
    for i in r:
        if (r[i] == r[i-1]):
            number = r[i]
            count+=1
        else:
            if (count > maxcount):
                maxcount = count
                count = 0
                number = r[i]
    return number
def checkchr(c):
    if (ord(c) < ord('a') or ord(c) > ord('z')):
        return 1
    else:
        return 0
def hack(string):
    count_lit = 0
    dict_lit = {'a': 0,'b': 0,'c': 0,'d': 0,
         'e': 0,'f': 0,'g': 0,'h': 0,
         'i': 0,'j': 0,'k':0,'l': 0,
         'm': 0,'n': 0,'o': 0,'p': 0,
         'q': 0,'r': 0,'s': 0,'t': 0,
         'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    for i in range(len(string)):
        if (checkchr(string[i]) == 0):
            count_lit+=1
            dict_lit[string[i]]+=1
    for i in range(len(dict_lit)):
        dict_lit[chr(ord('a') + i)]/=count_lit
        dict_lit[chr(ord('a') + i)]*=100
    shift = calc_shift(d, dict_lit)
    print(shift)
    
def main():
    global d
    d = {'a': 8.17,'b': 1.49,'c': 2.78,'d': 4.25,
    'e': 12.70,'f': 2.23,'g': 2.02,'h': 6.09,
    'i': 6.97,'j': 0.15,'k':0.77,'l': 4.03,
    'm': 2.41,'n': 6.75,'o': 7.51,'p': 1.93,
    'q': 0.10,'r': 5.99,'s': 6.33,'t': 9.06,
    'u': 2.76,'v': 0.98,'w': 2.36,'x': 0.15,'y': 1.97,'z': 0.07}
    
    g = open('text2.txt')
    string = g.read()
    hack(string)
    
if __name__=="__main__":
    main()
