with open("rosalind_revc.txt", "r") as rawdata:
    data = rawdata.read()

rna = []

keys = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for i in reversed(data):
    rna.append(keys[i])

output = ''.join(rna)

print(output)