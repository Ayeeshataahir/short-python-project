#print title and abstract one by one in single file

file=open('D:/wos_1-500 -.txt')
titleabstract= list()
 
data_file=list()
flag=False
for text in file:
    if text.startswith('TI'):
        flag=True
    if text.startswith('SO'):
            print(''.join(data_file))
            data_file=list()
            flag= False
    if flag:
        data_file.append(text)
    if text.startswith('AB'):
         titleabstract.append(text)
         print(text)
