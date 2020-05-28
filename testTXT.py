with open ('new.txt','w') as f:
 for i in range(1,10):
     system = i,i+2*i
     f.write(str(system)+'\n')