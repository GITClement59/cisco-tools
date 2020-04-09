#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : Clément M -GITCLEMENT59

#Version 1.0

#LastUpdate:  08/04/2020

#importation des modules
import getpass
import os
import datetime
import sys
#Récupération de l'user / mdp pour se connecter
print("Entrez vos informations de connexion: ")
username = input("Username: \n")
password = getpass.getpass("Password: \n")

def banner():
    cisco_banner = """\n
       _                     _              _     
      (_)                   | |            | |    
   ___ _ ___  ___ ___ ______| |_ ___   ___ | |___ 
  / __| / __|/ __/ _ \______| __/ _ \ / _ \| / __|
 | (__| \__ \ (_| (_) |     | || (_) | (_) | \__ \
\n  \___|_|___/\___\___/       \__\___/ \___/|_|___/
  """
    
    return cisco_banner

def hostname():
    sh_hostname = net_connect.send_command("show run | in hostname")
    hostname = sh_hostname.split()
    return hostname[1]

def save_dir():
    path_save = "save/{0}".format(hostname())
    rights = 0o755
    if not os.path.isdir(path_save):
        os.mkdir(path_save, rights)
        
#Fonction destiné à sauvegarder les confiugrations des équipements listé dans les deux fichiers

def save():
    with open('router.list') as f:
        ip_r = f.read().splitlines()
    with open('switch.list') as f:
        ip_s = f.read().splitlines()
    
    ip_add = ip_r + ip_s
    
    #Boucle sur chaque ligne de la liste ip_add 
    for ip in ip_add:        
  
        equipment = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
         }
        #Créer la connexion sur l'équipement
        net_connect = ConnectHandler(**equipment)
        save_dir()
        #récupération de la running-config
        run_cnf = net_connect.send_command("show running-config")
        now = datetime.now()
        date = now.strftime("%d_%m_%Y")
        path_save = "save/{0}/{1}".format(hostname(),date)
        show_result(path_save)
        
        #Ajoute la configuration au fichier texte créer ci dessus
        with open(path_save, "a") as file:
            file.write(CONFIGURATION  + "\n")
            
#Fonction d'affichage du menu et de sélection         
def menu():
    print (banner())
    choice ='0'
    while choice =='0':
        print("\n Choix disponible 1 à 4. \n")
        print("Choisir '1' pour la configuration avancée. ")
        print("Choisir '2' pour la sauvegarde intégrale. ")
        print("Choisir '3' pour l'effacement intégral. ")
        print("Choisir '4' pour quitter le programme. \n")
        
        choice = input ("Sélection: ")
        
    if choice == "4":
        print("\n Fin du programme, merci de votre utilisation.")
        sys.exit()
    elif choice == "2":
        print(lol)
        save()
 menu()
