outfile=open("outfile.txt","w")
outfile.writelines(["Hello"," ","world"])
outfile.close()
infile=open("outfile.txt","r")
infile.read()