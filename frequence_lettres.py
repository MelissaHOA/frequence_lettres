#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice : 2
# Analyse de la fréquence des lettres d’un texte
# Écrire un programme qui demande l’entrée d’une phrase à l’utilisateur
# et lui permet d’analyser le nombre de fois où chaque lettre
# qu’elle contient est présente (en ignorant les espaces et signes de ponctuation) ;
# par simplicité, on supprimera les accents de la phrase et elle sera passée en minuscules avant cette analyse

from unidecode import unidecode

# 1 : créer une fonction input_sentence qui demande à l’utilisateur l’entrée d’une phrase et retourne celle-ci

def input_sentence():
    """Input qui demande à l'utilisateur de rentrer une phrase """
    while True:
        user_sentence = input("Veuillez saisir une phrase : ")
        return user_sentence


# 2 : créer une fonction normalize_sentence qui prend en paramètre une chaîne de caractères
# et retourne celle-ci en minuscules et sans accent

def normalize_sentence(user_sentence):
    """ Chaine de caractères qui retourne tout en minuscules et sans accent"""
    while True:
        lowercase_sentence = str.lower(unidecode(user_sentence))
        return lowercase_sentence


def analyze_frequency():
    """Exécution du programme"""
    user_sentence = input_sentence()
    lowercase_sentence = normalize_sentence(user_sentence)

    print(f"Voici la phrase saisi : {user_sentence}")
    print(f"Voici la phrase en minuscule et sans accents : {lowercase_sentence}")


if __name__ == "__main__":
    analyze_frequency()