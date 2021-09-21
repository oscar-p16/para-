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

#transito
n_carro = int(input("digite el numero de carros que ingresaron a la ciudad:"));
amarillo=0;
rosado=0;
rojo=0;
verde=0;
azul=0;
print('')
for i in range (n_carro):
    color_c= int(input("digite el ultimo digito de la placa del carro:"));
    if color_c==1 or color_c==2:
        amarillo= amarillo+1;
    if color_c==3 or color_c==4:
        rosado= rosado+1;
    if color_c==5 or color_c==6:
        rojo=rojo+1;
    if color_c==7 or color_c==8:
        verde= verde+1;
    if color_c==9 or color_c==0:
        azul=azul+1;
    else:
        print('');
        
print('la cantidad de carros con calcomania amarilla son:', amarillo);
print('');
print('la cantidad de carros con calcomania rosada son:', rosado);
print('');
print('la cantidad de carros con calcomania roja son:', rojo);
print('');
print('la cantidad de carros con calcomania verde son:', verde);
print('');
print('la cantidad de carros con calcomania azul son:', azul)

print('........................................................'); 

#empresa
n_empleados= int(input("digite el numero de empleados:"));

for i in range(n_empleados):
    horas=int(input('digite el numero de horas trabajadas'));
    if horas<=40:
        salario=horas*20;
    else:
        horas_extras=horas-40;
        salario=40*20+(horas_extras*25);
    print('');
    print('el salario del trabajador',i+1,'es:''$',salario);    

print('........................................................'); 

#alumnos
edad1=0;
edad2=0;

hombres=int(input('digite el numero de los estudiantes que son barones:'));
mujeres=int(input('digite el numero de los estudiamtes que son mujeres:'));

for i in range(hombres):
    edad_h=int(input('ingrese la edad del estudiante:'));
    edad1= edad1+edad_h;
for i in range(mujeres):
    edad_m=int(input('ingrese la edad del estudiante:'));
    edad2=edad2+edad_m;

promedio1= edad1/hombres;
promedio2= edad2/mujeres;

print('');
print('el porcentaje de edad de los alumnos que son hombres es',promedio1,'%');
print('');
print('el porcentaje de edad de los alumnos que son mujeres es',promedio2,'%');    

print('........................................................');




















