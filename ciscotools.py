#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : Clément M -GITCLEMENT59

#Version 1.0

#LastUpdate:  09/04/2020

#importation des modules
import getpass
import os
from datetime import datetime
import sys
from netmiko import Netmiko
import time
import errno

def start():
    start = datetime.now()
#Récupération de l'user / mdp pour se connecter
print("Entrez vos informations de connexion: ")
#username = input("Username: \n")
#password = getpass.getpass("Password: \n")

username = "admin"
password = "azerty"
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
        
#Fonction destiné à sauvegarder les confiugrations des équipements listé dans les deux fichiers

def save():
    
    start = datetime.now()
    with open('router.list') as f:
        ip_r = f.read().splitlines()
    with open('switch.list') as f:
        ip_s = f.read().splitlines()
    
    ip_add = ip_r + ip_s
    
    for ip in ip_r:        
    
        equipment = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
         }

        net_connect = Netmiko(**equipment)
        #récupération de la running-config
        run_cnf = net_connect.send_command("sh run")
        now = datetime.now()
        date = now.strftime("%d_%m_%Y")
        def hostname():
            hst = net_connect.send_command("show run | in hostname")
            hostname = hst.split()
            return hostname[1]
        path_save = "save/{0}/{1}".format(hostname(),date)
        try:
            os.makedirs("save/{0}/".format(hostname())
        except:
            if exc.errno == errno.EEXIST and os.path.isdir(save/{0}/".format(hostname()):
                pass
        #Ajoute la configuration au fichier texte créer ci dessus
        with open(path_save, "a") as file:
            file.write(run_cnf  + "\n")
            net_connect.disconnect()
        end = datetime.now()
        duration = end - start
        print("Execution Duration : "+ str(duration))
          
#Affichage du menu 
def menu(): 
    print("\n Choix disponible 1 à 4. \n")
    print("Choisir '1' pour la configuration avancée. ")
    print("Choisir '2' pour la sauvegarde intégrale. ")
    print("Choisir '3' pour l'effacement intégral. ")
    print("Choisir '4' pour quitter le programme. \n")

print (banner())
menu()
choice ='0'
while choice =='0':
    choice = input ("Sélection: ")
if choice == "4":
    print("\n Fin du programme, merci de votre utilisation.")
    sys.exit()
elif choice == "2":
    save()
menu()
