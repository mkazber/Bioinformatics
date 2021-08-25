def trans(x):
    dna=x
    rna=list()
    if(len(dna)>10 or len(dna)<25):
        for seq in list(dna):
            seq1 = seq.replace('A','U').replace('T','A')
            if seq == 'G':
                seq1 = seq1.replace('G','C')
            else:
                seq1 = seq1.replace('C','G')
            rna.append(seq1)

    else:
        print('Zła długość')
    return rna