with open('note.csv','r') as f:
    contenu = f.readlines()
 
list = []

b= {}


for i in contenu:
    list.append(i.strip().split(","))
    

for i in list:
    key = i[0] + " " + i[1]
    if key in b:
        b[key] += [float(i[2])]
    else:
        b[key] = [float(i[2])]


for key , value in b.items():  
    res = 0
    big = value[0]
    smol = value[0]
    for i in value:
        if i > big:
            big = i
        if i < smol:
            smol = i
    print(f"le plus grand de  {key} est le {big}")
    print(f"le plus petie de {key} est le {smol}")




    for i in value:
        res += i
    moyin = res / len(value) 
    print(f"le moyin de  {key} est {moyin}")
    
    plesGrandMoyan = 0
    for i in value:
        if plesGrandMoyan < moyin:
            plesGrandMoyan = moyin
print(f"le plus grand moian est  {plesGrandMoyan}")