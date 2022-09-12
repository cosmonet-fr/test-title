import requests
import csv
from bs4 import BeautifulSoup

titresAttendue = []
titresPage = []
urlsTeste = []
validations = []

def titleCheck(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (soup.title.string)


with open('urls.csv') as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=';')

    for ligne in reader:
        print(" ")
        print("__________________________")
        print(" ")
        dataPage = titleCheck(ligne['url'])
        titresAttendue.append(ligne['titre'])
        titresPage.append(dataPage)
        urlsTeste.append(ligne['url'])
        if (dataPage == ligne['titre']):
            print(ligne['url'] + " »» Ok")
            validations.append('OK')
        elif (dataPage != ligne['titre']):
            print(ligne['url'] + " »» KO")
            print("Le titre de la page est: " + dataPage)
            print("Le résultat attendu est: " + ligne['titre'])
            validations.append("ECHEC")




# Créer une liste pour les en-têtes
en_tete = ["url", "titre_attendu", "titre_page", "validation"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('resultat.csv', 'w') as fichier_csv:
   # Créer un objet writer (écriture) avec ce fichier
   writer = csv.writer(fichier_csv, delimiter=';')
   writer.writerow(en_tete)
   # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
   for urlTeste, titreAttendue, titrePage, validation  in zip(urlsTeste, titresAttendue, titresPage, validations):
      # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
      ligne = [urlTeste, titreAttendue, titrePage, validation]
      writer.writerow(ligne)
print('Rapport enregisté dans le fichier "resultat.csv".')