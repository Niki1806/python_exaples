# -*- coding: utf-8 -*-
 
# # define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
        

def somma(a,b):
    return a+b

def sottrazione(a,b):
    return a-b

def moltiplicazione(a,b): 
    return a*b

def divisione(a,b):
    return a/b


print "Benvenuti nel programma calcolatrice"
    
notValid = True
while notValid:    
    print "------------------------------------"
    print "Operazioni disponibili:"
    print "1) Somma"
    print "2) Sottrazzione"
    print "3) Moltiplicazine"
    print "4) Divisione"
    print "------------------------------------"

    scelta = input("Inserire una scelta valida: ")

    if scelta not in [1,2,3,4]:
        print "Scelta non valida"
    else:
        notValid = False
    
a = input("Primo operando: ")
b = input("Secondo operando: ")
if scelta == 1:
    print "La somma è ", somma(a,b)
if scelta == 3:
    print "Il prodotto è ", moltiplicazione(a,b)
if scelta == 4:
    print "Il quoziente è ", divisione(a,b)
if scelta == 2:
    print "La differenza è ", sottrazione(a,b)

print ("\nGrazie e alla prossima!!!")