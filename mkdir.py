import os

dir_path = "./ABC"
letters = ["A", "B", "C"]

for i in range(1, 326):
  if os.path.isdir(dir_path+(str(i).zfill(3))):
    pass
  else:
    os.makedirs(dir_path+(str(i).zfill(3)))
    for j in range(3):
      file_path = (dir_path+(str(i).zfill(3))) + "/" + letters[j] + ".py"
      with open(file_path, mode="w") as f:
        f.write("")