import random

def digits(n):
    count = 0
    while n-int(n)>0:
        count += 1
        n *= 10
    return count

def changebit(value):
    e_probability = 0.1
    ran = random.randint(1,10**digits(e_probability))
    if ran == 1:
        if value == 0:
            return 1
        return 0
    return value

def error():
    for i in range(30):
        word = ''
        count = 0
        file = open("Archivos/EncodedFile"+str(i+1)+".txt","r")
        file2 = open("Archivos/NoisyFile"+str(i+1)+".txt","w")
        file3 = open("Archivos/OriginalNoisyFile"+str(i+1)+".txt","w")
        for line in file:
            for bit in line:
                    file2.write(str(changebit(bit)))
                    word += str(bit)
                    count += 1
                    if(count == 10):
                        word = word[:7]
                        toint = int(word,2)
                        file3.write(chr(toint))
                        word = ''
                        count = 0
        file.close()
        file2.close()
        file3.close()

error()