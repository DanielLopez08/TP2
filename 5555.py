import csv
import json
import math
import codecs
from math import radians, cos, sin, asin, sqrt


# 2.2#################################################################################################################

class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def str(self):
        return f"ville:{self.ville} - pays:{self.pays} - latitude: {self.latitude} - longitude : {self.longitude}"


# 2.3####################################################################################################################

liste = []


def lireDonneesCsv(nomFichier):
    fichiercsv = codecs.open(nomFichier, 'r', encoding='utf-8')
    reader = csv.DictReader(fichiercsv, delimiter=',')
    for ligne in reader:
        liste.append(ligne)
        # print(ligne)
    # for cle, valeur in ligne.items():
    #      print(cle, valeur)


lireDonneesCsv('pays.csv')


##2.4##################################################################################################################


def ecrireDonneesJson(nomFichier, listeObjDonnesGeo):
    data = {'Geo': listeObjDonnesGeo}
    with open(nomFichier, 'w', encoding='utf-8') as j:
        json.dump(data, j, indent=4)


ecrireDonneesJson('donnes.json', liste)


##2.5#####################################################################################################################
#######################################################################################
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


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # this is in miles.  For Earth radius in kilometers use 6372.8 km

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c



