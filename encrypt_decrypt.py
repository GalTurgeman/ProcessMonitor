'''
Created on 21 Apr 2018

@author: gal
'''
import base64
list= []
with open("/Users/gal/Desktop/old.csv") as old:
    l=old.readlines()
    for i in l: 
        list.append(base64.b16encode(i))
    print list
    for i in list:
        print base64.b16decode(i, False)