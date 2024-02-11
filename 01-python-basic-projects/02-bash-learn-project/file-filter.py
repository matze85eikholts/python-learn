#- i need to filter all entries in the file with bash commands
class Filter(object):
  def __init__(self):
    print("we need to filter all empty tabs and placeholders")
  
  #def filter(self, file):
  #  with open(file,'rb') as file_in:
  #    with open("output.txt",'wb') as file_out:
  #      for line in file_in:
  #        new_line = line.replace('\t', ' ')
  #        file_out.write(new_line)

  #  file_in.close()
  #  file_out.close()
  
#fileFilter = Filter()
#fileFilter.filter("bash-commands-to-filter.txt")
inputFile = open("bash-commands-to-filter.txt", 'r') 
exportFile = open("otextfile.txt", 'w')
for line in inputFile:
   new_line = line.replace('\t', ' ').lstrip().replace(' ',', ', 1)
   exportFile.write(new_line) 

inputFile.close()
exportFile.close()