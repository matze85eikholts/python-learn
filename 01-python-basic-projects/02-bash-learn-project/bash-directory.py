#-idea of that program is to read the lines of the txt file
#-save everything to a dictionary 
#- randomly create number of the list entry and 
#- ask the question about the selected command
import random
class Reader(object):
  def __init__(self):
    print("Let's learn a little bit bash-scripting")
    self.champDict = {}
  def read_commands(self, file):
    with open(file) as bash:
      #data = bash.read()
      x = len(bash.readlines())
    print(x)
  def read_in_dict(self, file_name):
    with open(file_name, "r") as file:
       for i,line in enumerate(file.readlines()):
           print(i)
           print(line)
           commands = line.split(",") #array of strings
           print(commands)
           self.champDict[i] = {"command": commands[0], "explanation": commands[1]}
       ranint = random.randint(0,i-1)
       print(ranint)
       print(self.champDict[ranint].values())
       #for word in self.champDict[ranint].values():
       #  print(word)
       listing = list(self.champDict[ranint].values())
       print(listing[0])   

bashReader = Reader()
bashReader.read_commands("bash-commands.txt")
bashReader.read_in_dict("bash-commands.txt")
