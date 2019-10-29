#!/bin/python3
import binascii

# Calcul du modulo
def n_premiers(lower,upper):
	print("Les nombres premiers entre",lower,"et",upper,"sont:")
	prime=[]
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	           #print(num)
	           prime.append(num)
	print(prime)

# Conversion en hexadecimal
def hexadeci(listed):
	listeh=[]
	for uni in listed:
		hexa = binascii.hexlify(uni.encode())
		listeh.append(hexa)
	print(listeh)
	return listeh

# Conversion en decimal
def deci(listeh):
	listed=[]
	for uni in listeh:
		deci = binascii.unhexlify(uni).decode()
		listed.append(deci)
	print(listed)
	return listed

def euclide_etendu(e, phi_n, val) :
  d = 1
  temp = (e*d)%phi_n
  while(temp != val):
    d = d+1
    temp = (e*d)%phi_n
  return d

# Cryptage et Decryptage

def crypter(m, phi_n, tab, coef) :
	cpt=[]
	## Cryptage
	print("code a chiffrer:" , m)
	y1=tab[(coef-1)%phi_n]
	y2=tab.index(m)+(coef*coef)
	indice = y2%phi_n
	cpt=tab[indice]
	print("code chiffre:", cpt)
	return cpt

def decrypter(m, phi_n, tab, coef) :
	dcpt=[]
	## Decryptage
	indice=tab.index(m)
	dec = (indice-coef*coef)%phi_n
	dcpt=tab[dec]
	print("code dechiffre:", dcpt)
	return dcpt