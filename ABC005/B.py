N=int(input())
m=101
for _ in range(N):
  T=int(input())
  if T<m:
    m=T
print(m)