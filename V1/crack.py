# Ce programme crack le jeux  par odin
from random import randint
deeType = ['héros', 'capitaine', 'soldat', 'traitre', 'maudit', 'mage']
sept = [1, 2, 0, 0, 1, 3]
t = 0
"""
for i in range(len(deeType)):
    print("Combien de", deeType[i], "as tu ? : ", end='')
    nb = int(input())
    t += nb
    for j in range(nb):
        sept.append(i)
print("nombre de dées :", t)
"""


def score(list):
    countType = [0]*6
    for i in range(6):
        countType[i] = list.count(i)
    point = 0
    point += countType[0]*3 
    point += countType[1]*2 
    point += countType[2]
    point += countType[3]
    for i in range(countType[3]):
        if countType[0] >= i+1:
            point -= 3
    point -= countType[4]
    point += (len(list)-countType[5])*countType[5]
    return point, countType

def new(archive, nouveau):
    if nouveau[0] in archive:
        return 0
    elif nouveau[1] in archive:
        return 0
    return True

T1 = 0
T2 = 1
c = 0
solution = 0
chauffe = 4000
sortir = False
save = [[],[],[]]
while  sortir == False:
    c += 1
    if c > chauffe:
        chauffe *= 2
        print("Ca chauffe !", chauffe, "tours")
        if chauffe > 50000:
            r = input("Continuer ? :")
            if r == 'n':
                sortir = True
    temp = sept[:]
    G1 = []
    n = randint(1, 6)
    for i in range(n):
        r = randint(0, len(temp)-1)
        G1.append(temp[r])
        del temp[r]
    print(G1)


    G2 = temp[:]
    temp = [[],[]]
    T1, temp[0] = score(G1)
    T2, temp[1] = score(G2)
    if T1 == T2 and new(save[0], temp) == True:
            save[0].append(temp[0])
            save[1].append(temp[1])
            save[2].append(T1)
            solution += 1
            print('>>>',solution, "trouvé(s) !")
            sortir = True

if solution == 0:
    print("\nAucune solution trouvée :'(")
for i in range(len(save[2])):
    print("\nSolution n°", i+1, "\nEquilibre =", save[2][i])
    for j in range(2):
        print("Groupe", j+1)
        for k in range(len(save[j][i])):
            if save[j][i][k] > 0:
                print(save[j][i][k], 'x', deeType[k])
