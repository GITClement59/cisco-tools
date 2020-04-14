![Python 3.6](https://img.shields.io/badge/python-3.6%2B-green)
![Netmiko 3.0.0](https://img.shields.io/badge/netmiko-3.0.0-yellow)

## cisco-tools
<pre>
       _                     _              _     
      (_)                   | |            | |    
   ___ _ ___  ___ ___ ______| |_ ___   ___ | |___ 
  / __| / __|/ __/ _ \______| __/ _ \ / _ \| / __|
 | (__| \__ \ (_| (_) |     | || (_) | (_) | \__ \
  \___|_|___/\___\___/       \__\___/ \___/|_|___/
                                                  
</pre>

## Compatibilité
 - CISCO IOS C7200
 - CISCO IOS C3725

## Pré-requis
 - Accès SSH aux équipements réseaux
 - Utilisation d'un utilisateur commun à chaque switch
 
## Configuration

1 /  Renseigner l'username dans la variable user du fichier **config.py**

2 / Modifier les fichiers listes en y ajoutant les **IPs** des équipements cibles : 
             - ROUTER.LIST = IP des routeurs
             - SWITCH.LIST = IP des switchs
             - SEND.LIST = IP pour envoyer la configuration
## Utilisation

1 / Appel du programme 

Après avoir cloner le repository, voici comment appeler le programme :

![Appel](https://zupimages.net/up/20/16/39j1.png)


