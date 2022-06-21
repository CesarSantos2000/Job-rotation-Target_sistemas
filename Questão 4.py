texto = str(input())
n = len(texto)
texto_invertido = ""
for i in range(n-1, -1, -1):
     texto_invertido = texto_invertido + texto[i]
print(texto_invertido)
