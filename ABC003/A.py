N=int(input())
sum_money=0
for i in range(N):
  sum_money+=10000*(i+1)
ans=sum_money/N
print(round(ans))