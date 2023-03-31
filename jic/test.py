nombres = "melanogaster,simulans,albopictus,aegypti"
especies = nombres.split(",")
print(str(especies))

proteina = "vlspadktnv"
subp = proteina[3:6]
print(subp)

adn = "ATCGATCACGATCTATCGTCGTACGTATGATATCTAGATATCGATCGTAGTC"
gcp = round(100*(adn.count("G")+adn.count("C"))/len(adn), 2)
print("Porcentaje de GC: "+str(gcp)+"%")

inicio = [5, 19]
pare = [32, 45]

codigo = []
for i in range(len(inicio)):
    exon = adn[inicio[i]:pare[i]]
    codigo.append(exon)
    print("Exon" + str(i+1) +": "+ codigo[i])

def gcp(dna):
    gcper = round(100*(adn.count("G")+adn.count("C"))/len(adn), 2)
    return gcper
print(gcp("ATCG"))


def aa_porcent(protein, aa):
    aa_contar = protein.count(aa)
    N_protein = len(protein)
    aa_porcentaje = aa_contar * 100 / N_protein
    return [protein, aa, aa_porcentaje]
print(aa_porcent("MSRSLLLRFLLFLLLLPPLP", "M"))

file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    else:
        file3.write(accession + "\n")

accs = ['ab56', 'gt84', 'abc5', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
result = []
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        result.append(acc)
print(result)
print(len(result))


pacientes = {"Paciente1": 'AGEKGKKIFVQKCSQCLTVCSQCHTVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA', 
             "Paciente2": 'AGAKGKKIFVQKCSQCHTVCSQCHTVEKGGKHKTGPNEKGKKIVVQKCSQCLTVLLGLFGRKTGQA',
             "Paciente3": 'AGAKGKKIFVQKCSQCLTVCSQCHTVEKGGKHTVCSQEKGKKIVVQKCSQCLTVLLGLFGRKTGQA', 
             "Paciente4": 'AGEKGKKIFVQKCSQCLTVCSQCHTVEKGGKHKTGPNEKGKKIFVQTAKCSQCHTVLLAKTGHLQA', 
             "Paciente5": 'AGAKGKKIFVQKCSQCNPLCSQCHTVEKGGKHKTGPNEKGKKIVVQKCSQDETVLLGLFGRKTGQA'}
import re
for k, v in pacientes.items():
    if re.search(r'LTVCSQ', v):
        print(k + " ENFERMO")
    else:
        print(k + " SANO")

adn = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", adn)
print(m)
print("entire match: " + m.group())
print("first bit: " + m.group(1))
print("second bit: " + m.group(2))


genes = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
for gen in genes:
    if re.search(r"(d.*e)", gen):
        print("\t" + gen)


enzimas = {'EcoRI' : r'GAATTC', 'AvaII' : r'GG(A|T)CC', 'BisI' : r'GC[ATGC]GC'}


dna = "ATGTTCGGT"
ultimo = len(dna) - 2
codones = []
for ini in range(0,ultimo,3):
    codon = dna[ini:ini+3]
    codones.append(codon)
print(codones)


Entrez.email = "gualapuro.moises@gmail.com" 
with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="KP691605.1") as handle:
    seq_record = SeqIO.read(handle, "fasta")
print("%s with %i features" % (seq_record.id, len(seq_record.features)))
seq_record.seq

Entrez.email = "gualapuro.moises@gmail.com"
handle = Entrez.esearch(db="pubmed", 
                        term="ecuador covid[Title/Abstract]",
                        usehistory="y")
record = Entrez.read(handle)
# generate a Python list with all Pubmed IDs of articles about Dengue Network
id_list = record["IdList"]
record["Count"]

pima2 = pima.loc[(pima['BMI'] != 0) & (pima['Insulin'] != 0) & (pima['BloodPressure'] != 0) & (pima['Glucose'] != 0)]