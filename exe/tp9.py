# # TP9 + TP10 - Exercices sur les fichiers en Python

# import csv

# def exercice1():
#     with open("bonjour.txt", "w", encoding="utf-8") as f:
#         f.write("Bonjour le monde !")
#     print("✅ Fichier 'bonjour.txt' créé avec succès.")

# def exercice2():
#     try:
#         with open("bonjour.txt", "r", encoding="utf-8") as f:
#             print(f.read())
#     except FileNotFoundError:
#         print("❌ Le fichier 'bonjour.txt' n'existe pas.")

# def exercice3():
#     courses = ["Pommes", "Lait", "Pain"]
#     with open("courses.txt", "w", encoding="utf-8") as f:
#         for item in courses:
#             f.write(item + "\n")
#     print("✅ Fichier 'courses.txt' créé avec une liste de courses.")
#     with open("courses.txt", "r", encoding="utf-8") as f:
#         for ligne in f:
#             print(ligne.strip())

# def exercice4():
#     with open("courses.txt", "a", encoding="utf-8") as f:
#         f.write("Fromage\n")
#     print("✅ 'Fromage' ajouté à la liste des courses.")

# def exercice5():
#     try:
#         with open("courses.txt", "r", encoding="utf-8") as f:
#             for i, ligne in enumerate(f, start=1):
#                 print(f"{i}. {ligne.strip()}")
#     except FileNotFoundError:
#         print("❌ Le fichier 'courses.txt' n'existe pas.")

# def exercice6():
#     try:
#         with open("source.txt", "r", encoding="utf-8") as source, \
#              open("copie.txt", "w", encoding="utf-8") as dest:
#             for ligne in source:
#                 dest.write(ligne)
#         print("✅ Contenu de 'source.txt' copié dans 'copie.txt'.")
#     except FileNotFoundError:
#         print("❌ Le fichier 'source.txt' n'existe pas.")

# def exercice7():
#     try:
#         with open("courses.txt", "r", encoding="utf-8") as f:
#             lignes = f.readlines()
#             print("Nombre de lignes :", len(lignes))
#     except FileNotFoundError:
#         print("❌ Le fichier 'courses.txt' n'existe pas.")

# def exercice8():
#     mot = input("Entrez un mot à rechercher : ")
#     try:
#         with open("courses.txt", "r", encoding="utf-8") as f:
#             contenu = f.read()
#         if mot in contenu:
#             print(f"✅ Le mot '{mot}' apparaît dans le fichier.")
#         else:
#             print(f"❌ Le mot '{mot}' n'apparaît pas dans le fichier.")
#     except FileNotFoundError:
#         print("❌ Le fichier 'courses.txt' n'existe pas.")

# def exercice9():
#     try:
#         with open("courses.txt", "r", encoding="utf-8") as f:
#             lignes = f.readlines()
#         lignes_inverse = lignes[::-1]
#         with open("courses_inverse.txt", "w", encoding="utf-8") as f:
#             f.writelines(lignes_inverse)
#         print("✅ Fichier 'courses_inverse.txt' créé avec succès.")
#     except FileNotFoundError:
#         print("❌ Le fichier 'courses.txt' n'existe pas.")

# def exercice10():
#     nombres = []
#     for _ in range(5):
#         nombre = int(input("Entrez un nombre entier : "))
#         nombres.append(nombre)
#     with open("nombres.txt", "w", encoding="utf-8") as f:
#         for nombre in nombres:
#             f.write(str(nombre) + "\n")
#     print("✅ Les nombres ont été sauvegardés dans 'nombres.txt'.")

# def exercice11():
#     try:
#         with open("nombres.txt", "r", encoding="utf-8") as f:
#             nombres = [int(ligne.strip()) for ligne in f]
#         print("La somme des nombres est :", sum(nombres))
#     except FileNotFoundError:
#         print("❌ Le fichier 'nombres.txt' n'existe pas.")

# def exercice12():
#     try:
#         with open("nombres.txt", "r", encoding="utf-8") as f:
#             nombres = [int(ligne.strip()) for ligne in f]
#         nombres.sort()
#         with open("nombres_tries.txt", "w", encoding="utf-8") as f:
#             for nombre in nombres:
#                 f.write(str(nombre) + "\n")
#         print("✅ Les nombres triés ont été sauvegardés dans 'nombres_tries.txt'.")
#     except FileNotFoundError:
#         print("❌ Le fichier 'nombres.txt' n'existe pas.")

# def exercice13():
#     eleves = [
#         ["Alice", 12],
#         ["Bob", 13],
#         ["Clara", 11],
#         ["David", 12],
#         ["Eva", 14]
#     ]
#     with open("eleves.csv", "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Prénom", "Âge"])
#         writer.writerows(eleves)
#     print("✅ Fichier 'eleves.csv' créé.")

#     with open("eleves.csv", "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
#         for ligne in reader:
#             print(ligne)

# def exercice14():
#     with open("bonjour.txt", "w", encoding="utf-8") as f:
#         f.write("Bonjour le monde !")
#     print("✅ Fichier 'bonjour.txt' créé avec succès.")

# # === Menu principal ===
# while True:
#     print("\n=== MENU TP9 + TP10 ===")
#     print("1 - Création et écriture (bonjour.txt)")
#     print("2 - Lecture de bonjour.txt")
#     print("3 - Liste de courses")
#     print("4 - Ajout d’un élément dans courses.txt")
#     print("5 - Numéroter les lignes de courses.txt")
#     print("6 - Copier source.txt vers copie.txt")
#     print("7 - Compter les lignes dans courses.txt")
#     print("8 - Recherche d’un mot dans courses.txt")
#     print("9 - Fichier inversé")
#     print("10 - Sauvegarder des nombres")
#     print("11 - Lire des nombres et calculer la somme")
#     print("12 - Trier un fichier de nombres")
#     print("13 - Fichier CSV simple")
#     print("14 - Utiliser with (Exercice 1)")
#     print("0 - Quitter")

#     choix = input("👉 Choisissez un exercice : ")

#     if choix == "1": exercice1()
#     elif choix == "2": exercice2()
#     elif choix == "3": exercice3()
#     elif choix == "4": exercice4()
#     elif choix == "5": exercice5()
#     elif choix == "6": exercice6()
#     elif choix == "7": exercice7()
#     elif choix == "8": exercice8()
#     elif choix == "9": exercice9()
#     elif choix == "10": exercice10()
#     elif choix == "11": exercice11()
#     elif choix == "12": exercice12()
#     elif choix == "13": exercice13()
#     elif choix == "14": exercice14()
#     elif choix == "0":
#         print("👋 Fin du programme.")
#         break
#     else:
#         print("⚠️ Choix invalide, réessayez.")
