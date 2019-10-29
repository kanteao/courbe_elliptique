#!/bin/python3
# cd /Users/kourakanewane/Desktop/rangement/Cours/M2\ RISM/Securite\ des\ services\ web
# cd \Documents\GitHub\Applications
import random
import math
from itertools import product
import binascii
from fonctions import n_premiers, hexadeci, deci, euclide_etendu, crypter, decrypter

listex=[]
listey=[]
a=4
b=1
lambd=0
modulo=1321
temp=0
i=1
kerr=2
# Calcul du Nombre de blocs
caracteres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
nchar=len(caracteres)
bl_size=nchar**2

up = bl_size + 50
n_premiers(bl_size,up)

# Genese des blocs de taille 2
print("\n \n")
combs = [''.join(comb) for comb in product(caracteres, repeat=kerr)]
print(combs)
print("\n \n")
combs = hexadeci(combs)



""" ETAPE 0 : CHOIX D'UN GENERATEUR """
while temp!=1:
	x=i;
	res=((x**3)+(a*x)+b)%modulo
	racine=math.sqrt(res)
	if racine.is_integer():
		y=int(racine)	
		temp=1
	else:
		i=i+1	
#print(x,y)
G=[x,y]
print("\n \n Notre generateur est ",G)
x1=x
y1=y


listex.append(x1)
listey.append(y1)
ordre=1


""" ETAPE 1 : DEFINITION DE (x3,x3) """

val=((3*x1**2)+2)%modulo
#phi_n=37
e=2*y1%modulo

lambda3 = euclide_etendu(e, modulo, val)
print("Lambda =",lambda3)

x3=((lambda3**2)-2*x1)%modulo
y3=(lambda3*(x1-x3)-y1)%modulo
ordre=ordre+1
# Ajout du deuxieme point (2*alpha) a la liste
listex.append(x3)
listey.append(y3)

tempo=0
while tempo!=1:
	x2=x3
	y2=y3
	val1=(y2-y1)%modulo
	e1=(x2-x1)%modulo
	lambda1 = euclide_etendu(e1, modulo, val1)
	x3=((lambda1**2)-x1-x2)%modulo
	y3=(lambda1*(x1-x3)-y1)%modulo
	if (x3 == G[0]):
		listex.append(x3)
		listey.append(y3)
		ordre=ordre+1
		print("Dernier point : (", x3 ,",",y3 ,")")
		tempo=1
	else:
		listex.append(x3)
		listey.append(y3)
		ordre=ordre+1
#print(listex)
#print(listey)
print("Nombre de points :",len(listex))
#print(len(listey))


couple = []
for x,y in zip(listex,listey):
 a = (x,y)
 couple.append(a)
#print (couple)
## Cryptage
k = 3265477 # cle publique ??
beta = k%modulo
texte="tempo22"
texte1='jevousaimee'
print(len(texte1))
result=[]
indice=0
message=''
hexamessage=''
bonus='y'

toto=0

if (len(texte1))%kerr==1:
	print("La chaine est impaire")
	texte1=texte1+bonus
	texte1 = binascii.hexlify(texte1.encode()) # Conversion en hexadecimal
else:
	print("La chaine est paire")
	texte1 = binascii.hexlify(texte1.encode()) # Conversion en hexadecimal

#for char in texte1:
while toto!=1:
	m=texte1[indice:indice+2*kerr]
	indice=indice+2*kerr
	print(" Message a chiffrer:", m)
	nombre=combs.index(m)

	point=(couple[nombre]) #equivalent du message dans la courbe elliptique

	crypte = crypter(point,modulo,couple,k)
	decrypte = decrypter(crypte,modulo,couple,k)
	index = couple.index(decrypte)
	decm=combs[index]
	print(" Le message dechiffre est :", decm)
	hexamessage = hexamessage + (str(decm))
	decm = binascii.unhexlify(decm).decode() # Conversion en chaine de caracteres
	message=message+decm

	result.append(decrypte)
	if(indice>=len(texte1)):
		toto=1

print("Code dechiffre: liste de points ",result)
#print(crypte)
#print(decrypte)
print("Message hexa dechiffre:", hexamessage)
print("Message dechiffre:", message)



