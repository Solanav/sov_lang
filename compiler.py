import sys
import lib

def clean(file0): # divides file in lines and instructions
    line = file0.read().split("\n")
    inst = []
    for x in line:
        inst.extend(x.split())

    return inst

def sovpile(inst): # creates file compiled into python
    file0 = open(sys.argv[1].split(".")[0] + ".py", "w+")
    for inst_name in inst:
        if inst_name == "in":
            sov = True
            pos = lib.position(inst_name, inst) + 1
            while sov:
                if inst[pos] == "in.":
                    sov = False
                else:
                    file0.write(lib.varinput(inst[pos]))
                pos = pos + 1

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
                            var1 = inst[pos]
                            var2 = inst[pos + 1]
                            var3 = inst[pos + 2]
                            file0.write(lib.nand(var1, var2, var3))
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


def main():
    file0 = open(sys.argv[1], "r")
    inst = clean(file0)
    sovpile(inst)
    print(">> Completed <<<")

if __name__=="__main__":
    main()
