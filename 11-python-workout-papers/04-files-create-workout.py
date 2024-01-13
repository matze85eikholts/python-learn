import os
# here also learn escape sequences for quotes \""
with open("20-bash-scripts-workout.py", "xt") as f:
  f.writelines("import os\n")
  f.writelines("os.system(\"echo Hello World\")")
  f.close()