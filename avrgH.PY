H=input("enter heights of you and your frds:")
h=H.split()
c=0
for i in h:
   c=c+1
print(c) 
for p in range(c):
    h[p]=int(h[p])
sum=0
for high in h:
 sum+=high
avrg=sum/c
print("avrg height is",round(avrg))