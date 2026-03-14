#Remove the file "demofile.txt":

import os
os.remove("demofile.txt")


#Check if file exists, then delete it:
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


#Remove the folder "myfolder":
os.rmdir("myfolder")


#copy
with open("data.txt", "r") as f:
    content = f.read()

with open("backup.txt", "w") as f:
    f.write(content)