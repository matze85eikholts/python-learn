#import os
#os.system("echo Hello World")

with open("test-exec.py") as hello:
  exec(hello.read())