#Importation du random nécessaire (pour être sur que la liste soit bien mélanger;) )
from random import*

Mouv= 0
myTable= [3,45,18,12,30,29,23,20]



for n in range (1:8):
    print('*',end='')
for i in range(1:8):
    print('*')


#List random Generator
for i in range(0,len(myTable)):
    myTable [i] = random.radint(0,100)
print("List to sort")
print (myTable)

#Creation de la boucle pour changer les chiffres plusieurs fois jusqu'au resultat attendu
for n in range(0,len(myTable)):
    for i in range (i,len(myTable)-1):
    if (myTable[i]>[i+1]):
        Mouv= myTable [i]
        myTable [i]= myTable [i+1]
        myTable [i+1]= Mouv
print("Sorted list")
print(myTable)

#Plus le programme avance plus il y a d'information à gérer
#Les itérarions se déculplent aux fur et à mesures des passages dans la boucle.





