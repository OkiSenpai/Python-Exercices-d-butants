
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

#------------------------------------------------------------
#------------------------------------------------------------

# Exercice 9 : Fichier inversé
# Lis le contenu de courses.txt et écris-le à l’envers (du bas vers le haut) dans un
# fichier courses_inverse.txt

# with open("numbers.txt" , "r") as f:
#     list = f.read()
#     for i in range( len(list) -1 , -1, -1):
#         print(list[i])



#------------------------------------------------------------
#------------------------------------------------------------


# Exercice 10 : Sauvegarder des nombres
# Demande à l’utilisateur 5 nombres entiers et écris-les (un par ligne) dans un fichier
# nombres.txt.

# with open("numbers.txt","w") as a:
#     list = []
#     counter = 1
#     for i in range(5):
#         nubers = int(input(f"tap  {counter} chiffre : "))
#         counter += 1 
#         a.write( f" {nubers} \n"  ) 
    


#------------------------------------------------------------
#------------------------------------------------------------


# Exercice 11 : Lire des nombres et calculer la somme
# Lis le fichier nombres.txt et calcule la somme des nombres contenus.

# with open("numbers.txt" , "r") as a:
#     items = a.readlines()
#     count= 0
#     for i in items:
#         count += int(i)
        
#     print(count)


#------------------------------------------------------------
#------------------------------------------------------------

# Exercice 12 : Trier un fichier de nombres
#  Lis le fichier nombres.txt, trie les nombres et sauvegarde-les dans un fichier
#  nombres_tries.txt

# ma maniere

# with open("numbers.txt" , "r") as a:
#     numbers =  a.readlines()
    
#     list1 = []
#     list2 =[]
    
#     for i in numbers:
#          list1.append(int(i.strip()))
#     print(list1)
#     while list1:
#         n = list1[0]
#         for i in list1:
#                 if n > i:
#                     n = i
                    
#         list2.append(n)
#         list1.remove(n)
                
           

#     with open("nombres_tries.txt" , "w") as f:
#          f.write(f"{list2}")
         
# la facone de souleiman

with open("numbers.txt" , "r") as f:
    n =  f.readlines()
    numbers = int(n)
    print(numbers)



for i in range(len(numbers)):
    for a in range(len(numbers)-1):
        if numbers[i] < numbers[a]:
            n = numbers[i]
            numbers[i]= numbers[a]
            numbers[a] = n
print(numbers)



