
# *** Exercice 10 : Jeu du plus grand ou plus petit ***

# chifre = 33
# devine = int(input("Devine chifrele: "))
# while devine != chifre:
#     if devine > chifre:
#         devine = int(input(" votre chifre est plus grand, essayez encore: "))
#     elif devine < chifre:
#         devine = int(input(" votre chifre est plus petit, essayez encore: "))
# else:
#     print("Bravo, vous avez deviné le chifre!")

#------------------------------------------------------------   


# ***Exercice 12 : Afficher une note en lettres***

# note = int(input("entre votre note entre 0 et 100: "))
# if note < 0 or note > 100:
#     print("note invalide")
# elif note >= 90 and note <=100:
#     print("A")
# elif note >= 80 and note < 90:
#     print("B")
# elif note >= 70 and note < 80:
#     print("C")
# elif note >= 60 and note < 70:
#     print("D")
# else:
#     print("F")  
#------------------------------------------------------------

# ***Exercice 13 : Deviner si un nombre est positif***

# nombre = int(input("entre un nombre: "))
# if nombre > 0:
#     print("le nombre est positif")
# elif nombre < 0:
#     print("le nombre est negatif")
# else:
#     print("le nombre est nul")
#------------------------------------------------------------

# ***Exercice 14 : Vérifier un triangle valide***
# a = int(input("entre la longueur du premier côté: "))
# b = int(input("entre la longueur du deuxième côté: "))
# c = int(input("entre la longueur du troisième côté: "))
# if a + b > c and a + c > b and b + c > a:
#     print("le triangle a deux coté plus grand")
# else:
#     print("le triangle n'est pas vrai")
#------------------------------------------------------------
# ***Exercice 15 : calculer le tarif d'un taxi ***

# distance = int(input("entre la distance en km: "))
# ten = 10
# tarifTenPlus = (distance - ten) * 0.75
# if distance > ten:
#     print( "le tarif est " + str(tarifTenPlus + ten))
# else:
#     print( "le tarif est " + str(distance * 1))



#------------------------------------------------------------
#------------------------------------------------------------
#BONUS 
#------------------------------------------------------------
# Exercice 1 simple calculator
#------------------------------------------------------------

# num1 = int(input("tapper le premier chifre "))
# num2 = int(input("tapper le deuxième chifre "))
# op = input("tapper l'opération (+, -, *, /) ")
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("opération non reconnue")

#------------------------------------------------------------
# Exercice 2 Reorganizer des caracteres d'une chaine
#------------------------------------------------------------

# word = str(input("tapper le ou les mots "))
# print(''.join(sorted(word)))

#------------------------------------------------------------
# Exercice 3 : Somme des chiffres d'un nombre
#------------------------------------------------------------

# num = input("tapper pluseiller chifre ")
# sortedNum = sorted(num)
# sumSum = sum(int(element) for element in sortedNum)
# print(sumSum) 

#------------------------------------------------------------
# Exercice 4 : Nombre pair ou impair
#------------------------------------------------------------

# num = int(input("tapper le nombre entier:  "))
# if num % 2 == 0:
#     print(str(num) + " le nombre est pair")
# else:
#     print(str(num) + " le nombre est impair")


#------------------------------------------------------------
# Exercice 5 : Convertion de temperature
#------------------------------------------------------------

# f = float(input("tapper la température en celsius "))
# print(float(f) * float(9/5) + 32)

#------------------------------------------------------------
# Exercice 6 : Calcule de l'aire d'un rectangle
#------------------------------------------------------------

# long = int(input("tapper la longueur du rectangle "))
# largeur = int(input("tapper la largeur du rectangle "))
# print(long * largeur)

#------------------------------------------------------------
# Exercice 7 : Repeter un mot plusieur fois
#------------------------------------------------------------

# mot = input("tapper le mot ")
# number= int(input("tapper le nombre "))

# while number != 0:
#     print(mot)
#     number -= 1

#------------------------------------------------------------
# Exercice 8 : detecter une voyelle 
#------------------------------------------------------------
# lettre = input("tapper la lettre ")
# if lettre in "aeiouAEIOU":
#     print("la lettre est une voyelle")
# else:
#     print("la lettre n'est pas une voielle")
#------------------------------------------------------------
# Exercice 9 : calculer l'age
#------------------------------------------------------------
# annee = int(input("tapper l'annee de naissance "))
# if annee < 2026:
#     print("vous avez:" , 2025 - annee )
# else:
#     print("vous n'etes pas né")
#------------------------------------------------------------
# Exercice 10 : temps en minutes et secondes
#------------------------------------------------------------
# temps= int(input("tapper les secondes "))
# minutes = temps // 60
# secondes = temps % 60
# print(f"il y a {minutes} minutes et {secondes} secondes")



# #ma facon
# seconds= int(input("tapper les secondes "))
# if seconds >= 60:
#     print(seconds // 60 , "minuts")
# elif seconds < 60:
#     print(seconds , "sec")

#------------------------------------------------------------
#------------------------------------------------------------
#------------------------------------------------------------

#EX TP4 Operator et condition avancer
#------------------------------------------------------------

#------------------------------------------------------------
# Exercice 1 : verifier si un caracter est une voyelle
#------------------------------------------------------------

# lettre = input("tapper une lettre ").lower()
# if lettre in "aeiou":
#     print("la lettre est une voyelle")  
# else:
#     print("la lettre n'est pas une voyelle")


#------------------------------------------------------------
# Exercice 2 : determier le signe d'un produit
#------------------------------------------------------------

# num1 = int(input("tapper le premier chifre "))
# num2 = int(input("tapper le deuxième chifre "))
# num3 = int(input("tapper le troisième chifre "))
# if num1 * num2 * num3 > 0:
#     print("le produit est positif")
# elif num1 * num2 * num3 < 0:
#     print("le produit est négatif")
# else:
#     print("le produit est nul")

#------------------------------------------------------------
# Exercice 3 : Comparer trois nombres
#------------------------------------------------------------

# num1 = int(input("tapper le premier chifre "))
# num2 = int(input("tapper le premier chifre "))
# num3 = int(input("tapper le premier chifre "))

# if num1 <= num2 and num2 <= num3:
#     if num2 <= num3:
#         print(num1 , num2 , num3)
#     else:
#         print(num1 , num3 , num2)
# elif num2 <= num1 and num2 <= num3:
#     if num1 <= num3:
#         print(num2 , num1 , num3)
#     else:
#         print(num2 , num3 , num1)
# elif num3 <= num1 and num3 <= num2:
#     if num1 <= num2:
#         print(num3 , num1 , num2)
#     else:
#         print(num3 , num2 , num1)
# else:
#     print("erreur")


#------------------------------------------------------------
# Exercice 4 : Mod de passe securisé
#------------------------------------------------------------

# password = input("mot de pass doit contnire au moin 8 lettre, une lettre majisucle et au moin un chifre ")
# a = 0
# x = password.isdigit
# for i in password:
#     a+=1
# # if a >= 8 and any(number.isdigit() for number in password) and  any(lettreMaj.isupper() for lettreMaj in password ):
# #     print("le mot de passe est securisé")
# # else:
# #     print("le mot de passe n'est pas securisé ")

# if a >= 8:
#     for number in password:
#         if number.isdigit():
#             for letreMaj in password:
#                 if letreMaj.isupper():
#                     print("le mot de passe est securisé")
#                     break
# else:
#      print("le mot de passe n'est pas securisé ")

# print(a)


#------------------------------------------------------------
#------------------------------------------------------------
#------------------------------------------------------------

#EX TP4  linguer d'une chain
#------------------------------------------------------------
# Exercice 1 : Longueur d'une chaine
#------------------------------------------------------------
# mot = input("tapper le mot ")
# tableu = sorted(mot)
# print( len(tableu))

#------------------------------------------------------------
# Exercice 2 : Convertir une chaine en majuscules
#------------------------------------------------------------
# s = input("tapper qqch en minuscules")
# print(s.upper())
#------------------------------------------------------------
# Exercice 3 : Convertir une chaine en minuscules
#------------------------------------------------------------
# s = input("tapper qqch en majuscules")
# print(s.lower())
# ------------------------------------------------------------
# Exercice 4 : compter les occurrences d'un caractere
# ------------------------------------------------------------
# mot = input("tapper le mot ")
# caracter = input("tapper une letre")
# tableu = list(mot)

# 1ere methode 
# print(mot.count(caracter))

#2eme methode 

# count = 0
# for i in tableu:
#     if caracter == i:
#         count += 1
#         print(count)

#------------------------------------------------------------
# Exercice 5 : Verifier si une chaine contient un mot
#------------------------------------------------------------
# 1ere method :
# 1ere method :
# 1ere method :
# s= input("tapper une phrase ")
# mot = input("tapper un mot ")
# array = s.split()
# if mot in array:
#     print("le mot est dans la phrase")
# else:
#     print("le mot n'est pas dans la phrase")

#2eme methode 
#2eme methode 
#2eme methode 
# s= input("tapper une phrase ")
# mot = input("tapper un mot ")
# print(mot in s)



#------------------------------------------------------------
# Exercice 6 : Remplacer un mot dans une chaine
#------------------------------------------------------------
# s = input("tapper une phrase ")
# oldMot = input("tapper un ancien mot ")
# newMot = input("tapper un new mot ")

# print(s.replace(oldMot , newMot))
#------------------------------------------------------------
# Exercice 7 : Afficher les 5 caracteres d'une chaine
#------------------------------------------------------------
# s = input("tapper une chaine ")
# print(s[3:8])
#------------------------------------------------------------
# Exercice 8 : verifier si une chaine est un palindrome
#------------------------------------------------------------
# s = input("tapper un mot ")
# tableu = list(s)
# tableu.reverse()
# print("tu as tapper" , s)
# palindrom = ''.join(tableu)
# if s == palindrom:
#     print("le mot est un palindrome")
# else:
#     print("le mot n'est pas un palindrome")
# print("lire de deriere", palindrom)
#------------------------------------------------------------
# Exercice 9 : Compter les mots dnas une chaine
#------------------------------------------------------------
# s = input("tapper une chaine ")
# array = s.split()
# print(array) 
# print(len(array))
#------------------------------------------------------------
#------------------------------------------------------------
#------------------------------------------------------------

#EX TP5  linguer d'une chain

#------------------------------------------------------------
#Exercice 1 : Creer une list et afficher ses elelement
#------------------------------------------------------------
# array = [1,2,3,4,5]
# for i in array:
#     print(i)
#------------------------------------------------------------
# Exercice 2 : Trouver la somme des elements d'une liste
#------------------------------------------------------------
# array = [1,2,3,4,5]
# print(sum(array))
#------------------------------------------------------------
# Exercice 3 : trouver le plus grand et le plus petit element
#------------------------------------------------------------
# array = [1,2,3,4,5]
# plusgrand = array[0]
# pluspetit = array[0]
# for i in array:
#     if i > plusgrand:
#         plusgrand = i
#     elif i < pluspetit:
#         pluspetit = i
# print("le nombre le plus grand est " , plusgrand)
# print("le nombre le plus petit est " , pluspetit)
        
#------------------------------------------------------------
# Exercice 4 : inverser une liste
#------------------------------------------------------------
# array = [1,2,3,4,5]
# array.reverse()
# print(array)
#------------------------------------------------------------
# Exercice 5 : Ajuter un element dans une liste
#------------------------------------------------------------
# array = [1,2,3,4,5]
# chiffre = input("tapper un chifre")
# array.append(chiffre)
# print(array)
#------------------------------------------------------------
# Exercice 6 :Suprimer un element dans une liste
#------------------------------------------------------------
# array = [1,2,3,4,5]
# array.remove(3)
# print(array)
#------------------------------------------------------------
# Exercice 7 : Compter les occurrences d'un element
#------------------------------------------------------------
# s = input("tapper une list des chifre ")
# chiffre = input("tapper un chifre pour verifier si il est dans la liste")
# i=0
# array = list(s)
# for e in array:
#     if e == chiffre:
#         i+=1
# if i > 0:
#     print(chiffre , "est" , i , "fois dans la list")
# else:
#     print(chiffre , "n'est pas danas la liste")       
# print(array)
#------------------------------------------------------------
# Exercice 8 : Verifier si un element et dans une liste
#------------------------------------------------------------
# s = input("tapper une list des chifre ")
# chiffre = input("tapper un chifre pour verifier si il est dans la list")
# array = list(s)
# i = 0
# for e in array:
#     if e == chiffre:
#         i = e
# if i !=0:
#     print(chiffre , "est dans la liste")
# else:
#     print(chiffre , "n'est pas dans la liste")
# print(array)
#------------------------------------------------------------
# Exercice 9 : Trier une liste sans utiliser sosrt()    
#------------------------------------------------------------
# je ne sais pas le faire
# s = input("tapper une liste")
# array = list(s)
# array.sort()
# print(array)
#------------------------------------------------------------
# Exercice 10 : fusioner deux list
#------------------------------------------------------------
# list1 = input("tapper une list")
# list2 = input("tapper encore une list")
# list3 = list1 + list2
# print(list3)



#------------------------------------------------------------
# Exercice 10 : fusioner deux list
#------------------------------------------------------------

# texte = "ja sam kralj";

# print("ja" in texte)

# print(texte[::-1])

# some = 0;

# for i in texte:
#     some += 1
# print(some)

#KeyError: 'username'
#KeyError: 'username'
#KeyError: 'username'
# user_info = {"name": "Alice", "age": 30}
# print(user_info["username"])

#IndexError: list index out of range
#IndexError: list index out of range
#IndexError: list index out of range
# numbers = [1, 2, 3]
# print(numbers[5])

list = []
n = input("donne moi le nombre des ellemoent des list").split(",")

# for i in range(n):
#     list +=[int(input ("donnes moi un chiffre"))]
# print(list)

for i in n:
    print(i)