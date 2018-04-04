#pipeline
memory = []
command = []
PC = 1
RI = []
r1 = 0
r2 = 0
r3 = 0
r4 = 0
termino = 0
altmem = 0

def convertRint(x):
    if RI[x] == 'r1':
        RI[x] = r1
    elif RI[x] == 'r1\n':
        RI[x] = r1
    elif RI[x] == 'r2':
        RI[x] = r2
    elif RI[x] == 'r2\n':
        RI[x] = r2
    elif RI[x] == 'r3':
        RI[x] = r3
    elif RI[x] == 'r3\n':
        RI[x] = r3
    elif RI[x] == 'r4':
        RI[x] = r4
    elif RI[x] == 'r4\n':
        RI[x] = r4
    else:
        RI[x] = int(RI[x])
    return

def convertRfloat(x):
    if RI[x] == 'r1':
        RI[x] = r1
    elif RI[x] == 'r1\n':
        RI[x] = r1
    elif RI[x] == 'r2':
        RI[x] = r2
    elif RI[x] == 'r2\n':
        RI[x] = r2
    elif RI[x] == 'r3':
        RI[x] = r3
    elif RI[x] == 'r3\n':
        RI[x] = r3
    elif RI[x] == 'r4':
        RI[x] = r4
    elif RI[x] == 'r4\n':
        RI[x] = r4
    else:
        RI[x] = float(RI[x])		
    return
	
def PZ(possZ):
    global termino
    if possZ == 0:
        print("tentantiva de divisão por 0, programa abortado")
        termino = 1
        return 0
    return 1
    
def loadMemory():
    memoria = open("memoria.txt","r")    
    global memory
    for line in memoria:
        memory.append(line)
    memoria.close()
    return

def loadCommand(txt):
    comando = open(txt,"r")
    global command
    global RI
    for line in comando:
        command.append(line.split(" "))
    comando.close()
    return

def fetch():
    global PC, RI
    RI[:] = command[PC-1]
    PC = PC + 1
    return

def decod():
    return{
        'ADD':1,
        'SUB':2,
        'MUL':3,
        'DIV':4,
        'MOV':5,
        'JMP':6,
        'JL':7,
        'JZ':8,
        'JG':9,
        'READ':10,
        'STORE':11,
        'END':12,
        'PRINT':13,
        'ESCREVAL':14,
        'GETINT':15,
	'GETFLOAT':16,
	'ADDF':17,
	'SUBF':18,
	'MULF':19,
	'DIVF':20,
        'INC':21,
        }[RI[0]]

def exec():
    op = decod()
    global r1, r2, r3, r4, termino, altmem, PC
    if op == 1: #add
        convertRint(1)
        convertRint(2)
        r1 = int(RI[1] + RI[2])
    elif op == 2: #sub
        convertRint(1)
        convertRint(2)
        r1 = int(RI[1] - RI[2])
    elif op == 3: #mul
        convertRint(1)
        convertRint(2)
        r1 = int(RI[1] * RI[2])
    elif op == 4: #div
        convertRint(1)
        convertRint(2)
        if PZ(RI[2]):
            r2 = RI[1] % RI[2]
            r1 = RI[1] // RI[2]
    elif op == 5: #mov
        convertRint(2)
        if RI[1] == 'r1':
            r1 = RI[2]
        elif RI[1] == 'r2':
            r2 = RI[2]
        elif RI[1] == 'r3':
            r3 = RI[2]
        else:
            r4 = RI[2]
    elif op == 6: #jmp
        convertRint(1)
        PC = RI[1]
    elif op == 7: #jl
        convertRint(1)
        if r1 < 0:
            PC = RI[1]
    elif op == 8: #jz
        convertRint(1)
        if r1 == 0:
            PC = RI[1]         
    elif op == 9: #jg
        convertRint(1)
        if r1 > 0:
            PC = RI[1]        
    elif op == 10: #read
        convertRint(2)
        if RI[1] == 'r1':
            r1 = int(memory[RI[2] - 1])
        elif RI[1] == 'r2':
            r2 = int(memory[RI[2] - 1])
        elif RI[1] == 'r3':
            r3 = int(memory[RI[2] - 1])
        else:
            r4 = int(memory[RI[2] - 1])
    elif op == 11: #store
        convertRint(1)
        convertRint(2)
        memory[RI[1] - 1] = str(RI[2]) + '\n'
        altmem = 1
    elif op == 12: #end
        termino = 1
    elif op == 13: #print
        R = RI[1].split("\n")
        print(R[0])
    elif op == 14: #escreval
        convertRfloat(1)
        print(RI[1])
    elif op == 15: #getint
        x = input()
        if RI[1] == 'r1\n':
            r1 = int(x)
        elif RI[1] == 'r2\n':
            r2 = int(x)
        elif RI[1] == 'r3\n':
            r3 = int(x)
        else:
            r4 = int(x)
    elif op == 16: #getfloat
        x = input()
        if RI[1] == 'r1\n':
            r1 = float(x)
        elif RI[1] == 'r2\n':
            r2 = float(x)
        elif RI[1] == 'r3\n':
            r3 = float(x)
        else:
            r4 = float(x)
    elif op == 17: #addf
        convertRfloat(1)
        convertRfloat(2)
        r1 = RI[1] + RI[2]
    elif op == 18: #subf
        convertRfloat(1)
        convertRfloat(2)
        r1 = RI[1] - RI[2]
    elif op == 19: #mulf
        convertRfloat(1)
        convertRfloat(2)
        r1 = RI[1] * RI[2]
    elif op == 20: #divf
        convertRfloat(1)
        convertRfloat(2)
        if PZ(RI[2]):
            r1 = RI[1] / RI[2]
    elif op == 21: #inc
        if RI[1] == 'r1\n':
            r1 += 1 
        elif RI[1] == 'r2\n':
            r2 += 1
        elif RI[1] == 'r3\n':
            r3 += 1
        else:
            r4 += 1
    else:
        print("ERRO DE DECODIFICAÇÃO")
    return

def attMemory():    
    if altmem:
        memoria = open("memoria.txt","w")    
        for element in memory:
            memoria.write(element)
        memoria.close()
    return


C = input()   
loadMemory()
loadCommand(C)
while(termino == 0):
    fetch()
    exec()
#attMemory()
