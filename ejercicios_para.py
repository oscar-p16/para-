# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:48:16 2021

@author: oscar perez
"""
print('........................................................');
#zoologico
categoria1=0;
categoria2=0;
categoria3=0;
print('zoologico de barranquilla');
print('');
print('1= elefante');
print('');
print('2= jirafas');
print('');
print('3= chimpanses');
print('');
n=int(input('seleecione un numero:'));
print('');

if n>0 and n<4:
   if n==1:
       animal= print('elefante');
       total=20;
       for i in range(total):
        edad = int(input("digite la edad del Elefante: "));
        if edad >= 0 and edad <= 1:
            categoria1 = categoria1+1;
        elif edad == 2:
            categoria2 = categoria2+1;
        elif edad >= 3:
            categoria3= categoria3+1;
if n==2:
       animal= print('jirafa');
       total=15;
       for i in range(total):
        edad = int(input("digite la edad de la jirafa: "));
        if edad >= 0 and edad <= 1:
            categoria1 = categoria1+1;
        elif edad == 2:
            categoria2 = categoria2+1;
        elif edad >= 3:
            categoria3= categoria3+1;
if n==3:
       animal= print('chimpanses');
       total= 40;
       for i in range(total):
        edad = int(input("digite la edad del chimpase: "));
        if edad >= 0 and edad <= 1:
            categoria1 = categoria1+1;
        elif edad == 2:
            categoria2 = categoria2+1;
        elif edad >= 3:
            categoria3= categoria3+1;

categoria1=(categoria1*100)/n;
categoria2=(categoria2*100)/n;
categoria3=(categoria3*100)/n;            

print('');    
print("Porcentajes de las edades de el animal que se escogió: ");
print('');
print("Porcentaje en la edad de 0 a 1 años es: ",categoria1);
print('');
print("Porcentaje en la edad de 1 a 2 años es: ", categoria2);
print('');
print("Porcentaje en la edad de 3 o más años: ",categoria3);    
print('........................................................');



    