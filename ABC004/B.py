c=[input().split() for _ in range(4)]
copy=[["","","",""] for _ in range(4)]
for i in range(4):
  for j in range(4):
    copy[i][j]=c[3-i][3-j]
for cc in copy:
  print(*cc)