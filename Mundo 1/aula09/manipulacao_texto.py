print(""""
|***********************|
|     Curso em Vídeo    |
|***********************|
""")

frase = '    Curso em Vídeo Python     '

print(frase.strip())
frase = frase.strip()
print(frase.replace("Python", "Android"))
print("Curso" in frase)
print(frase.find("Vídeo"))
print(frase.find("oi"))     # Caso seja -1, não achou
print(frase.split())
dividido = frase.split()
print(">".join(dividido))

print("----Separador----")
print(frase[6])
print(frase[6:14])
print(frase[:14])
print(frase[0:15:2])
print(frase[:15:2])
print(frase[2::2])
print(frase[::2])

print("----Separador----")
print(frase.count('o'))
print(frase.upper())
print(frase.upper().count('O'))
print(len(frase))

