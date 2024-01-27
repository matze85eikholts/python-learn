import random 
champDict = {}
with open("world_cup_champions.txt", "r") as file:
       for i,line in enumerate(file.readlines()):
           year, country, coach, captain = line.split(",")
           champDict[i] = {"year": year, "country": country,
                           "coach": coach, "captain": captain}
champDict.keys()
champDict.values()
keys_number = len(champDict.keys())
rand_key = random.randint(0, keys_number-1)
print(len(champDict.keys()))

for k, v in champDict.items():
    if k ==rand_key:
        print(k, v)
        for ik, iv in v.items():
         print(iv)