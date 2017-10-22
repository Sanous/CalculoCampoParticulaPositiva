#!/usr/bin/python

#Calculo de campo para particula positiva.

from __future__ import division
from visual import *
from scipy.constants import epsilon_0,e

#Posicion de los cilindros que representan los ejes positivos del sistema
xaxis = cylinder(pos=(10,0,0), axis=vector(10,0,0),radius=.1)
yaxis = cylinder(pos=(0,10,0), axis=vector(0,10,0),radius=.1)
zaxis = cylinder(pos=(0,0,10), axis=vector(0,0,10),radius=.1)

#Esfera que representa la ubicacion de la carga positiva
particula=sphere(pos=vector(0,0,0),color=color.red)

#Definicion de constantes
k=1/(4*pi*epsilon_0)
q=e

#Rango de valores 3D para variar los calculos
rango=range(-10,11,2)

for x in rango:
    for y in rango:
	for z in rango:
	    #Este if evita que se realizen calculos en la posicion de la particula cargada
	    if vector(x,y,z)==particula.pos:
	        continue
	    #Calculo del vector posicion en el punto que queremos calcular
	    r=vector(x,y,z)-particula.pos
	    #Calculo del vector unitario para el campo electrico
	    unit=r/mag(r)
	    #Calculo del vector Campo Electrico en el punto deseado
	    campo=k*q/(mag(r)**2)*unit
	    #print campo
	    #Visualizacion del vector calculado usando una flecha del visual.
	    #Aclaracion: el numero 1e10 que multiplica al campo solo tiene la intension de magnificar
	    #el tamano de la flecha debido a que las cargas usadas son muy pequenas para las distancias.
	    #Si desea observar la magnitud real del campo descomente la linea que contiene el print.
	    arrow(pos=vector(x,y,z),axis=1e10*campo)
