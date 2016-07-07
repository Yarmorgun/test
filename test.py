def openFile():
    for line in open("test.txt"):
         chunks = line.replace('%', '').replace('\n', '').split('\t')
         print(chunks[5])

openFile()
