#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : Clément M -GITCLEMENT59

#Version 1.0

#LastUpdate:  08/04/2020

#importation des modules
import getpass
import sys

#Récupération de l'user / mdp pour se connecter
print("Entrez vos informations de connexion: ")
username = input("Username: \n")
password = getpass.getpass("Password: \n")

def banner():
    cisco_banner = ""\
           _                     _              _     
      (_)                   | |            | |    
   ___ _ ___  ___ ___ ______| |_ ___   ___ | |___ 
  / __| / __|/ __/ _ \______| __/ _ \ / _ \| / __|
 | (__| \__ \ (_| (_) |     | || (_) | (_) | \__ \
  \___|_|___/\___\___/       \__\___/ \___/|_|___/
        \""
    return cisco_banner

def menu():
    print (banner())
    choice ='0'
    while choice =='0':
        print("CISCO-TOOLS \n Choix disponible 1 à 4. \n")
        print("Choisir '1' pour la configuration avancée. ")
        print("Choisir '2' pour la sauvegarde intégrale. ")
        print("Choisir '3' pour l'effacement intégral. ")
        print("Choisir '4' pour quitter le programme. \n")
        
        choice = input ("Sélection: ")
        
    if choice == "4":
        print("\n Fin du programme, merci de votre utilisation.")
        sys.exit()

menu()
