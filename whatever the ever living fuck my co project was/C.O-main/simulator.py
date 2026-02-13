import sys
file_input=sys.argv[1]
file_output=sys.argv[2]
#reg values
# sourcery skip: remove-duplicate-dict-key
reg_values = {
    'zero':'00000000000000000000000000000000', 'ra':'00000000000000000000000000000000', 'sp':'00000000000000000000000000000000',
    'gp':'00000000000000000000000000000000', 'tp':'00000000000000000000000000000000', 't0':'00000000000000000000000000000000',
    't1':'00000000000000000000000000000000', 't2':'00000000000000000000000000000000', 's0':'00000000000000000000000000000000',
    's1':'00000000000000000000000000000000', 'a0':'00000000000000000000000000000000', 'a1':'00000000000000000000000000000000',
    'a2':'00000000000000000000000000000000', 'a3':'00000000000000000000000000000000', 'a4':'00000000000000000000000000000000',
    'a5':'00000000000000000000000000000000', 'a6':'00000000000000000000000000000000', 'a7':'00000000000000000000000000000000',
    's2':'00000000000000000000000000000000', 's3':'00000000000000000000000000000000', 's4':'00000000000000000000000000000000',
    's5':'00000000000000000000000000000000', 's6':'00000000000000000000000000000000', 's7':'00000000000000000000000000000000',
    's8':'00000000000000000000000000000000', 's9':'00000000000000000000000000000000', 's10':'00000000000000000000000000000000',
    's11':'00000000000000000000000000000000', 't3':'00000000000000000000000000000000', 't4':'00000000000000000000000000000000',
    't5':'00000000000000000000000000000000', 't6':'00000000000000000000000000000000'
}

#memory allocation of registers
memory = {
    '0x00010000': '00000000000000000000000000000000', '0x00010004': '00000000000000000000000000000000',
    '0x00010008': '00000000000000000000000000000000', '0x0001000c': '00000000000000000000000000000000', 
    '0x00010010': '00000000000000000000000000000000', '0x00010014': '00000000000000000000000000000000',
    '0x00010018': '00000000000000000000000000000000', '0x0001001c': '00000000000000000000000000000000',
    '0x00010020': '00000000000000000000000000000000', '0x00010024': '00000000000000000000000000000000',
    '0x00010028': '00000000000000000000000000000000', '0x0001002c': '00000000000000000000000000000000',
    '0x00010030': '00000000000000000000000000000000', '0x00010034': '00000000000000000000000000000000',
    '0x00010038': '00000000000000000000000000000000', '0x0001003c': '00000000000000000000000000000000',
    '0x00010040': '00000000000000000000000000000000', '0x00010044': '00000000000000000000000000000000',
    '0x00010048': '00000000000000000000000000000000', '0x0001004c': '00000000000000000000000000000000',
    '0x00010050': '00000000000000000000000000000000', '0x00010054': '00000000000000000000000000000000',
    '0x00010058': '00000000000000000000000000000000', '0x0001005c': '00000000000000000000000000000000',
    '0x00010060': '00000000000000000000000000000000', '0x00010064': '00000000000000000000000000000000',
    '0x00010068': '00000000000000000000000000000000', '0x0001006c': '00000000000000000000000000000000',
    '0x00010070': '00000000000000000000000000000000', '0x00010074': '00000000000000000000000000000000',
    '0x00010078': '00000000000000000000000000000000', '0x0001007c': '00000000000000000000000000000000'
}

#dictionary for storing reg values
dict_registers = {
    '00000': '00000000000000000000000000000000',
    '00001': '00000000000000000000000000000000',
    '00010': '00000000000000000000000100000000',
    '00011': '00000000000000000000000000000000',
    '00100': '00000000000000000000000000000000',
    '00101': '00000000000000000000000000000000',
    '00110': '00000000000000000000000000000000',
    '00111': '00000000000000000000000000000000',
    '01000': '00000000000000000000000000000000',
    '01001': '00000000000000000000000000000000',
    '01010': '00000000000000000000000000000000',
    '01011': '00000000000000000000000000000000',
    '01100': '00000000000000000000000000000000',
    '01101': '00000000000000000000000000000000',
    '01110': '00000000000000000000000000000000',
    '01111': '00000000000000000000000000000000',
    '10000': '00000000000000000000000000000000',
    '10001': '00000000000000000000000000000000',
    '10010': '00000000000000000000000000000000',
    '10011': '00000000000000000000000000000000',
    '10100': '00000000000000000000000000000000',
    '10101': '00000000000000000000000000000000',
    '10110': '00000000000000000000000000000000',
    '10111': '00000000000000000000000000000000',
    '11000': '00000000000000000000000000000000',
    '11001': '00000000000000000000000000000000',
    '11010': '00000000000000000000000000000000',
    '11011': '00000000000000000000000000000000',
    '11100': '00000000000000000000000000000000',
    '11101': '00000000000000000000000000000000',
    '11110': '00000000000000000000000000000000',
    '11111': '00000000000000000000000000000000'
}

   # sourcery skip: simplify-numeric-comparison

# r type funcs

# binary to decimal and vice versa conversion
def decimal_to_binary(n):
    if n < 0:
        n = (1<<32) + n
    format_string = '{:0>' + str(32) + '}'
    return format_string.format(bin(n)[2:])

def binary_to_decimal(binary_string):
    if binary_string[0] == '1':
        return -1 * (int(''.join('1' if b == '0' else '0' for b in binary_string), 2) + 1)
    else:
        return int(binary_string, 2)

def binary_addition(a, b):  
    max_len = 32
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0

    # Traverse both strings from right to left
    for i in range(max_len-1, -1, -1):
        temp = carry
        temp += 1 if a[i] == '1' else 0
        temp += 1 if b[i] == '1' else 0
        result = ('1' if temp % 2 == 1 else '0') + result
        carry = 0 if temp < 2 else 1       

    if carry != 0: 
        result = f'1{result}'

    return result.zfill(max_len)
def binary_subtraction(a, b):
    # Convert b to its 2's complement form
    b = ''.join('1' if bit == '0' else '0' for bit in b)
    b = binary_addition(b, '1')

    # Perform binary addition
    result = binary_addition(a, b)

    # Ignore overflow
    result = result[-32:]

    return result
def binary_to_decimal_unsigned(binary_string):
    return int(binary_string, 2)
def R_type(ins):  # sourcery skip: for-index-underscore, low-code-quality, use-fstring-for-concatenation
    if ins[-32:-25]=="0100000":
        if ins[-20:-15]=='00000':
            dict_registers[ins[-12:-7]]=binary_subtraction('0', dict_registers[ins[-20:-15]])
            return
        dict_registers[ins[-12:-7]]=binary_subtraction(dict_registers[ins[-20:-15]], dict_registers[ins[-25:-20]])
        return
    elif ins[-15:-12]=="000":
        dict_registers[ins[-12:-7]]=binary_addition(dict_registers[ins[-20:-15]], dict_registers[ins[-25:-20]])
        return
    #doubt
    elif ins[-15:-12]=="001":
        x=binary_to_decimal_unsigned(dict_registers[ins[-25:-20]][-5::])
        dict_registers[ins[-12:-7]]=decimal_to_binary(binary_to_decimal(dict_registers[ins[-20:-15]])<<x)
        return
    elif ins[-15:-12]=="010":
        if binary_to_decimal(dict_registers[ins[-20:-15]]) < binary_to_decimal(dict_registers[ins[-25:-20]]):
            dict_registers[ins[-12:-7]]=decimal_to_binary(1)
            return
    elif ins[-15:-12]=="011":
        if binary_to_decimal_unsigned(dict_registers[ins[-20:-15]]) < (binary_to_decimal_unsigned(dict_registers[ins[-25:-20]])):
            dict_registers[ins[-12:-7]]=decimal_to_binary(1)
            return
    elif ins[-15:-12]=="100":
        a=dict_registers[ins[-20:-15]]
        b=dict_registers[ins[-25:-20]]
        x=''.join('0' if a[i]==b[i] else '1' for i in range(32))
        dict_registers[ins[-12:-7]]=x
        return
    elif ins[-15:-12]=="101":
        x=binary_to_decimal_unsigned(dict_registers[ins[-25:-20]][-5::])
        dict_registers[ins[-12:-7]]=decimal_to_binary(binary_to_decimal(dict_registers[ins[-20:-15]])>>x)

        #right shift will solve later
    elif ins[-15:-12]=="110":
        x=binary_to_decimal(dict_registers[ins[-25:-20]])
        y=binary_to_decimal(dict_registers[ins[-20:-15]])
        dict_registers[ins[-12:-7]]=decimal_to_binary(x|y)
    elif ins[-15:-12]=="111":
        print(dict_registers[ins[-25:-20]],dict_registers[ins[-20:-15]],dict_registers[ins[-25:-20]],sep='  ')
        x=binary_to_decimal(dict_registers[ins[-25:-20]])
        y=binary_to_decimal(dict_registers[ins[-20:-15]])
        dict_registers[ins[-12:-7]]=decimal_to_binary(x&y)
        return

#s type
def binary_to_hex(binary_string):
    return hex(int(binary_string, 2))
def S_type(ins):
    x=binary_addition(dict_registers[ins[-20:-15]],ins[0]*20+ins[-32:-25]+ins[-12:-7])
    y=binary_to_hex(x)
    if len(y)<10:
        y=y[:2]+'0'*(10-len(y))+y[2:]
    memory[y]=dict_registers[ins[-25:-20]]

#i type
def I_type(ins):  # sourcery skip: remove-redundant-if
    global pc
    if ins[25:32]=="0000011":
        if ins[-15:-12]=='010':
            x=binary_addition(dict_registers[ins[-20:-15]],ins[0]*20+ins[-32:-20])
            y=binary_to_hex(x)
            if len(y)<10:
                y=y[:2]+'0'*(10-len(y))+y[2:]
            print(y)
            dict_registers[ins[-12:-7]]=memory[y]
            prev=pc
            pc+=1
            return
    elif ins[25:32]=="0010011":
        if ins[-15:-12]=='000':
            dict_registers[ins[-12:-7]]=binary_addition(dict_registers[ins[-20:-15]],ins[0]*20+ins[-32:-20])
            prev=pc
            pc+=1
            return
    elif ins[25:32]=="0010011":
# sourcery skip: merge-nested-ifs
        if ins[-15:-12]=='011':
           if binary_to_decimal_unsigned(dict_registers[ins[-20:-15]]) < binary_to_decimal_unsigned(ins[-32:-20]):
            dict_registers[ins[-12:-7]]=decimal_to_binary(1)
        prev=pc
        pc+=1
        return

    elif ins[25:32]=="1100111":
        if ins[12:15]=='000':
            dict_registers[ins[-12:-7]]=decimal_to_binary(pc+1)
            d = f'{decimal_to_binary(pc)[:31]}0'
            a=binary_addition(reg_values['t1'],ins[0]*20+ins[-32:-20])
            prev=pc
            pc = f'{a[:31]}0'
            return
#u type instructions
def auipc(instruction_bin):
    # sourcery skip: inline-immediately-returned-variable
    global pc,prev
    instruction = binary_to_decimal(instruction_bin[-32:-12])<<12
    new=binary_addition(decimal_to_binary(prev*4),decimal_to_binary(instruction))
    return new
def U_type(ins):
    for i in dict_registers.keys():
        if ins[-12:-7]==i:
            a=i
            break
    if ins[-7::]=="0010111":
        dict_registers[a]=auipc(ins)
    elif ins[-7::]=="0110111":
        dict_registers[a]=decimal_to_binary(binary_to_decimal(ins[-32:-12])<<12)
    
        
#b type

def B_type(ins):
    global pc
    rs2 = dict_registers[ins[7:12]]
    rs1 = dict_registers[ins[12:17]]
    if ins[-15:-12]=='000':
        if binary_to_decimal(rs1)==binary_to_decimal(rs2):
            x=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
            print(x)
            print(pc+x)
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
        else:
            prev=pc
            pc+=1
        return
    if ins[-15:-12]=='001':
        if binary_to_decimal(rs1)!= binary_to_decimal(rs2):
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
        else:
            prev=pc
            pc+=1
        return
    if ins[-15:-12]=='100':
        if binary_to_decimal(rs1)<binary_to_decimal(rs2):
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[1:7] + ins[20:24] + "10")
        else:
            prev=pc
            pc+=1
        return
    if ins[-15:-12]=='101':
        if binary_to_decimal(rs1) >= binary_to_decimal(rs2):
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
        else:
            prev=pc
            pc+=1
        return

    if ins[-15:-12]=='110':
        if binary_to_decimal_unsigned(rs1) < binary_to_decimal_unsigned(rs2):
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
        else:
            prev=pc
            pc+=1
        return 

    if ins[-15:-12]=='111':
        if binary_to_decimal_unsigned(rs1) >= binary_to_decimal_unsigned(rs2):
            if binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")==0:
                prev=pc
                pc+=1
                return
            prev=pc
            pc+=binary_to_decimal(ins[24] + ins[1:7] + ins[20:24] + "0")
        else:
            prev=pc
            pc+=1
        return
#j type instructions
def J_type(ins):
    global pc,prev
    dict_registers[ins[-12:-7]]=decimal_to_binary(pc+4)
    y = f'{decimal_to_binary(pc)[:31]}0'
    x=decimal_to_binary(binary_to_decimal(ins[-32:-12])<<1)
    prev=pc
    pc=binary_to_decimal(binary_addition(x,y))
    return
#main function
with open(sys.argv[1],"r") as fobj:
    lines=fobj.readlines()
    n=len(lines)
with open(sys.argv[2],"w") as output:
    pc=1
    prev=1
    while pc<=n and (lines[pc-1].strip()!="00000000000000000000000001100011"):
        output.write(f'0b{decimal_to_binary(pc * 4)} ')
        line=lines[pc-1].strip()
        if line[-7::]=='0110011':
            R_type(line)
            prev=pc
            pc+=1
        elif line[-7::] in ['0000011','0010011','1100111']:
            I_type(line)
        elif line[-7::]=='0100011':
            S_type(line)
            prev=pc
            pc+=1
        elif line[-7::]=='1100011':
            B_type(line)
        elif line[-7::] in ['0010111','0110111']:
            U_type(line)
            prev=pc
            pc+=1
        elif line[-7::]=='1101111':
            J_type(line)
        else:
            pc+=1
        v=dict_registers.values()
        for i in v:
            output.write(f'0b{i} ')
        output.write('\n')
    output.write(f'0b{decimal_to_binary(prev*4)} ')
    for i in dict_registers.values():
        output.write(f'0b{i} ')
    output.write('\n')
    for key, value in memory.items():
        output.write(f'{key}:0b{value}\n')
    

