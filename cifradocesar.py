import nltk
import re
import numpy as np

texto = 'WDSFSDALALIHKXKWUNWFUASLISKSVWLUAXKSKUKAIMHYKSESLLWTSLSWFWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFDHLVALMAFMHLLAETHDHLWFNFDWFYNSBWVWMWKEAFSVHQDNWYHWLMNVASKDSXKWUNWFUASUHFDSJNWSISKWUWFWFDHLUKAIMHYKSESLQVWWLMSESFWKSWLMSTDWUWKNFSKWDSUAHFQHTMWFWKWDMWPMHIDSFHDSAVWSXNFVSEWFMSDWLJNWFHMHVSLDSLDWMKSLSISKWUWFUHFDSEALESXKWUNWFUASWFDHLMWPMHLLAFHJNWSDYNFSLSISKWUWFESLSEWFNVHJNWHMKSLUHFMSFVHDSLLAYFHLVWDMWPMHUAXKSVHQHKVWFSFVHDHLVWESQHKSEWFHKXKWUNWFUASIHVWEHLWLMSTDWUWKUHFBWMNKSLSUWKUSVWJNWDWMKSUHKKWLIHFVWSUSVSLAYFHWDSFSDALALLWUHEIDWMSUHFDSTNLJNWVSVWISDSTKSLXKWUNWFMWLUHEHSKMAUNDHLQIKWIHLAUAHFWLLASVWESLUHFHUWEHLHLHLIWUZSEHLVWSDYNFSISDSTKSJNWVWTSSISKWUWKWFWDEWFLSBWEWBHKJNWEWBHKWDKWLMHWLUNWLMAHFVWAFMNAUAHFLWYNFNFWLMNVAHLHTKWMWPMHLVWDVASKAHWDISALVWWFKAJNWXHFMSFADDHDSENWLMKSMHESVSVLHFDHLWBWEIDSKWLVWVAUZHVASKAHINTDAUSVHLVNKSFMWNFSLWESFSUAFUNWFMSQVHLEADLWALUAWFMHLVAWUAFNWÑWDWMKSLWFMHMSDDSXKWUNWFUASVWDSLDWMKSLWFUSLMWDDSFHWLSIKHPAESVSEWFMWDSJNWLAYNW'
alphabetS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

#funcion para limpiar el texto a cifrar
def limpiar(texto):
    t = texto.upper()
    t = t.replace('Á','A')
    t = t.replace('É','E')
    t = t.replace('Í','I')
    t = t.replace('Ó','O')
    t = t.replace('Ú','U')
    remover = [' ', '.', ',', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for w in remover:
        t = t.replace(w, '')
        return t
    
#funcion para realizar cifrado cesar
def cifrarceasar(t1, clave):
    cifrado=""
    for c in t1:
        cifrado += alphabetS[((alphabetS.index(c) + clave)%27)]
    return(cifrado)
        
#funcion para realizar decifrado cesar  
def decifradoceasar(cifrado, clave):
    descifrado=""
    for c in cifrado:
        descifrado += alphabetS[((alphabetS.index(c) - clave)%27)]
    return(descifrado)

t1 = limpiar(texto)

#se hallan monogramas (simbolos)
tokens = re.findall('.', t1)

#se genera un objeto de tipo FreqDist (contiene un diccionario adentro)
freq = nltk.FreqDist(tokens)
top = freq.most_common(50)
array = [a[1] for a in top]
f = np.array(array)

#se generan las probabilidades
p = f/f.sum()
pfreq= {top[i][0]: p[i] for i in range(0, len(top))}

#frecuencias teoricas de las letras
frecuenciasteoricas = {
                                  'A': 0.11525, 'B': 0.02215, 'C': 0.04019, 'D': 0.05010
                                , 'E': 0.12181, 'F': 0.00692, 'G': 0.01768, 'H': 0.00703
                                , 'I': 0.06247, 'J': 0.00493, 'K': 0.0011,  'L': 0.04967
                                , 'M': 0.03157, 'N': 0.06712, 'Ñ': 0.0031,  'O': 0.08683
                                , 'P': 0.02510, 'Q': 0.00877, 'R': 0.06871, 'S': 0.07977
                                , 'T': 0.04632, 'U': 0.02927, 'V': 0.01138, 'W': 0.00017
                                , 'X': 0.00215, 'Y': 0.01008, 'Z': 0.00467}

errorabsoluto ={}
for i in pfreq:
    errorabsoluto.update({i: abs((frecuenciasteoricas.get(i)-pfreq.get(i))/frecuenciasteoricas.get(i))} )

#se ordena de menor a mayor segun el error absoluto obtenido
errorordenado= sorted(errorabsoluto, key =errorabsoluto.get, reverse=False)

for i in range(0,10):
    print("clave:", errorordenado[i])
    print("")
    print(decifradoceasar(t1, alphabetS.index(errorordenado[i])))
    print("")


