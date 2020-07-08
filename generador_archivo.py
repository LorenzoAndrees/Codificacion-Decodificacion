import random, string, os

text_length = 4

def generarArchivos(n):
    for i in range(30):
        file = open("Archivos/OriginalFile"+str(i+1)+".txt","w")
        for _ in range(n):
            file.write(random.choice(string.ascii_uppercase))
        file.close()

generarArchivos(text_length)