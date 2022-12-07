import requests
import csv
from bs4 import BeautifulSoup

datasAttendue = []
datasPage = []
urlsTeste = []
validations = []

def reset():
    datasAttendue = []
    datasPage = []
    urlsTeste = []
    validations = []


def titleCheck(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (soup.title.string)

def metaCheck(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (soup.find_all('meta'))


def title():
    reset()
    with open('urlsTitles.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        i = 0
        for ligne in reader:
            i = i + 1
            print(" ")
            print("__________________________")
            print(i)
            dataPage = titleCheck(ligne['url'])
            datasAttendue.append(ligne['titre'])
            datasPage.append(dataPage)
            urlsTeste.append(ligne['url'])
            if (dataPage == ligne['titre']):
                print(ligne['url'] + " »» Ok")
                validations.append('OK')
            elif (dataPage != ligne['titre']):
                print(ligne['url'] + " »» KO")
                print("Le titre de la page est: " + dataPage)
                print("Le résultat attendu est: " + ligne['titre'])
                validations.append("ECHEC")
    saveCsv("Titre attendu", "Titre de la page", "resultat_titres.csv")

def meta(csvFile):
    reset()
    with open(csvFile) as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=';')
        i = 0
        for ligne in reader:
            i = i + 1
            print(" ")
            print("__________________________")
            print(i)
            dataPage = metaCheck(ligne['url'])
            datasAttendue.append(ligne['meta'])
            
            urlsTeste.append(ligne['url'])
            for m in dataPage:
                if m.get ('name') == 'description':
                    desc = m.get('content')
                    datasPage.append(desc)
                    if (desc == ligne['meta']):
                        print(ligne['url'] + " »» Ok")
                        validations.append('OK')
                    if (desc != ligne['meta']):
                        print(ligne['url'] + " »» KO")
                        validations.append("ECHEC")
    saveCsv("Meta attendu", "Meta de la page", "resultat_meta.csv")


def saveCsv(col2, col3, fileName):
    # Créer une liste pour les en-têtes
    en_tete = ["URL", col2, col3, "Validation"]
    #en_tete = ["URL", "Titre attendu", "Titre de la page", "Validation"]

    # Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
    with open(fileName, 'w', encoding="utf-8") as fichier_csv:
    #with open('resultat_titres.csv', 'w', encoding="utf-8") as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
        writer = csv.writer(fichier_csv, delimiter=';')
        writer.writerow(en_tete)
        # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
        for urlTeste, dataAttendue, dataPage, validation  in zip(urlsTeste, datasAttendue, datasPage, validations):
            # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
            ligne = [urlTeste, dataAttendue, dataPage, validation]
            writer.writerow(ligne)
        print('Rapport enregisté dans le fichier " '+ fileName +'".')
