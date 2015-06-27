arquivo = open('numeros.txt','w')
for linha in range(1,10):
    arquivo.write('%d\n' % linha)
arquivo.close()
