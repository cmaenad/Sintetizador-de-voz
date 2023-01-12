'''
Programa en python que recibe una oración en español y reproduce a voz (TTS)

Fue escrito por cmaenad (cruzmaciasenrique0@gmail.com) como proyecto de aficionado

Fecha de creacion: 20 de marzo de 2021 
Última modificación: 12 de enero de 2022

'''
import os,sounddevice
from playsound import playsound

sounddevice.play(5)
salida=[]

dictletras = {
'a':"a.wav",
'b':'b.wav',
'c':'k.wav',
'd':'d.wav',
'ch':'cha.wav',
'e':'e.wav',
'f':'f.wav',
'g':'g.wav',
'i':'i.wav',
'j':'j.wav',
'k':'k.wav',
'l':'l.wav',
'll':"ll.wav",
'm':'m.wav',
'n':'n.wav',
'o':'o.wav',
'p':'p.wav',
'q':'k.wav',
'r':'r.wav',
'rr':'rr.wav',
's':'s.wav',
't':'t.wav',
'u':'u.wav',
'v':'b.wav',
'w':'w.wav',
'x':'x.wav',
'y':'ll.wav',
'z':'s.wav',
'-':'-.wav'

}

letrasunicas=['a','b','d','e','f','i','j','k','m','n','o','p','q','s','t','v','w','x','z']
vocalesalternas=['e','i']

while True:
    print("Introduzca una oracion en español (sin acentos ni signos de puntuacion) para reproducir en voz")
    salida.clear()
    texto=input("Introduzca el texto que desea\n\n")
    i=-1
    for letra in texto:
        i=i+1
        if letra in letrasunicas:
            salida.append(dictletras[letra])
        elif letra == 'c':
            if i+1<len(texto) and texto[i+1] in vocalesalternas:
                salida.append(dictletras['s'])
            elif i+1<len(texto) and texto[i+1]=='h':
                salida.append(dictletras['ch'])
            else:
                salida.append(dictletras['c'])
        elif letra=='g':
            if i+1<len(texto) and texto[i+1] not in vocalesalternas:
                salida.append(dictletras["g"])
            else:
                salida.append(dictletras["j"])
        elif letra=='h':
            continue
        elif letra=='r':
            if (i+1<len(texto) and (texto[i+1]=='r' or texto[i-1]==' ') ) or i==0:
                salida.append(dictletras['rr'])
            else:
                salida.append(dictletras['r'])
        elif letra=='u':
            if i-1>=0 and i<len(texto)-1 and (texto[i-1]=='q' or texto[i-1]=='g') and (texto[i+1] in vocalesalternas):
                continue
            else:
                salida.append(dictletras['u'])
        elif len(texto)==i+1 and letra=='y':
            salida.append(dictletras['i'])
        elif letra==' ':
            salida.append('espacio.wav')

        elif letra == 'l':
            if i+1<len(texto) and texto[i+1] =='l':
                salida.append(dictletras['ll'])
            elif i+1<len(texto) and i-1>=0 and texto[i-1]=='l':
                continue
            else:
                salida.append(dictletras['l'])
        elif letra == 'ñ':
            salida.append(dictletras['n'])
            salida.append(dictletras['i'])
        elif letra == '-':
            salida.append(dictletras['-'])
        elif letra == 'y':
            if texto[i-1]==' ':
                salida.append(dictletras['i'])
    for palabras in salida:
        playsound(palabras)

    os.system("cls")
