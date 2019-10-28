#!/bin/python3
# cd /Users/kourakanewane/Desktop/rangement/Cours/M2\ RISM/Securite\ des\ services\ web
# cd \Documents\GitHub\Applications
import random
import math
from itertools import product

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

up = bl_size + 50
n_premiers(bl_size,up)

# Genese des blocs de taille 2
print("\n \n")

combs = [''.join(comb) for comb in product(caracteres, repeat=kerr)]
print(combs)


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
def euclide_etendu(e, phi_n, val) :
  d = 1
  temp = (e*d)%phi_n
  while(temp != val):
    d = d+1
    temp = (e*d)%phi_n
  return d

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


# Cryptage et Decryptage

def crypter(m, phi_n, tab, coef) :
	cpt=[]
	## Cryptage
	print("code a chiffrer:" , m)
	y1=tab[(coef-1)%phi_n]
	y2=tab.index(m)+(coef*coef)
	indice = y2%phi_n
	cpt=couple[indice]
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

couple = []
for x,y in zip(listex,listey):
 a = (x,y)
 couple.append(a)
#print (couple)
## Cryptage
k = 3265477 # cle publique ??
beta = k%modulo
texte="tempo22"
texte1="jevousaimee"
print(len(texte1))
result=[]
indice=0
message=''
bonus='y'

toto=0

if (len(texte1))%kerr==1:
	print("La chaine est impaire")
	texte1=texte1+bonus
else:
	print("La chaine est paire")

#for char in texte1:
while toto!=1:
	m=texte1[indice:indice+kerr]
	indice=indice+kerr
	print(" Message a chiffrer:", m)
	nombre=combs.index(m)

	point=(couple[nombre]) #equivalent du message dans la courbe elliptique

	crypte = crypter(point,modulo,couple,k)
	decrypte = decrypter(crypte,modulo,couple,k)
	index = couple.index(decrypte)
	decm=combs[index]
	message=message+decm
	print(" Le message dechiffre est :", decm)

	result.append(decrypte)
	if(indice>=len(texte1)):
		toto=1

print(result)
print(crypte)
print(decrypte)
print("Message dechiffre:", message)


"""hexa=texte1.encode("hex")
print(hexa)
deci=hexa.decode("hex")
print(deci)"""
