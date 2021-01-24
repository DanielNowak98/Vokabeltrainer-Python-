#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import random
import os
from os import system, name 
import time


# In[ ]:


df = pd.read_excel('Vokabelliste.xlsx')
a = len(df)
i = 0


richtig = 0
falsch = 0
Prozent = 0

# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
clear()

print("--------------- Latein Vokabeltrainer --------------- \n\n")
print("Wie viele Vokabeln sollen gelernt werden?")
x = int(input("Anzahl eingeben: \n"))

print("\n" + "jetzt werden " + str(x) + " Vokabeln abgefragt.... Los gehts: \n")
time.sleep(3)
clear()

def neueVokabel():
     
    b = random.randint(0,a)
    c = df["Latein"][b]
    
    print("Was heißt "+ c + " auf Deutsch?")
    d = input("Antwort: \n")

    e = df["Deutsch"][b]

    if (d == e):
        global richtig
        richtig = richtig + 1
        print("\n \n Richtig!\n")
        time.sleep(3)
        clear()
        return richtig
        
        
    else:
        global falsch
        falsch = falsch + 1
        print("\n \n Falsch!\n \n Die richtige Antwort lautet: " + e + "\n")
        time.sleep(4)
        clear()
        return falsch
        
        

    
while i < x:
    print("Vokabel " + str(i + 1) + "\n")
    neueVokabel()
    i = i + 1


clear()
Prozent = (richtig / x) * 100
print("Ende des Tests. \n \n Auswertung:")
print("Von "+ str(x) + " Vokabeln waren " + str(richtig) + " richtig und " + str(falsch) + " falsch!" )
print("Es waren: " +str(Prozent) + " % richtig!")
    