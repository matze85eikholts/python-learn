file_path = './verbos.txt'
open_file = open(file_path, 'r')
#text = open_file.read()

#output with separate symbol in eevery line
#for i in text:
#  print(i)

#as separate lines
text1 = open_file.readlines()
len(text1)
for i in range(len(text1)):
  print(text1[i])

open_file.close()