m1 = int(input("Enter marks for test1 : "))
m2 = int(input("Enter marks for test2 : "))
m3 = int(input("Enter marks for test3 : "))
if m1 <= m2 and m1 <= m3:
       avgMarks = (m2+m3)/2
elif m2 <= m1 and m2 <= m3:
      avgMarks = (m1+m3)/2
elif m3 <= m1 and m2 <= m2:
      avgMarks = (m1+m2)/2 
print("Average of best two test marks is :", avgMarks)

n1 = int(input("Enter marks for test1 : "))
n2 = int(input("Enter marks for test2 : "))
n3 = int(input("Enter marks for test3 : "))
mini=min(m1,m2,m3)
avg=(m1+m2+m3-mini)/2
print("best of marks:",avg)