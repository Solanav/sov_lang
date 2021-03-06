""" Library for functions """

def dnot(var0, result):
    """ var0 : variable a cambiar
        result: var0 inversa
    """
    return "\tif "+var0+"==1:\n\t\t"+var0+"=0\n\telse:\n\t\t"+var0+"=1\n"

    if var0==1:
        var0=0
    else:
        var0=1

def dand(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of and x and y 
    """
    return "\tif "+var0+"=="+var1+" and "+var0+"==1:\n\t\t"+result+"=1\n\telse:\n\t\t"+result+"=0\n"

def dnand(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of nand x and y 
    """
    return "\tif "+var0+"=="+var1+" and "+var0+"==1:\n\t\t"+result+"=0\n\telse:\n\t\t"+result+"=1\n"

def dor(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of or x and y 
    """
    return "\tif "+var0+"==1 or "+var1+"==1:\n\t\t"+result+"=1\n\telse:\n\t\t"+result+"=0\n"

def dnor(var0, var1, result):
    """ var0 : variable 1
        var1 : variable 2
        result : result of or x and y 
    """
    return "\tif "+var0+"==1 or "+var1+"==1:\n\t\t"+result+"=0\n\telse:\n\t\t"+result+"=1\n"

def varinput(name, number):
    """ creates variable and gets value with input() """
    return "\t"+name+"=int(sys.argv["+str(number)+"])\n"

def var(name, value):
    """ creates variable and initialices it to 0 """
    if value == 0:
        return "\t"+name+"=0\n"
    else:
        return "\t"+name+"=1\n"

def printvar(name):
    """ prints given variable """
    return "\tprint(\""+name+" >>> \"+str("+name+"))\n"

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