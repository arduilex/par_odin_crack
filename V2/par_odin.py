from random import randint
import json

dee = [
    {
        "type": "heros",
        "nombre":0,
        "force":+3
    },
    {
        "type":"capitaine",
        "nombre":0,
        "force":+2
    },
    {
        "type":"soldat",
        "nombre":0,
        "force":+1
    },
    {
        "type":"traitre",
        "nombre":0,
        "force":+1
    },
    {
        "type":"maudit",
        "nombre":0,
        "force":-1
    },
    {
        "type":"mage",
        "nombre":0,
        "force":0
    },
    {
        "type":"Fenrir",
        "nombre":0
    },
    {
        "type":"Jormungand",
        "nombre":0
    },
    {
        "type":"Sleipnir",
        "nombre":0
    },
    {
        "type":"Fafnir",
        "nombre":0
    },
    {
        "type":"Gullinbursti",
        "nombre":0
    },
    {
        "type":"Hraesvelg",
        "nombre":0
    }
]

def setting(dee, mode):
    global manuel
    manuel = []
    if mode == 1:
        i = 0
        skip = False
        while i < len(dee) and skip == False:
            print("Nombre de", dee[i]["type"], ": ", end="")
            r = input()
            if r == 's':
                skip = True
            elif r:
                dee[i]["nombre"] = int(r)
                manuel.append(int(r))
            i+=1
    elif mode == 2:
        for i in range(12):
            r = randint(0, 10)
            manuel.append(r)
            dee[i]["nombre"] = r
        print(manuel)
    elif mode == 3:
        manuel = [0, 3, 1, 0, 2, 1, 0, 0, 0, 0, 1]
        for i, k in enumerate(manuel):
            dee[i]["nombre"] = k
    elif mode == 4:
        f = open("save.txt", 'r')
        manuel = eval(f.readline())
        for i, k in enumerate(manuel):
            dee[i]["nombre"] = k
    return dee

def calcul(G, active):
    t = 0
    t_blanc = 0
    t_heros = 0
    t_traitre = 0
    t_mage = 0
    mage = None
    l_strong = []
    l_identique = []
    l_blanc = ["heros", "capitaine", "soldat", "traitre", "maudit", "mage"]
    for i, k in enumerate(G):
        name = k["type"]
        nombre = k["nombre"]
        if name in l_blanc:
            l_identique.append(nombre)
            if name == "heros":
                t_heros = nombre
            elif name == "traitre":
                t_traitre = nombre
            if name == "mage":
                mage = i
                t_mage = nombre
            else:
                t_blanc += nombre
                l_strong.append(k["force"])
    if t_heros and t_traitre and t_traitre >= t_heros:
        del l_strong[0]
    if mage:
        G[mage]["force"] = t_blanc
   
    for k in G:
        name = k["type"]
        t_in = k["nombre"]  # total in le type actuelle
        if name in l_blanc:
            result = k["force"]
            t += result*t_in
            if name == "mage":
                l_strong.append(result)
        if name == "traitre" and t_heros > 0:
            if  t_heros > t_in:
                t -= 3*t_in
            else:
                t -= 3*t_heros
    #FRIGG DEFIE !
    if l_strong:
        stronger = 0
        for k in l_strong:
            if k > stronger:
                stronger = k
        l_identique.sort(reverse=True)
        first = l_identique[0]
        if first == 1:
            l_identique = []
        else:
            l_identique = [k for k in l_identique if k==first]
        for k in G:
            name = k["type"]
            if name == "Fenrir" and l_strong:
                t += stronger
            elif name == "Jormungand" and l_strong:
                t -= stronger*2
            elif name == "Sleipnir":
                t += t_blanc+t_mage
            elif name == "Fafnir":
                t -= t_blanc+t_mage
            elif l_identique:
                if name == "Gullinbursti":
                    plus = l_identique[randint(0, len(l_identique)-1)]
                    t += plus
                elif name == "Hraesvelg":
                    plus = l_identique[randint(0, len(l_identique)-1)]
                    t -= plus

    return t

def cracking(dee):
    find = False
    man = [[2, 0], [0, 1],  [1, 2], [0, 0], [0, 0], [0, 1]]
    c = 0
    pr = 1000
    while not find:
        c+=1
        team1, team2 = [], []
        for k in dee[:-2]:
            if k["nombre"]:
                a = randint(0, k["nombre"])
                b = k["nombre"] - a
                new = '{"type":"'+k["type"]+'"'
                if len(k) == 3:
                    new += ', "force":'+str(k["force"])
                if a:
                    team1.append(json.loads(new+', "nombre":'+str(a)+'}'))
                if b:
                    team2.append(json.loads(new+', "nombre":'+str(b)+'}'))
        for k in dee[-2:]:
            if k["nombre"]:
                add = json.loads('{"type":"'+k["type"]+'", "nombre": '+str(k["nombre"])+'}')
                team1.append(add)
                team2.append(add)

        if calcul(team1, 0) == calcul(team2, 0):
            find = True
        if c > pr:
            pr *=2
            print("Tour de boucle :", c)
    return team1, team2, calcul(team1, 0), c

setting(dee, 1)

solution = cracking(dee)
for i in range(2):
    print("\nTeam ",i+1,':',sep='')
    for k in solution[i]:
        if k["nombre"]:
            print("  ",k["nombre"], "x", k["type"])
print("\nTOTAL =", solution[2])
print("(en ",solution[3], ")", sep="")
f = open("save.txt", 'w')
f.write(str(manuel))
f.close()