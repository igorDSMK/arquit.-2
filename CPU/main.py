from CPU import *

C = input()
C += ".txt"
loadMemory()
loadCommand(C)

while(executando()):
    fetch()    
    exec()

attMemory()

