# this code makes 100 .py files in the directory it is run
x = 1
while x<=100:
    a = open(f"{x}.py", "w")
    a.close
    x+=1
