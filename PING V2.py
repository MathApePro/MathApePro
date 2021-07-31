print ("[SCRIPT FEITA POR: MATHEUS ZK && MALWARE GHOST]")
print ("")
import os
print (">PING BY MATHEUS ZK && MALWARE GHOST<")
print ("")
print ("")
print ("CARREGANDO")
import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
        file.write("\n")
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
        file.write("\n")
    file.flush()
    
import time

for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(0.1)
print ("Carregamento concluido")
print ("")
print ("")
p = "ping " 
s = input("Digite um site aqui:") 
x = p+s 
os.system(x)
print(" TMJ VLW POR USAR O PING ")