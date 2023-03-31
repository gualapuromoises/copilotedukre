import sys
fh = open("hemo_flebo.fasta",'r')
fh.readline()
file = fh.readlines() 
x = file

def gcp(x):
    c=0
    a=0
    g=0
    t=0

    for n in x:
        if "C" in n:
            c+=1    
        elif "G" in n:
            g+=1
        elif "A" in n:
            a+=1    
        elif "T" in n:
            t+=1
    print("C=%d, G=%d, A=%d, T=%d" %(c,g,a,t))
    gc_content=round((g+c)*100/(a+t+g+c),2)
    print ("gc_content= %2.2f" %(gc_content))
    return list([x, a, t, g, c, gc_content])

result = gcp(x)
print(result)