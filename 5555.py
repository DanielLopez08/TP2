# Gestion de données géographiques
#   Samy Debbah et Daniel Lopez
#      e1960719 et e2033426
#           21-05-2024








import csv
import json
import math
from math import radians, cos, sin, asin, sqrt


# 2.2#################################################################################################################

#création de la classe DonnesGeo avec ses attributs initalisés dans le constructeur
class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = str(ville)
        self.pays = str(pays)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

#retourne la valeur des attributs de la classe en str
    def __str__(self):
        return f"ville:{self.ville} - pays:{self.pays} - latitude: {self.latitude} - longitude : {self.longitude}"


# 2.3####################################################################################################################

liste = []

#ouverture du fichier csv en mode read en prenant en compte les accents
#chaque ligne du fichier est un dictionnaire qui sera ajouté à la liste et affiché
def lireDonneesCsv(nomFichier):
    fichiercsv = open(nomFichier, 'r', encoding='utf-8')
    reader = csv.DictReader(fichiercsv, delimiter=',')
    for ligne in reader:
        liste.append(ligne)
        print(ligne)



lireDonneesCsv('pays.csv')


##2.4##################################################################################################################

# fonction prend la liste de dictionnaire en paramètre et le fichier json dans lequel la liste de dictionnaire sera écrite
def ecrireDonneesJson(nomFichier, listeObjDonnesGeo):
    data = {'Geo': listeObjDonnesGeo}
    with open(nomFichier, 'w', encoding='utf-8') as j:
        json.dump(data, j, indent=4)


ecrireDonneesJson('donnes.json', liste)


##2.5#####################################################################################################################

def trouverDistanceMin (nomFichier):
    with open (nomFichier,'r') as f:
        data = json.load(f)
# trouver la distance
        distance = []#liste vide
        for i in range(data): #premiere ville
            ville1=data[i]
            for k in range(i+1,(data):#deuxieme ville qui est differente de la premiere
                ville2 = data[k]
                
                distance.append([ville1['ville 1'],ville2['ville 2'], distance])#rajouter les infos a la liste vide
              # Sauvegarder les résultats dans un fichier CSV
                with open ('distance.csv', 'a', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerow([ville1['ville 1'],ville2['ville2'], distance])

    
            
          
 while True:
        print('''
        1- Lire les données du fichier csv, créer les objets et afficher les données.
        2- Sauvegarder les données dans un fichier .json.
        3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.
        Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :''')
        choix = int(input())
        if choix == '1':
            afficher_donnees_csv('pays.csv')
        elif choix == '2':
            with open('pays.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                donnees = {row['ville']: row for row in reader}
                sauvegarder_donnees_json(donnees, 'donnees.json')
        elif choix == '3':
            donnees = lire_donnees_json('donnees.json')
            distances = calculer_distances_minimales(donnees)
            sauvegarder_distances(distances, 'distances.csv')
        elif choix == 'q':
            break
        else:
         input('Choix invalide, appuyez sur une touche pour continuer...')



