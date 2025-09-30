
#------------------------------------------------------------
#------------------------------------------------------------

# TP9 : Exercices sur les Fichiers en Python

#------------------------------------------------------------
#------------------------------------------------------------
# Exercice 1 : Création et écriture simple
# Crée un fichier bonjour.txt et écris dedans la phrase "Bonjour le monde !".

# with open("bonjour.txt", "w") as a:
#     a.write("hi")
#------------------------------------------------------------
#------------------------------------------------------------
#Exercice 2 : Lecture d’un fichier
#Lis le fichier bonjour.txt et affiche son contenu à l’écran

# with open("bonjour.txt", "r") as a:
#     read = a.read()
#     print(read)
#------------------------------------------------------------
#------------------------------------------------------------

#Exercice 3 : Liste de courses
#Écris une liste de courses (3 éléments minimum) dans un fichier courses.txt, puis
#lis et affiche son contenu ligne par ligne


# jedan nacin sa \n
# with open("courses.txt", "w") as a:
#     a.write("b\n")
#     a.write("c\n")
#     a.write("d\n")
    
# drugi nacin sa listom

# list = ["b", "c","d"]

# with open("courses.txt", "w") as a:
#     for i in list:
#         a.write(i + "\n")

# with open("courses.txt", "r") as b:
#     read = b.readlines()    
#     for i in read:
#         print(i)
#------------------------------------------------------------
#------------------------------------------------------------

# Exercice 4 : Ajout de données
# Ajoute un nouvel élément à la fin du fichier courses.txt sans écraser les données
# existantes


# with open("courses.txt", "a") as a:
#     a.write("e \n")

#------------------------------------------------------------
#------------------------------------------------------------

# Exercice 5 : Numéroter les lignes
# Lis le fichier courses.txt et affiche chaque ligne précédée de son numéro de ligne.

# with open("courses.txt", "r") as a:
#      counter = 1
#      for i in a:
#          print(counter , i)
#          counter += 1

#------------------------------------------------------------
#------------------------------------------------------------
#Exercice 6 : Copier un fichier
#Écris un programme qui copie le contenu d’un fichier source.txt dans un autre
#fichier copie.txt




#------------------------------------------------------------
#------------------------------------------------------------

#Exercice 7 : Compter les lignes
# Écris un programme qui compte et affiche le nombre de lignes dans courses.txt.


# with open("courses.txt", "r") as a:
#      counter = 0
#      for i in a:
       
#          counter += 1
#      print(counter)


#------------------------------------------------------------
#------------------------------------------------------------

# Exercice 8 : Recherche dans un fichier
#  Écris un programme qui demande un mot à l’utilisateur et vérifie si ce mot apparaît
#  dans courses.txt.

# mot = input("mot : ")

# with open("courses.txt", "r") as f:
#    list = f.read()

# if mot in list:
#     print(f"Le mot {mot} est la.")
# else:
#     print(f"Le mot {mot} nest pas la.")
