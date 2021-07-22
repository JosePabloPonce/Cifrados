import math

abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
n = len(abc)
texto = "caracola"
llave = [5, 8]
k1 = 5
k2 = 8

#Se implemento el algoritmo euclidiano para encontrar el modulo inverso.
#https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
def egcd(a, b): 
  x,y, u,v = 0,1, 1,0
  while a != 0: 
    q, r = b//a, b%a 
    m, n = x-u*q, y-v*q 
    b,a, x,y, u,v = a,r, u,v, m,n 
  gcd = b 
  return gcd, x, y

def invmod(a, n): 
  gcd, x, y = egcd(a, n)
  #Cuando no tiene modulo inverso.
  if gcd != 1: 
    return None 
  else: 
    return x % n

#Implementacion del Cifrado Afin.
#Encrptar
def CifradoAfin(texto, llave):       
    cripto = ""
    for letra in texto: 
        mi = abc.index(letra.upper())
        ci = ((k1*mi)+k2) % n
        cripto += abc[ci]
            
    return(cripto)

#Desencriptar
def DesAfin(cripto, llave):
    if math.gcd(k1, n) != 1:
        print("No se puede cifrar")
    
    else:
        texto = ""
        for letra in cripto: 
            ci = abc.index(letra.upper())
            mi = int(invmod(k1, n) *(ci-k2+27 if ci-k2 < 0 else ci-k2)% n)
            texto += abc[mi]
        return(texto)

enc_text = CifradoAfin(texto, llave) 
print('Texto Encripado: {}'.format(enc_text))

print('Texto : {}'.format(DesAfin(enc_text, llave)))
