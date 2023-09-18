infile="textfile.txt"
n=int(input("enter n value:"))
with open(infile,'r')as filedata:
      lineslist=filedata.readlines()
print("first {n} lines are:")
for textline in (lineslist[:n]):
      print(textline,end='')
filedata.close()
word=input("search wt?")
k=0
with open(infile,'r')as f:
      for line in f:
            words=line.split()
            for i in words:
                  if(i==word):
                        k+=1
      print("occurance is ",k)