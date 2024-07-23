#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice : 2
# Analyse de la fréquence des lettres d’un texte
# Écrire un programme qui demande l’entrée d’une phrase à l’utilisateur
# et lui permet d’analyser le nombre de fois où chaque lettre
# qu’elle contient est présente (en ignorant les espaces et signes de ponctuation) ;
# par simplicité, on supprimera les accents de la phrase et elle sera passée en minuscules avant cette analyse


#1 : créer une fonction input_sentence qui demande à l’utilisateur l’entrée d’une phrase et retourne celle-ci

def input_sentence():
    """Input qui demande à l'utilisateur de rentrer une phrase
    :return:
    """

    user_sentence = input("Veuillez saisir une phrase : ")
    print(user_sentence)


input_sentence()