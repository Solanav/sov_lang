def clear(lines):
    print("\n" * lines)

def binput(data):
    while(True):
        output = int(input(data))
        if output==1 or output==0:
            return output
        else:
            print("Error: not binary input")

def neg_(in0):
    if in0 == 0:
        return 1
    else:
        return 0

def and_(in0, in1):
    if in0==1 and in1==1:
        return 1
    else:
        return 0

def nand_(in0, in1):
    return neg_(and_(in0, in1))
