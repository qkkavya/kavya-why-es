import sys
file_input=sys.argv[1]
file_output=sys.argv[2]
# import math

# with open ('C:\\Users\\rayak\\OneDrive\\Documents\\sample1 test.txt', 'r') as file:
#     lines=[]
#     for i in file:
#         lines.append(i.strip())

def convert_binary(n): 
    x= bin(abs(n)).replace("0b", "")
    if len(x)+1>32:
        return "error"
    if n>=0:
        return ('0'*(32-len(x))+x)
    l=len(x)+1
    final=bin(2**l+n).replace('0b',"")

    return (final[0]*(32-len(final))+final)

registers_encodings = {
    'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100',
    't0': '00101', 't1': '00110', 't2': '00111', 's0': '01000', 's1': '01001',
    'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110',
    'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011',
    's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000',
    's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101',
    't5': '11110', 't6': '11111'
}

#R type
r_type = {
    'add': '000', 'sub': '000', 'sll': '001', 'slt': '010',
    'sltu':'011', 'xor': '100','srl':'101',
    'or': '110', 'and': '111'}

def r_encoding(line,ins):
    if ins=='sub':
        funct7='0100000'
    else:
        funct7='0000000'
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
    for i in reg[:0:-1]:
        s+=registers_encodings[i]
    return funct7+s+r_type[ins]+registers_encodings[reg[0]]+"0110011"
#I type
i_type = {'addi': '000','sltiu': '011', 'lw': '010', 'jalr': '000'}
def i_encoding(line,ins):
    if ins=='lw':
        opcode='0000011'
    elif ins == 'jalr':
        opcode='1100111'
    else:
        opcode= '0010011'

    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    if "(" in reg[1]:
        num=''
        for ch in reg[1]:
            if ch.isdigit() or ch=='-':
                num+=ch
            else:
                break
        reg[1]=reg[1][reg[1].index("(")+1:-1:]

        if convert_binary(int(num))=='error':
            return 'error'
        k=convert_binary(int(num))
        for i in reg:
            if i not in registers_encodings.keys():
                return 'error'
            else:
                s+=registers_encodings[i]
        return k[20::]+s[5:]+i_type[ins]+s[:5]+opcode
    else:
        if convert_binary(int(reg[-1]))=='error':
            return 'error'
        k=convert_binary(int(reg[-1]))
        for i in reg[:-1:]:
            if i not in registers_encodings.keys():
                return 'error'
            else:
                s+=registers_encodings[i]
        return k[20::]+s[5:]+i_type[ins]+s[:5]+opcode
#B type
b_type = {'beq': '000','bne': '001','blt': '100','bge':'101'}
def b_encoding(line,ins):
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    if convert_binary(int(reg[-1]))=='error':
        return 'error'
    k=convert_binary(int(reg[-1]))
    k=k[-1::-1]
    reg=reg[0:-1]
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
        else:
            s+=registers_encodings[i]
    return k[12]+k[10:4:-1]+s+b_type[ins]+k[4:0:-1]+k[11]+"1100011"
#U type
u_type={"lui":"0110111","auipc":"0010111"}
def u_encoding(line,op):
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    if convert_binary(int(reg[-1]))=='error':
        return 'error'
    k=convert_binary(int(reg[-1]))
    k=k[-1::-1]
    reg=reg[0:-1]
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
        else:
            s+=registers_encodings[i]
        return k[31:11:-1]+s+u_type[op]
# J type
def j_encoding(line):
    reg=(line[line.index(" ")+1::]).split(',')
    if reg[0] in registers_encodings.keys():
        x=convert_binary(int(reg[1]))[::-1]
        return x[20]+x[10:0:-1]+x[11]+x[19:11:-1]+registers_encodings[reg[0]]+'1101111'
    return 'error'
# S type
def s_encoding(line,ins):
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    if "(" in reg[1]:
        num=''
        for ch in reg[1]:
            if ch.isdigit() or ch=='-':
                num+=ch
            else:
                break
        reg[1]=reg[1][reg[1].index("(")+1:-1:]

        if convert_binary(int(num))=='error':
            return 'error'
        k=convert_binary(int(num))
        for i in reg:
            if i not in registers_encodings.keys():
                return 'error'
            else:
                s+=registers_encodings[i]
        return k[11:4:-1]+s[:5]+s[5:]+"010"+k[4::-1]+"0100011"
    return 'error'
    

lists=['add','sub','sll','slt','sltu','xor','srl','or','and','lw','addi','sltiu','jalr','sw','beq','bne','blt','bge','bltu','bgeu','lui','auipc','jal','qwr']
output = sys.stdout

fobj=open("name.txt",'r')
output=open("Output.txt",'w')
data=fobj.readlines()
if 'beq zero,zero,0' not in data:
    print('error virtual hault not there')
else:
    for line in data:
        if line!=" ":
            ins=''
            line=line.strip()
            for ch in line:
                if not ch.isspace():
                    ins+=ch
                else:
                    break
            if ins not in lists:
                print(f'error {line}')
                break

            elif ins in r_type.keys():
                if r_encoding(line,ins)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(r_encoding(line,ins)+'\n')
            elif ins in i_type.keys():
                if i_encoding(line,ins)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(i_encoding(line,ins)+'\n')
            elif ins in b_type.keys():
                if b_encoding(line,ins)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(b_encoding(line,ins)+'\n')
            elif ins in u_type.keys():
                if u_encoding(line,ins)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(u_encoding(line,ins)+'\n')
            elif ins=='jal':
                if j_encoding(line)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(j_encoding(line)+'\n')
            elif ins=='sw':
                if s_encoding(line,ins)=='error':
                    print(f'error in line {line}')
                    break
                output.writelines(s_encoding(line,ins)+'\n')
            
            if line =='beq zero,zero,0':
                break

        else: 
            print(f'error in line {line}')
            break
output.close()
