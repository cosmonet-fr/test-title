import requests
import csv
from bs4 import BeautifulSoup

metasAttendue = []
metasPage = []
urlsTeste = []
validations = []

def titleCheck(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (soup.find_all('meta'))


with open('urlsMeta.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=';')
    i = 0
    for ligne in reader:
        i = i + 1
        print(" ")
        print("__________________________")
        print(i)
        dataPage = titleCheck(ligne['url'])
        metasAttendue.append(ligne['meta'])
        
        urlsTeste.append(ligne['url'])
        for m in dataPage:
            if m.get ('name') == 'description':
                desc = m.get('content')
                metasPage.append(desc)
                if (desc == ligne['meta']):
                    print(ligne['url'] + " »» Ok")
                    validations.append('OK')
                elif (desc != ligne['meta']):
                    print(ligne['url'] + " »» KO")
                    validations.append("ECHEC")



# Créer une liste pour les en-têtes
en_tete = ["URL", "Meta attendu", "Meta de la page", "Validation"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('resultat_meta.csv', 'w', encoding="utf-8") as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=';')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for urlTeste, metaAttendue, metaPage, validation  in zip(urlsTeste, metasAttendue, metasPage, validations):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [urlTeste, metaAttendue, metaPage, validation]
      writer.writerow(ligne)
print('Rapport enregisté dans le fichier "resultat_meta.csv".')

