class Randomizer:
  def __init__(self, name):
    self.name = name
  methods = ["getstate()","setstate()", "getrandbits()", "randrange()", "randint()", "choice()", 
             "choices()", "shuffle()", "sample()", "random()", "uniform()"]
  def select(self, i):
    return self.methods[i]
  def bark(self):
    print("whuf-whuf")
  def get_name(self):
    return self.name
  def set_name(self, name):
    self.name = name

class RandomizerAgain:
  def __init__(self, name):
    self.name = name
  methods = {1:"random()",
             2: "shuffle()",
             3: "getrandbits()",
             4: "getstate()",
             5: "setstate()",
             6: "seed()",
             7: "sample()",
             8: "uniform()"}
  def select(self, i):
    return self.methods.get(i)


r = Randomizer("Misha")
r.bark()

#print ("random module has "+ len(r.methods) + " methods")


for i in range(len(r.methods)):
  print(r.select(i))

ragain = RandomizerAgain("Sasha")
for i in len(ragain.methods):
  print(ragain.select(i))

#class MyClass:
#  def __init__(self, list):
#    self.list = list
#  def getitem(self, index):
#    return self.list[index-1]
  
#obj = MyClass([1,2,3,4,5])
#result = obj[3] + obj[1]