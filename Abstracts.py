#Take Abstract part which starts from AB and ends to C1 in file

file=open('D:/wos_1-500 -.txt')

abstract=list()
flag=False
for word in file:
    if word.startswith('AB'):
        flag=True
    if word.startswith('C1'):
            print(''.join(abstract))
            abstract=list()
            flag= False
    if flag:
        abstract.append(word)           







