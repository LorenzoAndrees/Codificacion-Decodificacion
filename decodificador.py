text_length = 4

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

def pair(A):
    count = 0
    for i in A:
        if i == 1:
            count += 1
    if count%2 == 0:
        return 0
    return 1

def productMatrix(A,B):
    C = []
    temp = [0 for col in range(len(A))]
    for j in range(len(B[0])):
        for k in range(len(B)):
            temp[k] = int(A[k])*B[k][j]
        C.append(pair(temp))
    return C

def xor(a,b):
    if a == b:
        return 0
    return 1

def xorArray(A,B):
    C = []
    for k in range(len(B)):
        C.append(xor(A[k],B[k]))
    return C

def sindrom(n, Ht):
    S = [0 for i in range(len(n))]
    for i in range(len(S)):
        S[i] = productMatrix(n[i],Ht)
    return S

def decode(word, N, Ht, S):
    bintoint = []
    for bit in word:
        bintoint.append(int(bit))
    value = productMatrix(bintoint,H_t)
    pos = 0
    for s in S:
        if value == s:
            e = N[pos]
            break
        pos += 1
    c = xorArray(bintoint,e)
    decode_word = ''
    for bit in c:
        decode_word += str(bit)
    return decode_word

def saveFile(N, Ht, S):
    for i in range(30):
        file = open("Archivos/NoisyFile"+str(i+1)+".txt","r")
        file2 = open("Archivos/DesencodedFile"+str(i+1)+".txt","w")
        file3 = open("Archivos/DesencodedOriginalFile"+str(i+1)+".txt","w")
        for line in file:
            word = ''
            count= 0
            for bit in line:
                word += bit
                count += 1
                if count == 10:
                    decoded_word = decode(word, N, Ht, S)
                    #print("Arhivo" + str(i+1) + ": {}".format(decoded_word))
                    no_parity = decoded_word[0:7]
                    toint = int(no_parity,2)
                    file2.write(decoded_word)
                    file3.write(chr(toint))
                    word = ''
                    count = 0
        file.close()
        file2.close()
        file3.close()


modification = [[0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,1]]

s = sindrom(modification,H_t)
saveFile(modification, H_t, s)