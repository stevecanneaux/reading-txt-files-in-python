#read file line by line (type print line out for each new line)
fh = open("demotxt.py", "r")
print(fh.readline())
print(fh.readline())
print()

#read/print all lines in doc
fhandler = open("demotxt.py")
for x in fhandler:
    print(x)
print()

#read entire doc
fhr = open("demotxt.py", "r")
print(fh.read())
print()

#read specific character
fha = open("demotxt.py", "r")
print(fh.read(5))
print()

#find total number of lines of text in doc
fhand = open("demotxt.py")
count = 0
for line in fhand:
    count = count +1
print("line count: ", count)

#this code will not execute as second IF statement
#look for a line starting with a value
fh = open("demotxt.py")
for line in fh:
    line = line.rstrip()
    if line.startswith("This"):
        print(line)
    else:
        print("not on this line")
#### OR:
fh = open("demotxt.py")
for line in fh:
    line = line.rstrip()
    if line.startswith("This"):
        continue
    else:
        print(line)