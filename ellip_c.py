#!/usr/bin/python3
import math
# fonction d'euclude etendu ___________________________________________
def euclide_etendu(e, phi_n,x) :
  d = 1 
  tempo = (e*d)%phi_n
  while(tempo != x):
    d = d+1
    tempo = (e*d)%phi_n
  return d

#y**2=x**3+2*x+9

#calcul de 2 alpha
def calc_2alpha(x1,y1,mod,a):
	lamda=0	
	e=2*y1%mod
	omega = (3*(x1**2)+a) % mod


	lamda = euclide_etendu(e,mod,omega)
	#2*y1*lamda=3*(x1**2)+a ========> e*lamda=omega % mod
	#calcul de lamda
	print ("\n(",e,",",lamda,")")

	x3=(lamda**2-2*x1)%mod
	y3=(lamda*(x1-x3)-y1)%mod

	#print ("\n(",x3,",",y3,")")
	temp=[]
	temp.append(x3)
	temp.append(y3)
	return temp
#calcul des autres alpha a partir de 3 alpha_______________________ 
def calc_o_alpha(x1,y1,x2,y2,mod,a):
	lamda=0	
	e=(x2-x1) % mod
	omega = (y2-y1) % mod
	#print('e',e)
	#print('omega',omega)


	lamda = euclide_etendu(e,mod,omega)
	#2*y1*lamda=3*(x1**2)+a ========> e*lamda=omega % mod
	#calcul de lamda
	#print ("\n(",e,",",lamda,")")

	x3=(lamda**2-x1-x2)%mod
	y3=(lamda*(x1-x3)-y1)%mod

	#print ("\n(",x3,",",y3,")")
	temp=[]
	temp.append(x3)
	temp.append(y3)
	return temp
#calcul du generateur____________________________________________________________
def calc_G(a,b,mod):
	x=1
	y=0
	while 1:
		#y=math.sqrt(((x**3)+(2*x)+9))
		y=math.sqrt(((x**3)+(a*x)+b))
		if y.is_integer():
			y=y%mod
			print ("\n( le generateur est ",x,",",y,")")
			break
		else:
			x=x+1
	return [x,y]
###################################################################################
# main ___________________________________________________________
mod=37
a=2
b=9
G=calc_G(a,b,mod)
x1=G[0]
y1=G[1]
#all_alpha=[]
#all_alpha.append(G)
all_alpha={}
all_alpha['a']=G
current_alpha=[]
cur_a=calc_2alpha(G[0],G[1],mod,a)
#all_alpha.append(cur_a)
all_alpha['2a']=cur_a
#print ('all_alpha',all_alpha)
#print('cur_a',cur_a)
i =3
while 1:
	cur_a=calc_o_alpha(G[0],G[1],cur_a[0],cur_a[1],mod,a)
	#all_alpha.append(cur_a)
	all_alpha[str(i)+'a']=cur_a
	i=i+1
	if cur_a[0] == G[0]:
		#all_alpha.append(cur_a)
		#print('cur_a___________________1',cur_a)
		#all_alpha.append(cur_a)
		break
	#print('cur_a',cur_a)
	#print ('all_alpha',all_alpha)
	#i=i-1
#all_alpha.append(cur_a)
print ('all_alpha',all_alpha)

#chiffrement______________________________________________________

#mes_x= input('Entrer la valeur de x du message ')
#mes_y= input('Entrer la valeur de y du message ')
#k=int(input('Entrer la valeur de k du message '))
#mes=[int(mes_x),int(mes_y)]
#print('mes ',mes)
#print('k ',k)

def chiffrer(mes,k,all_alpha):
	alpha_y1=str((k%mod))+'a'
	beta=k%mod
	for x,y in all_alpha.items():
		if mes==y:
			print('mes_x',x)
			if(x=='a'):
				x_alpha=1
			else:
				x_alpha=int(x[0:-1])
			print('x_alpha',x_alpha)
			a_y2=(x_alpha+k*beta)
			alpha_y2=str(a_y2)+'a'
	print('alpha_y1',alpha_y1)
	print('alpha_y2',alpha_y2)
	c=all_alpha[alpha_y2]
	print('le message chiffré est : ',c)
	return c
#dechiffrement______________________________________________________
def dechiffrer(c,k,all_alpha):
	beta=k%mod
	for x,y in all_alpha.items():
		if c==y:
			print('chif_x',y)
			c_alpha=int(x[0:-1])
			print('x_alpha',c_alpha)
			mes_f_a=str((c_alpha-k*beta))+'a'
			print('mes_f_a',mes_f_a)
	mes_f=all_alpha[mes_f_a]
	print('mes_f',mes_f)
	
points=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0,'#','@','!','&','$','%']
point_dict=dict()
#print(points)
r=1
for pp in points:
	if r==1:
		point_dict[pp]=all_alpha['a']
	else:
		point_dict[pp]=all_alpha[str(r)+'a']
	r=r+1
print(point_dict)
	
#chif=chiffrer(mes,k,all_alpha)
#dechiffrer(chif,k,all_alpha)

text=input('Entrer le message a chiffrer')
k=int(input('Entrer la valeur de k du message '))
print('text',text)
text_chif=''
for txt in text: 
	print('txt',txt)
	#chif=chiffrer(mes,k,all_alpha)
	for x,y in point_dict.items():
		if txt==x:
			message=y
			print('message',message)
			chif=chiffrer(message,k,all_alpha)
			for x,y in point_dict.items():
				if chif==y:
					text_chif=text_chif+x
print('text_chif',text_chif)
	
	


#d_alpha = calc_2alpha(x1,y1,mod,a)
#all_alpha=calc_all_alpha(G,a,mod)




	
	





