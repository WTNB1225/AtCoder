#A=int(input())
#B=int(input())
#C=int(input())
#score=[A,B,C]
#for i in score:
#  if i==max(score):
#    print(1)
#  elif i==min(score):
#    print(3)
#  else:
#    print(2)
abc=[int(input()) for _ in range(3)]
r=sorted(abc,reverse=True)
for i in range(3):
    print(r.index(abc[i]) + 1)