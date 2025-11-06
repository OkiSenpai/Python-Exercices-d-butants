# # ============================================
# # TP : Exercices sur les Dictionnaires en Python
# # ============================================

# # 1. Création et accès : Crée un dictionnaire avec nom, age, ville. Affiche nom et ville.
# personne = {"nom": "Jean", "age": 30, "ville": "Paris"}
# print("Nom:", personne["nom"])
# print("Ville:", personne["ville"])

# # 2. Ajout et modification : Ajoute "tel", modifie "ville", affiche le dictionnaire.
# personne["tel"] = "0123456789"
# personne["ville"] = "Lyon"
# print("Personne mise à jour:", personne)

# # 3. Suppression et accès sécurisé : Supprime "tel", affiche note avec get, explique différence.
# personne.pop("tel", None)
# print("Note:", personne.get("note", "pas de note"))
# # d["cle"] lève une erreur si la clé n'existe pas
# # d.get("cle") retourne None ou une valeur par défaut

# # 4. Parcours de clés / valeurs : Affiche clés, valeurs, items d’un dictionnaire.
# etudiant = {"nom": "Alice", "note": 15, "groupe": "A"}
# print("Clés:", list(etudiant.keys()))
# print("Valeurs:", list(etudiant.values()))
# print("Items:", list(etudiant.items()))

# # 5. Compteur de fréquences (lettres) : Compte les lettres dans une chaîne.
# texte = "python est cool"
# frequences = {}
# for lettre in texte:
#     if lettre != " ":
#         frequences[lettre] = frequences.get(lettre, 0) + 1
# print("Fréquences des lettres:", frequences)

# # 6. Dictionnaire de listes : Ajoute une note, calcule moyenne par matière.
# notes = {"math": [15, 12, 18], "info": [10, 14]}
# notes["info"].append(16)
# for matiere, liste in notes.items():
#     moyenne = sum(liste) / len(liste)
#     print(f"{matiere} -> moyenne: {moyenne:.2f}")

# # 7. Liste de dictionnaires : Affiche nom et note, trouve meilleur étudiant.
# etudiants = [
#     {"nom": "Alice", "note": 15},
#     {"nom": "Bob", "note": 12},
#     {"nom": "Chloe", "note": 18}
# ]
# for e in etudiants:
#     print(f"{e['nom']} : {e['note']}")
# meilleur = etudiants[0]
# for e in etudiants:
#     if e["note"] > meilleur["note"]:
#         meilleur = e
# print("Meilleur (manuel):", meilleur)
# meilleur2 = max(etudiants, key=lambda e: e["note"])
# print("Meilleur (max):", meilleur2)

# # 8. Fusion et mise à jour : Fusionne deux dictionnaires avec priorité à b.
# a = {"x": 1, "y": 2}
# b = {"y": 99, "z": 3}
# c1 = {**a, **b}
# print("Fusion avec **:", c1)
# c2 = a.copy()
# c2.update(b)
# print("Fusion avec update:", c2)

# # 9. Inversion clé/valeur : Inverse un dict, gère doublons avec liste.
# def inverser(d):
#     inverse = {}
#     for k, v in d.items():
#         inverse.setdefault(v, []).append(k)
#     return inverse
# print("Inversé:", inverser({"a": 1, "b": 2, "c": 1}))

# # 10. Compréhensions de dict : Crée dict nom:len(nom), filtre noms ≥ 4.
# noms = ["alice", "bob", "chloe"]
# d1 = {nom: len(nom) for nom in noms}
# d2 = {nom: len(nom) for nom in noms if len(nom) >= 4}
# print("Longueurs:", d1)
# print("Longueur ≥ 4:", d2)

# # 11. setdefault et regroupement : Regroupe prénoms par initiale.
# prenoms = ["Ali", "Amine", "Sara", "Samir", "Noa"]
# groupes = {}
# for p in prenoms:
#     initiale = p[0]
#     groupes.setdefault(initiale, []).append(p)
# print("Groupes par initiale:", groupes)

# # 12. Tri par valeurs : Trie dict par score croissant et décroissant.
# scores = {"alice": 15, "bob": 9, "chloe": 18, "dali": 12}
# asc = sorted(scores.items(), key=lambda x: x[1])
# desc = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# print("Croissant:", asc)
# print("Décroissant:", desc)
# print("Dict croissant:", dict(asc))
# print("Dict décroissant:", dict(desc))

# # 13. Dictionnaires imbriqués : Ajoute élève, modifie note, calcule moyennes.
# classe = {"A": {"alice": 15, "bob": 12}, "B": {"chloe": 18}}
# classe["B"]["dali"] = 14
# classe["A"]["bob"] = 13
# for groupe, eleves in classe.items():
#     moyenne = sum(eleves.values()) / len(eleves)
#     print(f"Moyenne {groupe} : {moyenne:.2f}")
# total = sum(note for g in classe.values() for note in g.values())
# nb = sum(len(g) for g in classe.values())
# print(f"Moyenne générale : {total / nb:.2f}")

# # 14. Validation de clés : Vérifie si toutes les clés obligatoires sont présentes.
# def verifier_cles(d, obligatoires):
#     manquantes = [k for k in obligatoires if k not in d]
#     return len(manquantes) == 0, manquantes
# print("Validation:", verifier_cles({"nom": "Ali", "age": 20}, ["nom", "age", "ville"]))

# # 15. Comptage de mots : Compte les mots dans une phrase, affiche top 3.
# import string
# phrase = input("Entrez une phrase : ").lower()
# for p in ".,;!?":
#     phrase = phrase.replace(p, "")
# mots = phrase.split()
# frequences = {}
# for mot in mots:
#     frequences[mot] = frequences.get(mot, 0) + 1
# top3 = sorted(frequences.items(), key=lambda x: x[1], reverse=True)[:3]
# print("Top 3 mots:", top3)

# # 16. Filtrage par condition : Sépare produits <2€ et ≥2€, calcule total.
# produits = {"pomme": 2.0, "banane": 1.0, "mangue": 3.5, "poire": 2.2}
# moins2 = {k: v for k, v in produits.items() if v < 2}
# plus2 = {k: v for k, v in produits.items() if v >= 2}
# print("Moins de 2€:", moins2, "Total:", sum(moins2.values()))
# print("2€ ou plus:", plus2, "Total:", sum(plus2.values()))

# # 17. Normalisation de données : Transforme valeurs en pourcentages.
# bruts = {"A": 10, "B": 20, "C": 30}
# total = sum(bruts.values())
# pourcentages = {k: f"{(v/total)*100:.1f}%" for k, v in bruts.items()}
# print("Pourcentages:", pourcentages)

# # 18. Sécurisation d'accès : safe_get(d, chemin) retourne None si clé manquante.
# def safe_get(d, chemin):
#     for cle in chemin:
#         if isinstance(d, dict) and cle in d:
#             d = d[cle]
#         else:
#             return None
#     return d
# cfg = {"db": {"host": "localhost"}}
# print("Accès sécurisé:", safe_get(cfg, ["db", "host"]))
# print("Clé manquante:", safe_get(cfg, ["db", "port"]))

# # 19. Transformation de structure : Liste de tuples → dict → tri par nom et note.
# liste = [("alice",15),("bob",12), ("chloe",18)]
# d = dict(liste)
# par_nom = sorted(d.items())
# par_note = sorted(d.items(), key=lambda x: x[1])
# print("Tri par nom:", par_nom)
# print("Tri par note:", par_note)

# # 20. Mini-ORM : Crée dict users avec id, fonctions CRUD.
# users = {}
# next_id = 1
# def create_user(users, nom, email):
#     global next_id
#     users[next_id] = {"nom": nom, "email": email}
#     next_id += 1
# def read_user(users, id):
#     return users.get(id)
# def update_user(users, id, **attrs):
#     if id in users:
#         users[id].update(attrs)
# def delete_user(users, id):
#     users.pop(id, None)

# # Exemple d'utilisation
# create_user(users, "Ali", "ali@mail.com")
# create_user(users, "Sara", "sara@mail.com")
# create_user(users, "Noa", "noa@mail.com")

# print("Tous les utilisateurs:", users)

# print("Lire utilisateur ID 2:", read_user(users, 2))

# update_user(users, 1, email="ali.nouveau@mail.com", nom="Ali B.")
# print("Après mise à jour ID 1:", users[1])

# delete_user(users, 3)
# print("Après suppression ID 3:", users)



a = "a"
if ord('a') <= ord(a) <= ord('z'):
    print(ord("a"))