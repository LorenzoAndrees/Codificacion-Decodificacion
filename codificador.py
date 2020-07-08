text_length = 4

def pair(A):
    count = 0
    for i in A:
        if i == 1:
            count += 1
    if count%2 == 0:
        return 0
    return 1

def msgtobin():
    letters = []
    for i in range(30):
        file = open("Archivos/OriginalFile"+str(i+1)+".txt","r")
        letters.append([])
        for line in file:
            for ch in line:
                letters[i].append(bin(ord(ch))[2:])
        file.close()
    return letters

def productMatrix(A,B):
    C = []
    temp = [0 for col in range(len(A))]
    for j in range(len(B[0])):
        for k in range(len(B)):
            temp[k] = int(A[k])*B[k][j]
        C.append(pair(temp))
    return C

def codificacion(OriginalMatrix,GenerationalMatrix,n):
    for i in range(30):
        file = open("Archivos/EncodedFile"+str(i+1)+".txt","w")
        for col in range(n):
            bintoint = []
            for bit in OriginalMatrix[i][col]:
                bintoint.append(int(bit))
            for k in productMatrix(bintoint,GenerationalMatrix):
                file.write(str(k))
        file.close()


P = [[1,0,1,1,0,1,1],
     [1,1,0,1,1,0,1],
     [1,1,1,0,1,1,1]]

G = [[1,0,0,0,0,0,0,1,1,1],
     [0,1,0,0,0,0,0,0,1,1],
     [0,0,1,0,0,0,0,1,0,1],
     [0,0,0,1,0,0,0,1,1,0],
     [0,0,0,0,1,0,0,0,1,1],
     [0,0,0,0,0,1,0,1,0,1],
     [0,0,0,0,0,0,1,1,1,1]]

H = [[1,0,1,1,0,1,1,1,0,0],
     [1,1,0,1,1,0,1,0,1,0],
     [1,1,1,0,1,1,1,0,0,1]]

H_t = [[1,1,1],
       [0,1,1],
       [1,0,1],
       [1,1,0],
       [0,1,0],
       [0,0,1],
       [1,1,1],
       [1,0,0],
       [0,1,0],
       [0,0,1]]

vector = msgtobin()
codificacion(vector,G,text_length)