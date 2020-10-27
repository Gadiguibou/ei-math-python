#Travail d'évaluation interne de mathématiques - Les parties de batailles les plus courtes de l'histoire
#Analyse du problème de manière numérique

#Les commentaires indiquent la signification des lignes de code qui les suivent
#Le programme est écrit dans le langage Python 3.7

#J'importe le module contenant les fonctions de hasard à être utilisées
import random
#J'importe le module nécessaire au chronométrage du programme
import time
#N. B. J'utilise la barre de progression du module tqdm
from tqdm import tqdm
#Je débute le chronométrage
tempdebut = time.time()
#J'initialise les variables qui retourneront les résultats finaux 
issuesfav=0
issuesfav1=0
issuesfav2=0
#Je définis le nombre de partie à "jouer"
n=2000000000
#J'affiche le nombre de partie jouées
print("Le programme joue", n/1000000, "million(s) de parties")

#J'initialise le paquet de carte qui sera utilisé
paquet=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]

#Je débute une "for-loop" pour jouer les parties
for x in tqdm(range(n)):
	#Le paquet de carte est mélangé
	random.shuffle(paquet)
	#Le paquet est divisé également entre les deux joueurs
	J1=paquet[:26]
	J2=paquet[-26:]

	#À enlever du commentaire pour tester
	#J1=[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14]
	#J2=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

	#La variable pour le résultat du premier tour est créée
	tour1=0
	#Je compare la première carte du paquet des deux joueurs
	if J1[0] > J2[0]:
		tour1=1
	elif J1[0] < J2[0]:
		tour1=2
	#J'initialise une nouvelle variable "i"
	i=1

	#Je débute une boucle "while" qui vérifie si le résultat de chaque tour correspond au résultat du premier tour
	while J1[i]>J2[i] and tour1==1 or J1[i]<J2[i] and tour1==2:
		#et ajoute 1 aux résultats finaux lorsque la partie prend fin en 26 tours
		if i==25:
			issuesfav+=1
			if tour1==1:
				issuesfav1+=1
			else:
				issuesfav2+=1
			break
		i+=1
#J'affiche les résultats
print (issuesfav, "parties ont été gagnées en 26 coups dont:", issuesfav1, "par le joueur 1", "et", issuesfav2, "par le joueur 2.")
#J'affiche le temps d'exécution
print("Le programme s'est exécuté en: --- %s minutes --- " % ((time.time()-tempdebut)/60))