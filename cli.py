import functions as function

test = input("Pour tester les balises <titles> tapez 1, pour tester la meta description tapez 2 \n")

if (test == '1'):
    function.title()
elif (test == '2'):
    function.meta()
else:
    print("Le numéro que vous avez entré est incorecte" )