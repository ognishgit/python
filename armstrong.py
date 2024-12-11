n=int(input("enter a no"))
s=0
x=n
while(n!=0):
    d=n%10
    n=n//10
    s=s+d**3
if x==s:
    print("armstrong no")
else:
    print("not armstrong")
    
