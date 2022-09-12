import requests
import csv
from bs4 import BeautifulSoup

def titleCheck(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return (soup.title.string)


with open('urls.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=';')
    for ligne in reader:
        print(" ")
        print("__________________________")
        print(" ")
        title = titleCheck(ligne[0])
        if (title == ligne[1]):
            print(ligne[0] + " »» Ok")
        elif (title != ligne[1]):
            print(ligne[0] + " »» KO")
            print("Le titre de la page est: " + title)
            print("Le résultat attendu est: " + ligne[1])
