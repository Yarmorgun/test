def openFile():
    for line in open("test.txt"):
         chunks = line.replace('%', '').replace('\n', '').split('\t')
         print(chunks[2])

openFile()
