fo1=open(r"C:\Users\User\Desktop\python\day10\123a.txt","r")
fo2=open(r"C:\Users\User\Desktop\python\day10\test.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()

print("file copied")
