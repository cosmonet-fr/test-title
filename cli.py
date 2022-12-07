import functions as function

test = input("Pour tester les balises <titles> tapez 1, pour tester la meta description tapez 2 \n")

if (test == '1'):
    function.title('./urlsTitles.csv')
elif (test == '2'):
    function.meta('./urlsMeta.csv')
else:
    print("Le numéro que vous avez entré est incorecte" )

fileName = input("Voulez-vous enregistrer le résultat dans un fichier CSV ? \n Si Oui, entrez le nom du fichier. \n Si non entrez la lettre n \n")

if (fileName != 'n'):
    function.saveCsv("Texte attendu", "Texte de la page", fileName+".csv")
