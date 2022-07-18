#programa en python que recibe una oración y la transforma en palabras

import os
from playsound import playsound

salida=[]

dictletras = {
'a':"a.mp3",
'b':'b.mp3',
'c':'k.mp3',
'd':'d.mp3',
'ch':'cha.mp3',
'e':'e.mp3',
'f':'f.mp3',
'g':'g.mp3',
'i':'i.mp3',
'j':'j.mp3',
'k':'k.mp3',
'l':'l.mp3',
'll':"ll.mp3",
'm':'m.mp3',
'n':'n.mp3',
'o':'o.mp3',
'p':'p.mp3',
'q':'k.mp3',
'r':'r.mp3',
'rr':'rr.mp3',
's':'s.mp3',
't':'t.mp3',
'u':'u.mp3',
'v':'b.mp3',
'w':'w.mp3',
'x':'x.mp3',
'y':'ll.mp3',
'z':'s.mp3'

}

letrasunicas=['a','b','d','e','f','i','j','k','m','n','o','p','q','s','t','v','w','x','y','z']
vocalesalternas=['e','i']

while True:
    print(salida)
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
            salida.append('espacio.mp3')

        elif letra == 'l':
            if i+1<len(texto) and texto[i+1] =='l':
                salida.append(dictletras['ll'])
            elif i+1<len(texto) and i-1>=0 and texto[i-1]=='l':
                continue
            else:
                salida.append(dictletras['l'])

    for palabras in salida:
        playsound(palabras)

    os.system("cls")
