#Take Title part TI from file

file=open('D:/wos_1-500 -.txt')

title=list()
flag=False
for word in file:
    if word.startswith('TI'):
        flag=True
    if word.startswith('SO'):
            print(''.join(title))
            title=list()
            flag= False
    if flag:
            title.append(word)






