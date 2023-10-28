n=int(input())
a=[0,0,1]
if n==1 or n==2:
  exit(print(0))
if n==3:
  exit(print(1))
for i in range(n-3):
  sum=a[-1]+a[-2]+a[-3]
  a.append(sum%10007)
print(a[-1])