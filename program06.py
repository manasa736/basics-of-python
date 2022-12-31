fo=open(r"C:\Users\User\Desktop\python\day10\123a.txt","a")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
