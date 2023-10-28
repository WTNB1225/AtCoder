W = input()
omit = ["a","i", "u", "e", "o"]
for i in omit:
    W = W.replace(i, "")
print(W)