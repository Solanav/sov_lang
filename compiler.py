import sys
import lib

def clean(file0):
    """ Gets instructions out of file
        and returns them in a list

        file0 : file to clean
    """
    line = file0.read().split("\n")
    inst = []
    for x in line:
        inst.extend(x.split())

    return inst

def sovpile(inst):
    """ Takes instructions and writes the python
        equivalent in a new file named the same as
        the .sov one but with .py extension

        inst : instructions from the clean() function
    """
    num_bits = 0
    file0 = open(sys.argv[1].split(".")[0] + ".py", "w+")
    file0.write("import sys\n")
    file0.write("if sys.argv[1] == \"-m\":\n")
    for inst_name in inst:
        if inst_name == "in":
            sov = True
            argv_num = 2
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst[pos] == "in.":
                    sov = False
                else:
                    file0.write(lib.varinput(inst[pos], argv_num))
                pos = pos + 1
                argv_num = argv_num + 1
            num_bits = argv_num - 3
        elif inst_name == "var":
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst[pos] == "var.":
                    sov = False
                else:
                    if "*" in inst[pos]:
                        var_name = inst[pos].split("*")
                        file0.write(lib.var(var_name[1], 1))
                    else:
                        file0.write(lib.var(inst[pos], 0))
                pos = pos + 1
        
        elif "not" in inst_name:
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst_name == "not.":
                    sov = False
                else:
                    if pos+2 < len(inst):
                        if inst[pos + 2] == "not.":
                            lib.info("Data correct for "+inst_name)
                            var0 = inst[pos]
                            result = inst[pos + 1]
                            file0.write(lib.dnot(var0, result))
                            sov = False

        elif "and" in inst_name and "nand" not in inst_name :
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst_name == "and.":
                    sov = False
                else:
                    if pos+3 < len(inst):
                        if inst[pos + 3] == "and.":
                            lib.info("Data correct for "+inst_name)
                            var0 = inst[pos]
                            var1 = inst[pos + 1]
                            result = inst[pos + 2]
                            file0.write(lib.dand(var0, var1, result))
                            sov = False
                pos = pos + 1

        elif "nand" in inst_name:
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst_name == "nand.":
                    sov = False
                else:
                    if pos+3 < len(inst):
                        if inst[pos + 3] == "nand.":
                            lib.info("Data correct for "+inst_name)
                            var0 = inst[pos]
                            var1 = inst[pos + 1]
                            result = inst[pos + 2]
                            file0.write(lib.dnand(var0, var1, result))
                            sov = False
                pos = pos + 1

        elif "or" in inst_name and "nor" not in inst_name:
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst_name == "or.":
                    sov = False
                else:
                    if pos+3 < len(inst):
                        if inst[pos + 3] == "or.":
                            lib.info("Data correct for "+inst_name)
                            var0 = inst[pos]
                            var1 = inst[pos + 1]
                            result = inst[pos + 2]
                            file0.write(lib.dor(var0, var1, result))
                            sov = False
                pos = pos + 1

        elif "nor" in inst_name:
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst_name == "nor.":
                    sov = False
                else:
                    if pos+3 < len(inst):
                        if inst[pos + 3] == "nor.":
                            lib.info("Data correct for "+inst_name)
                            var0 = inst[pos]
                            var1 = inst[pos + 1]
                            result = inst[pos + 2]
                            file0.write(lib.dnor(var0, var1, result))
                            sov = False
                pos = pos + 1

        elif inst_name == "print":
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst[pos] == "print.":
                    sov = False
                else:
                    file0.write(lib.printvar(inst[pos]))
                pos = pos + 1
        

    ending = """
elif sys.argv[1] == "-a":
    try:
        import truth_table
    except ImportError:
        print("ERROR: truth_table.py couldn't be found, please use manual (-m) mode.")
        exit()
    truth_table.gen_truth({0}, sys.argv[0])
    """
    file0.write(ending.format(num_bits))

def main():
    if sys.argv[1].split(".")[1] == "sov": # Check  if file is .sov
        file0 = open(sys.argv[1], "r")
        inst = clean(file0)
        sovpile(inst)
        print(">>> Completed <<<")
    else:
        print("error")

if __name__=="__main__":
    main()
