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

#numero menor
n=int(input('dijite la cantidad de numeros:'));
numero= [];
for i in range(n):
    numero.append(int(input('dijite el numero:')));
print('');
print('el arreglo es:',numero);      
print('');
print("El valor minimo es:", min(numero));

print('........................................................');

#peso
p1=0;
p2=0;
p3=0;
p4=0;
p5=0;
p1_inicial=int(input('digite el peso inical de la primera persona:'));
p2_inicial=int(input('digite el peso inical de la segunda persona:'));
p3_inicial=int(input('digite el peso inical de la tercera persona:'));
p4_inicial=int(input('digite el peso inical de la cuarta persona:'));
p5_inicial=int(input('digite el peso inical de la quinta persona:'));


for i in range(10):
    p1_pesos=int(input("digite el peso de la primera persona en los pesos:"));
    p1=p1+p1_pesos;
    promedio=p1/10;
    diferencia=promedio-p1_inicial;
if diferencia >0:
        print('subio de peso la diferencia es de:',diferencia,'kg');
else:
        print('bajo de peso la diferencia es de:',diferencia,'kg');        
 
    
for i in range(10):
    p2_pesos=int(input("digite el peso de la segunda persona en los pesos:"));
    p2=p2+p2_pesos;
    promedio=p2/10;
    diferencia=promedio-p2_inicial;
if diferencia >0:
        print('subio de peso la diferencia es de:',diferencia,'kg');
else:
        print('bajo de peso la diferencia es de:',diferencia,'kg');      

    
for i in range(10):
    p3_pesos=int(input("digite el peso de la tercera persona en los pesos:"));
    p3=p3+p3_pesos;
    promedio=p3/10;
    diferencia=promedio-p3_inicial;
if diferencia >0:
        print('subio de peso la diferencia es de:',diferencia,'kg');
else:
        print('bajo de peso la diferencia es de:',diferencia,'kg');      

for i in range(10):
    p4_pesos=int(input("digite el peso de la cuarta persona en los pesos:"));
    p4=p4+p4_pesos;
    promedio=p4/10;
    diferencia=promedio-p4_inicial;
if diferencia >0:
        print('subio de peso la diferencia es de:',diferencia,'kg');
else:
        print('bajo de peso la diferencia es de:',diferencia,'kg');  

for i in range(10):
    p5_pesos=int(input("digite el peso de la quinta persona en los pesos:"));
    p5=p5+p5_pesos;
    promedio=p5/10;
    diferencia=promedio-p5_inicial;
if diferencia >0:
        print('subio de peso la diferencia es de:',diferencia,'kg');
else:
        print('bajo de peso la diferencia es de:',diferencia,'kg');  

print('........................................................');

#tienda
contenedor=0;

while True:
    cantidad=int(input('digite la cantidad de este articulo:'));
    precio=int(input('digite el precio de deste articulo:'));
    print('');
    
    if cantidad == 0:
            break
        
    total=cantidad*precio;
    contenedor=contenedor+total;
    
    print('el total de este articulo es:','$',total);
    print('');
    print('si decea salir digite 0 en las dos opciones');
    
print('');    
print('el total de la compra es:','$', contenedor);    
    
print('........................................................');

#teatro
p_asiento=int(input('digite el precio de las entradas sin descuento:'));
personas=int(input('digite el numero de personas dentro del teatro:'));
c=0;
for i in range(personas):
    edad_p=int(input('digite la edad de los clientes'));
    if edad_p<5:
        print('no se permite su ingreso');
        
    if edad_p>=5 and edad_p<=14:
        descuento_p=p_asiento*0.35;
        print('');
        print('el descuento realizado a esta persona es de','$',descuento_p);
        c=c+descuento_p;
        
    if edad_p>=15 and edad_p<=19:
        descuento_p=p_asiento*0.25;
        print('');
        print('el descuento realizado a esta persona es de','$',descuento_p);
        c=c+descuento_p;
        
    if edad_p>=20 and edad_p<=45:
        descuento_p=p_asiento*0.10;
        print('');
        print('el descuento realizado a esta persona es de','$',descuento_p);
        c=c+descuento_p;
        
    if edad_p>=46 and edad_p<=65:
        descuento_p=p_asiento*0.25;
        print('');
        print('el descuento realizado a esta persona es de','$',descuento_p);
        c=c+descuento_p;
     
    if  edad_p>=66:
        descuento_p=p_asiento*0.35;
        print('');
        print('el descuento realizado a esta persona es de','$',descuento_p);
        c=c+descuento_p;
print('');        
print('el teatro dejo de recibir','$',c,'en descuentos');

print('........................................................');

#vendedores
for i in range(100):
    v = int(input("Digite cuanto dinero en millones obtivo el vendedor: "))
    if v <= 20:
        comision = v * 0.10
        print('Su comisión es de:','$',comision,)
    if v> 20 and v < 40:
        comision = v * 0.15
        print('Su comisión es de:','$',comision,)
    if v >= 40 and v < 80:
        comision = v * 0.20
        print('Su comisión es de:','$',comision,)
    if v >= 80 and v < 160:
        comision = v * 0.25
        print('Su comisión es de:','$',comision,)
    if v >= 160:
        comision = v * 0.30
        print('Su comisión es de:','$',comision,)
    else: 
        print('No recibe comisiones')
        
print('........................................................');

#votos
import random
p1= 0;
p2= 0;
p3= 0;
for i in range(50000):
    votos=random.randint(1,3);
    if votos==1:
        p1+=1;
    if votos==2:
        p2+=1;
    else:
       p3+=1;
if p1==p2 and p1==p3:
    print('empate');
if p1>p2 and p1>p3:
    print('gano el primer candidato');
if p2>p1 and p2>p3:
    print('gano el segundo candidato');
if p3>p2 and p3>p1:
    print('gano el tercer candidato');

print('votos total del primer candidato:',p1);
print('votos total del segundo candidato:',p2);
print('votos total del tercer candidato:',p3);

print('........................................................');









