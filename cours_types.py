#----------------------------------------------------#
#                   Types de données                 #
#----------------------------------------------------#


#----------------------------------------------------
# A) Les nombres entiers :

# Nombres positifs ou négatifs sans partie decimale

nb_positif = 3
nb_negatif = -3

nb_input_int = int(input("donnez un nb entier"))


#----------------------------------------------------
# B) Les nombres floattant :

# Nombres positifs ou négatifs avec partie decimale

nb_float = 1.15

nb_input_int = float(input("donnez un nb entier"))


#----------------------------------------------------
# C) Les booléens :

# Utilisé pour le conditionnelle

true_or_false = True #True == 1
true_or_false = False #False == 0


#----------------------------------------------------
# D) Séquences :

# 1) Strings
# Les chaînes de caractères représentent une séquence de caractères
chaine_strings = "Hello"

# 2) Listes
# Les listes sont des séquences modifiable d'éléments de différents types déclarées avec des crochets []

liste = [1, 2, 3, "Hello", 1.5]

# 3) Tuples
# Les tuples sont des séquences non-modifiable d'éléments déclarés avec des parenthèses ()

liste = (1, 2, 3, "Hello", 1.5)


#----------------------------------------------------
# E) Dictionnaires :

# Collections non ordonnées de paires clé-valeur, déclarés avec des accolades {}

dictionnaire = dict()
dictionnaire["clé1"] = "valeur1"
dictionnaire["clé2"] = "123"
dictionnaire["clé3"] = "valeur2"

print(dictionnaire)

#----------------------------------------------------
# F) Conversion de Types :

# On peut utiliser des fonctions de conversion pour passer d'un type à un autre

a = 42
chaine_a = str(a)
entier_a = int("123")
flottant_a = float("3.14")
# bool() --> chaine non vide en True

val = 3.15
lav_int = int(val)
print(lav_int)