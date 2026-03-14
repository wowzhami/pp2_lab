#Open the file "demofile.txt" and append content to the file:

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")


#Open the file "demofile.txt" and overwrite the content:

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!") 


#reate a new file called "myfile.txt":
#"x" - Create - will create a file, returns an error if the file exists
f = open("myfile.txt", "x")