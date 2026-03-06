sentence=input()

croatia=["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    sentence=sentence.replace(c,"*")

print(len(sentence))