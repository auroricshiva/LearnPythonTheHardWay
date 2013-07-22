from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want to erase, hit CTRL-C (^C).")
print ("If you do want to erase, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!") # not necessary bc opening a file to write truncates it
target.truncate()

print ("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these lines to the file.")
nl = "\n"
target.write(line1 + nl + line2 + nl + line3 + nl)

print ("And finally, we close it.")
target.close()