with open('Encoding.txt','w',encoding='utf-8') as f:
    f.write('Hi🙂')

with open('Encoding.txt','r',encoding='utf-8') as f:
    print(f.read())