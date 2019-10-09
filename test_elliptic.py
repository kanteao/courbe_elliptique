#!/bin/python3
# cd /Users/kourakanewane/Desktop/Cours/M2\ RISM/Securite\ des\ services\ web
import random
import math
# m : message
# pub : cle publique
# priv : cle privee
# signature : calculee Sign(m,priv)
# verify : Ver(signature,m,pub)
listex=[]
listey=[]
G=[5,25]
a=2
b=9
x1=G[0]
print(x1)
y1=G[1]
print(y1)
lambd=0
modulo=37
temp=0
i=1

""" ETAPE 0 : CHOIX D'UN GENERATEUR """
while temp!=1:
	x=i;
	res=((x**3)+(a*x)+b)%modulo
	racine=math.sqrt(res)
	if racine.is_integer():
		y=racine	
		temp=1
	else:
		i=i+1	
print(x,y)
#x1=x
#y1=y
listex.append(x1)
listey.append(y1)

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
print(lambda3)

x3=((lambda3**2)-2*x1)%modulo
y3=(lambda3*(x1-x3)-y1)%modulo

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

	if x3 == G[0]:
		listex.append(x3)
		listey.append(y3)
		tempo=1
	else:
		listex.append(x3)
		listey.append(y3)
		#x2=x3
		#y2=y3

print(listex)
print(listey)

caracteres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','#','@','!','&','$','%']
print(caracteres)
print(len(listex))
print(len(listey))
print(len(caracteres))

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
	dec = (indice-k*k)%phi_n
	dcpt=tab[dec]
	print("code dechiffre:", dcpt)
	return dcpt

"""couple={}

for i in listex:
	couple[i]=listex[i],listey[i]
print(couple)"""


couple = []
for x,y in zip(listex,listey):
 a = (x,y)
 couple.append(a)
print couple
## Cryptage
k = 3265477
beta = k%modulo
texte="tempo22"
texte1="jevousaime"
result=[]


for char in texte1:
	print(" Message a chiffrer:", char)
	nombre=caracteres.index(char)
	#print(nombre)
	point=(couple[nombre]) #equivalent du message dans la courbe elliptique
	#print(point)
	crypte = crypter(point,modulo,couple,k)
	decrypte = decrypter(crypte,modulo,couple,k)
	indice = couple.index(decrypte)
	print(" Le message dechiffrer est :", caracteres[indice])
	result.append(decrypte)
print(result)




"""message = (15,11)
crypte = crypter(message,modulo,couple,k)
decrypte = decrypter(crypte,modulo,couple,k)"""

"""
## Cryptage
print("message a chiffrer:" , message)
y1=couple[(k-1)%modulo]
y2=couple.index(message)+(k*k)
cipher = y2%modulo
print("message chiffre:", couple[cipher])
## Decryptage
dec = (cipher-k*k)%modulo
print("message dechiffre:", couple[dec])"""

#nombre=couple.index(message)
#print(nombre)
#print(caracteres[nombre])

