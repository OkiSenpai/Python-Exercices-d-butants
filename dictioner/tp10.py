# personne = {
#     "nom" : "omer",
#     "age" : 31,
#     "ville" : "Bruxellses"
# }

# personne["tel"] = "046583547"
# personne["ville"] = "Barcelone"

# if "tel" in personne:
#     del personne["tel"]

# print(personne.get("note","pas de note")) 


# etudiant = {
#     "nom": "Alice", 
#     "note": 15, 
#     "groupe":"A"
#     }

# for i in etudiant.items():
#     print(i)

    
# p = "chocolad"

# c={}
# for i in p:
#     c[i]=c.get(i,0)+1
# print(c)



# classes={
#     "a":{
#         "alice": 15,
#         "bob": 12,
#     },
#     "b":{
#         "chloe": 18
#     }
# }


# classes["b"]["omer"] = 25

# classes["a"]["bob"] = 15

# print(classes["a"]["bob"]) 

obl = {
    "omer": 10,
    "soulaiman": 15,
   
}
have = []
haveNot = []

def veri(d, obligatoires):
   
    for i in obligatoires:
        if i in d:
            have.append(i)
           
        else:
            haveNot.append(i)
    if not haveNot:
        return True
    else:
        return False

            
            
veri(obl,["omer", "soulaiman","massin"])       
print(haveNot)
