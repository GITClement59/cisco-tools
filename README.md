![Python 3.6](https://img.shields.io/badge/python-3.6%2B-green)
![Netmiko 3.0.0](https://img.shields.io/badge/netmiko-3.0.0-yellow)

## cisco-tools

### Outil pour configurer, sauvegarder et visualiser des équipements réseaux CISCO automatiquement
<pre>
       _                     _              _     
      (_)                   | |            | |    
   ___ _ ___  ___ ___ ______| |_ ___   ___ | |___ 
  / __| / __|/ __/ _ \______| __/ _ \ / _ \| / __|
 | (__| \__ \ (_| (_) |     | || (_) | (_) | \__ \
  \___|_|___/\___\___/       \__\___/ \___/|_|___/
                                                  
</pre>

## Compatibilité
 - :white_check_mark:CISCO IOS C7200
 - :white_check_mark:CISCO IOS C3725

## Pré-requis
 - Accès SSH aux équipements réseaux
 - Utilisation d'un utilisateur commun à chaque switch
 
## Configuration

1 /  Renseigner l'username dans la variable user du fichier **config.py**

2 / Modifier les fichiers listes en y ajoutant les **IPs** des équipements cibles :<br> 
             - ROUTER.LIST = IP des routeurs<br>
             - SWITCH.LIST = IP des switchs<br>
             - SEND.LIST = IP pour envoyer la configuration
## Utilisation

#### 1 / Appel du programme 

Après avoir cloner le repository, voici comment appeler le programme :

![Appel](https://zupimages.net/up/20/16/39j1.png)

#### 2 / Menu 

Voici l'ensemble des possibilitées :

![Menu](https://zupimages.net/up/20/16/lovi.png)

#### 3 / Détail

**Choix 1** :<br>
       - Envoi de la configuration listé dans le fichier "conf" sur le ou les équipements listés dans le fichier **SEND.LIST**
       <br>Attention, la configuration ne sera pas sauvegardé avec cette option, pensé à bien sauvegarder après avoir fait la configuration via l'option 3<br>
**Choix 2** :<br>
       - Sauvegarde de la configuration sur l'ordinateur local dans le fichier **save/** <br>
**Choix 3** :<br>
       - Copy run-start de la configuration sur l'équipement cible <br>
**Choix 4** :<br>
       - Vérifie la version cible
       
## Informations importantes

Les configurations sont stockées dans le dossier save/HOSTNAME/, au format DD_MM_YY.txt.

