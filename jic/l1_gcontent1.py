seq = input("Ingrese su secuencia:").upper()

g = seq.count("G")
c = seq.count("C")
n = len(seq)
gc = round(100*(g+c)/n,3)

print("Secuencia: ", seq, "\nLongitud: ", n, "\nPorcentaje GC: ", gc)