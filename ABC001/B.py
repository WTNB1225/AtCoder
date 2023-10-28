m=int(input())
if m < 100:
  print("00")
elif m >=100 and m <= 5000:
  if m<1000:
    print(str(int((m/1000)*10)).zfill(2))
  else:
    print(int(((m/1000)*10)))
elif m>=6000 and m<=30000:
  print(int(50+(m/1000)))
elif m>=35000 and m<=70000:
  print(int((((m/1000)-30)/5)+80))
elif m>70000:
  print(89)