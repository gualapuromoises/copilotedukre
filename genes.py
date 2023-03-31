def descargar(input, output):
    """
    descargar: usa las accesiones de un archivo file.txt y descarga la información correspondiente 
    a los identificadores usando el ENTREZ de Biopythony luego guarda la información en file.fasta
    input: file.txt archivo de accesiones recuperados del NCBI
    output: file.fasta, archivo de identificadores y secuencias
    """
    from Bio import Entrez
    from Bio import SeqIO
    # abrimos el archivo txt   
    with open(input, 'r+') as lista:
        accs = lista.read().split("\n")
        Entrez.email= "gualapuro.moises@gmail.com"
        genes = []
        with Entrez.efetch( db="nucleotide", rettype="fasta", retmode="text", id= accs) as handle:
            for seq_record in SeqIO.parse(handle, "fasta"): 
                genes.append(seq_record)
                SeqIO.write(genes, output, "fasta") 
    return(genes)


def propiedades(input, output):
    from Bio.SeqUtils.ProtParam import ProteinAnalysis
    import pandas as pd

    prots = []
    mws = []
    iis = []
    for gen in input: 
        prot = gen.seq.translate().split('*')
        prots.extend(prot)
    for prot in prots:
        mw = ProteinAnalysis(prot).molecular_weight()
        ii = ProteinAnalysis(prot).instability_index()
        mws.append(mw)
        iis.append(ii)
    gendf = pd.DataFrame(list(zip(prots, mws, iis)), columns = ["Protein", "MolecularWeight", "InstabilityIndex"])
    gendf.to_csv(output)
    return(gendf)

def figura(input, output):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    plot= sns.jointplot(data=input, x='MolecularWeight', y='InstabilityIndex', kind="kde",  color='k')
    plot.set_axis_labels(xlabel='Peso Molecular [Da]', ylabel='InstabilityIndex [U]')
    plt.savefig(output, dpi=300)
    plt.show()