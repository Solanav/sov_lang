import sys
import subprocess
import itertools

def gen_truth(x, y):
    num_in = int(x) # Cuantos inputs quieres generar
    out_fi = y # Archivo en el que quieres probar
    bin_co = []
    for zero in range(0, num_in):
        bin_co.append(0)

    for i in itertools.product([0,1], repeat=num_in):
        bin_co = []
        for x in range(0,num_in):
            bin_co.append(i[x])
        bin_co2 = " ".join(map(str, bin_co))
        print("\n\n"+bin_co2)
        subprocess.call("python3 "+out_fi+" -m "+bin_co2 , shell=True)
    

        



