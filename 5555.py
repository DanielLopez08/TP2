#Gestion de données géographiques
#Samy Debbah et Daniel Lopez
#    e1960719 et eYYYYYY
#         21-05-2024








import csv
import json
import math
import codecs
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
    def str(self):
        return f"ville:{self.ville} - pays:{self.pays} - latitude: {self.latitude} - longitude : {self.longitude}"


# 2.3####################################################################################################################

liste = []

#ouverture du fichier csv en mode read en prenant en compte les accents
#chaque ligne du fichier est un dictionnaire qui sera ajouté à la liste et affiché
def lireDonneesCsv(nomFichier):
    fichiercsv = codecs.open(nomFichier, 'r', encoding='utf-8')
    reader = csv.DictReader(fichiercsv, delimiter=',')
    for ligne in reader:
        liste.append(ligne)
        print(ligne)



lireDonneesCsv('pays.csv')


##2.4##################################################################################################################

# fonction prend la liste de dictionnaire en paramètre et le fichier json dans lequel la liste de dictionnaire de type Geo sera écrite
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
        distance = []
        for i in range(len(data)):
            ville1=data[i]
            for k in range(i+1, len(data)):
                ville2 = data[k]
                distance = Calculdistance(ville1['latitude'], ville1['longitude'],ville2['latitude'], ville2['longitude'])
                distance.append([ville1['ville'],ville2['ville'], distance])

                with open ('distance.csv', 'a', newline = '') as f:
                    writer = csv.writer(f)
                    writer.writerow([ville1['ville'],ville2['ville'], distance])

        # Sauvegarder les résultats dans un fichier CSV
        with open('distances.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([ville1, ville2,distance])






