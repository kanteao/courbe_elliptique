#!/usr/bin/python3
import math

def euclide_etendu(e, phi_n,x) :
  d = 1 
  temp = (e*d)%phi_n
  while(temp != x):
    d = d+1
    temp = (e*d)%phi_n
  return d
e=8
mod=11
omega=5
lamda = euclide_etendu(e,mod,omega)  
x1=5
y1=2
x2=2
y2=7
x3=(lamda**2-x1-x2)%mod
y3=(lamda*(x1-x3)-y1)%mod
print('lamda',lamda)
print('x3',x3)
print('y3',y3)
