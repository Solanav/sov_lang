""" Library for functions """
def dand(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of and x and y 
    """
    return "if "+var0+"=="+var1+" and "+var0+"==1:\n\t"+result+"=1\nelse:\n\t"+result+"=0\n"

def dnand(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of nand x and y 
    """
    return "if "+var0+"=="+var1+" and "+var0+"==1:\n\t"+result+"=0\nelse:\n\t"+result+"=1\n"

def dor(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of or x and y 
    """
    return "if "+var0+"==1 or "+var1+"==1:\n\t"+result+"=1\nelse:\n\t"+result+"=0"

def dnor(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of or x and y 
    """
    return "if "+var0+"==1 or "+var1+"==1:\n\t"+result+"=0\nelse:\n\t"+result+"=1"

def varinput(name):
    """ creates variable and gets value with input() """
    return name+"=int(input(\""+name+" >>> \"))\n"

def var(name, value):
    """ creates variable and initialices it to 0 """
    if value == 0:
        return name+"=0\n"
    else:
        return name+"=1\n"

def printvar(name):
    """ prints given variable """
    return "print(\"\\n"+name+" >>> \"+str("+name+"))\n"

def info(data):
    """ prints info """
    print("Info: "+data)

def position(var0, list):
    """ returns postion of something in a list """
    return list.index(var0)

def clean(file):
    """ divides file in lines and instructions """
    line = file.read().split("\n")
    inst = []
    for x in line:
        inst.extend(x.split())

    return inst