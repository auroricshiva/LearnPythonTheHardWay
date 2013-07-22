from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

#in_file = open(from_file)
indata = open(from_file).read()

"""
print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Hit RETURN to continue, CTRL-C to cancel."),
input()
"""

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Done.")

out_file.close()
#in_file.close()