#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author : Clément M -GITCLEMENT59

#Version 1.0

#LastUpdate:  14/04/2020

#importation des modules
import getpass
import os
from datetime import datetime
import sys
from netmiko import Netmiko
import time
   
#Récupération de l'user / mdp pour se connecter sur les équipements
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
   
    
#Fonction qui permet de calculer la durée de la tâche     
def duration(start):
    print("[Execution time : {0} seconds]".format(round(time.time() - start)))
      
#Fonction destiné à sauvegarder les confiugrations des équipements listé dans les deux fichiers
def envoi():
   
    start = time.time()  
    #On parcourt le fichier de conf pour lire les commandes à envoyer et le fichier send.list pour l'IP ou les IPs où diffuser la conf
    with open('conf') as f:
        lines = f.read().splitlines()
    with open('send.list') as f:
        ip = f.read().splitlines() 
    for ip in ip:   
        print("Envoi de la configuration sur l'adresse : "+ ip)
        #Définition de l'equipment utilisé pour la connexion netmiko 
        equipment = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
        'blocking_timeout': 16
         }

        net_connect = Netmiko(**equipment) 
        with open('conf') as f:
            lines = f.read().splitlines()
        print(net_connect.find_prompt())
        #envoi de la configuration
        output = net_connect.send_config_set(lines)
        print(net_connect.find_prompt())
        time.sleep(5)
        net_connect.disconnect()
        print(output)
        print("Pensez à sauvegarder la configuration envoyée à l'équipement" +"\n" )
    duration(start)
   
#Fonction destinée à sauvegarder la configuration de l'ensemble des équipements dans un fichier txt
def save_loc():
    start = time.time()
    with open('router.list') as f:
        ip_r = f.read().splitlines()
    with open('switch.list') as f:
        ip_s = f.read().splitlines()

    ip_add = ip_r + ip_s
#On parcourt la liste d'IP
    for ip in ip_add:        
        print("Sauvegarde de la configuration de l'équipement ayant l'adresse : "+ ip)

        equipment = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
         }
      
        #On initialise la connexion Netmiko sur l'équipement cible
        net_connect = Netmiko(**equipment)
        #récupération de la running-config
        run_cnf = net_connect.send_command("show running-config")
        print("Configuration Sauvegardée : "+ "\n" + run_cnf)
        now = datetime.now()
        date = now.strftime("%d_%m_%Y")
        
        #Récupération du hostname
        def hostname():
            hst = net_connect.send_command("show running-config | in hostname")
            hostname = hst.split()
            return hostname[1]
        path_save = "save/{0}/".format(hostname())
      
        #Création du dossier de backup si nécessaire
        try:
            os.makedirs(path_save)
        except:
            pass
        file_save = "save/{0}/{1}.txt".format(hostname(),date)
        #Ajoute la configuration au fichier texte créer ci dessus
        with open(file_save, "a") as file:
            file.write(run_cnf  + "\n")
        print("Configuration Sauvegardée dans le fichier:" + file_save +"\n")
        net_connect.disconnect()
    duration(start)
def cpy():
    start = time.time()
      
    with open('router.list') as f:
        ip_r = f.read().splitlines()
    with open('switch.list') as f:
        ip_s = f.read().splitlines()

    ip_add = ip_r + ip_s
    #On parcourt la liste d'IP
    for ip in ip_add:        
        print("Sauvegarde de la configuration de l'équipement ayant l'adresse : "+ ip)

        equipment = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': username,
        'password': password,
         }
      
        #On initialise la connexion Netmiko sur l'équipement cible
        net_connect = Netmiko(**equipment)  
        output = net_connect.send_command("copy run start")
        output = net_connect.send_command("startup-config")
        if "confirm" in output:
            output += net_connect.send_command_timing("y", strip_prompt=False, strip_command=False)
        net_connect.disconnect()
#Récupére la version des équipements listés      
def firmware():
    start = time.time()
    with open('router.list') as f:
      ip_r = f.read().splitlines()
    with open('switch.list') as f:
      ip_s = f.read().splitlines()
    ip_add = ip_r + ip_s

    for ip in ip_add: 

       equipment = {
       'device_type': 'cisco_ios',
       'ip': ip,
       'username': username,
       'password': password,
       }

       net_connect = Netmiko(**equipment)
       print(net_connect.send_command("show version | in IOS") +"\n")
       net_connect.disconnect()
    duration(start)
      
#Affichage du menu 
def menu(): 
      choice ='0'
      print("\n Choix disponible 1 à 4. \n")
      print("Choisir '1' pour l'envoi de configuration sur un équipement. ")
      print("Choisir '2' pour sauvegarder les configurations actuelles des équipements réseaux sur cette machine locale")
      print("Choisir '3' pour effectuer un copy run-start sur l'équipement réseau")
      print("Choisir '4' pour vérifier les versions installées")
      print("Choisir '5' pour quitter le programme. \n")
      while choice =='0':
         choice = input ("Sélection: ")
      if choice == "5":
         print("\n Fin du programme, merci de votre utilisation.")
         sys.exit()
      elif choice == "1":
         envoi()
         menu()
      elif choice == "2":
         save_loc()
         menu()
      elif choice == "3":
         cpy()
         menu()
      elif choice == "4":
         firmware()
         menu()
menu()
