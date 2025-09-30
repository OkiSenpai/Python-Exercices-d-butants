#------------------------------------------------------------
# Exercice 1 : Fonction simple
# Créez une fonction bonjour() qui affiche « Bonjour tout le monde!
#------------------------------------------------------------

# def bonjour():
#     return("bonjour tout le mond")
# print(bonjour())

#------------------------------------------------------------
# Exercice 2 : Salutation personnalisée
# Écrivez une fonction saluer(nom) qui retourne la phrase « Bonjour, nom!
#------------------------------------------------------------

# def saluer(nom):
#     return("bonjour" + nom)
# print(saluer(" alice"))

#------------------------------------------------------------
# Exercice 3 : Pair ou impair
# Écrivez une fonction est_pair(nombre) qui retourne True si un nombre est pair,sinon False.
#------------------------------------------------------------

# def est_pair(n):
#     if n %2 == 0:
#         return(True)
#     else:
#         return(False)

# print(est_pair(7))

#------------------------------------------------------------
# Exercice 4 : Factorielle
# Écrivez une fonction factorielle(n) qui calcule la factorielle d’un nombre à l’aide d’une boucle.
#------------------------------------------------------------


def factorielle(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

    return (result)

print(factorielle(5))




#------------------------------------------------------------
# Exercice 5 : Compter les voyelles
#  Écrivez une fonction compter_voyelles(chaine) qui retourne le nombre de voyelles dans une chaîne.
#------------------------------------------------------------
# word = input(" tapper un mot avec de voyelles")
# def compter_voyelles(str):
#     count = 0
#     for b in str:
#         if b == "a" or b == "e" or b == "i" or b == "o" or b == "u" or b == "y":
#             count += 1
#     return(count)

# print(compter_voyelles(word))


#------------------------------------------------------------
# Exercice 6 : Liste inversée
# Écrivez une fonction inverse_liste(liste) qui retourne une liste inversée.
#------------------------------------------------------------

# list = [1,2,3,4,5]


# def inverse_liste(liste):
#     list2 = []
#     for i in range(len(liste) -1 ,-1 ,-1):
#         list2 += [liste[i]]
#     return (list2)

# print(inverse_liste(list))