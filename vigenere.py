import nltk 
import re
import numpy as np
import collections
from itertools import *

letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
letras2 = 'abcdefghijklmnñopqrstuvwxyz'



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
    
def encriptado(mensaje, clave):
    mensaje_edited = mensaje.replace(' ', '')
    result = ''
    alphabet = list(letras)
    chars_mensaje = [char for char in mensaje_edited.upper()]
    chars_key = [char for char in clave.upper()]
    
    key = []
    for i in range(len(chars_mensaje)):
        key.append(chars_key[i%len(chars_key)])
        result+=alphabet[(alphabet.index(key[i])+alphabet.index(chars_mensaje[i]))%27]
    return result

def desencriptado(mensaje, clave):
    mensaje_edited = mensaje.replace(' ', '')
    result = ''
    alphabet = list(letras)
    chars_mensaje = [char for char in mensaje_edited.upper()]
    chars_key = [char for char in clave.upper()]
    
    key = []
    for i in range(len(chars_mensaje)):
        key.append(chars_key[i%len(chars_key)])
        if (alphabet.index(chars_mensaje[i])-alphabet.index(key[i])) >= 0:
            result+=alphabet[(alphabet.index(chars_mensaje[i])-alphabet.index(key[i]))%27]
        elif (alphabet.index(chars_mensaje[i])-alphabet.index(key[i])) < 0:
            result+=alphabet[((alphabet.index(chars_mensaje[i])-alphabet.index(key[i]) + 27))%27]
    return result

probabilidad_teorica = [0.1253, 0.0142, 0.0468, 0.0586, 0.1368, 0.0069, 0.0101, 0.007, 0.0625, 0.0044, 0.0002, 0.0497, 0.0315, 0.0671, 0.0031, 0.0868, 0.0251, 0.0088, 0.0687, 0.0798, 0.0463, 0.0393, 0.009, 0.0001, 0.0022, 0.009, 0.0052]
def distribucion(mensajeo):
    mensajeo = mensajeo.lower()
    tokens = re.findall('.',mensajeo)
    freq = nltk.FreqDist(tokens)

    top = freq.most_common(27)
    ordenado = collections.OrderedDict(sorted(top))
    array = []
    for letra in letras2:
        if letra in ordenado:
            array.append(ordenado[letra])
        else:
            array.append(0)
   
    f = np.array(array)
    p= f/f.sum()

    return p

def comparar(probabilidades):
    array = [abs(probabilidades[i]-probabilidad_teorica[i]) for i in range(27)]
    return array

def diccionarioOrdenado(distribuciones):
  probs = comparar(distribuciones)
  diccionario = {}
  cont = 0
  for letra in letras2:
      diccionario[letra] = probs[cont]
      cont = cont + 1
  return sorted(diccionario.items(), key=lambda x: x[1])

mensaje = 'DYEFESJKBCFSSXSDPPISSVERPOELFWMFUMSIFVHAESEUFTXHRYIQBQEVBTSVSMELBOZSSOSDBWIDWETHEIVHTEHWHYEMFPEDBOSZBFMSBTVWTEHHJPTDBGETMICVFJMFJXMÑBEQMFWYAHQSKBQGABXSIPKVSGMGSTIWWÑXSUPQXKBQUNJOMVBHEWTTIKBVOSNYIKUIUNJWSEPVMKBOOATMQFJQKNÑEILQIVSÑDESJWOSESGHÑIOIFQWSNMIFUSJAKSIFMEILQERSEMWMBQXWQEVMJGYDBVPWÑXIWÑIOUPQZWÑXSVFOSLBFVHKSWVPQHWDEVDPWUNJQXHDSQVFWGWÑHMWSEYFBZIRBFEBBVHWTYIEJQIFDMEIBVEVFGMKMIUNFGSFGMETBIQWMGIDPVIDJKMHTSHWTYOSCSVKFHIFUSVSBOHWTTIKUEVLFIQUPQXKPVSVFEHHQSVNÑKVNQSHWJQHAHIQSTHIKPWXKPMPIBWMTMIUNFWIVJWTHÑMEFBWEUSMJADEVDPEQMFYQSMXEKVQEDUEVJVIETBVXHMSPWMITSSIGAPGSEPIODFGLHFQUNFHILDEQLBVMSBOJAÑHILVWXWNSVWTHILVHILUMQHEIWANMWEPXVWTERHTIQWMTEATOIZBFMSÑGSFGIVAESYFNIHABQSVPPMFJSHWMEWDFQKNBWQSUMZSTMQMFQXHBOKHEMNHBOKNÑEWIBOETSEWJVIJNFVSFDSPISIQVJHELFQXHÑGILGOSKFGMHFQIDVQEAEIEJVIXNWSTHSHMYÑEHWTYXSMIQMPCHWTYGNMXYKBYQAWIVLBOCVFWYSSHYHDSQHDMPAFQXHEIEKJWXHUIOWTVIUPVHHRYIIBVEWTIHABWIWTTIKBFENÑIGDJTWWUSXSMHILPOCVJWTNTSIFMSPSTMQMJPSÑBOIKTIHWBUYWMGSFPGMEJIQMPTEKBIQYBREKBWYLPTVWTSVWTCWSMZEKMEZAEEWANIPSUEMLMIWVJNSIVIHHIEGWSUYWFOWHMWIHTGYKFDGSFQWNBOXNSEOHTMQVJKIFBWOHNMVSSSQXJNEEFQXWZFEKUSOHNIWHSTVWÑHMHMEMFDVIVVOMVBHIFTYWHKSWÑJSUNFWIISSHNKSYFQIUNFRSUPQWWKSCWTTIKPGSFGMEVPQSLJQGAFVXHEIWVFQHHTLSKBWHWTTYWTIOUPVERPQHWGVEQCEVMPOSEFEVKBDSDBGLHSVISCEWNTEQYSIZWIIPWÑXILPFVWMETAFHVSEIOHTWEUSMJADMSLCVMDMEQMFFEBPOEHQEGSMYDVFYQLPOIUMMTLBHSEJIQMSEWNÑSHWMSWAÑHMYFQELSIGAUEFSTMQFJQKNÑEMFGOIPJSQVFZSRTMQISMWSVQEIPVYFBOELJQJAÑMXSTJIUIEWWÑUYWTITKPHYUJVMSÑIGDJTWWTWSDBVILZOYFBVILRYIDPWELUVSFPPSLEIOSDSPNÑMHSEPEQBLETJEQISIZATXSQBQSMBHSWÑWYLDSHADIWLJQOSWEOAPWESZYHSEIEKJWXHUIOWT'

limite = 10
llave = ''
for clave in [''.join(tupla) for tupla in list(product(letras2,repeat=4))]:
    suma = sum(comparar(distribucion(desencriptado(mensaje, clave))))
    if suma < limite:
      limite = suma
      llave = clave
  
print('\nError abosluto: ',limite, '\n')
print('Clave: ',llave, '\n')
print('Mensaje Descifrado: ', desencriptado(mensaje, llave), '\n')

