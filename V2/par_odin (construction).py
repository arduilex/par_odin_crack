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
        "nombre":0
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
        "type":"Faafnir",
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

force = ["heros", "capitaine", "soldat", "traitre", "maudit"]



mode = 3
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
        i+=1
elif mode == 2:
    for i in range(6):
        dee[i]["nombre"] = randint(0, 10)
elif mode == 3:
    manuel = [1, 2, 0, 0, 1, 3]
    for i, k in enumerate(manuel):
        dee[i]["nombre"] = k



def calcul(l, active):
    t = 0
    t_blanc = 0
    for k in l:
        if active:
            print(k["type"], "x", k["nombre"])
        if k["type"] in force:
            t_blanc += k["nombre"]
    #if active:
        #print("t_blanc =", t_blanc)
    for k in l:
        name = k["type"]
        t_in = k["nombre"]  # total in le type actuelle
        if name in force:
            t += k["force"]*t_in
            if active:
                print("[force] t =", t)
        if name == "traitre" and l[0]["type"] == "heros":
            t_heros = l[0]["nombre"]
            if  t_heros > t_in:
                t -= 3*t_in
            else:
                t -= 3*t_heros
            if active:
                print("[traitre malus] t =", t)
        elif name == "mage":
            t += t_blanc*k["nombre"]
            if active:
                print("[mage] t =", t)
    if active:
        print("")
    return t

def cracking(dee):
    find = False
    man = [[2, 0], [0, 1],  [1, 2], [0, 0], [0, 0], [0, 1]]
    c = 0
    while not find:
        c+=1
        team1, team2 = [], []
        for k in dee:
            if k["nombre"]:
                a = randint(0, k["nombre"])
                b = k["nombre"] - a
                new = '{'+'"type":'+'"'+k["type"]+'"'
                if len(k) == 3:
                    new += ', "force":'+str(k["force"])
                if a:
                    team1.append(json.loads(new+', "nombre":'+str(a)+'}'))
                if b:
                    team2.append(json.loads(new+', "nombre":'+str(b)+'}'))
        if calcul(team1, 0) == calcul(team2, 0):
            find = True
            #calcul(team1, 1)
            #calcul(team2, 1)
    return team1, team2, calcul(team1, 0), c

solution = cracking(dee)
for i in range(2):
    print("\nTeam ",i+1,':',sep='')
    for k in solution[i]:
        if k["nombre"]:
            print("  ",k["nombre"], "x", k["type"])
print("\nTOTAL =", solution[2])
print("en",solution[3])




"""
a = man[i][0]
b = man[i][1]
new = '{'+'"type":'+'"'+dee[i]["type"]+'"'
if len(dee[i]) == 3:
    new += ', "force":'+str(dee[i]["force"])
if a:
    team1.append(json.loads(new+', "nombre":'+str(a)+'}'))
if b:
    team2.append(json.loads(new+', "nombre":'+str(b)+'}'))
"""