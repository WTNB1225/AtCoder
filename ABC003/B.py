S=input()
T=input()
li=["a","t","c","o","d","e","r"]
for i in range(S):
  if S[i]==T[i]:
    pass
  elif S[i]=="@" and T[i] in li:
    pass
  else:
    isLose=True
    break
if isLose:
  print("You will lose")
else:
  print("You can win")