def dna_complement(sequence):
    if len(sequence) == 0:
        return None
    else:
        complement = ''
        for i in range(len(sequence)):
            if sequence[i].upper() in ['A','C','T','G']:
                if sequence[i].upper() == 'A':
                    complement += 'T'
                elif sequence[i].upper() == 'C':
                    complement += 'G'

                elif sequence[i].upper() == 'T':
                    complement += 'A'

                else:
                    complement += 'C'

            else:
                return None
        return complement




input1 = 'AATTCGCGTGCTCGTA'
print('Input 1 is: ' + input1)
print(dna_complement(input1))

input2 = 'AATCGCGBTAGBGJ'
print('Input 2 is: ' + input2)
print(dna_complement(input2))


