for i in range(30):
    count = 0
    fileone = []
    filetwo = []
    file2 = open("Archivos/NoisyFile"+str(i+1)+".txt","r")
    file = open("Archivos/EncodedFile"+str(i+1)+".txt","r")
    fileone = file.readline()
    filetwo = file2.readline()
    for k in range(len(fileone)):
        if fileone[k] != filetwo[k]:
            count +=1
    print("Archivo {}: {} errores".format(i+1,count))